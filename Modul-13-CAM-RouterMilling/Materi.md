# MATERI MODUL 13: CAM — CNC ROUTER MILLING

## Praktikum CAD/CAM — Pertemuan 13

---

## 1. Pendahuluan & Konteks

### Koneksi dari Modul 08 (Project Konveyor)
Modul ini adalah **realisasi** part-part konveyor yang telah didesain di Modul 08. File STEP yang sudah diekspor akan diimport ke Fusion 360 untuk pembuatan toolpath CNC router milling. Selain part konveyor, mahasiswa juga akan **membuat ukiran nama** menggunakan teknik V-carving/engraving.

```
Alur Realisasi:
Modul 08 (CAD)              →    Modul 13 (CAM CNC Router)
──────────────               →    ───────────────────────
SolidWorks Design            →    Import STEP ke Fusion 360
Bearing Block (.STEP)        →    Pocket + Contour + Drill
Motor Mount Plate (.STEP)    →    Pocket + Profile
Side Plate (.STEP)           →    Contour + Drill
+ Ukiran Nama (baru)         →    V-Carve / Engrave toolpath
```

### Apa itu CNC Router Milling?
**CNC Router Milling** adalah proses manufaktur **subtraktif** di mana material (kayu, MDF, akrilik, aluminium) dipotong menggunakan cutter/bit yang berputar (spindle), dikendalikan oleh komputer melalui G-code.

### Perbedaan CNC Router vs CNC Milling Center
| Aspek | CNC Router | CNC Milling Center |
|-------|------------|-------------------|
| Material | Kayu, MDF, akrilik, plastik | Logam (baja, aluminium) |
| Spindle | High RPM (12000–24000) | Moderate RPM (1000–10000) |
| Rigidity | Sedang | Sangat tinggi |
| Area Kerja | Besar (600×900mm+) | Lebih kecil, lebih presisi |
| Harga | Terjangkau | Sangat mahal |
| Coolant | Dry / vacuum | Wet (oli, coolant) |
| Penggunaan | Sign making, woodwork, prototipe | Production machining |

---

## 2. Anatomi Mesin CNC Router

### Komponen Utama
```
┌──────────────────────────────────────────┐
│              GANTRY                       │
│   ┌──────────────────────┐               │
│   │    SPINDLE MOTOR      │               │
│   │   ┌──────────────┐   │               │
│   │   │   COLLET      │   │ ← Z-Axis     │
│   │   │  ┌────────┐  │   │   (naik/turun)│
│   │   │  │END MILL│  │   │               │
│   │   │  └────┘   │  │   │               │
│   │   └──────────────┘   │               │
│   └──────────────────────┘               │
│       ← X-Axis (kiri/kanan) →            │
│                                          │
│   ┌──────────────────────────────────┐   │
│   │         SPOILBOARD / BED          │   │
│   │   ┌────────────────┐             │   │
│   │   │  WORKPIECE     │ ← Clamp     │   │
│   │   │  (MDF/Kayu)    │             │   │
│   │   └────────────────┘             │   │
│   └──────────────────────────────────┘   │
│       ← Y-Axis (maju/mundur) →           │
└──────────────────────────────────────────┘
```

### Komponen Detail
| Komponen | Fungsi | Keterangan |
|----------|--------|------------|
| **Spindle** | Memutar cutter | 12000–24000 RPM |
| **Collet/ER** | Menjepit cutter | ER11 / ER16 / ER20 |
| **Stepper Motor** | Menggerakkan sumbu X,Y,Z | NEMA 23 / NEMA 34 |
| **Lead Screw / Belt** | Transmisi gerakan | Ball screw lebih presisi |
| **Spoilboard** | Alas pengorbanan | MDF, diganti berkala |
| **Clamp** | Menahan benda kerja | T-slot, toe clamp, vacuum |
| **Controller** | Menjalankan G-code | GRBL, Mach3, LinuxCNC |
| **Limit Switch** | Homing & batas gerak | Mekanikal / optik |
| **Dust Collection** | Menyedot debu | Vacuum / shoe |

