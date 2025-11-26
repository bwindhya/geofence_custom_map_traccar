Berikut alur penggunaan dan penjelasan dari masing-masing file :

1. cek_isi_dxf.py - cek jenis geometry dan untuk mengetahui jumlah poin koordinat
2. shapely_geof.py - mengurangi jumlah poin koordinat dengan metode simplify geometry. Outputnya berupa file .txt yang kemudian akan dibungkus dengan LINESTRING
3. convert_dxf_gpx.py - konversi file dxf ke gpx
4. cek_isi_gpx.py - cek isi file gpx hasil konversi. Outputnya berupa file .txt yang kemudian dibungkus dengan LINESTRING
5. xyz_tile_test.py - test / uji coba server XYZ tile apakah sesuai dengan base map google. Outputnya berupa file .html
