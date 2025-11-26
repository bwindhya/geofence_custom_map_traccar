import folium

# buat peta dengan basemap OSM
m = folium.Map(location=[-3.8715191144698475, 115.15427225153445], zoom_start=15, tiles=None)

folium.TileLayer(
    tiles='http://10.30.241.7/tile/{z}/{x}/{y}.png',
    attr='My XYZ Tiles',
    name='Custom Tiles',
    overlay=True,
    control=True,
    fmt='image/jpeg',
    # tms=True
).add_to(m)

folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr='Google',
    name='Google Hybrid',
    overlay=False,
    control=True
).add_to(m)

# tambahkan layer control biar bisa gonta-ganti
folium.LayerControl().add_to(m)

# simpan ke HTML
m.save(r"D:\Python\API\lat_api\data\geospasial\html\xyz_tile_test.html")

print("Peta berhasil dibuat")