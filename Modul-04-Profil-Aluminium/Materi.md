# MODUL 4: PROJECT CAD — DESAIN PROFIL ALUMINIUM

## Praktikum CAD/CAM — Pertemuan 4

---

## 4.1 Pendahuluan

Profil aluminium ekstrusi adalah komponen struktural yang sangat umum digunakan dalam industri manufaktur, terutama untuk membuat rangka mesin, konveyor, meja kerja, enclosure, dan struktur robot. Standar paling umum adalah profil aluminium seri **20xx, 30xx, 40xx, 45xx** (dalam mm).

---

## 4.2 Jenis-Jenis Profil Aluminium

### Seri Umum:

| Seri | Ukuran (mm) | Slot Width | Penggunaan |
|------|-------------|------------|------------|
| **2020** | 20 x 20 | 6mm | Struktur ringan, 3D printer |
| **2040** | 20 x 40 | 6mm | Frame mesin kecil |
| **2060** | 20 x 60 | 6mm | Frame mesin kecil-menengah |
| **3030** | 30 x 30 | 8mm | Struktur medium |
| **3060** | 30 x 60 | 8mm | Struktur medium |
| **4040** | 40 x 40 | 8mm | Struktur berat, mesin CNC |
| **4080** | 40 x 80 | 8mm | Struktur berat |
| **4545** | 45 x 45 | 10mm | Heavy duty |
| **4590** | 45 x 90 | 10mm | Heavy duty |

### Aksesoris Profil Aluminium:

| No | Aksesoris | Fungsi |
|----|-----------|--------|
| 1 | **T-Nut** | Mur yang masuk ke slot profil |
| 2 | **Corner Bracket** | Sambungan sudut 90° |
| 3 | **T-Bracket** | Sambungan T |
| 4 | **End Cap** | Penutup ujung profil |
| 5 | **Hinge** | Engsel untuk pintu/panel |
| 6 | **Panel Holder** | Penjepit panel/akrilik |
| 7 | **Leveling Foot** | Kaki adjuster |
| 8 | **Caster Wheel** | Roda untuk mobility |
| 9 | **Gusset Plate** | Plat penguat sudut |
| 10 | **Door Handle** | Handle pintu/panel |

---

## 4.3 Membaca Katalog Profil Aluminium

### Informasi dalam Katalog:
1. **Cross-section drawing** — Penampang profil dengan dimensi
2. **Slot dimension** — Ukuran alur (T-slot)
3. **Center bore** — Lubang tengah untuk mounting
4. **Weight** — Berat per meter (kg/m)
5. **Moment of inertia** — Ix, Iy untuk perhitungan struktur
6. **Material** — Umumnya Aluminum 6063-T5 atau 6061-T6

### Contoh Spesifikasi Profil 2020:
```
Cross Section: 20 x 20 mm
Slot Width: 6mm
Slot Depth: 6mm
Center Bore: Ø4.2mm (for M5)
Weight: 0.52 kg/m
Moment of Inertia Ix = Iy = 0.70 cm⁴
Material: Al 6063-T5
Surface: Natural anodized / Black anodized
```

---

## 4.4 Teknik Menggambar Profil Aluminium di SolidWorks

### Langkah Umum:
1. **Buat sketch penampang** (cross-section) sesuai katalog
2. **Extrude** sesuai panjang yang dibutuhkan
3. **Tambahkan detail**: lubang mounting, chamfer ujung
4. **Assign material**: Aluminum 6063-T5

### Tips Sketching Profil:
- Manfaatkan **simetri** — profil umumnya simetris 4 arah
- Gambar 1/4 profil → Mirror 2x
- Gunakan **Offset** untuk ketebalan dinding
- Perhatikan detail T-slot (undercut)

---

## 4.5 Percobaan 1-10: Desain Profil Aluminium

