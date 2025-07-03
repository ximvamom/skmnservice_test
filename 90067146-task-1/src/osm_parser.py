import xml.etree.ElementTree as ET

def parse_osm(osm_path):
    tree = ET.parse(osm_path)
    root = tree.getroot()
    
    node_dict = {}
    road_segments = []
    
    for node in root.findall('node'):
        node_id = node.attrib['id']
        lat = float(node.attrib['lat'])
        lon = float(node.attrib['lon'])
        node_dict[node_id] = (lat, lon)
        
    for way in root.findall('way'):
        refs = [nd.attri['ref'] for nd in way.findall('nd')]
        coords = [node_dict[ref] for ref in refs if ref in node_dict]
        for i in range(len(coords) - 1):
            road_segments.append((coords[i], coords[i + 1]))

    return road_segments