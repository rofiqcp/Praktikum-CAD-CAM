# JOBSHEET MODUL 2: CAD GAMBAR 2D — SKETCHING, DIMENSIONING & CONSTRAINTS

## Praktikum CAD/CAM — Pertemuan 2

---

## I. Tujuan Praktikum

1. Mahasiswa mampu membuat sketch 2D menggunakan semua entitas sketch di SolidWorks
2. Mahasiswa mampu menerapkan Smart Dimension dan berbagai tipe dimensi
3. Mahasiswa mampu menggunakan Sketch Relations (Constraints) dengan benar
4. Mahasiswa mampu menggunakan Sketch Tools: Trim, Offset, Mirror, Pattern
5. Mahasiswa mampu membuat sketch yang Fully Defined
6. Mahasiswa mampu membuat profil gambar teknik standar industri

---

## II. Alat dan Bahan

### Perangkat Keras:
| No | Alat/Bahan | Jumlah |
|----|------------|--------|
| 1 | Laptop/PC dengan SolidWorks | 1 unit |
| 2 | Mouse 3-button | 1 unit |

### Perangkat Lunak:
| No | Software | Keterangan |
|----|----------|------------|
| 1 | SolidWorks 2021+ | Sudah dikonfigurasi (MMGS, ISO) |
| 2 | OBS Studio | Screen recording |

---

## III. Landasan Teori

(Lihat **Materi.md** Modul 2 untuk teori lengkap tentang Sketching, Dimensioning, dan Constraints)

Ringkasan konsep kunci:
- **Sketch Entities**: Line, Rectangle, Circle, Arc, Polygon, Slot, Spline, Ellipse
- **Sketch Tools**: Trim, Extend, Offset, Mirror, Pattern, Fillet, Chamfer
- **Dimensions**: Smart Dimension, Horizontal, Vertical, Ordinate
- **Constraints**: Horizontal, Vertical, Coincident, Tangent, Perpendicular, Parallel, Equal, Symmetric, Midpoint, Concentric, Collinear
- **Sketch Status**: Fully Defined (hitam), Under Defined (biru), Over Defined (merah)

---

## IV. Langkah Percobaan

### Percobaan 1: Geometri Dasar — Garis dan Persegi Panjang
*(Detail lengkap ada di Materi.md)*
1. New Part → Front Plane → Sketch
2. Gambar Rectangle luar 80 x 50 mm
3. Gambar Rectangle dalam 30 x 20 mm
4. Beri dimensi dan posisikan (15mm dari tepi kiri, 15mm dari bawah)
5. Verifikasi **Fully Defined**

### Percobaan 2: Lingkaran dan Arc
1. Gambar Lingkaran Ø60mm di Origin
2. Gambar Lingkaran Ø20mm (Concentric)
3. Gambar Lingkaran Ø10mm center (0,15)
4. Gambar 4 Arc R15 pada posisi kardinal
5. Tambahkan constraint Tangent dan Equal

### Percobaan 3: Polygon dan Slot
1. Gambar Hexagon inscribed Ø40mm
2. Gambar 6 Straight Slot (15x5mm)
3. Gunakan Circular Pattern
4. Gambar lingkaran pusat Ø10mm

### Percobaan 4: Teknik Trim, Extend, dan Offset
1. Gambar profil L-bracket
2. Gunakan Offset 3mm ke dalam
3. Tambahkan Fillet R5 (dalam) dan R3 (luar)
4. Gambar 2 lubang Ø6mm

### Percobaan 5: Mirror dan Pattern
1. Gambar 1/4 plat 120x80mm
2. Mirror dua kali (horizontal & vertikal)
3. Gambar lubang dan pattern ke semua posisi
4. Tambahkan slot dan Fillet R8

### Percobaan 6: Profil Kompleks — Cam
1. Gambar 2 lingkaran (dasar Ø30, lobe Ø20)
2. Buat garis tangent penghubung
3. Trim profil luar cam
4. Buat lubang center Ø8 + keyway

### Percobaan 7: Spline — Airfoil
1. Plot titik-titik koordinat airfoil
2. Gambar Spline melalui titik-titik
3. Mirror untuk lower surface
4. Sesuaikan leading & trailing edge

### Percobaan 8: Gasket
1. Gambar profil gasket 150x100mm dengan fillet
2. Gambar lubang oval 80x40mm di tengah
3. Gambar 6 lubang baut Ø10mm dengan pattern

