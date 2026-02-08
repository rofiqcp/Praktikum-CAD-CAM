# MODUL 8: PROJECT CAD — DESAIN KONVEYOR BELT MINI

## Praktikum CAD/CAM — Pertemuan 8

---

## Daftar Isi
1. [Pendahuluan](#81-pendahuluan)
2. [Konsep Konveyor Belt](#82-konsep-konveyor-belt)
3. [Komponen dan BOM Konveyor](#83-komponen-dan-bom-konveyor)
4. [Motor Stepper NEMA 17](#84-motor-stepper-nema-17)
5. [Profil Aluminium sebagai Rangka](#85-profil-aluminium-sebagai-rangka)
6. [Dudukan & Holder dari Akrilik (Laser Cut)](#86-dudukan--holder-dari-akrilik-laser-cut)
7. [Part Milling (CNC Router)](#87-part-milling-cnc-router)
8. [Sistem Transmisi & Roller](#88-sistem-transmisi--roller)
9. [Koneksi Antar-Modul (Realisasi)](#89-koneksi-antar-modul-realisasi)
10. [Percobaan 1–10](#810-percobaan-110)

---

## 8.1 Pendahuluan

Konveyor (conveyor) adalah sistem transportasi material yang banyak digunakan di industri manufaktur, logistik, dan packaging. Dalam praktikum ini, kita akan mendesain **Belt Conveyor Mini** yang **siap direalisasikan** dengan kombinasi tiga proses manufaktur:

| Proses Manufaktur | Part yang Dibuat | Modul Realisasi |
|-------------------|------------------|-----------------|
| **Laser Cutting Akrilik** | Dudukan/holder motor, bearing housing, end plate, side guide | Modul 10 / 14 |
| **CNC Router Milling** | Part struktural (bearing block, coupler adapter, mounting plate), ukiran nama | Modul 13 |
| **Profil Aluminium** | Frame/rangka utama | Dibeli / kit |

> **Penting:** Desain konveyor di modul ini menjadi **dasar project** yang akan difabrikasi nyata di Modul 10 (Laser Cutting), Modul 13 (Router Milling), dan Modul 14 (Laser + Bending Akrilik). Pastikan desain Anda **feasible** untuk diproduksi!

---

## 8.2 Konsep Konveyor Belt

### 8.2.1 Prinsip Kerja
Belt conveyor menggunakan sabuk (belt) yang berputar di antara dua roller:
- **Drive Roller** — roller penggerak yang dihubungkan ke motor stepper
- **Idler Roller** — roller pembalik di ujung lain yang bisa diatur posisinya (tensioning)

Material/benda diletakkan di atas belt dan berpindah dari satu ujung ke ujung lain.

### 8.2.2 Parameter Desain
| Parameter | Nilai (Mini Conveyor) |
|-----------|----------------------|
| Panjang belt area | 300–400 mm |
| Lebar belt | 60–100 mm |
| Kecepatan belt | 10–100 mm/s (adjustable via stepper) |
| Kapasitas beban | < 500 gram |
| Motor | **NEMA 17 Stepper** (1.8°/step) |
| Kontrol | Arduino + Driver A4988/DRV8825 |

### 8.2.3 Mengapa Stepper NEMA 17?
- **Presisi** — 200 steps/revolution, bisa microstepping hingga 3200 steps/rev
- **Torsi cukup** — 0.4–0.6 Nm (holding torque) untuk mini conveyor
- **Kontrol kecepatan** — bisa mengontrol RPM dengan mengubah frekuensi pulse
- **Kontrol posisi** — bisa mengontrol jarak perpindahan belt dengan tepat
- **Mudah didapat** — standar industri, banyak digunakan di 3D printer & CNC
- **Driver murah** — A4988 / DRV8825 / TMC2208

### 8.2.4 Perhitungan Sederhana
```
Kecepatan Belt:
v = π × D × (RPM / 60)

Contoh:
- Diameter roller D = 25mm = 0.025m
- Stepper: 200 step/rev, driver 1/16 microstepping = 3200 step/rev
- Step frequency = 1600 Hz → RPM = 1600/3200 × 60 = 30 RPM
- v = π × 0.025 × (30/60) = 0.039 m/s ≈ 39 mm/s

Torsi yang dibutuhkan:
τ = F × r
- Beban max 500g = 4.9N, friction µ=0.3 → F = 1.47N
- r = 12.5mm = 0.0125m
- τ = 1.47 × 0.0125 = 0.018 Nm → jauh di bawah 0.4Nm NEMA17 ✓
```

---

## 8.3 Komponen dan BOM Konveyor

| No | Komponen | Qty | Material/Sumber | Proses Manufaktur |
|----|----------|-----|-----------------|-------------------|
| 1 | Frame Samping | 2 | Profil Al 2040, 400mm | Dipotong/beli |
| 2 | Cross Member | 4 | Profil Al 2020, 120mm | Dipotong/beli |
| 3 | End Plate Motor Side | 2 | Akrilik 5mm | **Laser Cut** |
| 4 | End Plate Idler Side | 2 | Akrilik 5mm | **Laser Cut** |
| 5 | Motor Bracket/Holder | 1 | Akrilik 5mm | **Laser Cut** |
| 6 | Bearing Housing | 4 set | Akrilik 5mm (×2 stack) | **Laser Cut** |
| 7 | Side Guide | 2 | Akrilik 3mm | **Laser Cut** |
| 8 | Bearing Block | 2 | MDF/Kayu 18mm | **CNC Milling** |
| 9 | Motor Mounting Plate | 1 | MDF/Kayu 18mm | **CNC Milling** |
| 10 | Name Plate (ukiran) | 1 | MDF/Kayu 18mm | **CNC Milling** |
| 11 | Drive Roller | 1 | Pipa Alu/PVC Ø25mm | Beli/modifikasi |
| 12 | Idler Roller | 1 | Pipa Alu/PVC Ø25mm | Beli/modifikasi |
| 13 | Belt | 1 | Flat belt / timing belt | Beli |
| 14 | Stepper NEMA 17 | 1 | 42BYGH motor | Beli |
| 15 | Bearing 608ZZ | 4 | Ø22×8mm, bore Ø8mm | Beli |
| 16 | Shaft Ø8mm | 2 | Stainless steel, 150mm | Beli |
| 17 | Coupler 5mm→8mm | 1 | Aluminum rigid coupler | Beli |
| 18 | Fasteners | ~30 | M3, M4, M5 + T-nut | Beli |
| 19 | Support Legs | 4 | Profil Al 2020, 150mm | Dipotong/beli |
| 20 | Arduino + A4988 + PSU | 1 set | Elektronik | Beli |

---

## 8.4 Motor Stepper NEMA 17

### 8.4.1 Spesifikasi Umum
| Parameter | Nilai |
|-----------|-------|
| Frame Size | 42 × 42 mm |
| Step Angle | 1.8° (200 steps/rev) |
| Shaft Diameter | Ø5mm, D-cut |
| Shaft Length | 24mm |
| Mounting Holes | 4× M3, PCD 31mm |
| Mounting Pattern | □ 31 × 31 mm (center-to-center) |
| Body Length | 34–48 mm |
| Holding Torque | 0.4–0.6 Nm |
| Rated Current | 1.2–1.7 A/phase |
| Weight | 280–350 gram |

### 8.4.2 Dimensi Mounting NEMA 17
```
         42mm
    ┌──────────────┐
    │ ○          ○ │  ← Mounting holes M3 (×4)
    │              │
    │    ┌────┐    │  ← Center pilot Ø22mm, depth 2mm
    │    │ D  │    │  ← Shaft Ø5mm, D-cut flat
    │    └────┘    │
    │              │
    │ ○          ○ │  ← Hole spacing: 31 × 31mm
    └──────────────┘     (±15.5mm dari center)
         42mm
```

### 8.4.3 Kontrol Stepper Motor
```
Wiring Diagram:
Arduino Uno → A4988 Driver Board → NEMA 17 Stepper
                  │
                  ├── VMOT: 12V Power Supply (≥1A)
                  ├── GND: Common ground (Arduino + PSU)
                  ├── STEP: Arduino Digital Pin (D3) — pulse = 1 step
                  ├── DIR: Arduino Digital Pin (D4) — HIGH/LOW = CW/CCW
                  ├── EN: Arduino Digital Pin (D5) — LOW = enabled
                  ├── MS1,MS2,MS3: Microstepping (all HIGH = 1/16)
                  └── 1A,1B,2A,2B: Motor coil wires

Kode Arduino Sederhana:
  #define STEP_PIN 3
  #define DIR_PIN 4
  
  void setup() {
    pinMode(STEP_PIN, OUTPUT);
    pinMode(DIR_PIN, OUTPUT);
    digitalWrite(DIR_PIN, HIGH); // arah CW
  }
  
  void loop() {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(500);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(500);
    // Frekuensi = 1000 Hz → RPM = 1000/200 × 60 = 300 RPM (full step)
  }
```

---

## 8.5 Profil Aluminium sebagai Rangka

### 8.5.1 Profil 2040 (Frame Samping)
| Parameter | Nilai |
|-----------|-------|
| Cross-section | 20 × 40 mm |
| T-slot width | 6mm (untuk M5 T-nut) |
| Panjang | 400mm |
| Jumlah | 4 batang (2 atas + 2 bawah, per sisi) |

### 8.5.2 Profil 2020 (Cross Member & Legs)
| Parameter | Nilai |
|-----------|-------|
| Cross-section | 20 × 20 mm |
| T-slot width | 6mm |
| Panjang Cross Member | 120mm (lebar konveyor) |
| Panjang Legs | 150mm |

### 8.5.3 Aksesori Profil Aluminium
| Aksesori | Fungsi | Qty |
|----------|--------|-----|
| Corner Bracket (L) | Sambungan sudut 90° | 12–16 |
| T-Nut M5 | Mur geser di slot profil | 30+ |
| T-Bolt M5×10 | Baut untuk T-nut | 30+ |
| End Cap 2020 | Penutup ujung profil | 8 |
| End Cap 2040 | Penutup ujung profil | 4 |

---

## 8.6 Dudukan & Holder dari Akrilik (Laser Cut)

### 8.6.1 Mengapa Akrilik?
- Mudah dipotong laser cutter (presisi ±0.1mm)
- Cukup kuat untuk holder/bracket mini conveyor
- Transparan → estetis, bisa melihat mekanisme internal
- Bisa di-stack (ditumpuk) untuk ketebalan/kekuatan ekstra
- Harga terjangkau, mudah didapat

### 8.6.2 Part Akrilik yang Harus Didesain

#### A. End Plate Motor Side (2 pcs, akrilik 5mm)
```
Spesifikasi:
- Ukuran: 120 × 80 mm, fillet R5
- Lubang center shaft: Ø8.5mm
- Lubang NEMA 17 mounting: 4× Ø3.5mm, pattern 31×31mm
- Center pilot NEMA 17: Ø22.5mm
- Lubang mounting ke profil: 4× slot 5.5×10mm (untuk M5 T-nut)
- Engraving teks: "MOTOR SIDE"
```

#### B. End Plate Idler Side (2 pcs, akrilik 5mm)
```
Spesifikasi:
- Ukuran: 120 × 80 mm, fillet R5
- Slot tensioning shaft: 8.5 × 20mm (horizontal, untuk adjust posisi idler)
- Lubang mounting ke profil: 4× slot 5.5×10mm
- Engraving teks: "IDLER SIDE"
```

#### C. Motor Bracket/Holder (1 pc, akrilik 5mm)
```
Spesifikasi:
- L-bracket (2 piece tab-slot assembly)
- Lubang NEMA 17: pattern 31×31mm, 4× Ø3.5mm
- Center pilot: Ø22.5mm
- Tab-slot: slot = 5.15mm (akrilik 5mm + toleransi 0.15mm)
- Mounting ke profil aluminium via T-nut
```

#### D. Bearing Housing (4 set, akrilik 5mm × 2 layer)
```
Spesifikasi:
- Ukuran per layer: 40 × 30 mm
- Bearing seat: Ø22mm (press fit bearing 608ZZ, OD=22mm)
- Mounting holes: 2× Ø4mm
- Total: 8 pieces akrilik (4 housing × 2 layer = 10mm per housing)
- Versi drive: lubang bulat
- Versi idler: slot horizontal untuk tensioning
```

#### E. Side Guide (2 pcs, akrilik 3mm)
```
Spesifikasi:
- Ukuran: 350 × 25 mm
- 3× slot mounting 5.5×10mm (untuk M5 T-nut)
- Jarak dari belt: adjustable
```

### 8.6.3 Tips Desain Akrilik untuk Laser Cut
1. **Toleransi lubang**: +0.1mm dari nominal
2. **Tab-slot**: slot width = material thickness + 0.15mm
3. **Fillet sudut dalam**: R ≥ 1mm (laser tidak bisa sudut dalam tajam sempurna)
4. **Jarak lubang ke tepi**: minimum 2× ketebalan material
5. **Kerf**: ~0.15mm (kompensasi saat dibutuhkan press-fit)
6. **DXF layer**: pisahkan cut (merah) dan engrave (biru/hitam)

---

## 8.7 Part Milling (CNC Router)

### 8.7.1 Mengapa Perlu Part Milling?
Part tertentu membutuhkan **ketebalan** dan **fitur 3D** yang tidak bisa dibuat laser cutting (2D only):
- **Bearing block** — perlu **pocket** (ceruk) untuk bearing seat dengan kedalaman tertentu
- **Motor mounting plate** — perlu **recess** untuk face motor
- **Name plate** — perlu **engraving 3D / ukiran relief** yang memiliki kedalaman bervariasi

### 8.7.2 Part yang Akan Di-Milling (Direalisasikan di Modul 13)

#### A. Bearing Block (2 pcs, MDF/Kayu 18mm)
```
Spesifikasi:
- Ukuran: 50 × 40 × 18 mm
- Pocket bearing seat: Ø22mm, depth 8mm
- Through hole shaft: Ø8.5mm (menerus)
- Mounting holes: 2× Ø5mm (countersunk)
- Chamfer edge: 2mm × 45°

Operasi CNC yang diperlukan:
1. Face — ratakan permukaan atas
2. 2D Pocket — bearing seat Ø22mm, depth 8mm
3. Drill — shaft hole Ø8.5mm + mounting holes
4. 2D Contour — profil luar + chamfer
```

#### B. Motor Mounting Plate (1 pc, MDF/Kayu 18mm)
```
Spesifikasi:
- Ukuran: 60 × 60 × 18 mm
- Center hole: Ø22.5mm (NEMA 17 pilot)
- Mounting holes: 4× Ø3.5mm, pattern 31×31mm
- Pocket recess: Ø38mm, depth 5mm (motor face clearance)
- Mounting ke frame: 4× Ø5mm

Operasi CNC:
1. Face
2. 2D Pocket — motor recess Ø38mm
3. Drill — all holes
4. 2D Contour — profil luar
```

#### C. Name Plate / Label (1 pc, MDF/Kayu 18mm)
```
Spesifikasi:
- Ukuran: 100 × 40 × 18 mm
- Pocket background: depth 3mm (area sekitar teks)
- Teks timbul (relief): teks menonjol 3mm dari pocket
  → Nama / NIM / "MINI CONVEYOR"
- Border: chamfer atau profil dekoratif
- Mounting: 2× Ø4mm

Operasi CNC:
1. Face — ratakan
2. 2D Pocket — background area (teks jadi timbul)
3. Engrave — detail kecil pada teks
4. 2D Contour — profil luar dekoratif
5. Drill — mounting holes
```

---

## 8.8 Sistem Transmisi & Roller

### 8.8.1 Drive System
```
Opsi 1 — Direct Coupling:
NEMA 17 (Ø5mm shaft) → Rigid Coupler 5→8mm → Shaft Ø8mm → Drive Roller

Opsi 2 — Belt/Pulley:
NEMA 17 → GT2 Pulley 20T → GT2 Belt → GT2 Pulley 20T → Shaft → Drive Roller
(Rasio 1:1, atau ganti jumlah teeth untuk speed/torque ratio)
```

### 8.8.2 Roller Assembly
```
Bearing 608ZZ ← Shaft Ø8mm → Roller Tube Ø25×100mm → Shaft Ø8mm → Bearing 608ZZ
     │                                                                    │
 Bearing Housing                                                   Bearing Housing
   (Akrilik stacked)                                                 (Akrilik stacked)
     │                                                                    │
  End Plate ──────────── Frame Profil Aluminium ──────────────── End Plate
```

### 8.8.3 Belt Tensioning System
- Idler roller dipasang di **slot** (bukan lubang bulat) pada end plate idler
- Slot horizontal memungkinkan penggeseran posisi idler ±10mm
- Belt tension diatur dengan menggeser idler **menjauhi** drive roller
- Setelah tension optimal → kunci dengan baut M8 + washer + wing nut
- Opsional: pegas/spring untuk auto-tension

---

## 8.9 Koneksi Antar-Modul (Realisasi)

### Peta Realisasi Konveyor
```
┌──────────────────────────────┐
│ MODUL 8 (ini)                │  → Desain CAD lengkap semua part
│ Project Konveyor — CAD       │  → Assembly, BOM, Drawing
│                              │  → Export: DXF + STEP + STL
└──────────┬───────────────────┘
           │
     ┌─────┼──────────────────────────┐
     ▼     ▼                          ▼
┌──────────────┐  ┌────────────────┐  ┌─────────────────┐
│ MODUL 10     │  │ MODUL 13       │  │ MODUL 14        │
│ Laser Cut    │  │ CNC Milling    │  │ Laser + Bending │
│              │  │                │  │                 │
│ • End plates │  │ • Bearing      │  │ • Casing box    │
│ • Holders    │  │   block        │  │   (opsional)    │
│ • Bearing    │  │ • Mounting     │  │                 │
│   housing    │  │   plate        │  │                 │
│ • Side guide │  │ • Name plate   │  │                 │
│              │  │   (ukiran nama)│  │                 │
└──────────────┘  └────────────────┘  └─────────────────┘
```

### Checklist Export File
| Part | Format Export | Untuk Modul |
|------|-------------|-------------|
| End plates, holders, guides, bearing housing | **DXF** (flat 2D) | Modul 10 (Laser Cut) |
| Bearing block, motor mounting plate | **STEP** (3D) | Modul 13 (CNC Milling) |
| Name plate (ukiran) | **STEP** (3D) | Modul 13 (CNC Milling) |
| Part opsional (cable clip, cover, dll.) | **STL** (3D) | Modul 12 (3D Print) |

---

## 8.10 Percobaan 1–10

### Percobaan 1: Frame Samping (Profil Aluminium 2040)
```
Spesifikasi:
- 2 batang profil 2040 × 400mm (horizontal atas & bawah)
- 2 batang profil 2040 × 120mm (tiang vertikal ujung)
- Corner bracket di 4 sudut

Langkah SolidWorks:
1. Buat sketch cross-section profil 2040 (20×40mm dengan T-slot)
2. Extrude 400mm → simpan sebagai part
3. Assembly: 2 horizontal + 2 vertikal → 1 frame sisi
4. Tambahkan corner bracket di setiap sudut
5. Verifikasi dimensi: 400mm panjang × ~160mm tinggi
```

### Percobaan 2: Cross Member, Legs & Rangka Lengkap
```
Spesifikasi:
- 4 batang profil 2020 × 120mm (cross member atas & bawah)
- 4 batang profil 2020 × 150mm (support legs)
- Corner bracket penghubung

Langkah:
1. Assembly: hubungkan 2 frame samping (P1) dengan 4 cross member
2. Tambahkan 4 legs di bawah frame
3. Tambahkan cross brace antar legs (opsional)
4. Verifikasi: rangka square, stabil, semua mate benar
```

### Percobaan 3: End Plate Motor Side (Akrilik 5mm — untuk Laser Cut)
```
Spesifikasi:
- Material: Akrilik 5mm
- Ukuran: 120 × 80 mm, fillet R5 pada 4 sudut
- Lubang center shaft: Ø8.5mm
- Lubang NEMA 17: 4× Ø3.5mm, pattern 31×31mm (±15.5mm dari center)
- Center pilot NEMA 17: Ø22.5mm
- Lubang mounting profil: 4× slot 5.5×10mm (posisi sesuai profil T-slot)
- Engraving text: "MOTOR SIDE"

Langkah:
1. Sketch rectangle 120×80mm → fillet R5
2. Sketch lubang NEMA 17 (gunakan dimensi dari Materi 8.4.2)
3. Sketch slot mounting (Linear Pattern)
4. Extrude 5mm
5. Tambahkan Sketch Text "MOTOR SIDE" (Engraved Cut 0.3mm)
6. File → Save As → DXF (untuk Modul 10)
```

### Percobaan 4: End Plate Idler Side (Akrilik 5mm — untuk Laser Cut)
```
Spesifikasi:
- Material: Akrilik 5mm
- Ukuran: 120 × 80 mm, fillet R5
- Slot tensioning shaft: 8.5 × 20mm (horizontal slot)
- Lubang mounting profil: 4× slot 5.5×10mm
- Engraving text: "IDLER SIDE"

Langkah:
1. Modifikasi desain dari Percobaan 3 (Save As → edit)
2. Ganti lubang shaft Ø8.5mm menjadi slot 8.5×20mm
3. Hapus lubang NEMA 17 dan center pilot
4. Ganti engraving → "IDLER SIDE"
5. Export DXF
```

### Percobaan 5: Bearing Housing Akrilik (Stack 2 Layer)
```
Spesifikasi:
- Material: Akrilik 5mm × 2 layer (total 10mm per housing)
- Ukuran per layer: 40 × 30 mm
- Bearing seat: Ø22mm (OD bearing 608ZZ)
- Mounting holes: 2× Ø4mm, jarak 30mm center-to-center
- Jumlah: 4 housing = 8 pieces akrilik total
- Versi drive: lubang bulat Ø8.5mm (shaft)
- Versi idler: slot 8.5×15mm (tensioning)

Langkah:
1. Sketch 40×30mm rectangle
2. Lingkaran Ø22mm di center
3. 2 lubang Ø4mm simetris
4. Extrude 5mm
5. Buat 2 konfigurasi: Drive (hole) & Idler (slot)
6. Export DXF kedua versi
```

### Percobaan 6: Drive Roller & Idler Roller
```
Spesifikasi:
- Roller tube: Ø25mm OD, wall 2mm, panjang 100mm
- Shaft: Ø8mm, panjang 150mm (extend 25mm di tiap sisi)
- End cap/hub: Ø25mm → Ø8mm transition
- Drive roller: shaft ada D-cut/flat untuk coupler
- Idler roller: shaft polos (free spinning)

Langkah:
1. Sketch profil roller → Revolve 360°
2. Buat shaft → Extrude Ø8mm × 150mm
3. End cap: Revolve + Extrude
4. Buat D-cut pada shaft drive roller
5. Assembly: tube + 2 end cap + shaft
6. Buat 2 versi (drive & idler)
```

### Percobaan 7: Motor Bracket NEMA 17 (Akrilik 5mm)
```
Spesifikasi:
- Material: Akrilik 5mm
- Desain: L-bracket (2 piece tab-slot)
  - Piece A (face plate): lubang NEMA 17 pattern
  - Piece B (mounting plate): slot untuk T-nut profil
- Tab: 10mm × 5mm (×3 tabs)
- Slot: 10mm × 5.15mm (toleransi +0.15mm)
- Center pilot: Ø22.5mm

Langkah:
1. Desain Piece A (face plate) → lubang NEMA 17 + center pilot
2. Desain Piece B (mounting plate) → slot T-nut + tab slots
3. Tambahkan tabs pada Piece A bagian bawah
4. Assembly: Piece A + Piece B → verifikasi 90°
5. Export DXF kedua piece
```

### Percobaan 8: Bearing Block untuk CNC Milling (MDF 18mm)
```
Spesifikasi:
- Material: MDF/Kayu 18mm
- Ukuran: 50 × 40 × 18 mm
- Pocket bearing seat: Ø22mm, depth 8mm (dari atas)
- Through hole shaft: Ø8.5mm (menerus 18mm)
- Mounting holes: 2× Ø5mm + countersink Ø10mm × depth 3mm
- Chamfer edge: 2mm × 45° (opsional, estetika)

Langkah:
1. Sketch rectangle 50×40mm → Extrude 18mm
2. Extruded Cut: circle Ø22mm, depth 8mm (pocket bearing)
3. Extruded Cut: circle Ø8.5mm, through all (shaft hole)
4. Hole Wizard: 2× Ø5mm countersunk
5. Chamfer edges
6. File → Save As → STEP AP214 (untuk Fusion 360 CAM Modul 13)
```

### Percobaan 9: Side Guide & Name Plate
```
Side Guide (Akrilik 3mm):
- 350 × 25 mm
- 3× slot mounting 5.5×10mm
- Export DXF

Name Plate (MDF 18mm — untuk CNC Milling):
- 100 × 40 × 18 mm
- Pocket background: depth 3mm (area kosong diturunkan)
- Teks timbul: "MINI CONVEYOR" + Nama + NIM
- Border dekoratif: fillet/chamfer
- Mounting: 2× Ø4mm
- Export STEP

Langkah:
1. Side guide: sketch → extrude 3mm → DXF
2. Name plate: sketch → extrude 18mm
3. Sketch Text → Wrap → Deboss area sekitar teks (pocket)
   → Teks menjadi timbul 3mm
4. Export STEP (untuk Fusion 360 CAM Modul 13)
```

### Percobaan 10: Assembly Lengkap Konveyor + BOM + Drawing
```
Rakit semua komponen menjadi assembly lengkap:
1. Frame rangka (P1+P2)
2. End Plate Motor Side (P3) × 2
3. End Plate Idler Side (P4) × 2
4. Bearing Housing (P5) × 4 set
5. Drive Roller + Idler Roller (P6)
6. Motor Bracket + NEMA 17 (P7)
7. Bearing Block milling (P8) × 2
8. Side Guide (P9) × 2
9. Name Plate (P9)
10. Belt (surface/sheet body simplified)
11. Coupler 5→8mm
12. Bearing 608ZZ × 4
13. Fasteners (T-nut, bolts, nuts, spacers)
14. Support Legs × 4

Output yang wajib dibuat:
✅ Assembly file (.sldasm) — semua mate benar
✅ Exploded View — dengan balloon nomor
✅ BOM (Bill of Materials) — qty, material, sumber, proses
✅ Drawing Package:
   - Assembly drawing dengan dimensi keseluruhan
   - 3 detail drawing part custom
   - Flat pattern drawing untuk part akrilik
✅ Export File Table:
   | Part | Format | Proses | Modul |
   |------|--------|--------|-------|
   | End plates | DXF | Laser | 10 |
   | Holders | DXF | Laser | 10 |
   | Bearing block | STEP | Milling | 13 |
   | Name plate | STEP | Milling | 13 |
```

---

## 8.11 Tips Desain Konveyor
1. **Design for Manufacturing** — Setiap part harus bisa difabrikasi dengan proses yang ditentukan
2. **Toleransi** — Akrilik laser cut: ±0.1mm, CNC Milling: ±0.2mm
3. **Alignment** — Kedua roller HARUS parallel dan center-aligned
4. **Tensioning** — Pastikan idler bisa digeser minimal 10mm untuk adjust belt
5. **Aksesibilitas** — Bearing housing harus bisa dilepas untuk maintenance
6. **Modular** — Manfaatkan T-slot profil aluminium agar posisi fleksibel
7. **Torsi** — Hitung torsi load agar tidak melebihi kemampuan NEMA 17
8. **Wiring** — Sediakan jalur/clip untuk kabel motor & sensor

---

*Modul Praktikum CAD/CAM — Modul 8: Project Konveyor*
*Disusun untuk keperluan pendidikan*
