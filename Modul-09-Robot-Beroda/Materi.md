# MODUL 9: PROJECT CAD — ROBOT BERODA (DESAIN AKRILIK FLAT-PACK)

## Praktikum CAD/CAM — Pertemuan 9

---

## Daftar Isi
1. [Pendahuluan](#91-pendahuluan)
2. [Konsep Differential Drive](#92-konsep-differential-drive)
3. [Konsep Desain Flat-Pack Akrilik (2D → 3D)](#93-konsep-desain-flat-pack-akrilik-2d--3d)
4. [Komponen & BOM Robot Beroda](#94-komponen--bom-robot-beroda)
5. [Teknik Interlocking Tab-Slot](#95-teknik-interlocking-tab-slot)
6. [Koneksi ke Modul Realisasi](#96-koneksi-ke-modul-realisasi)
7. [Percobaan 1–10](#97-percobaan-110)

---

## 9.1 Pendahuluan

Robot beroda differential drive menggunakan **2 roda penggerak independen** dan **1–2 castor wheel** untuk stabilitas. Dalam praktikum ini, kita mendesain robot beroda yang **seluruh bodi/chassis-nya dibuat dari lembaran akrilik 2D** yang dipotong laser, kemudian **disusun/dirakit menjadi struktur 3D** seperti balok/kubus menggunakan teknik **interlocking tab-slot** (tanpa lem jika memungkinkan).

### Filosofi Desain: Balok 2D → 3D
```
Konsep:
┌─────────────┐     Laser Cut     ┌──────────┐     Assembly      ┌──────────┐
│ Lembaran    │  ──────────────→  │ Potongan  │  ────────────→   │ Struktur │
│ Akrilik 2D  │    (flat pieces)  │ 2D datar  │   (tab-slot)     │ 3D Kubus │
│ (3mm sheet) │                   │ 6 sisi    │                  │ Robot    │
└─────────────┘                   └──────────┘                   └──────────┘
```

Robot ini mirip konsep **flat-pack furniture** (seperti IKEA) — semua part adalah panel datar 2D yang ketika dirakit membentuk bodi 3D berbentuk **balok/kubus**.

### Keuntungan Desain Flat-Pack Akrilik:
- **Murah** — hanya butuh 1 lembar akrilik
- **Cepat produksi** — laser cut semua part sekaligus (nesting)
- **Presisi** — laser cut akurat ±0.1mm
- **Mudah dirakit** — interlocking tanpa perlu skill khusus
- **Transportable** — bisa dikirim dalam bentuk flat, dirakit di tempat
- **Modifiable** — mudah redesain dan laser cut ulang

---

## 9.2 Konsep Differential Drive

### Kinematika:
| Gerakan | Roda Kiri | Roda Kanan |
|---------|-----------|------------|
| **Maju lurus** | Maju, kecepatan V | Maju, kecepatan V |
| **Belok kiri** | Maju, kecepatan rendah | Maju, kecepatan tinggi |
| **Belok kanan** | Maju, kecepatan tinggi | Maju, kecepatan rendah |
| **Putar di tempat (CW)** | Maju, kecepatan V | Mundur, kecepatan V |
| **Putar di tempat (CCW)** | Mundur, kecepatan V | Maju, kecepatan V |

### Komponen Utama:
| No | Komponen | Fungsi | Material/Sumber |
|----|----------|--------|-----------------|
| 1 | Chassis Body (6 panel) | Bodi utama bentuk balok | Akrilik 3mm (Laser Cut) |
| 2 | Motor Mount (internal) | Penahan motor di dalam bodi | Akrilik 3mm (Laser Cut) |
| 3 | Drive Wheels (2×) | Roda penggerak | Beli (Ø65mm) |
| 4 | DC Motors (2×) | Motor penggerak | Beli (N20/130-size) |
| 5 | Castor Wheel (1–2×) | Stabilisasi | Beli (ball castor) |
| 6 | Battery Holder | Tempat baterai | Akrilik 3mm (Laser Cut) |
| 7 | Arduino/ESP32 Mount | Dudukan controller | Akrilik 3mm (Laser Cut) |
| 8 | Sensor Bracket | Bracket sensor | Akrilik 3mm (Laser Cut) |
| 9 | Top Cover | Penutup atas | Akrilik 3mm (Laser Cut) |
| 10 | Name Plate (engraving) | Identitas | Engrave di panel |

---

## 9.3 Konsep Desain Flat-Pack Akrilik (2D → 3D)

### 9.3.1 Bentuk Dasar: Balok/Kubus
```
Bodi robot berbentuk balok dengan 6 panel:

        ┌──────────────┐
       /│  TOP COVER   /│
      / │             / │
     /  │            /  │
    ┌───┼───────────┐   │
    │   │  SIDE R   │   │  Ukuran: ~150 × 120 × 80mm (P×L×T)
    │   └───────────┼───┘
    │  /  BOTTOM    │  /
    │ /  (chassis)  │ /
    │/              │/
    └───────────────┘
    
    6 Panel:
    1. BOTTOM (chassis utama) — lubang motor, castor, wiring
    2. TOP (cover) — lubang akses, ventilasi, mounting sensor atas
    3. FRONT — lubang sensor ultrasonic, bumper
    4. BACK — lubang switch, USB, charging port
    5. SIDE LEFT — slot roda kiri, lubang motor shaft
    6. SIDE RIGHT — slot roda kanan, lubang motor shaft
```

### 9.3.2 Dimensi Balok Robot
| Parameter | Nilai |
|-----------|-------|
| Panjang (P) | 150 mm |
| Lebar (L) | 120 mm |
| Tinggi (T) | 80 mm |
| Material | Akrilik 3mm |
| Tebal dinding | 3mm (= 1 layer akrilik) |

### 9.3.3 Tab-Slot pada Setiap Edge
Setiap edge (rusuk) balok memiliki tab-slot interlocking:
```
Panel A (dengan tab):         Panel B (dengan slot):
┌────────────────────┐        ┌──┐    ┌──┐    ┌──┐
│    ┌──┐  ┌──┐     │        │  │    │  │    │  │
│    │  │  │  │     │   →    │  └────┘  └────┘  │
│    │  │  │  │     │        │                   │
└────┘  └──┘  └─────┘        └───────────────────┘

Tab: 10mm wide × 3mm deep (= material thickness)
Slot: 10.15mm wide × 3.15mm deep (toleransi +0.15mm)
Jarak antar tab: 15–20mm
```

### 9.3.4 Internal Support & Divider
Selain 6 panel luar, tambahkan panel internal:
- **Motor Mount Panel** — panel vertikal internal untuk mounting motor
- **Battery Divider** — pemisah kompartemen baterai
- **PCB Shelf** — rak horizontal untuk Arduino/driver

```
Tampak atas (tanpa top cover):
┌───────────────────────────────┐
│                               │
│  ┌─────────┐   ┌──────────┐  │
│  │ Motor L │   │ Motor R  │  │
│  └────┬────┘   └────┬─────┘  │
│       │              │        │
│  ─────┼──────────────┼─────  │ ← Motor mount panel (internal)
│       │              │        │
│  ┌────┴──────────────┴─────┐  │
│  │     Arduino / Driver     │  │ ← PCB shelf
│  └──────────────────────────┘  │
│  ┌──────────────────────────┐  │
│  │       Battery area       │  │
│  └──────────────────────────┘  │
└───────────────────────────────┘
```

---

## 9.4 Komponen & BOM Robot Beroda

| No | Part | Qty | Material | Proses | DXF? |
|----|------|-----|----------|--------|------|
| 1 | Bottom Panel (Chassis) | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 2 | Top Panel (Cover) | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 3 | Front Panel | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 4 | Back Panel | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 5 | Side Panel Left | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 6 | Side Panel Right | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 7 | Motor Mount Panel (internal) | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 8 | PCB Shelf (internal) | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 9 | Battery Holder Bracket | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 10 | Sensor Bracket (front) | 1 | Akrilik 3mm | Laser Cut | ✅ |
| 11 | **Name Plate (engrave)** | 1 | Pada Top/Front panel | **Laser Engrave** | ✅ |
| 12 | Drive Wheel | 2 | Rubber/Plastic Ø65mm | Beli | — |
| 13 | DC Motor N20 / 130-size | 2 | Motor DC | Beli | — |
| 14 | Ball Castor | 1–2 | Metal Ø15mm | Beli | — |
| 15 | Arduino Uno / ESP32 | 1 | PCB | Beli | — |
| 16 | Motor Driver L298N / L293D | 1 | PCB | Beli | — |
| 17 | Battery (4×AA atau Li-Po) | 1 set | Elektronik | Beli | — |
| 18 | Sensor Ultrasonic HC-SR04 | 1 | Elektronik | Beli | — |
| 19 | Fasteners (M3 bolts, nuts, standoffs) | ~20 | Hardware | Beli | — |

---

## 9.5 Teknik Interlocking Tab-Slot

### 9.5.1 Dimensi Tab-Slot untuk Akrilik 3mm
| Parameter | Nilai | Keterangan |
|-----------|-------|------------|
| Tab width | 10 mm | Lebar tab |
| Tab depth | 3.00 mm | = ketebalan material |
| Slot width | 10.15 mm | Tab + toleransi 0.15mm |
| Slot depth | 3.15 mm | Tab depth + 0.15mm |
| Tab spacing | 15–20 mm | Jarak center-to-center |
| Min tabs per edge | 2 | Untuk edge pendek (80mm) |
| Max tabs per edge | 4 | Untuk edge panjang (150mm) |

### 9.5.2 Kerf Compensation
- Laser kerf ≈ 0.15mm (material yang hilang karena laser)
- **Tab** (bagian yang menonjol): jadi lebih kecil → OK, sedikit loose
- **Slot** (lubang): jadi lebih besar → OK, memberikan clearance
- Jika terlalu loose: kurangi slot width 0.05mm
- Jika terlalu tight: tambah slot width 0.05mm
- Selalu **test cut** dulu sebelum potong final!

### 9.5.3 Tips Assembly
- Rakit **bottom dulu** → side panels → front/back → internal → top
- Gunakan **lem akrilik** (solvent cement) untuk joint permanen
- Atau cukup **press-fit** untuk assembly bongkar-pasang
- Tab-slot yang presisi bisa self-holding tanpa lem

---

## 9.6 Koneksi ke Modul Realisasi

### Peta Fabrikasi
```
┌─────────────────────────────┐
│ MODUL 9 (ini)               │
│ Robot Beroda — CAD Design   │
│ Semua part flat-pack akrilik│
│ Export: DXF (semua panel)   │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ MODUL 10 — Laser Cutting    │
│                             │
│ • Laser cut semua panel     │
│ • Engrave nama pada panel   │
│ • Engrave tulisan/logo      │
│ • Nesting di 1 sheet akrilik│
│ • Assembly robot fisik      │
└─────────────────────────────┘
```

### Yang Harus Disiapkan untuk Modul 10:
1. **DXF semua panel** (10+ part) — dengan layer cut dan engrave
2. **Nesting layout** — semua part muat di 1 sheet akrilik (300×400mm atau 400×600mm)
3. **Warna layer**:
   - **Merah**: cutting (kontur luar + lubang)
   - **Biru**: engraving vektor (logo, motif)
   - **Hitam**: raster engraving (teks nama, NIM)
4. **Assembly sequence** — urutan perakitan yang jelas

---

## 9.7 Percobaan 1–10

### Percobaan 1: Bottom Panel / Chassis
```
Spesifikasi:
- Material: Akrilik 3mm
- Ukuran: 150 × 120 mm
- Lubang motor mount: 2 set (sesuai motor N20/130-size)
- Lubang castor: 1–2 set (Ø3mm × 4, sesuai pattern castor)
- Lubang Arduino mount: 4× Ø3mm (sesuai pattern Arduino)
- Slot kabel: 2× slot 10×5mm
- Tab pada 4 sisi: sesuai koneksi ke side/front/back panel
- Slot pada center: untuk motor mount panel internal

Langkah SolidWorks:
1. New Part → Sketch rectangle 150×120mm
2. Tambahkan tab pattern di 4 sisi (10mm wide, 3mm deep)
3. Buat lubang motor mounting (sesuai datasheet motor)
4. Buat lubang castor wheel mounting
5. Buat lubang Arduino mounting (68.6×53.4mm pattern)
6. Tambahkan slot untuk motor mount panel internal
7. Extrude 3mm
8. Export DXF
```

### Percobaan 2: Side Panel Left & Right (Simetris)
```
Spesifikasi:
- Material: Akrilik 3mm
- Ukuran: 150 × 80 mm (panjang × tinggi)
- Slot roda: cutout Ø65mm semi-circle atau slot U untuk roda
- Lubang motor shaft: Ø6mm (untuk shaft motor menembus)
- Tab pada 3 sisi (bawah, depan, belakang) → koneksi ke panel lain
- Slot pada bagian atas → koneksi ke top panel
- Slot internal → koneksi ke motor mount panel & PCB shelf

Langkah:
1. Sketch 150×80mm rectangle
2. Buat cutout roda: U-shape atau semi-circle di posisi motor
3. Tambahkan lubang shaft motor
4. Buat tab/slot pattern di setiap edge
5. Sisi kiri dan kanan: Mirror (atau Save As → edit jika tidak simetris)
6. Extrude 3mm
7. Export DXF (2 file: left & right, atau 1 file jika identik)
```

### Percobaan 3: Front Panel
```
Spesifikasi:
- Material: Akrilik 3mm
- Ukuran: 120 × 80 mm (lebar × tinggi)
- Lubang sensor ultrasonic: 2× Ø16mm (jarak center 26mm)
- Lubang LED indicator: 2–3× Ø5mm
- Tab pada 3 sisi (bawah, kiri, kanan) → koneksi
- Slot pada atas → koneksi ke top panel
- Engraving: logo/motif dekoratif (opsional)

Langkah:
1. Sketch 120×80mm rectangle
2. Buat lubang sensor HC-SR04 (2× Ø16mm, center 26mm apart)
3. Tambahkan lubang LED
4. Buat tab/slot pattern
5. Extrude 3mm
6. Tambahkan sketch untuk engraving (Extruded Cut 0.3mm)
7. Export DXF (pisahkan layer cut & engrave)
```

### Percobaan 4: Back Panel
```
Spesifikasi:
- Material: Akrilik 3mm
- Ukuran: 120 × 80 mm
- Lubang switch ON/OFF: Ø12mm atau slot 12×8mm
- Lubang USB port: slot 12×7mm (untuk akses USB Arduino)
- Lubang charging port: Ø5.5mm (DC jack) — opsional
- Lubang ventilasi: pattern 4× Ø5mm
- Tab/slot pattern di setiap edge

Langkah:
1. Sketch 120×80mm rectangle
2. Buat cutout switch, USB, charging
3. Buat ventilation holes (Circular/Linear Pattern)
4. Tab/slot pattern
5. Extrude 3mm
6. Export DXF
```

### Percobaan 5: Top Panel / Cover + ENGRAVING NAMA
```
Spesifikasi:
- Material: Akrilik 3mm
- Ukuran: 150 × 120 mm
- Lubang ventilasi: pattern dekoratif (hex/circle)
- Lubang akses: 1× slot besar 40×20mm (untuk kabel/akses)
- Slot koneksi: di 4 sisi (ke side/front/back)
- ★ ENGRAVING NAMA: Nama mahasiswa + NIM + "ROBOT BERODA"
- ★ ENGRAVING LOGO: Logo kampus/prodi (opsional)
- ★ ENGRAVING MOTIF: Dekoratif (garis, pattern, dll.)

Langkah:
1. Sketch 150×120mm rectangle
2. Buat ventilation pattern (Circular/Linear Pattern)
3. Buat access slot
4. Tab/slot pattern di 4 sisi
5. PENTING — Sketch Text → Nama, NIM, "ROBOT BERODA"
6. Extruded Cut 0.3mm (engrave) untuk teks
7. Tambahkan logo/motif dekoratif (sketch curves)
8. Extrude 3mm (panel) + Cut 0.3mm (engrave)
9. Export DXF:
   - Layer MERAH: cutting (outline + lubang)
   - Layer HITAM: raster engrave (teks nama)
   - Layer BIRU: vektor engrave (logo/motif)
```

### Percobaan 6: Motor Mount Panel (Internal)
```
Spesifikasi:
- Material: Akrilik 3mm
- Panel vertikal internal, posisi di tengah chassis
- Ukuran: 120 × 50 mm (lebar × tinggi internal)
- Lubang motor mount: 2 set (kiri & kanan)
  - Motor N20: 2× Ø3mm + slot clamp
  - Motor 130-size: Ø25mm center + 2× Ø3mm tab
- Tab di bawah: koneksi ke bottom panel
- Tab di samping: koneksi ke side panels

Langkah:
1. Sketch 120×50mm
2. Buat lubang motor sesuai datasheet
3. Tab pattern di bawah dan samping
4. Extrude 3mm
5. Export DXF
```

### Percobaan 7: PCB Shelf & Battery Bracket (Internal)
```
PCB Shelf:
- Material: Akrilik 3mm
- Panel horizontal internal (rak untuk Arduino)
- Ukuran: 80 × 60 mm
- Lubang standoff Arduino: 4× Ø3mm
- Tab di 2 sisi (koneksi ke side panels)

Battery Bracket:
- Material: Akrilik 3mm
- L-shape atau flat bracket
- Ukuran sesuai battery holder (4×AA atau Li-Po)
- Tab koneksi ke bottom panel

Langkah:
1. Desain PCB shelf → tab di 2 sisi
2. Desain battery bracket
3. Extrude 3mm masing-masing
4. Export DXF
```

### Percobaan 8: Sensor Bracket (External/Front)
```
Spesifikasi:
- Material: Akrilik 3mm
- Bracket untuk HC-SR04 (menempel di front panel)
- Adjustable angle: tab-slot dengan beberapa posisi
- Ukuran: 50 × 30 mm
- Lubang sensor: 2× Ø16mm, jarak 26mm
- Mounting: tab ke front panel

Opsional — Bumper:
- Akrilik 3mm, bentuk arc
- Mounting di depan front panel
- Bisa menampung micro switch

Langkah:
1. Sketch bracket → lubang sensor → tab
2. Extrude 3mm
3. Export DXF
```

### Percobaan 9: Verifikasi Assembly & Nesting DXF
```
Assembly Robot Lengkap:
1. Assembly SolidWorks — rakit semua panel:
   - Bottom → Side L + Side R → Front + Back → Motor Mount → PCB Shelf → Top
2. Tambahkan komponen beli:
   - 2× Motor + Wheel
   - 1× Castor wheel
   - 1× Arduino Uno
   - 1× Battery holder
   - 1× Sensor HC-SR04
3. Verifikasi:
   - Semua tab-slot masuk (tidak interferensi)
   - Roda menyentuh ground (clearance OK)
   - Motor shaft menembus side panel ke wheel
   - Sensor terlihat dari depan
   - Kabel bisa diakses
4. Exploded View + BOM

Nesting DXF (untuk Modul 10):
5. Kumpulkan semua DXF panel
6. Buka CorelDRAW → import semua
7. Nesting di sheet akrilik (300×400mm atau 400×600mm)
8. Pastikan semua muat dalam 1 sheet
9. Atur jarak antar part: min 3mm
10. Layer: Merah (cut), Hitam (engrave teks), Biru (engrave vektor)
```

### Percobaan 10: Drawing Package & Export Final
```
Drawing Package:
1. Assembly Drawing — tampak depan, samping, atas + dimensi overall
2. Exploded View Drawing — dengan balloon nomor sesuai BOM
3. Individual Part Drawing — minimal 3 panel (bottom, side, top)
4. Flat Pattern Layout — semua panel di 1 sheet (nesting)

Export Files:
5. DXF semua panel → folder DXF/
6. Assembly file → .sldasm
7. BOM → Excel/PDF dengan kolom:
   | No | Part | Qty | Material | Proses | DXF file |
8. Assembly Sequence Document:
   - Langkah 1: Pasang motor di motor mount panel
   - Langkah 2: Pasang motor mount panel ke bottom
   - Langkah 3: Pasang side panels
   - dst.

Video preparation:
9. Screen record assembly SolidWorks
10. Dokumentasi nesting layout
```

---

## 9.8 Variasi Desain (Opsional)
Eksplorasi bentuk bodi selain balok:
1. **Hexagonal** — 6 panel sisi + top + bottom
2. **Wedge** — depan rendah, belakang tinggi (aerodinamis)
3. **Stepped** — 2 tingkat (deck atas lebih kecil)
4. **Cylindrical** — panel lengkung (memerlukan bending — bisa di Modul 14)

---

*Modul Praktikum CAD/CAM — Modul 9: Project Robot Beroda*
*Disusun untuk keperluan pendidikan*
