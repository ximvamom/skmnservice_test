import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def to_xy(lat, lon):
    R = 6371000
    x = R * math.radians(lon)
    y = R * math.radians(lat)
    return x, y

def to_latlon(x, y):
    R = 6371000
    lon = math.degrees(x / R)
    lat = math.degrees(y / R)
    return lat, lon

def point_line_distance(gps_point, line_start, line_end):
    px, py = to_xy(*gps_point)
    x1, y1 = to_xy(*line_start)
    x2, y2 = to_xy(*line_end)
    
    if (x1, y1) == (x2, y2):
        dist = math.hypot(px - x1, py - y1)
        return dist, line_start
    
    dx, dy = x2 - x1, y2 - y1
    t = ((px - x1) * dx + (py - y1) * dy) / (dx**2 + dy**2)
    t = max(0, min(1, t))
    
    closest_x = x1 + t * dx
    closest_y = y1 + t * dy
    closest_latlon = to_latlon(closest_x, closest_y)
    dist = math.hypot(px - closest_x, py - closest_y)
    return dist, closest_latlon