---

## 3. Cutting Tools (End Mill & Bit)

### Jenis End Mill
| Tipe | Bentuk | Penggunaan |
|------|--------|------------|
| **Flat End Mill** | Ujung datar | Pocket, contour, face milling |
| **Ball End Mill** | Ujung bola | 3D surface, finishing |
| **V-Bit** | Ujung V (60°, 90°) | **Engraving, V-carving** |
| **Drill Bit** | Ujung drill | Lubang (hole drilling) |
| **Compression Bit** | Up + Down cut | Plywood, laminasi |

### Parameter End Mill
| Istilah | Deskripsi |
|---------|-----------|
| **Diameter** | Ukuran cutter (3mm, 6mm, dll.) |
| **Flute Count** | Jumlah alur potong (1, 2, 3) |
| **Flute Length** | Panjang bagian yang bisa potong |
| **Shank Diameter** | Diameter batang yang dijepit collet |
| **Up Cut** | Chips naik → surface bawah halus |
| **Down Cut** | Chips turun → surface atas halus |

### Tool yang Digunakan di Praktikum
| No | Tool | Diameter | Fungsi |
|----|------|----------|--------|
| 1 | Flat End Mill | 6mm, 2-flute | Pocket, contour utama |
| 2 | Flat End Mill | 3mm, 2-flute | Detail kecil, slot |
| 3 | V-Bit | 60° atau 90° | **Ukiran nama (engraving)** |
| 4 | Drill Bit | 3mm, 5mm | Lubang baut |

---

## 4. Parameter Cutting (Feeds & Speeds)

### Istilah Penting
| Parameter | Simbol | Satuan | Deskripsi |
|-----------|--------|--------|-----------|
| **Spindle Speed** | S / RPM | rev/min | Kecepatan putar spindle |
| **Feed Rate** | F | mm/min | Kecepatan gerak cutter horizontal |
| **Plunge Rate** | Fp | mm/min | Kecepatan masuk ke material (Z) |
| **Depth of Cut (DOC)** | ap | mm | Kedalaman per pass |
| **Width of Cut (WOC)** | ae | mm | Lebar per pass (stepover) |
| **Chip Load** | fz | mm/tooth | Material per gigi per putaran |

### Rumus Dasar
$$Feed\ Rate\ (F) = RPM \times Flute \times Chip\ Load$$

$$F = S \times z \times f_z$$

Contoh:
- End mill 6mm, 2-flute, MDF
- RPM = 18000, Chip Load = 0.05mm/tooth
- F = 18000 × 2 × 0.05 = **1800 mm/min**

### Parameter Rekomendasi untuk MDF
| Operasi | Tool | RPM | Feed (mm/min) | DOC (mm) | WOC (mm) |
|---------|------|-----|---------------|----------|----------|
| **Pocket** | 6mm flat | 18000 | 1500–2000 | 3mm | 3mm (50%) |
| **Contour** | 6mm flat | 18000 | 1500–2000 | 3mm | 6mm (full) |
| **Detail** | 3mm flat | 18000 | 800–1200 | 2mm | 1.5mm |
| **Drill** | 3mm drill | 12000 | Plunge 300 | Full | - |
| **Engrave** | V-bit 60° | 15000 | 600–1000 | 0.5–1mm | - |

### Parameter untuk Kayu Solid (Pine/Jati)
| Operasi | Tool | RPM | Feed (mm/min) | DOC (mm) |
|---------|------|-----|---------------|----------|
| Pocket | 6mm flat | 16000 | 1200–1600 | 2.5mm |
| Contour | 6mm flat | 16000 | 1200–1600 | 2.5mm |
| Engrave | V-bit | 14000 | 500–800 | 0.5–1mm |

---

## 5. Software CAM: Fusion 360

