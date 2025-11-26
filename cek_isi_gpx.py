import gpxpy

with open(r"D:\Python\API\lat_api\data\geospasial\gpx\bdy_3059.gpx", "r") as f:
    gpx = gpxpy.parse(f)

coords = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            coords.append(f"{point.latitude} {point.longitude}")

# gabungkan jadi satu string dipisahkan koma
geofence_str = ", ".join(coords)

with open(r"D:\Python\API\lat_api\data\geospasial\txt\bdy_3059.txt", "w") as f:
    f.write(geofence_str)
# print(geofence_str)

print("Done")