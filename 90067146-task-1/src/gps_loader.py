import csv

def load_gps_points(csv_path):
    gps_points = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lat = float(row['Latitude'])
            lon = float(row['Longitude'])
            gps_points.append((lat, lon))
    return gps_points