# MODUL 2: CAD GAMBAR 2D — SKETCHING, DIMENSIONING & CONSTRAINTS

## Praktikum CAD/CAM — Pertemuan 2

---

## 2.1 Pendahuluan

Gambar 2D (Sketch) adalah fondasi dari semua pemodelan 3D di SolidWorks. Setiap model 3D dimulai dari sketch 2D yang kemudian diberi feature (extrude, revolve, dll.). Penguasaan teknik sketching, dimensioning, dan constraints sangat penting untuk menghasilkan model yang presisi dan parametrik.

---

## 2.2 Konsep Dasar Sketching

### Apa itu Sketch?
Sketch adalah gambar 2D yang dibuat pada sebuah plane (bidang) atau face (permukaan) dari model 3D. Sketch terdiri dari:
- **Entitas geometri**: Garis, lingkaran, arc, spline, dll.
- **Constraints (Relations)**: Hubungan geometris antar entitas
- **Dimensions**: Ukuran yang mendefinisikan geometri

### Status Sketch:

| Status | Warna | Keterangan |
|--------|-------|------------|
| **Fully Defined** | Hitam | Semua geometri sudah terdefinisi posisi dan ukurannya |
| **Under Defined** | Biru | Masih ada derajat kebebasan yang belum terdefinisi |
| **Over Defined** | Merah | Ada constraint/dimension yang berlebihan (konflik) |

> **PENTING**: Selalu usahakan sketch dalam kondisi **Fully Defined** sebelum membuat feature 3D!

### Memulai Sketch:
1. Klik plane (Front/Top/Right) atau face
2. Klik **Sketch** di Command Manager, atau
3. Klik kanan pada plane → **Sketch**

### Mengakhiri Sketch:
- Klik **Exit Sketch** di pojok kanan atas, atau
- Klik ikon **Exit Sketch** di Command Manager, atau
- Klik kanan → **Exit Sketch**

---

## 2.3 Entitas Sketch (Sketch Entities)

### 2.3.1 Line (Garis) — Shortcut: L
- **Fungsi**: Membuat garis lurus
- **Cara**: Klik titik awal → klik titik akhir
- **Opsi**: 
  - As Construction: Garis bantu (tidak digunakan untuk feature)
  - Infinite Length: Garis tak hingga
  - Midpoint Line: Garis dari titik tengah

### 2.3.2 Rectangle (Persegi Panjang) — Shortcut: R
- **Tipe-tipe Rectangle**:
  1. **Corner Rectangle**: Klik sudut 1 → klik sudut berlawanan
  2. **Center Rectangle**: Klik pusat → klik sudut
  3. **3 Point Corner Rectangle**: Klik 3 titik
  4. **3 Point Center Rectangle**: Klik pusat → klik 2 titik
  5. **Parallelogram**: Membuat jajaran genjang

### 2.3.3 Circle (Lingkaran) — Shortcut: C
- **Tipe-tipe Circle**:
  1. **Circle**: Klik pusat → klik radius
  2. **Perimeter Circle**: Klik 3 titik pada keliling

### 2.3.4 Arc (Busur)
- **Tipe-tipe Arc**:
  1. **Centerpoint Arc**: Klik pusat → klik 2 titik ujung
  2. **Tangent Arc**: Arc yang tangent dengan entitas sebelumnya
  3. **3 Point Arc**: Klik 3 titik

### 2.3.5 Polygon (Segi Banyak)
- Membuat polygon beraturan (3-40 sisi)
- **Opsi**: Inscribed in circle / Circumscribed about circle

### 2.3.6 Ellipse (Elips)
- Klik pusat → klik sumbu mayor → klik sumbu minor

### 2.3.7 Slot
- **Tipe-tipe Slot**:
  1. **Straight Slot**: Slot lurus
  2. **Centerpoint Straight Slot**: Slot lurus dari pusat
  3. **3 Point Arc Slot**: Slot melengkung
  4. **Centerpoint Arc Slot**: Slot melengkung dari pusat

### 2.3.8 Spline
- Kurva halus melalui beberapa titik kontrol
- **Tipe**: Spline, Style Spline, Spline on Surface

### 2.3.9 Point
- Membuat titik referensi pada sketch

### 2.3.10 Centerline (Garis Pusat)
- Garis bantu untuk:
  - Sumbu revolve
  - Referensi mirror
  - Referensi dimensi

### 2.3.11 Text
- Membuat teks pada sketch (untuk engrave/emboss)