### Percobaan 9: Bracket/Engsel
1. Gambar profil bracket segitiga
2. Tambahkan rib penguat
3. Gambar lubang mounting
4. Tambahkan Fillet dan Chamfer

### Percobaan 10: Flange
1. Gambar lingkaran-lingkaran konsentris
2. Gambar 8 lubang baut pada BCD dengan Circular Pattern
3. Lengkapi semua dimensi

### Percobaan 11: Equations dan Parametric Design
1. Buat Global Variable "BaseWidth" = 100
2. Buat plat dengan dimensi menggunakan equation
3. Semua proporsi relatif terhadap BaseWidth
4. Test ubah BaseWidth → semua dimensi menyesuaikan

### Percobaan 12: Sketch Blocks — Profil Standar
1. Buat sketch profil T-Slot (alur aluminium)
2. Make Block dan simpan sebagai .sldblk
3. Insert 4 block, susun menjadi profil 4040

### Percobaan 13: 3D Sketch — Pipe Path
1. Insert 3D Sketch
2. Gambar path pipa L-shape 3D
3. Gunakan Tab untuk switch plane
4. Tambahkan fillet pada bend

### Percobaan 14: Drawing dari Sketch
1. Make Drawing from Part (Flange)
2. Tambahkan Standard Views + Section
3. Tambahkan semua dimensi
4. Export ke PDF

### Percobaan 15: GD&T Basic
1. Tambahkan Datum pada Drawing
2. Tambahkan Position tolerance
3. Tambahkan Flatness dan Perpendicularity

---

## V. Analisa dan Pembahasan

### Pertanyaan Analisa:

1. **Jelaskan perbedaan antara constraint dan dimension** dalam mendefinisikan sketch. Kapan sebaiknya menggunakan constraint dan kapan menggunakan dimension?

2. **Jelaskan konsep Design Intent** dengan contoh dari percobaan yang telah dilakukan. Bagaimana pemilihan constraint dan dimension mempengaruhi perilaku sketch saat dimodifikasi?

3. **Bandingkan penggunaan Mirror vs Copy** dalam pembuatan sketch. Apa kelebihan dan kekurangan masing-masing dari segi:
   - Efisiensi waktu
   - Kemudahan modifikasi
   - Design intent

4. **Analisis percobaan yang paling menantang**. Jelaskan:
   - Kesulitan apa yang dihadapi
   - Bagaimana mengatasinya
   - Constraint apa yang paling sering digunakan

5. **Jelaskan strategi** untuk membuat sketch yang efisien dan mudah dimodifikasi. Berikan contoh dari percobaan.

### Pembahasan:

1. Diskusikan perbedaan membuat sketch dari Origin vs dari sembarang titik
2. Jelaskan dampak sketch yang Under Defined terhadap feature 3D
3. Bandingkan penggunaan Sketch Fillet vs Feature Fillet (di level 3D)
4. Diskusikan kapan menggunakan Construction Geometry dan manfaatnya
5. Jelaskan teknik troubleshooting sketch yang Over Defined

---

## VI. Kesimpulan

Tuliskan kesimpulan mencakup:
1. Teknik-teknik sketching yang telah dikuasai
2. Pentingnya Fully Defined sketch
3. Penggunaan constraints vs dimensions
4. Tips efisiensi dalam membuat sketch 2D
5. Kesiapan untuk pembuatan model 3D di modul selanjutnya

---

## VII. Tugas

### Tugas Video (10-15 menit):
1. **Penjelasan Materi** (5-7 menit): Jelaskan konsep sketching, dimensioning, constraints, dan sketch tools
2. **Screen Record Percobaan 1-15** (5-7 menit): Demonstrasikan setiap percobaan dengan narasi
3. **Analisa & Kesimpulan** (2-3 menit)

### Ketentuan:
- Wajah terlihat saat penjelasan materi
- Screen record saat demonstrasi percobaan
- File: `NIM_Nama_Modul02_Video.mp4`

### Pengumpulan:
- 15 file .sldprt (Percobaan 1-15)
- 1 file project .sldprt
- 1 file drawing .slddrw (Percobaan 14)
- 1 video .mp4
- 1 laporan .pdf
- Dikemas dalam: `NIM_Nama_Modul02.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 2: CAD Gambar 2D*
*Disusun untuk keperluan pendidikan*
