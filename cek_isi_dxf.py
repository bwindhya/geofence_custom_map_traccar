import ezdxf

# Buka file DXF
doc = ezdxf.readfile(r"D:\Python\API\lat_api\data\geospasial\dxf\bdy_3059.dxf")
# doc = ezdxf.readfile(r"D:\Python\API\lat_api\bdy_jlnBarteng_merge_dok1.dxf")
msp = doc.modelspace()

# Cek semua entity yang ada
for entity in msp:
    print(entity.dxftype())  # tipe: LINE, POLYLINE, LWPOLYLINE, POINT, dll.

# Kalau mau cek koordinat
for e in msp.query("LINE"):
    print("LINE:", e.dxf.start, "->", e.dxf.end)

for e in msp.query("POINT"):
    print("POINT:", e.dxf.location)

# Untuk polyline lama (POLYLINE)
for pl in msp.query("POLYLINE"):
    print("POLYLINE:")
    for v in pl.vertices:  # ambil vertex
        print(v.dxf.location)

# Untuk polyline baru (LWPOLYLINE)
for lw in msp.query("LWPOLYLINE"):
    print("LWPOLYLINE:")
    print(lw.get_points())