### 2.3.12 Construction Geometry
- Mengubah entitas sketch menjadi garis bantu
- Ditampilkan dengan garis putus-putus
- Tidak digunakan sebagai profil feature

---

## 2.4 Sketch Tools (Alat Bantu Sketch)

### 2.4.1 Trim Entities
- **Trim to Closest**: Menghapus bagian entitas sampai intersection terdekat
- **Corner**: Membuat sudut dari 2 garis
- **Trim Away Inside/Outside**: Menghapus bagian dalam/luar 2 boundary
- **Shortcut**: T

### 2.4.2 Extend Entities
- Memperpanjang entitas sampai bertemu entitas lain

### 2.4.3 Offset Entities
- Membuat salinan entitas dengan jarak tertentu
- **Parameter**: Distance, Reverse, Select Chain, Bi-directional

### 2.4.4 Convert Entities
- Mengkonversi edge/face model 3D menjadi entitas sketch

### 2.4.5 Mirror Entities
- Mencerminkan entitas sketch terhadap centerline

### 2.4.6 Move/Copy/Rotate/Scale Entities
- **Move**: Memindahkan entitas
- **Copy**: Menyalin entitas
- **Rotate**: Memutar entitas
- **Scale**: Mengubah skala entitas

### 2.4.7 Linear Sketch Pattern
- Mengulang entitas secara linear (baris dan kolom)
- Parameter: Direction, spacing, count

### 2.4.8 Circular Sketch Pattern
- Mengulang entitas secara melingkar
- Parameter: Center, angle, count

### 2.4.9 Sketch Fillet
- Membuat fillet (pembulatan sudut) pada sketch
- Parameter: Radius

### 2.4.10 Sketch Chamfer
- Membuat chamfer (potongan sudut) pada sketch
- Parameter: Distance, Angle, Equal Distance

---

## 2.5 Dimensions (Dimensi) — Shortcut: D

### 2.5.1 Smart Dimension
Tool utama untuk memberikan dimensi. Secara otomatis mendeteksi tipe dimensi berdasarkan entitas yang dipilih.

| Entitas yang dipilih | Tipe Dimensi |
|---------------------|--------------|
| Garis | Panjang garis |
| 2 garis paralel | Jarak antar garis |
| 2 garis miring | Sudut antar garis |
| Lingkaran | Diameter atau Radius |
| Arc | Radius arc |
| 2 titik | Jarak antar titik |
| Titik ke garis | Jarak tegak lurus |

### 2.5.2 Horizontal Dimension
- Memberikan dimensi horisontal antara 2 titik/entitas

### 2.5.3 Vertical Dimension
- Memberikan dimensi vertikal antara 2 titik/entitas

### 2.5.4 Ordinate Dimension
- Dimensi berantai dari satu titik referensi (datum)

### 2.5.5 Baseline Dimension
- Dimensi paralel dari satu baseline

### 2.5.6 Path Dimension
- Dimensi sepanjang jalur (path)

### Tips Dimensioning:
1. **Selalu mulai dari Origin** — Kunci posisi sketch terhadap origin
2. **Beri dimensi yang bermakna** — Gunakan dimensi yang sesuai design intent
3. **Hindari dimensi redundan** — Jangan memberi dimensi ganda pada entitas yang sama
4. **Gunakan Driven Dimension** — Untuk dimensi referensi (tidak mengontrol geometri)

---

## 2.6 Sketch Relations (Constraints)

### Constraints Otomatis vs Manual:
- **Otomatis**: SolidWorks mendeteksi dan menambahkan constraint saat sketching (bisa diaktifkan/nonaktifkan)
- **Manual**: Ditambahkan pengguna dengan **Add Relation**

### Jenis-jenis Constraints:

| No | Constraint | Simbol | Deskripsi |
|----|-----------|--------|-----------|
| 1 | **Horizontal** | — | Membuat garis horizontal |
| 2 | **Vertical** | \| | Membuat garis vertikal |
| 3 | **Coincident** | ● | Membuat 2 titik bertemu |
| 4 | **Concentric** | ◎ | Membuat 2 lingkaran/arc sepusat |
| 5 | **Tangent** | ⟨ | Membuat entitas bersinggungan |
| 6 | **Perpendicular** | ⊥ | Membuat 2 garis tegak lurus |
| 7 | **Parallel** | ∥ | Membuat 2 garis sejajar |
| 8 | **Equal** | = | Membuat 2 entitas sama ukuran |
| 9 | **Midpoint** | M | Menempatkan titik di tengah entitas |
| 10 | **Symmetric** | ↔ | Membuat entitas simetris terhadap centerline |
| 11 | **Collinear** | — | Membuat 2 garis segaris |
| 12 | **Coradial** | ◎ | Membuat 2 arc/lingkaran seradius dan sepusat |
| 13 | **Fix** | 📌 | Mengunci posisi entitas |
| 14 | **Pierce** | ✕ | Titik di mana sketch menembus kurva/edge 3D |
| 15 | **Merge** | ● | Menggabungkan 2 titik menjadi 1 |

