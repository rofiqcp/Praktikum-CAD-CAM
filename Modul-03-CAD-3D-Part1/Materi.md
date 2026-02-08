# MODUL 3: CAD GAMBAR 3D — PART 1 (FEATURE DASAR)

## Praktikum CAD/CAM — Pertemuan 3

---

## 3.1 Pendahuluan

Setelah menguasai sketch 2D, langkah selanjutnya adalah mengubah sketch menjadi model 3D menggunakan **Feature**. Feature adalah operasi 3D yang diterapkan pada sketch untuk membentuk solid model. Modul ini membahas feature-feature dasar yang paling sering digunakan.

---

## 3.2 Konsep Dasar Feature

### Feature-Based Modeling
SolidWorks menggunakan pendekatan **feature-based parametric modeling**:
- Setiap feature dibangun di atas feature sebelumnya
- Feature tersimpan secara berurutan di Feature Manager Design Tree
- Mengubah dimensi feature akan memperbarui model secara otomatis (parametrik)

### Urutan Umum Pembuatan Part:
```
Base Feature (Extrude/Revolve) → Boss/Cut → Fillet/Chamfer → Pattern → Detail Features
```

---

## 3.3 Feature Dasar

### 3.3.1 Extruded Boss/Base
Menarik sketch 2D menjadi bentuk 3D solid.

**Parameter:**
| Parameter | Deskripsi |
|-----------|-----------|
| Direction | Arah extrude (satu arah / dua arah) |
| End Condition | Blind (jarak tertentu), Through All, Up To Surface, Up To Vertex, Mid Plane |
| Depth | Kedalaman extrude (untuk Blind) |
| Draft | Sudut draft (kemiringan dinding) |
| Thin Feature | Membuat extrude dengan ketebalan (bukan solid) |

### 3.3.2 Extruded Cut
Memotong material dari solid menggunakan profil sketch.

**Parameter sama dengan Boss** ditambah:
- Flip side to cut: Membalik sisi yang dipotong
- Normal cut: Pemotongan tegak lurus terhadap face

### 3.3.3 Revolved Boss/Base
Memutar sketch 2D mengelilingi sumbu (axis) menjadi bentuk 3D.

**Parameter:**
| Parameter | Deskripsi |
|-----------|-----------|
| Axis | Sumbu putar (centerline pada sketch) |
| Angle | Sudut revolve (360° = penuh) |
| Direction | Satu arah / dua arah |
| Thin Feature | Revolve dengan ketebalan |

**Syarat Sketch Revolve:**
- Harus ada **Centerline** sebagai sumbu putar
- Profil sketch harus **tertutup** dan di satu sisi centerline
- Profil tidak boleh memotong centerline

### 3.3.4 Revolved Cut
Memotong material dengan memutar profil sketch mengelilingi sumbu.

### 3.3.5 Fillet (3D)
Membuat pembulatan pada edge atau face model 3D.

**Tipe Fillet:**
| Tipe | Deskripsi |
|------|-----------|
| Constant Size | Radius konstan pada semua edge yang dipilih |
| Variable Size | Radius berbeda di titik-titik pada edge |
| Face Fillet | Fillet antara 2 face |
| Full Round Fillet | Fillet yang menghubungkan 3 face |

### 3.3.6 Chamfer
Membuat potongan miring pada edge model 3D.

**Tipe Chamfer:**
| Tipe | Deskripsi |
|------|-----------|
| Angle Distance | Sudut dan jarak |
| Distance Distance | 2 jarak berbeda |
| Equal Distance | Jarak sama di kedua sisi |
| Vertex | Chamfer pada vertex (sudut 3 edge) |

### 3.3.7 Shell
Membuat benda menjadi berongga dengan menghilangkan face tertentu.

**Parameter:**
- Thickness: Ketebalan dinding
- Face to Remove: Face yang dihilangkan (menjadi lubang)
- Shell outwards: Menambah material ke luar (bukan ke dalam)

### 3.3.8 Draft
Menambahkan sudut kemiringan pada face (untuk proses molding).

### 3.3.9 Hole Wizard
Tool khusus untuk membuat berbagai jenis lubang standar.

**Jenis Lubang:**
| Jenis | Deskripsi |
|-------|-----------|
| Counterbore | Lubang bertingkat untuk baut socket head |
| Countersink | Lubang kerucut untuk baut flat head |
| Hole | Lubang sederhana |
| Straight Tap | Lubang berulir lurus |
| Tapered Tap | Lubang berulir tirus |
| Legacy | Lubang standar lama |