### Mengapa Fusion 360?
| Kelebihan | Keterangan |
|-----------|------------|
| Free untuk edukasi | Lisensi student |
| CAD + CAM terintegrasi | Tidak perlu software terpisah |
| Banyak tutorial | Komunitas besar |
| Simulation | Preview toolpath sebelum eksekusi |
| Post-processor | Support GRBL, Mach3, LinuxCNC |

### Workspace di Fusion 360
```
DESIGN (CAD)  →  MANUFACTURE (CAM)  →  DRAWING (Opsional)
```

### Workflow CAM di Fusion 360
```
1. IMPORT STEP
   └── File → Open → pilih .STEP dari Modul 08

2. SETUP
   ├── Origin (WCS) → tentukan titik nol (X0, Y0, Z0)
   ├── Stock → material mentah (MDF thickness)
   └── Fixture → clamp position

3. TOOLPATH — untuk setiap operasi:
   ├── a. FACE (ratakan permukaan atas)
   ├── b. POCKET (cavity / lubang besar)
   ├── c. CONTOUR (profil luar / kontur)
   ├── d. DRILL (lubang baut)
   └── e. ENGRAVE (ukiran nama — V-bit)

4. SIMULATE
   └── Cek collision, gouging, air cut

5. POST-PROCESS
   └── Generate G-code → pilih post processor (GRBL)
   └── Save .nc / .gcode file
```

---

## 6. Setup — Langkah Detail

### Import STEP File
1. Buka Fusion 360 → **File → Open** → pilih .STEP
2. File dari SolidWorks akan ter-import sebagai body
3. **Pastikan unit mm** (Document Settings)
4. Orient model sesuai posisi machining

### Setup Machining
```
MANUFACTURE workspace → Setup → New Setup
├── Machine: Router / Milling
├── WCS (Work Coordinate System):
│   ├── Origin: Stock Box Point
│   ├── X: kiri-kanan
│   ├── Y: maju-mundur
│   └── Z top: permukaan atas stock
├── Stock:
│   ├── Mode: Fixed Size Box
│   ├── Width × Length: sesuai material
│   └── Height: ketebalan MDF (misal 18mm)
└── Model: select body yang akan di-machining
```

### Menentukan Origin (Titik Nol)
| Posisi Origin | Keterangan |
|---------------|------------|
| **Top-Left Corner** | Paling umum untuk CNC router |
| Top-Right Corner | Alternatif |
| Center | Untuk part simetris |

**Z Origin:**
- **Top of Stock** = Z0 di permukaan atas material ← **paling umum**
- Bottom of Stock = Z0 di bawah material

---

## 7. Operasi Toolpath

### 7.1 Face Milling
Meratakan permukaan atas material.
```
Manufacture → 2D → Face
├── Tool: 6mm Flat End Mill
├── Passes: 
│   ├── Stepover: 50% (3mm)
│   └── Stock to Leave: 0
└── Heights:
    ├── Top: Stock Top
    └── Bottom: Stock Top - 0.5mm
```

### 7.2 2D Pocket
Membuat cavity/rongga — misal pocket untuk bearing pada bearing block.
```
Manufacture → 2D → 2D Pocket
├── Tool: 6mm Flat End Mill (roughing) → 3mm (finishing)
├── Geometry: Select bottom face of pocket
├── Passes:
│   ├── Stepover: 40–50%
│   ├── DOC: 3mm per pass
│   └── Stock to Leave: 0.1mm (finishing nanti)
├── Heights:
│   ├── Top: Stock Top
│   └── Bottom: Pocket bottom
└── Linking:
    ├── Ramp: Helix (lebih halus dari plunge)
    └── Lead-in/out: Arc
```

