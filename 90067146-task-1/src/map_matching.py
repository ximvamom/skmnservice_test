from utils import point_line_distance

def map_match(gps_points, road_segments, threshold = 30):
    
    for gps in gps_points:
        min_dist = float('inf')
        for start, end in road_segments:
            dist, _ = point_line_distance(gps, start, end)
            if dist < min_dist:
                min_dist = dist
        if min_dist > threshold:
            return True
        
    return False