### Percobaan 1: Profil 2020 (20x20mm, 1 slot per sisi)
```
Spesifikasi dari katalog:
- Penampang: 20 x 20 mm
- T-slot: 6mm width, 6mm depth, setiap sisi
- Center bore: Ø4.2mm
- Ketebalan dinding: 1.5mm
- Fillet internal: R0.5
- Panjang extrude: 200mm

Langkah:
1. Gambar 1/4 penampang dari Origin (manfaatkan simetri)
2. Gambar T-slot pada sisi kanan dan atas
3. Mirror horizontal → Mirror vertikal → profil penuh
4. Gambar center bore Ø4.2mm
5. Extrude 200mm
6. Chamfer 0.5x45° pada ujung
7. Assign material Al 6063-T5
```

### Percobaan 2: Profil 2040 (20x40mm, 2 slot sisi panjang)
```
Spesifikasi:
- Penampang: 20 x 40 mm
- T-slot: 6mm, 1 slot sisi pendek, 2 slot sisi panjang
- Center bore: Ø4.2mm
- Internal cross rib
- Panjang: 300mm
```

### Percobaan 3: Profil 3030 (30x30mm)
```
Spesifikasi:
- Penampang: 30 x 30 mm
- T-slot: 8mm width
- Center bore: Ø6.8mm (for M8)
- Ketebalan dinding: 2mm
- Panjang: 250mm
```

### Percobaan 4: Profil 4040 (40x40mm)
```
Spesifikasi:
- Penampang: 40 x 40 mm
- T-slot: 8mm width, 10mm depth
- Center bore: Ø6.8mm
- Cross rib internal 4 arah
- Ketebalan dinding: 2mm
- Fillet internal: R1
- Panjang: 400mm
```

### Percobaan 5: Profil 4040 Light (40x40mm, versi ringan)
```
Spesifikasi:
- Penampang: 40 x 40 mm (versi ringan - less material)
- T-slot: 8mm
- Center bore: Ø6.8mm
- Tanpa internal cross rib (hanya perimeter)
- Panjang: 400mm
- Bandingkan berat dengan Percobaan 4
```

### Percobaan 6: Profil 4080 (40x80mm)
```
Spesifikasi:
- Penampang: 40 x 80 mm
- T-slot: 8mm, 2 slot per sisi pendek, 4 slot per sisi panjang
- 2 center bore: Ø6.8mm (jarak 40mm)
- Internal ribs
- Panjang: 500mm
```

### Percobaan 7: Corner Bracket (Aksesoris)
```
Spesifikasi:
- Bracket sudut 90° untuk profil 2020
- Material: Die-cast Zinc / Aluminum
- Dimensi: 20x20x17mm
- 2 lubang untuk M5 bolt
- Slot sesuai T-slot 6mm
```

### Percobaan 8: T-Nut dan Bolt Set (Aksesoris)
```
Spesifikasi:
- T-Nut untuk slot 6mm:
  - Lebar: 11mm, Tinggi: 5mm
  - Lubang berulir: M5
  - Drop-in type (spring loaded)
- Bolt M5x10mm (hex socket head)
- Washer M5
```

### Percobaan 9: End Cap (Aksesoris)
```
Spesifikasi:
- End cap untuk profil 2020: 20x20mm
- Material: Nylon/PP (plastik)
- Clip-on type (dengan spring tab)
- Ketebalan: 3mm
```

### Percobaan 10: Gusset Plate / Corner Plate (Aksesoris)
```
Spesifikasi:
- Gusset plate segitiga untuk penguat sudut
- Ukuran: 40x40mm
- Ketebalan: 4mm
- 2 slot untuk T-nut: 6mm
- Material: Aluminum 6061-T6
- Fillet R5 pada sudut luar
```

---

## 4.6 Referensi Katalog

Gunakan katalog dari produsen berikut sebagai referensi dimensi:
- **Bosch Rexroth** — Aluminum Structural Profiles
- **80/20 Inc** — T-Slot Aluminum
- **Item Profiles** — MB Building Kit System
- **Misumi** — Aluminum Extrusion

---

*Modul Praktikum CAD/CAM — Modul 4: Project Desain Profil Aluminium*
*Disusun untuk keperluan pendidikan*