### 7.3 2D Contour
Memotong profil luar part — memisahkan part dari stock.
```
Manufacture → 2D → 2D Contour
├── Tool: 6mm Flat End Mill
├── Geometry: Select outer contour edges
├── Passes:
│   ├── DOC: 3mm per pass
│   └── Stock to Leave: 0
├── Heights:
│   ├── Top: Stock Top
│   └── Bottom: Stock Bottom + 0.3mm (onion skin)
│         ATAU: Stock Bottom (full cut-through + tabs)
└── Tabs:
    ├── Tab Width: 5mm
    ├── Tab Height: 2mm
    └── Tab Count: 4 per part
```

**PENTING — TABS/BRIDGES:**
Tabs menahan part agar tidak lepas dan terbang saat kontur selesai dipotong. Tanpa tabs, part akan terlempar oleh cutter!

```
Contour dengan Tabs:
┌─────────────────┐
│                 │
│    ┌─────┐      │
│    │PART │ ← Tabs menahan
│    │     ├──┤   │
│    │     │  │   │
│    └─┬───┘  │   │
│      │TAB│  │   │
└──────┴──────┴───┘
```

### 7.4 Drilling
Membuat lubang baut.
```
Manufacture → Drilling → Drill
├── Tool: 3mm Drill Bit (atau 5mm sesuai kebutuhan)
├── Geometry: Select hole center points
├── Cycle Type: 
│   ├── Drilling (simple) — lubang dangkal
│   └── Peck Drilling — lubang dalam (retract periodik)
├── Peck Depth: 3mm
└── Heights:
    ├── Top: Stock Top + 2mm (clearance)
    └── Bottom: Through (stock bottom)
```

### 7.5 Engrave — Ukiran Nama ⭐
```
Manufacture → 2D → Engrave (atau Trace)
├── Tool: V-Bit 60° (atau 90°)
├── Geometry: Select text/sketch curves
├── Depth: 0.5–1.0mm
├── Feed: 600–1000 mm/min
├── RPM: 15000
└── Multi-pass: 1 pass (untuk V-bit)
```

**Cara Membuat Teks untuk Ukiran:**
1. Di Fusion 360: **Sketch → Text** di permukaan stock
2. Ketik nama + NIM
3. **Explode Text** (klik kanan → Explode Text) → menjadi kurva
4. Gunakan kurva sebagai geometry untuk Engrave toolpath

**ATAU:** Import DXF teks dari SolidWorks/CorelDRAW

### Tips V-Carving
| Parameter | Nilai |
|-----------|-------|
| Kedalaman V-bit | 0.5–1.0mm |
| Lebar huruf minimum | 3mm (agar V terlihat jelas) |
| Font | Sans-serif (Arial, Helvetica) lebih mudah |
| Spacing | 2mm antar huruf minimum |

---

## 8. Simulasi & Post-Processing

### Simulasi Toolpath
```
Manufacture → Simulate (tombol play)
├── Cek:
│   ├── Collision (tool vs clamp vs fixture)
│   ├── Gouging (tool masuk terlalu dalam)
│   ├── Air Cut (gerakan sia-sia)
│   └── Remaining Stock (material tersisa)
└── Pastikan toolpath sudah benar sebelum post-process!
```

### Post-Processing
```
Manufacture → Post Process
├── Post Processor: GRBL / Mach3 / sesuai controller
├── Output: .nc atau .gcode
├── Settings:
│   ├── Safe Z Height: 5–10mm
│   ├── Units: mm
│   └── Program Comment: include
└── Save file
```

**Post-Processor untuk GRBL:**
- Nama: "grbl.cps" (biasanya sudah include di Fusion 360)
- Output format: G-code standar

---

## 9. Eksekusi di Mesin CNC

