# MATERI MODUL 12: CAM — 3D PRINTING (FDM)

## Praktikum CAD/CAM — Pertemuan 12

---

## 1. Pendahuluan & Konteks

### Koneksi dari Modul 11 (Robot Lengan 3-DOF)
Modul ini adalah **realisasi** dari desain robot lengan 3-DOF yang telah dibuat di Modul 11. File STL yang sudah dipersiapkan sebelumnya akan di-slice, dioptimasi, dan dicetak menggunakan mesin 3D printer FDM.

```
Alur Realisasi:
Modul 11 (CAD)          →    Modul 12 (CAM 3D Print)
──────────────           →    ──────────────────────
SolidWorks Design        →    Import STL ke Slicer
Part Robot (.STL)        →    Slice & Generate G-code
Huruf Timbul (.STL)      →    Print part + huruf timbul
Assembly Reference       →    Assembly fisik robot
```

### Apa itu 3D Printing FDM?
**Fused Deposition Modeling (FDM)** adalah proses manufaktur aditif di mana filamen termoplastik (PLA, ABS, PETG, dll.) dipanaskan hingga meleleh dan diextrudasi melalui nozzle, lalu diendapkan lapis demi lapis (layer by layer) untuk membentuk objek 3D.

### Perbedaan Aditif vs Subtraktif
| Aspek | Aditif (3D Print) | Subtraktif (CNC/Laser) |
|-------|-------------------|------------------------|
| Proses | Menambah material lapis demi lapis | Mengurangi material dari blok |
| Waste | Minimal (hanya support) | Signifikan (chips/dust) |
| Geometri | Bebas (internal cavity, organic) | Terbatas akses tool |
| Material | Filamen termoplastik | Logam, kayu, akrilik |
| Toleransi | ±0.2–0.5mm | ±0.05–0.1mm |
| Kecepatan | Lambat (jam) | Cepat untuk part sederhana |

---

## 2. Anatomi Mesin 3D Printer FDM

### Komponen Utama
```
┌──────────────────────────────────────┐
│            FRAME / GANTRY            │
│  ┌─────────────────────────────┐     │
│  │   X-Axis (Nozzle kiri-kanan)│     │
│  │  ┌──────────┐              │     │
│  │  │ EXTRUDER │              │     │
│  │  │ ┌──────┐ │              │     │
│  │  │ │HOTEND│ │  ←── Nozzle  │     │
│  │  │ └──────┘ │     (0.4mm)  │     │
│  │  └──────────┘              │     │
│  └─────────────────────────────┘     │
│                                      │
│  ┌──────────────────────────────┐    │
│  │      HEATED BED (60°C)      │    │
│  │      Y-Axis (maju-mundur)   │    │
│  └──────────────────────────────┘    │
│                                      │
│  Z-Axis (naik per layer)             │
└──────────────────────────────────────┘
```

### Komponen Detail
| Komponen | Fungsi | Parameter Kunci |
|----------|--------|-----------------|
| **Extruder** | Mendorong filamen ke hotend | Tension, gear ratio |
| **Hotend** | Melelehkan filamen | Suhu 190–230°C (PLA) |
| **Nozzle** | Mengeluarkan filamen cair | Diameter 0.4mm (standar) |
| **Heated Bed** | Mencegah warping | 50–60°C (PLA) |
| **Stepper Motor** | Menggerakkan sumbu X, Y, Z | Presisi step |
| **Fan** | Pendinginan layer | Part cooling fan |
| **Endstop/Probe** | Homing & auto bed leveling | Akurasi Z offset |

---

## 3. Material: PLA (Polylactic Acid)

### Mengapa PLA untuk Praktikum?
| Aspek | PLA | ABS | PETG |
|-------|-----|-----|------|
| Kemudahan Print | ★★★★★ | ★★☆☆☆ | ★★★★☆ |
| Tidak Perlu Enclosure | ✅ | ❌ | ✅ |
| Bau | Minimal | Kuat (berbahaya) | Minimal |
| Bed Adhesion | Mudah (60°C) | Sulit (100°C+) | Sedang (80°C) |
| Kekuatan | Cukup untuk prototipe | Lebih kuat | Paling kuat |
| Biodegradable | ✅ | ❌ | ❌ |
| Harga | Murah | Sedang | Sedang |

