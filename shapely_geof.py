import gpxpy
import shapely.geometry as geom

with open(r"D:\Python\API\lat_api\data\geospasial\gpx\wk47_disp.gpx", "r") as f:
    gpx = gpxpy.parse(f)

coords = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            coords.append((point.longitude, point.latitude))

poly = geom.Polygon(coords)

# 0.0001 adalah toleransi jarak dalam derajat, sesuaikan sesuai kebutuhan
# Titik-titik yang jaraknya lebih kecil dari nilai ini dianggap “tidak penting” dan bisa dihapus
# Jadi semakin besar nilainya → semakin banyak titik yang hilang → bentuk semakin kasar
simplified = poly.simplify(0.0001, preserve_topology=True)

print("Titik asli:", len(coords))
print("Titik setelah simplify:", len(simplified.exterior.coords))

# Format sesuai Traccar (lat lon dipisah koma)
geofence_str = ",".join([f"{lat} {lon}" for lon, lat in simplified.exterior.coords])

with open(r"D:\Python\API\lat_api\data\geospasial\txt\wk47_disp_shapely.txt", "w") as f:
    f.write(geofence_str)

print("Hasil export disimpan di geofence_traccar.txt")