### Persiapan Mesin
```
1. SETUP MESIN
   ├── Nyalakan spindle controller
   ├── Pasang end mill di collet (kunci dengan wrench)
   ├── Pasang material MDF di bed (clamp / screw)
   └── Nyalakan dust collector

2. HOMING
   └── Jalankan homing cycle (G28 atau $H di GRBL)

3. SET ORIGIN (Titik Nol)
   ├── Jog ke posisi kiri-atas material
   ├── Z probe / manual Z touch-off
   │   └── Kertas test: letakkan kertas, turunkan Z sampai kertas terjepit
   └── Set X0, Y0, Z0

4. LOAD G-CODE
   └── Transfer via USB / SD / WiFi ke controller

5. DRY RUN (Opsional)
   └── Jalankan G-code tanpa spindle ON → cek movement

6. SPINDLE ON
   └── START program → JANGAN TINGGALKAN MESIN!

7. MONITOR
   ├── Dengarkan suara — abnormal = STOP
   ├── Cek chips — terlalu halus? ↑ feed rate
   ├── Cek workpiece — masih aman di clamp?
   └── Emergency stop jika ada masalah
```

### Set Z Origin dengan Z-Probe
```
Metode Kertas (Manual):
1. Jog Z turun pelan-pelan
2. Selipkan kertas antara bit dan material
3. Turunkan lagi sampai kertas terasa resist
4. Set Z = 0 (offset kertas ~0.1mm)

Metode Z-Probe (Otomatis):
1. Letakkan Z-probe plate di atas material
2. Jalankan probe cycle
3. Controller otomatis set Z = 0
```

---

## 10. Safety & Best Practices

### Keselamatan Kerja
| Wajib | Keterangan |
|-------|------------|
| 🥽 Safety Glasses | Chips / debu bisa mengenai mata |
| 🔇 Ear Protection | Spindle sangat bising |
| 🫁 Dust Mask | Debu MDF berbahaya untuk paru-paru |
| ✋ Jangan sentuh spindle saat berputar | SANGAT BAHAYA |
| 🔴 Ketahui posisi Emergency Stop | Sebelum mulai |
| 👀 Jangan tinggalkan mesin | Monitoring wajib |

### Best Practices
1. **Selalu dry run** sebelum spindle ON
2. **Kencangkan clamp** — material terbang = bahaya
3. **Cek collet** — end mill harus kencang
4. **Start slow** — turunkan feed rate 50% di awal, naikkan gradual
5. **Tabs/bridges wajib** untuk contour — part lepas = rusak + bahaya
6. **Spoilboard** — jangan potong terlalu dalam (Z terlalu rendah)
7. **Dust collection** — debu MDF karsinogenik

---

## 11. G-code untuk CNC Router

### G-code Umum
| G-code | Fungsi |
|--------|--------|
| G0 X_ Y_ Z_ | Rapid move (tanpa potong) |
| G1 X_ Y_ Z_ F_ | Linear feed move (potong) |
| G2 X_ Y_ I_ J_ F_ | Arc clockwise |
| G3 X_ Y_ I_ J_ F_ | Arc counter-clockwise |
| G28 | Home all axes |
| G90 | Absolute positioning |
| G91 | Incremental positioning |
| M3 S18000 | Spindle ON clockwise, 18000 RPM |
| M5 | Spindle OFF |
| M0 | Program pause |
| M30 | Program end |

### Contoh G-code Sederhana
```gcode
; === START ===
G90             ; Absolute mode
G21             ; Unit mm
G28             ; Home
M3 S18000       ; Spindle ON 18000 RPM
G4 P3           ; Wait 3 detik (spindle ramp up)

; === ENGRAVE NAMA ===
G0 Z5           ; Safe height
G0 X10 Y10      ; Move ke start point
G1 Z-0.5 F300   ; Plunge ke kedalaman engrave
G1 X30 F800     ; Engrave garis horizontal
G1 Y20          ; Engrave garis vertikal
G0 Z5           ; Retract

; === END ===
M5              ; Spindle OFF
G28             ; Home
M30             ; End program
```

---

## 12. Percobaan

### Percobaan 1: Mengenal Mesin CNC Router
- Identifikasi komponen mesin: spindle, bed, collet, controller
- Coba jog manual X, Y, Z
- Latihan pasang dan lepas end mill dari collet