### Parameter Print PLA
| Parameter | Nilai Tipikal | Rentang |
|-----------|---------------|---------|
| Nozzle Temperature | 200°C | 190–220°C |
| Bed Temperature | 60°C | 50–70°C |
| Print Speed | 50 mm/s | 30–80 mm/s |
| First Layer Speed | 25 mm/s | 15–30 mm/s |
| Cooling Fan | 100% (setelah layer 2) | 0–100% |
| Retraction Distance | 5 mm (Bowden) / 1 mm (Direct) | 1–7 mm |
| Retraction Speed | 45 mm/s | 25–60 mm/s |

---

## 4. Software Slicer

### Pilihan Slicer
| Software | Kelebihan | Lisensi |
|----------|-----------|---------|
| **Cura** | Paling banyak profil printer, intuitif | Free |
| **PrusaSlicer** | Fitur paint-on support, variable layer | Free |
| **OrcaSlicer** | Fork PrusaSlicer, fitur banyak | Free |
| **Simplify3D** | Presisi tinggi | Berbayar |

### Workflow Slicer (Cura)
```
Import STL → Posisi & Orientasi → Setting Parameter → Preview (Layer) → Export G-code → Print
```

### Parameter Slicer Penting

#### Layer & Shell
| Parameter | Deskripsi | Nilai Rekomendasi |
|-----------|-----------|-------------------|
| **Layer Height** | Ketebalan per layer | 0.2mm (standar), 0.12mm (detail) |
| **First Layer Height** | Layer pertama lebih tebal | 0.28–0.3mm |
| **Wall Count** | Jumlah dinding | 3 (1.2mm total) |
| **Top/Bottom Layers** | Layer atas/bawah solid | 4–5 layer |
| **Line Width** | Lebar extrusion | 0.4mm (= nozzle) |

#### Infill
| Pattern | Kekuatan | Kecepatan | Penggunaan |
|---------|----------|-----------|------------|
| Grid | ★★★☆☆ | ★★★★☆ | Umum |
| **Gyroid** | ★★★★☆ | ★★★☆☆ | Kekuatan merata |
| Cubic | ★★★★☆ | ★★★☆☆ | Structural |
| Triangles | ★★★★★ | ★★☆☆☆ | Beban tinggi |
| Lines | ★★☆☆☆ | ★★★★★ | Non-structural |

**Infill Density Rekomendasi:**
- **Bracket Servo** (beban tinggi): 40–60%
- **Link / Arm** (beban sedang): 25–40%
- **Base Plate** (structural): 30–50%
- **Huruf Timbul** (non-structural): 15–20%
- **Gripper** (detail): 30–40%

#### Support
| Parameter | Nilai |
|-----------|-------|
| **Support Type** | Tree (lebih mudah lepas) atau Normal |
| **Support Angle** | 45° (overhang di atas ini perlu support) |
| **Support Density** | 10–15% |
| **Support Z Distance** | 0.2mm (1 layer) |
| **Support Interface** | Dense, 2 layer |

#### Adhesion
| Tipe | Deskripsi | Kapan Pakai |
|------|-----------|-------------|
| **Skirt** | Garis di sekeliling part | Default, always |
| **Brim** | Flap menempel di base | Part kecil / tipis |
| **Raft** | Platform di bawah part | Bed tidak rata |

---

## 5. Orientasi Print — Sangat Krusial!

### Prinsip Orientasi
Orientasi part di bed menentukan:
- **Kekuatan** (layer direction vs load direction)
- **Support** (semakin sedikit semakin baik)
- **Surface Quality** (face yang kontak bed paling halus)
- **Waktu Print** (tinggi Z = waktu)

### Orientasi Part Robot Lengan
```
Part: Shoulder Bracket (U-Shape)
──────────────────────────────

SALAH (perlu banyak support):     BENAR (tidak perlu support):
    ┌─┐   ┌─┐                       ┌───────────────┐
    │ │   │ │                       │               │
    │ │   │ │  ← Overhang!         │  ┌─────────┐  │
    │ │   │ │                       │  │  pocket  │  │
    └─┴───┴─┘                       │  │  servo   │  │
                                    └──┴─────────┴──┘
    U menghadap atas                 U menghadap samping
    → banyak support                → zero support!
```

### Rekomendasi Orientasi Per Part
| Part | Orientasi | Alasan |
|------|-----------|--------|
| Base Plate | Flat face di bed | Luas kontak, stabil |
| Turntable | Flat circle di bed | Natural, no support |
| Shoulder Bracket | U-shape horizontal (buka ke samping) | Minimal support |
| Upper Arm Link | Flat / lying down | Kekuatan lentur |
| Elbow Bracket | Sama seperti shoulder | Minimal support |
| Forearm Link | Flat / lying down | Kekuatan lentur |
| Gripper | Tergantung desain | Custom support |
| Servo Horn Adapter | Flat face di bed | Detail presisi |
| **Huruf Timbul** | **Text menghadap atas** | **Detail huruf jelas** |