### Cara Menambahkan Constraint:
1. Pilih entitas yang ingin diberi constraint
2. Di Property Manager, pilih constraint yang diinginkan
3. Atau: Pilih entitas → klik kanan → **Add Relation** → pilih constraint

### Cara Melihat dan Menghapus Constraint:
1. Klik entitas → lihat constraint di Property Manager
2. Untuk menghapus: Klik constraint di Property Manager → Delete
3. Atau: `Display/Delete Relations` dari menu Sketch

---

## 2.7 Teknik Sketching Lanjutan

### 2.7.1 Design Intent
Design intent adalah cara Anda mendefinisikan sketch agar perubahan dimensi menghasilkan perilaku yang diinginkan.

**Contoh**: Membuat lubang di tengah plat
- ❌ Memberi dimensi dari tepi kiri DAN tepi kanan
- ✅ Menggunakan constraint **Symmetric** terhadap centerline

### 2.7.2 Fully Define Sketch
Tool otomatis untuk menambahkan dimensi dan constraint yang kurang:
`Tools → Dimensions → Fully Define Sketch`

### 2.7.3 Check Sketch for Feature
Memvalidasi apakah sketch siap untuk feature tertentu:
`Tools → Sketch Tools → Check Sketch for Feature`

### 2.7.4 Sketch Picture
Menyisipkan gambar sebagai referensi untuk tracing:
`Tools → Sketch Tools → Sketch Picture`

### 2.7.5 Contour Selection
Memilih kontur tertentu dari sketch yang tumpang tindih untuk digunakan sebagai profil feature.

### 2.7.6 Power Trim
Trim dengan menyeret mouse melalui entitas yang ingin dihapus.

### 2.7.7 Rapid Sketch
Mode sketching cepat yang otomatis menambahkan constraint:
- Inference Lines: Garis bantu otomatis
- Snap to Grid: Snap ke grid

---

## 2.8 Gambar Teknik 2D (Drawing Standards)

### Garis dalam Gambar Teknik:

| Tipe Garis | Tampilan | Fungsi |
|-----------|----------|--------|
| Garis Tebal (Visible) | ———— | Garis yang terlihat |
| Garis Tipis (Hidden) | - - - - | Garis tersembunyi |
| Garis Pusat (Center) | —·—·— | Sumbu simetri |
| Garis Dimensi | ←——→ | Garis ukuran |
| Garis Phantom | —··—··— | Posisi alternatif |
| Garis Section | ———— (tebal) | Garis potong |

### Standar Penulisan Dimensi (ISO):
1. Dimensi ditulis di atas garis dimensi
2. Panah mengarah ke luar jika ruang sempit
3. Gunakan satuan mm (tanpa menulis "mm")
4. Toleransi ditulis sesuai standar ISO
5. Simbol: Ø (diameter), R (radius), □ (square)

---

## 2.9 Percobaan 1-10: Gambar 2D

### Percobaan 1: Geometri Dasar — Garis dan Persegi Panjang
**Tujuan**: Menguasai tool Line dan Rectangle dengan dimensi

**Gambar yang harus dibuat:**
```
    ┌──── 80 ────┐
    │             │
    │    ┌─30─┐   │ 50
    │    │    │   │
    │    └────┘   │
    │             │
    └─────────────┘

Spesifikasi:
- Rectangle luar: 80 x 50 mm
- Rectangle dalam: 30 x 20 mm
- Rectangle dalam berjarak 15mm dari tepi kiri dan 15mm dari tepi bawah
- Semua sudut 90°
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buka SolidWorks → New → Part
2. Pilih **Front Plane** → Sketch
3. Gambar Rectangle luar dari origin: 80 x 50 mm (gunakan Corner Rectangle)
4. Beri dimensi dengan **Smart Dimension** (D): Width = 80, Height = 50
5. Gambar Rectangle dalam: 30 x 20 mm
6. Beri dimensi: Width = 30, Height = 20
7. Beri dimensi jarak dari tepi kiri = 15mm
8. Beri dimensi jarak dari tepi bawah = 15mm
9. Pastikan sketch **Fully Defined** (semua garis berwarna hitam)
10. Exit Sketch → Simpan file

---

### Percobaan 2: Lingkaran dan Arc
**Tujuan**: Menguasai tool Circle dan Arc dengan constraints

**Gambar yang harus dibuat:**
```
         R15
        ╭───╮
       ╱     ╲
      ╱  ○R5  ╲
     │  Ø20    │   Lingkaran besar R30
     │ ╭─╮    │
      ╲│ │   ╱
       ╲╰─╯ ╱
        ╰───╯

