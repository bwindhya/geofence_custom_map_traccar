import ezdxf
from pyproj import Transformer
import gpxpy
import gpxpy.gpx

# baca file DXF
dxf_file = r"D:\Python\API\lat_api\data\geospasial\dxf\bdy_3059.dxf"
doc = ezdxf.readfile(dxf_file)
msp = doc.modelspace()

# transform UTM Zone 50S (EPSG:32750) -> WGS84 (EPSG:4326)
transformer = Transformer.from_crs("EPSG:32750", "EPSG:4326", always_xy=True)

# Pengumpulan Koordinat
coords_wgs84 = []
for pl in msp.query("POLYLINE"):
    for v in pl.vertices:
        x, y, z = v.dxf.location
        lon, lat = transformer.transform(x, y)
        coords_wgs84.append((lat, lon))

# Buat GPX
gpx = gpxpy.gpx.GPX()
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

for lat, lon in coords_wgs84:
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon))

with open(r"D:\Python\API\lat_api\data\geospasial\gpx\bdy_3059.gpx", "w") as f:
    f.write(gpx.to_xml())

print("Konversi selesai.")