### 3.3.10 Linear Pattern
Mengulang feature secara linear (satu atau dua arah).

### 3.3.11 Circular Pattern
Mengulang feature secara melingkar.

### 3.3.12 Mirror Feature
Mencerminkan feature terhadap plane.

---

## 3.4 Percobaan 1-10

### Percobaan 1: Balok dengan Fillet dan Chamfer
**Tujuan**: Menguasai Extruded Boss, Fillet, dan Chamfer

```
Spesifikasi:
- Balok: 80 x 50 x 30 mm
- Fillet R5 pada 4 edge vertikal
- Chamfer 3x3mm pada 4 edge atas
- Lubang tembus Ø15mm di tengah face atas (Through All)
- Counterbore Ø8/Ø15/depth 5mm di tengah face depan
```

**Langkah:**
1. Front Plane → Sketch → Rectangle 80x50mm → Exit Sketch
2. Features → Extruded Boss/Base → Blind → 30mm → OK
3. Pilih 4 edge vertikal → Fillet → R5 → OK
4. Pilih 4 edge atas → Chamfer → 3mm → OK
5. Pilih face atas → Sketch → Circle Ø15 di tengah → Exit Sketch
6. Extruded Cut → Through All → OK
7. Pilih face depan → Hole Wizard → Counterbore → Ø8/Ø15/5mm
8. Posisikan lubang di tengah face
9. Verifikasi model → Material: Aluminum 6061
10. Simpan: `M03_P01_Balok.sldprt`

---

### Percobaan 2: Silinder dengan Revolve
**Tujuan**: Menguasai Revolved Boss dan Cut

```
Spesifikasi:
- Poros bertingkat (stepped shaft):
  - Diameter 1: Ø40mm, panjang 20mm
  - Diameter 2: Ø30mm, panjang 40mm
  - Diameter 3: Ø20mm, panjang 30mm
- Chamfer 2x45° pada semua ujung
- Fillet R2 pada semua step transition
- Lubang center: Ø8mm Through All
```

**Langkah:**
1. Front Plane → Sketch
2. Gambar Centerline horizontal dari Origin
3. Gambar profil setengah poros di atas centerline
4. Beri dimensi: Ø40x20, Ø30x40, Ø20x30
5. Exit Sketch → Revolved Boss → Axis: Centerline → 360°
6. Tambahkan Chamfer 2x45° pada semua ujung
7. Tambahkan Fillet R2 pada transisi step
8. Right Plane → Sketch → Circle Ø8 di Origin → Extruded Cut Through All
9. Assign material: Steel AISI 1045
10. Simpan: `M03_P02_Poros.sldprt`

---

### Percobaan 3: Plat dengan Lubang Pattern
**Tujuan**: Menguasai Linear dan Circular Pattern

```
Spesifikasi:
- Plat: 150 x 100 x 10mm
- Fillet R8 pada 4 sudut
- Linear Pattern lubang Ø6mm:
  - 5 kolom x 3 baris
  - Jarak horizontal: 30mm, jarak vertikal: 35mm
  - Dimulai 15mm dari tepi kiri, 17.5mm dari tepi bawah
- Lubang center: Ø20mm
```

**Langkah:**
1. Top Plane → Sketch → Rectangle 150x100 → Extrude 10mm
2. Fillet R8 pada 4 sudut vertikal
3. Face atas → Sketch → Circle Ø6 → posisi 15mm dari kiri, 17.5mm dari bawah
4. Extruded Cut → Through All
5. Linear Pattern → Direction 1: horizontal, 30mm, 5 buah
6. Direction 2: vertikal, 35mm, 3 buah → OK
7. Face atas → Sketch → Circle Ø20 di tengah plat
8. Extruded Cut → Through All
9. Assign material: Aluminum 6061
10. Simpan: `M03_P03_Plat.sldprt`

---

### Percobaan 4: Pully (Revolve + Pattern)
**Tujuan**: Menguasai Revolve dengan profil kompleks dan Circular Pattern

```
Spesifikasi:
- Diameter luar pulley: Ø80mm
- Lebar pulley: 20mm
- Groove (alur V): sudut 40°, kedalaman 5mm
- Hub diameter: Ø30mm
- Lubang poros: Ø12mm dengan keyway 4x4mm
- Spoke holes: 4x Ø10mm pada PCD Ø50mm (Circular Pattern)
```