Spesifikasi:
- Lingkaran besar: Ø60mm (R30), center di Origin
- Lingkaran kecil 1: Ø20mm, concentric dengan lingkaran besar
- Lingkaran kecil 2: Ø10mm (R5), center di (0, 15)
- 4 buah arc R15 pada posisi 0°, 90°, 180°, 270° dari pusat
- Semua arc tangent dengan lingkaran besar
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar Circle Ø60 di Origin
3. Gambar Circle Ø20 di Origin (auto Concentric)
4. Gambar Circle Ø10 dengan center di (0, 15) — beri dimensi vertikal
5. Gambar 4 Centerpoint Arc R15 pada posisi kardinal
6. Tambahkan constraint **Tangent** antara arc dan lingkaran besar
7. Tambahkan constraint **Equal** pada semua 4 arc
8. Beri dimensi R15 pada salah satu arc
9. Pastikan Fully Defined
10. Simpan file

---

### Percobaan 3: Polygon dan Slot
**Tujuan**: Menguasai tool Polygon dan Slot

**Gambar yang harus dibuat:**
```
Spesifikasi:
- Hexagon (segi-6): Inscribed circle Ø40mm, center di Origin
- Di setiap sisi hexagon, buat Straight Slot:
  - Panjang slot: 15mm
  - Lebar slot: 5mm
  - Slot tegak lurus terhadap sisi hexagon
  - Jarak center slot dari center hexagon: 25mm
- Lingkaran pusat: Ø10mm
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar **Polygon** 6 sisi, Inscribed, Ø40mm di Origin
3. Gambar **Centerline** dari Origin ke tengah setiap sisi
4. Gambar **Straight Slot** pada salah satu sisi: panjang 15mm, lebar 5mm
5. Beri dimensi slot dan jarak dari pusat
6. Gunakan **Circular Sketch Pattern** untuk menduplikasi slot ke 6 posisi
7. Gambar lingkaran pusat Ø10mm di Origin
8. Pastikan semua constraint (Equal, Perpendicular) sudah benar
9. Pastikan Fully Defined
10. Simpan file

---

### Percobaan 4: Teknik Trim, Extend, dan Offset
**Tujuan**: Menguasai tool Trim, Extend, dan Offset

**Gambar yang harus dibuat:**
```
Spesifikasi:
- Gambar profil berbentuk "L" (L-bracket) view samping:
  - Tinggi total: 60mm
  - Lebar total: 50mm
  - Ketebalan: 8mm
- Buat Offset 3mm ke dalam (membuat profil paralel)
- Tambahkan Fillet R5 pada sudut dalam "L"
- Tambahkan Fillet R3 pada semua sudut luar
- Tambahkan 2 lubang Ø6mm untuk baut:
  - Lubang 1: di tengah lengan vertikal
  - Lubang 2: di tengah lengan horizontal
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar garis-garis profil L menggunakan Line tool
3. Beri dimensi: tinggi 60mm, lebar 50mm, tebal 8mm
4. Gunakan **Trim Entities** untuk menghapus garis yang tidak diperlukan
5. Gunakan **Offset Entities** 3mm ke dalam
6. Tambahkan **Sketch Fillet** R5 pada sudut dalam
7. Tambahkan **Sketch Fillet** R3 pada sudut luar
8. Gambar 2 Circle Ø6mm di tengah masing-masing lengan
9. Tambahkan constraint **Midpoint** dan **Symmetric**
10. Pastikan Fully Defined → Simpan

---

### Percobaan 5: Mirror dan Pattern
**Tujuan**: Menguasai tool Mirror dan Pattern untuk efisiensi

