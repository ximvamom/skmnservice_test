import os
from glob import glob
from src.osm_parser import parse_osm
from src.gps_loader import load_gps_points
from src.map_matching import map_match

def run_map_matching(osm_file, gps_folder):
    road_segments = parse_osm(osm_file)
    gps_files = glob(os.path.join(gps_folder, '*.csv'))
    
    result = {}
    for gps_file in gps_files:
        gps_points = load_gps_points(gps_file)
        is_deviated = map_match(gps_points, road_segments)
        result[os.path.basename(gps_file)] = "경로 이탈" if is_deviated else "정상 주행"
        
    return result

if __name__ == "__main__":
    osm_file = "./data/roads.osm"
    gps_folder = "./data/gps_csvs"
    
    result = run_map_matching(osm_file, gps_folder)
    for filename, status in result.items():
        print(f"{filename}: {status}")