**Langkah:**
1. Front Plane → Sketch → Centerline horizontal
2. Gambar profil setengah pulley dengan groove V
3. Revolve 360° → dapatkan pulley
4. Right Plane → Sketch → Circle Ø10 pada PCD Ø50
5. Extruded Cut → Through All
6. Circular Pattern → 4 lubang, 360°, Equal Spacing
7. Right Plane → Sketch → Lubang poros Ø12 + keyway 4x4
8. Extruded Cut → Through All
9. Fillet R1 pada edge-edge tajam
10. Simpan: `M03_P04_Pulley.sldprt`

---

### Percobaan 5: Bracket L dengan Shell
**Tujuan**: Menguasai Shell dan kombinasi feature

```
Spesifikasi:
- Bracket L:
  - Lengan vertikal: 60 x 40 x 15mm (tebal awal, sebelum shell)
  - Lengan horizontal: 50 x 40 x 15mm
  - Fillet R10 pada sudut dalam L
- Shell: ketebalan 3mm, remove face belakang
- 2 lubang mounting di lengan vertikal: Ø8mm
- 2 lubang mounting di lengan horizontal: Ø8mm
- Rib penguat: tebal 3mm, tinggi 20mm (segitiga)
```

**Langkah:**
1. Front Plane → Sketch profil L → Extrude 40mm
2. Fillet R10 pada sudut dalam L
3. Shell → 3mm → Remove face belakang
4. Lengan vertikal face depan → Sketch → 2 Circle Ø8 → Cut Through All
5. Lengan horizontal face atas → Sketch → 2 Circle Ø8 → Cut Through All
6. Buat plane baru di tengah bracket
7. Sketch profil rib (segitiga) → Rib feature → tebal 3mm
8. Fillet R2 pada edge rib
9. Assign material: Aluminum 6061
10. Simpan: `M03_P05_BracketL.sldprt`

---

### Percobaan 6: Tutup Botol (Revolve + Knurling Pattern)
**Tujuan**: Menguasai Revolve + Circular Pattern detail

```
Spesifikasi:
- Diameter luar: Ø30mm
- Tinggi: 15mm
- Ketebalan dinding: 2mm (Shell)
- Fillet atas: R3
- Knurling pattern: 36 buah groove vertikal di sisi luar
  - Groove: depth 0.5mm, width 1mm
```

**Langkah:**
1. Front Plane → Sketch → Centerline + profil tutup
2. Revolve 360°
3. Shell → 2mm → Remove face bawah
4. Fillet R3 pada edge atas luar
5. Right Plane → Sketch → Profil groove kecil di sisi luar
6. Extruded Cut → Through All (satu sisi)
7. Circular Pattern → 36 instances, 360°
8. Fillet R0.2 pada edge groove
9. Assign material: HDPE Plastic
10. Simpan: `M03_P06_TutupBotol.sldprt`

---

### Percobaan 7: Gear Spur Sederhana (Revolve + Circular Pattern)
**Tujuan**: Membuat gear sederhana

```
Spesifikasi:
- Module: 2
- Jumlah gigi: 20
- Diameter pitch: Ø40mm (module x jumlah gigi)
- Diameter luar: Ø44mm (pitch + 2*module)
- Diameter root: Ø35mm (pitch - 2.5*module)
- Lebar gigi: 15mm
- Lubang poros: Ø10mm dengan keyway 3x3mm
- Profil gigi: involute (disederhanakan dengan arc)
```

**Langkah:**
1. Front Plane → Sketch → gambar profil 1 gigi (involute disederhanakan)
2. Gambar lingkaran pitch, root, dan tip sebagai construction
3. Buat profil 1 gigi menggunakan arc dan line
4. Exit Sketch → Extrude 15mm
5. Circular Pattern → 20 instances, 360°
6. Right Plane → Sketch → Lingkaran Ø10 + keyway → Cut Through All
7. Chamfer 0.5x45° pada edge gigi
8. Fillet R1 pada root gigi
9. Assign material: Steel AISI 1045
10. Simpan: `M03_P07_GearSpur.sldprt`

---

### Percobaan 8: Flange 3D (Revolve + Hole Wizard)
**Tujuan**: Menguasai Revolve + Hole Wizard

```
Spesifikasi:
- Diameter luar flange: Ø120mm
- Diameter pipe: Ø50mm
- Ketebalan flange: 15mm
- Raised face: Ø80mm, tinggi 2mm dari face flange
- Panjang pipe neck: 40mm
- 8 lubang baut M10 pada BCD Ø95mm (Hole Wizard)
- Chamfer 2x45° pada ujung pipe
- Fillet R3 pada junction flange-pipe
```