**Gambar yang harus dibuat:**
```
Spesifikasi:
- Plat persegi panjang: 120 x 80 mm
- Simetris terhadap sumbu horizontal DAN vertikal
- Pola lubang:
  - 4 lubang Ø5mm di sudut (jarak 10mm dari tepi)
  - 3 lubang Ø8mm di tengah secara horizontal (jarak antar center 30mm)
- Slot di tengah atas dan bawah: 20 x 5mm
- Fillet R8 pada 4 sudut plat
- Gunakan MIRROR dan LINEAR PATTERN
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar **Centerline** horizontal dan vertikal melalui Origin
3. Gambar 1/4 bagian rectangle (sudut kanan atas): 60 x 40mm dari Origin
4. **Mirror** terhadap centerline vertikal → dapat separuh atas
5. **Mirror** terhadap centerline horizontal → dapat seluruh rectangle
6. Gambar 1 lubang Ø5mm di sudut kanan atas (10mm dari tepi)
7. **Mirror** lubang ke 4 sudut menggunakan kedua centerline
8. Gambar 1 lubang Ø8mm di center → gunakan **Linear Pattern** untuk 3 lubang
9. Gambar 1 slot di atas → **Mirror** ke bawah
10. Tambahkan Fillet R8 pada 4 sudut → Pastikan Fully Defined → Simpan

---

### Percobaan 6: Profil Kompleks dengan Constraints
**Tujuan**: Menguasai penggunaan multiple constraints untuk profil kompleks

**Gambar yang harus dibuat:**
```
Spesifikasi:
Profil Cam (nok) — Berbentuk seperti telur yang tidak simetris
- Lingkaran dasar: Ø30mm, center di Origin
- Lingkaran lobe: Ø20mm, center di (0, 20)
- 2 garis tangent menghubungkan kedua lingkaran (kiri dan kanan)
- Trim bagian dalam sehingga hanya tersisa profil luar cam
- Lubang center: Ø8mm dengan keyway 3x3mm
- Semua constraint Tangent harus diterapkan
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar Circle Ø30mm di Origin (lingkaran dasar)
3. Gambar Circle Ø20mm dengan center di (0, 20)
4. Gambar 2 garis dari tepi lingkaran besar ke lingkaran kecil
5. Tambahkan constraint **Tangent** pada setiap garis terhadap kedua lingkaran
6. Gunakan **Trim Entities** untuk menghapus bagian dalam
7. Gambar lubang center Ø8mm di Origin
8. Gambar keyway 3x3mm pada lubang center
9. Beri semua dimensi yang diperlukan
10. Pastikan Fully Defined → Simpan

---

### Percobaan 7: Spline dan Kurva Bebas
**Tujuan**: Menguasai Spline untuk bentuk organik

**Gambar yang harus dibuat:**
```
Spesifikasi:
Profil Airfoil (sayap pesawat) — NACA 0012
- Chord length (panjang): 100mm
- Gunakan Spline melalui titik-titik:
  Upper surface: (0,0), (1.25, 2.24), (2.5, 3.04), (5, 4.09), 
                 (10, 5.39), (20, 6.57), (30, 6.85), (40, 6.59),
                 (50, 5.95), (60, 5.04), (70, 3.91), (80, 2.63),
                 (90, 1.26), (100, 0.13)
  Lower surface: Mirror dari upper (symmetric airfoil)
- Leading edge radius: R1.1mm
- Trailing edge: Tajam atau R0.1mm
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar **Centerline** horizontal dari Origin ke (100, 0)
3. Plot titik-titik menggunakan **Point** tool (atau langsung dengan Spline)
4. Gambar **Spline** melalui titik-titik upper surface
5. **Mirror** spline terhadap centerline untuk lower surface
6. Atau: Gambar spline lower surface secara manual
7. Tambahkan constraint **Symmetric** pada titik-titik atas dan bawah
8. Sesuaikan tangent handle pada leading dan trailing edge
9. Beri dimensi chord length = 100mm
10. Pastikan Fully Defined → Simpan

---

### Percobaan 8: Gambar Teknik — Gasket
**Tujuan**: Membuat profil gasket industri dengan berbagai geometri

**Gambar yang harus dibuat:**
```
Spesifikasi:
Gasket berbentuk persegi panjang dengan sudut radius:
- Ukuran luar: 150 x 100mm
- Fillet sudut luar: R10
- Lubang tengah oval: 80 x 40mm, fillet R20
- 6 lubang baut: Ø10mm
  - 2 lubang di atas dan bawah (jarak antar center 100mm, jarak dari tepi 15mm)
  - 1 lubang di kiri dan kanan (di tengah, jarak dari tepi 15mm)