### Percobaan 2: Import STEP ke Fusion 360
- Import file STEP bearing block dari Modul 08
- Cek dimensi dan orientasi
- Masuk ke MANUFACTURE workspace

### Percobaan 3: Setup Machining
- Buat New Setup → tentukan WCS origin
- Set stock size sesuai MDF yang tersedia
- Pilih model/body yang akan di-machining

### Percobaan 4: Toolpath — Pocket
- Buat 2D Pocket untuk pocket bearing
- Set tool 6mm flat, DOC 3mm, stepover 50%
- Preview toolpath → cek jumlah pass

### Percobaan 5: Toolpath — Contour dengan Tabs
- Buat 2D Contour untuk profil luar bearing block
- Tambahkan tabs: 4 buah, lebar 5mm, tinggi 2mm
- Preview → cek posisi tabs

### Percobaan 6: Toolpath — Drilling
- Buat drilling toolpath untuk lubang baut
- Pilih peck drilling, peck depth 3mm
- Verify lubang pada posisi yang benar

### Percobaan 7: Toolpath — Engrave Ukiran Nama ⭐
- Buat sketch teks di permukaan stock (nama + NIM)
- Explode text → kurva
- Buat Engrave toolpath dengan V-bit 60°
- Set kedalaman 0.5–1.0mm, feed 800 mm/min

### Percobaan 8: Simulasi & Post-Process
- Jalankan simulasi semua toolpath
- Identifikasi collision atau gouging → perbaiki
- Post-process → export G-code (GRBL)

### Percobaan 9: Eksekusi CNC
- Pasang material MDF di bed → clamp
- Set origin (X0, Y0, Z0)
- Load G-code → dry run (tanpa spindle)
- Jalankan program → monitor proses

### Percobaan 10: Finishing & Evaluasi
- Lepas part dari stock (potong tabs dengan cutter manual)
- Amplas tepi yang kasar
- Ukur dimensi part vs desain CAD
- Evaluasi kualitas ukiran nama

---

## 13. Peta Koneksi Modul
```
┌────────────────────────┐
│   MODUL 08 (Input)     │
│   Project Konveyor     │
│   └── .STEP files:     │
│       ├── Bearing Block│
│       ├── Motor Mount  │
│       └── Side Plate   │
└──────────┬─────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│            MODUL 13 (Proses)                │
│    CAM CNC Router Milling                   │
│    ├── Import STEP → Fusion 360             │
│    ├── Setup (WCS, Stock, Fixture)          │
│    ├── Toolpath:                            │
│    │   ├── Face (ratakan)                   │
│    │   ├── 2D Pocket (cavity)               │
│    │   ├── 2D Contour + Tabs (profil luar)  │
│    │   ├── Drill (lubang baut)              │
│    │   └── Engrave — Ukiran Nama ⭐         │
│    ├── Simulate & Post-Process              │
│    ├── Execute CNC Router                   │
│    └── Finishing (tabs, amplas)             │
└─────────────────────────────────────────────┘
```

---

## 14. Checklist Kesiapan
- [ ] File STEP dari Modul 08 sudah siap (bearing block, motor mount, side plate)
- [ ] Fusion 360 terinstall + lisensi student aktif
- [ ] Material MDF/kayu tersedia, ketebalan diketahui
- [ ] End mill tersedia (6mm flat, 3mm flat, V-bit, drill bit)
- [ ] CNC Router siap operasi (controller, spindle, dust collection)
- [ ] Safety equipment (kacamata, masker, ear plug)

---

## Referensi
1. Autodesk Fusion 360 CAM Documentation — https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-manufacturing
2. Feeds and Speeds Calculator — https://www.cnccookbook.com/feeds-speeds-calculator/
3. GRBL Controller Documentation — https://github.com/gnea/grbl
4. CNC Router Basics — https://www.shapeoko.com/wiki/

---

*Materi Praktikum CAD/CAM — Modul 13*