---

## 6. Huruf Timbul — Pertimbangan 3D Print

### Dari CAD ke Print
File STL huruf timbul dari Modul 11 perlu perhatian khusus:

| Aspek | Rekomendasi |
|-------|-------------|
| Layer Height | 0.12–0.16mm (detail) |
| Orientasi | Text face **menghadap atas** (away from bed) |
| Infill | 15–20% (non-structural) |
| Wall Count | 3 minimum (agar huruf solid) |
| Top Layers | 5+ (surface quality) |
| Support | Tidak perlu jika text menghadap atas |

### Multi-Color (Opsional)
Jika printer support:
- **Filament Change at Layer**: Ganti warna pada layer tertentu
- Di Cura: Extensions → Post Processing → Filament Change
- Misal: base putih, huruf hitam — ganti filamen di layer awal huruf

```
G-code pause:
M600  ; Filament Change (Marlin firmware)
atau
M0    ; Unconditional Stop
```

---

## 7. Troubleshooting 3D Print

### Masalah Umum & Solusi
| Masalah | Penyebab | Solusi |
|---------|----------|-------|
| **Warping** | Bed terlalu dingin, no adhesion | ↑ Bed temp, gunakan brim/raft |
| **Stringing** | Retraction kurang | ↑ Retraction distance/speed |
| **Layer Shifting** | Belt loose, speed terlalu tinggi | Kencangkan belt, ↓ speed |
| **Under-extrusion** | Nozzle tersumbat, tension kurang | Bersihkan nozzle, ↑ tension |
| **Over-extrusion** | Flow rate terlalu tinggi | ↓ Flow rate (95–98%) |
| **Elephant Foot** | Nozzle terlalu dekat bed | Calibrate Z offset, ↑ initial Z |
| **Poor Bridging** | Fan kurang, speed terlalu rendah | Fan 100%, ↑ bridge speed |
| **Support Sulit Lepas** | Z distance terlalu kecil | ↑ Support Z distance |
| **Part Tidak Presisi** | Flow, shrinkage PLA ~0.3% | Calibrate flow, compensation |

### Kalibrasi Penting
1. **Bed Leveling** — sebelum setiap print session
2. **E-steps** — pastikan extrusi 100mm = benar 100mm
3. **Flow Rate** — print calibration cube, ukur dinding
4. **Temperature Tower** — tentukan suhu optimal per filamen
5. **Retraction Test** — tuning stringing

---

## 8. G-code Dasar untuk 3D Printing

### G-code yang Sering Muncul
| G-code | Fungsi |
|--------|--------|
| G28 | Home all axes |
| G29 | Auto bed leveling |
| G1 X_ Y_ Z_ E_ F_ | Linear move + extrude |
| M104 S200 | Set nozzle temp (no wait) |
| M109 S200 | Set nozzle temp (wait) |
| M140 S60 | Set bed temp (no wait) |
| M190 S60 | Set bed temp (wait) |
| M106 S255 | Fan ON (max) |
| M107 | Fan OFF |
| M600 | Filament change |
| G92 E0 | Reset extruder position |

### Struktur File G-code
```gcode
; === START GCODE ===
G28             ; Home
M190 S60        ; Wait bed temp
M109 S200       ; Wait nozzle temp
G29             ; Auto level
G92 E0          ; Reset extruder
G1 Z5 F3000     ; Lift nozzle

; === LAYER 0 (First Layer) ===
G1 Z0.3 F1200   ; Move to first layer
G1 X10 Y10 E1 F600  ; Start printing

; ... ribuan garis G1 dari slicer ...

; === END GCODE ===
M104 S0         ; Nozzle off
M140 S0         ; Bed off
G28 X Y         ; Home X Y
M84             ; Disable steppers
```

---

## 9. Workflow Lengkap: STL → Print