- Ketebalan gasket terlihat dari dimensi
- Semua simetris terhadap 2 sumbu
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar Centerline horizontal dan vertikal di Origin
3. Gambar 1/4 Rectangle luar: 75 x 50mm dari Origin
4. Mirror ke 4 kuadran → Rectangle 150 x 100mm
5. Tambahkan Sketch Fillet R10 pada 4 sudut
6. Gambar 1/4 oval dalam menggunakan arc dan line
7. Mirror ke 4 kuadran → Oval 80 x 40mm
8. Gambar 1 lubang baut Ø10mm di kuadran kanan atas
9. Gunakan Mirror dan Pattern untuk semua 6 lubang
10. Pastikan Fully Defined → Simpan

---

### Percobaan 9: Gambar Teknik — Engsel (Bracket)
**Tujuan**: Membuat profil bracket/engsel dengan teknik lengkap

**Gambar yang harus dibuat:**
```
Spesifikasi:
Bracket berbentuk segitiga dengan penguatan:
- Alas: 80mm
- Tinggi: 60mm
- Ketebalan material: 5mm
- Lubang mounting bawah: 2x Ø8mm, jarak dari tepi 10mm
- Lubang mounting samping: 2x Ø8mm, jarak dari tepi 10mm
- Rib penguat diagonal: tebal 5mm
- Fillet R5 pada semua sudut dalam
- Fillet R3 pada semua sudut luar
- Chamfer 2x2mm pada ujung-ujung tertentu
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar profil luar bracket menggunakan Line tool
3. Beri dimensi: alas 80mm, tinggi 60mm
4. Gambar profil dalam dengan Offset 5mm (ketebalan)
5. Gambar rib diagonal tebal 5mm
6. Tambahkan Sketch Fillet R5 pada sudut dalam
7. Tambahkan Sketch Fillet R3 pada sudut luar
8. Tambahkan Chamfer 2x2mm
9. Gambar 4 lubang mounting Ø8mm
10. Pastikan Fully Defined → Simpan

---

### Percobaan 10: Gambar Teknik Lengkap — Flange
**Tujuan**: Membuat gambar teknik lengkap profil flange

**Gambar yang harus dibuat:**
```
Spesifikasi:
Flange (tampak depan — profil lingkaran):
- Diameter luar flange: Ø120mm
- Diameter lubang center: Ø40mm
- Raised face diameter: Ø80mm (area yang menonjol)
- Bolt Circle Diameter (BCD): Ø95mm
- Jumlah lubang baut: 8 buah
- Diameter lubang baut: Ø12mm
- Lubang baut tersebar merata 360° (setiap 45°)
- Chamfer pada lubang center: 2x45°
- Ketebalan flange terlihat dari cross-section
- Semua simetris terhadap pusat
- Sketch harus Fully Defined
```

**Langkah-langkah:**
1. Buat sketch baru di Front Plane
2. Gambar Lingkaran luar Ø120mm di Origin
3. Gambar Lingkaran raised face Ø80mm (Concentric)
4. Gambar Lingkaran lubang center Ø40mm (Concentric)
5. Gambar Lingkaran BCD Ø95mm sebagai **Construction Line**
6. Gambar 1 lubang baut Ø12mm pada BCD di posisi 0°
7. Gunakan **Circular Sketch Pattern**: 8 lubang, 360°, Equal Spacing
8. Tambahkan Centerline sebagai cross-hair pada pusat
9. Tambahkan semua dimensi sesuai spesifikasi
10. Pastikan Fully Defined → Simpan

---

## 2.10 Tips dan Best Practices

### Do's ✅
1. Selalu mulai sketch dari Origin
2. Gunakan constraints sebelum dimensi
3. Buat sketch Fully Defined
4. Gunakan Construction Lines untuk referensi
5. Manfaatkan Mirror dan Pattern untuk efisiensi
6. Beri nama yang deskriptif pada sketch

### Don'ts ❌
1. Jangan membuat sketch Over Defined
2. Jangan menggunakan Fix constraint secara berlebihan
3. Jangan mengabaikan Design Intent
4. Jangan membuat sketch terlalu kompleks (pecah menjadi beberapa sketch)
5. Jangan lupa menyimpan file secara berkala

---

*Modul Praktikum CAD/CAM — Modul 2: CAD Gambar 2D*
*Disusun untuk keperluan pendidikan*