**Langkah:**
1. Front Plane → Sketch → Centerline + profil flange dengan pipe
2. Revolve 360°
3. Face atas flange → Hole Wizard → M10 Through All
4. Posisi: pada BCD Ø95 → gunakan Circular Pattern di Hole Wizard
5. 8 lubang, Equal Spacing
6. Chamfer 2x45° pada ujung pipe
7. Fillet R3 pada junction flange-pipe
8. Shell → untuk membuat pipe hollow (bore Ø40mm) atau Cut Revolve
9. Assign material: Stainless Steel AISI 304
10. Simpan: `M03_P08_Flange.sldprt`

---

### Percobaan 9: Housing Sederhana (Extrude + Shell + Rib)
**Tujuan**: Membuat housing/enclosure

```
Spesifikasi:
- Box luar: 100 x 60 x 40mm
- Fillet R5 pada semua edge vertikal luar
- Shell: 3mm, remove face atas
- 4 bosses silinder untuk sekrup di sudut dalam:
  - Ø8mm luar, Ø4mm dalam (lubang sekrup), tinggi 38mm
- 2 Rib penguat: tebal 2mm, di tengah sisi panjang
- Lip (bibir) pada tepi atas: offset 2mm ke dalam, tinggi 3mm
```

**Langkah:**
1. Top Plane → Sketch → Rectangle 100x60 → Extrude 40mm
2. Fillet R5 pada 4 edge vertikal
3. Shell → 3mm → Remove face atas
4. Sketch pada face bawah bagian dalam → Circle Ø8 di sudut → Extrude 38mm (Boss)
5. Sketch pada face atas boss → Circle Ø4 → Cut Through All
6. Circular pattern atau Mirror untuk 4 bosses
7. Buat sketch rib → Rib feature → 2mm
8. Sketch lip pada tepi atas → Extrude 3mm (offset dari tepi)
9. Fillet R1 pada edge internal
10. Simpan: `M03_P09_Housing.sldprt`

---

### Percobaan 10: Motor Mount (Kombinasi Semua Feature)
**Tujuan**: Menggunakan semua feature yang telah dipelajari

```
Spesifikasi:
- Base plate: 80 x 60 x 8mm
- 4 lubang mounting plate: Ø6.5mm, countersink Ø12mm
  (posisi 10mm dari tepi, Linear Pattern)
- Raised circular boss di tengah: Ø50mm, tinggi 5mm
- Lubang motor bore: Ø25mm (Through All)
- 4 lubang mounting motor: Ø4.5mm pada PCD Ø38mm (Circular Pattern)
- 2 slot untuk adjustment: 20x6mm, simetris
- Fillet R3 pada semua edge tajam
- Chamfer 1x45° pada lubang motor bore (kedua sisi)
```

**Langkah:**
1. Top Plane → Sketch → Rectangle 80x60 → Extrude 8mm
2. Face atas → Sketch → Circle Ø50 di tengah → Extrude 5mm (Boss)
3. Face atas boss → Sketch → Circle Ø25 → Cut Through All
4. Hole Wizard → Countersink Ø6.5/Ø12 → posisikan di 4 sudut (Linear Pattern)
5. Face atas boss → Sketch → Circle Ø4.5 pada PCD Ø38 → Cut Through All
6. Circular Pattern → 4 lubang motor
7. Face atas → Sketch → Slot 20x6mm → Cut Through All → Mirror
8. Chamfer 1x45° pada edge lubang bore
9. Fillet R3 pada edge tajam
10. Simpan: `M03_P10_MotorMount.sldprt`

---

## 3.5 Tips Pembuatan Feature 3D

1. **Base Feature**: Selalu mulai dengan feature utama yang mendefinisikan bentuk dasar
2. **Boss sebelum Cut**: Buat semua boss (penambahan material) sebelum cut (pengurangan)
3. **Fillet/Chamfer terakhir**: Tambahkan fillet dan chamfer setelah semua feature utama selesai
4. **Feature Tree terorganisir**: Beri nama deskriptif pada setiap feature
5. **Reference Geometry**: Gunakan plane tambahan jika diperlukan
6. **End Condition**: Pilih end condition yang sesuai design intent (Through All vs Blind)

---

*Modul Praktikum CAD/CAM — Modul 3: CAD Gambar 3D Part 1*
*Disusun untuk keperluan pendidikan*