### Step-by-Step
```
1. IMPORT STL
   └── Slicer → File → Open → pilih .stl dari Modul 11

2. ORIENTASI
   └── Rotate part → minimal support, max strength
   └── Gunakan "Lay Flat" atau manual rotate

3. SCALING CHECK
   └── Pastikan dimensi benar (1:1)
   └── Cek unit: mm bukan inch!

4. PARAMETER SETTING
   ├── Layer Height: 0.2mm (standar) atau 0.12mm (detail)
   ├── Infill: sesuai fungsi part (15–60%)
   ├── Support: hanya jika overhang >45°
   ├── Adhesion: brim untuk part kecil
   └── Speed: 50mm/s standar, 25mm/s first layer

5. PREVIEW LAYER-BY-LAYER
   └── Cek setiap layer — ada masalah?
   └── Perhatikan: support, bridges, thin walls

6. ESTIMASI
   ├── Waktu print: cek estimasi slicer
   ├── Filamen: gram / meter
   └── Feasible dalam sesi praktikum?

7. EXPORT G-CODE
   └── Save → SD Card / USB / OctoPrint

8. PRE-PRINT CHECK
   ├── Bed leveling OK?
   ├── Filamen loaded?
   ├── Nozzle bersih?
   └── Bed adhesion (glue stick / hairspray)?

9. PRINT
   └── Monitor first 3 layers!
   └── Jika gagal → stop, re-level, re-print

10. POST-PROCESSING
    ├── Lepas dari bed (spatula)
    ├── Buang support (tang)
    ├── Amplas jika perlu
    └── Test fit servo → pocket pas?
```

---

## 10. Percobaan

### Percobaan 1: Setup dan Kalibrasi Printer
- Kenali bagian-bagian printer FDM
- Lakukan bed leveling manual (paper test)
- Load filamen PLA, test extrude

### Percobaan 2: Import STL Base Plate
- Import STL base plate robot dari Modul 11
- Pastikan skala benar (1:1, mm)
- Posisikan di center bed

### Percobaan 3: Parameter Base Plate
- Set layer height 0.2mm
- Wall 3, top/bottom 4, infill 30% grid
- Adhesion: skirt
- Preview & cek estimasi waktu

### Percobaan 4: Import & Orientasi Shoulder Bracket
- Import STL shoulder bracket
- Rotate agar U-shape horizontal → minimal support
- Compare estimasi waktu: orientasi benar vs salah

### Percobaan 5: Multi-Part Plating
- Import semua STL part robot
- Arrange di bed → perhatikan jarak antar part (≥5mm)
- Apakah semua muat di 1 bed? Jika tidak, bagi ke beberapa batch

### Percobaan 6: Support Strategy
- Identifikasi part mana yang butuh support
- Compare: normal support vs tree support
- Cek estimasi waktu & filamen perbedaannya

### Percobaan 7: Huruf Timbul — Detail Print
- Import STL huruf timbul
- Set layer height 0.12mm (high detail)
- Orientasi: text menghadap atas
- Preview: apakah huruf terlihat jelas di layer view?

### Percobaan 8: Filament Change untuk Multi-Color (Demo)
- Di Cura: Extensions → Post Processing → Modify G-code
- Tambahkan Filament Change di layer tertentu
- Preview G-code — cari M600

### Percobaan 9: Print Part Pertama
- Print base plate atau part kecil sebagai test
- Monitor first 3 layers
- Evaluasi: bed adhesion, dimensi, surface quality

### Percobaan 10: Post-Processing & Assembly
- Lepas part dari bed
- Buang support (jika ada)
- Test fit servo SG90 ke pocket
- Evaluasi: toleransi pas? Perlu adjustment?

---

## 11. Peta Koneksi Modul
```
┌─────────────────────┐
│  MODUL 11 (Input)   │
│  Robot Lengan CAD    │
│  └── STL files      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────────────────────────┐
│           MODUL 12 (Proses)             │
│   CAM 3D Printing                       │
│   ├── Import STL → Slicer               │
│   ├── Orientasi + Parameter             │
│   ├── Generate G-code                   │
│   ├── Print semua part robot            │
│   ├── Print huruf timbul               │
│   └── Assembly fisik robot lengan       │
└─────────────────────────────────────────┘
```

---

## 12. Checklist Kesiapan
- [ ] File STL dari Modul 11 sudah lengkap dan watertight
- [ ] Slicer terinstall (Cura / PrusaSlicer)
- [ ] Profil printer sudah di-setup di slicer
- [ ] Filamen PLA tersedia dan loaded
- [ ] Bed sudah di-level
- [ ] SD Card / USB / koneksi OctoPrint siap

---

## Referensi
1. Ultimaker Cura Documentation — https://support.ultimaker.com
2. PrusaSlicer Documentation — https://help.prusa3d.com
3. All3DP 3D Printing Guides — https://all3dp.com
4. Marlin Firmware G-code Reference — https://marlinfw.org/meta/gcode/

---

*Materi Praktikum CAD/CAM — Modul 12*
