# MODUL 13: CAM ROUTER MILLING — SolidWorks → Fusion 360 → Fusion 360 CAM

## Praktikum CAD/CAM — Pertemuan 13

---

## 13.1 Pendahuluan

CNC Router milling adalah proses manufaktur subtractive di mana material dihilangkan dari stock (bahan mentah) menggunakan alat potong yang berputar. Fusion 360 digunakan sebagai CAM software untuk menghasilkan toolpath dan G-code.

---

## 13.2 Alur Kerja CNC Router Milling

```
SolidWorks (Part 3D) → Export STEP → Fusion 360 (Import) → 
Fusion 360 CAM (Setup + Toolpath) → Post Process (G-code) → 
CNC Router (Eksekusi)
```

---

## 13.3 Konsep Dasar CNC Milling

### Sumbu Mesin:
- **X**: Horizontal (kiri-kanan)
- **Y**: Horizontal (depan-belakang)
- **Z**: Vertikal (atas-bawah)

### Jenis Operasi:
| Operasi | Deskripsi |
|---------|-----------|
| **Face** | Meratakan permukaan atas stock |
| **2D Contour** | Memotong kontur 2D (profil luar/dalam) |
| **2D Pocket** | Mengosongkan area tertutup |
| **2D Adaptive** | Roughing efisien dengan toolpath adaptive |
| **Drill** | Membuat lubang |
| **Bore** | Memperbesar lubang yang sudah ada |
| **Engrave** | Mengukir teks atau pattern |
| **3D Contour** | Finishing permukaan 3D |
| **3D Adaptive** | Roughing 3D |
| **3D Parallel** | Finishing dengan jalur paralel |
| **3D Scallop** | Finishing dengan jalur scallop |

### Parameter Pemotongan:

| Parameter | Deskripsi | Contoh (Kayu, Ø6mm end mill) |
|-----------|-----------|-------------------------------|
| **Spindle Speed** | Kecepatan putar spindle (RPM) | 12000-18000 RPM |
| **Feed Rate** | Kecepatan makan horizontal | 1000-2000 mm/min |
| **Plunge Rate** | Kecepatan makan vertikal | 500-800 mm/min |
| **DOC (axial)** | Kedalaman per pass | 2-3mm |
| **WOC (radial)** | Lebar pemotongan | 3-4.5mm (50-75% tool Ø) |
| **Stepover** | Jarak antar jalur finishing | 0.5-2mm |

---

## 13.4 Fusion 360 CAM Setup

### Langkah Setup:
1. **Import STEP** dari SolidWorks
2. Masuk ke **Manufacture** workspace
3. **Setup**: Definisikan:
   - Operation type: Milling
   - Machine: Generic 3-axis
   - Work Coordinate System (WCS): origin pada stock
   - Stock: Box from solid (offset)
4. **Toolpath**: Pilih operasi (2D/3D)
5. **Tool**: Pilih alat potong (end mill, ball end, dll.)
6. **Geometry**: Pilih kontur/pocket/face
7. **Parameters**: Atur speeds & feeds
8. **Simulate**: Verifikasi toolpath
9. **Post Process**: Generate G-code

### Pemilihan Tool:

| Tool | Deskripsi | Penggunaan |
|------|-----------|------------|
| **Flat End Mill** | Ujung datar | Pocket, contour, face |
| **Ball End Mill** | Ujung bulat | 3D surfacing, finishing |
| **Bull Nose** | Ujung datar + radius | Semi-finishing |
| **V-Bit** | Ujung V-shape | Engraving, chamfer |
| **Drill Bit** | Mata bor | Drilling holes |

---

## 13.5 Percobaan 1-10

### Percobaan 1: Import STEP ke Fusion 360
```
Langkah:
1. Buat part sederhana di SolidWorks (plat 100x80x15mm dengan pocket)
2. Export sebagai STEP: File → Save As → STEP AP214
3. Buka Fusion 360
4. File → Open → Import STEP
5. Verifikasi geometri benar (dimensi, features)
6. Switch ke Manufacture workspace
7. Explore interface CAM
8. Identifikasi: Setup, Toolpath, Tool Library, Simulate
9. Screenshot model di Fusion 360
10. Compare dengan model SolidWorks
```

### Percobaan 2: CAM Setup — Stock dan WCS
```
Langkah:
1. Klik Setup → New Setup
2. Operation Type: Milling
3. Machine: Generic 3-axis (atau mesin spesifik di lab)
4. WCS Orientation: Model → Top (Z up)
5. Origin: Stock box point → pilih sudut kiri depan atas
6. Stock:
   - Mode: Relative size box
   - Offset: 1mm setiap sisi (kecuali bawah = 0)
7. Verifikasi stock size
8. OK
9. Screenshot setup dengan WCS axes terlihat
10. Screenshot stock boundaries
```

### Percobaan 3: Face Operation
```
Langkah:
1. Dari percobaan 2, tambahkan operasi Face
2. Tool: Flat End Mill Ø10mm
3. Speeds: 12000 RPM, Feed 1500 mm/min
4. Geometry: Stock top face
5. Passes: Stepover 7mm (70% tool Ø)
6. Heights: Default (dari stock top ke model top)
7. OK → Generate toolpath
8. Klik Simulate → watch material removal
9. Verifikasi semua permukaan atas terface dengan rata
10. Screenshot toolpath + simulasi
```

### Percobaan 4: 2D Contour (Profil Luar)
```
Langkah:
1. Tambahkan operasi 2D Contour
2. Tool: Flat End Mill Ø6mm
3. Geometry: Pilih bottom edge (kontur luar part)
4. Tabs: Enable tabs (3mm wide, 1mm height, 4 tabs)
5. Passes:
   - Multiple depths: 3mm per pass
   - Stock to leave: 0mm (finishing)
6. Entry: Lead-in arc
7. Heights: From stock top to bottom
8. Generate → Simulate
9. Verifikasi part terpisah dari stock (with tabs)
10. Screenshot toolpath
```

### Percobaan 5: 2D Pocket
```
Langkah:
1. Desain part dengan pocket (SolidWorks): 
   Plat 100x80x15mm, pocket 60x40x10mm di tengah
2. Export STEP → Import Fusion 360
3. New Setup → Stock
4. Operasi 2D Pocket
5. Tool: Flat End Mill Ø6mm
6. Geometry: Pilih bottom face pocket
7. Passes: Multiple depths 3mm, Finishing pass
8. Ramp: Helical (spiral masuk)
9. Generate → Simulate
10. Catat: waktu estimasi, jumlah pass
```

### Percobaan 6: Drilling
```
Langkah:
1. Modifikasi part: tambahkan 4 lubang Ø8mm pada 4 sudut
2. Export STEP → Import
3. Operasi: Drill
4. Tool: Drill Ø8mm (dari library)
5. Geometry: Pilih 4 lubang
6. Cycle type: Drilling — peck drill (G83)
7. Peck depth: 3mm
8. Generate → Simulate
9. Verifikasi semua lubang terbor
10. Screenshot
```

### Percobaan 7: Engraving (V-Carve)
```
Langkah:
1. Desain part dengan text engrave "CADCAM LAB"
   (SolidWorks: Sketch text → Extruded Cut 0.5mm)
2. Export STEP → Import
3. Operasi: Engrave (atau 2D Contour)
4. Tool: V-bit 60° atau Flat End Mill Ø1mm
5. Geometry: Pilih kontur text
6. Depth: 0.5mm
7. Generate → Simulate
8. Perhatikan detail text terbaca
```

### Percobaan 8: 3D Adaptive Clearing (Roughing)
```
Langkah:
1. Desain part 3D (dome/freeform surface dari Modul 5)
2. Export STEP → Import
3. Operasi: 3D Adaptive Clearing
4. Tool: Flat End Mill Ø6mm
5. Stock to leave: 0.5mm (untuk finishing)
6. Optimal load: 40% WOC
7. Generate → Simulate → lihat roughing pass
8. Catat waktu estimasi roughing
```

### Percobaan 9: 3D Finishing (Parallel)
```
Langkah:
1. Lanjutkan dari percobaan 8
2. Operasi: Parallel (3D finishing)
3. Tool: Ball End Mill Ø6mm
4. Stepover: 0.5mm (untuk permukaan halus)
5. Stock to leave: 0mm
6. Direction: Along X atau Along Y
7. Generate → Simulate
8. Bandingkan waktu roughing vs finishing
9. Catat total machining time
```

### Percobaan 10: Post Processing dan Eksekusi
```
Langkah:
1. Finalisasi semua toolpath dari percobaan 3-9
2. Atur urutan operasi: Face → Pocket → Drill → Contour
3. Post Process:
   - Select: All operations
   - Post: Generic GRBL / LinuxCNC / sesuai mesin di lab
   - Output folder
   - Program name: NIM_test
4. Generate G-code
5. Review G-code (buka dengan text editor)
6. Transfer ke CNC Router
7. Setup mesin: Home, set WCS zero, install tool
8. Dry run (tanpa material) jika memungkinkan
9. EKSEKUSI pada material (kayu/MDF)
10. Rekam proses dengan HP (VIDEO WAJIB)
```

---

## 13.6 Keselamatan Kerja CNC Router

⚠️ **WAJIB:**
1. Gunakan kacamata pelindung dan masker debu
2. Pastikan material terjepit kuat (clamp/vacuum)
3. Jangan mendekati spindle yang berputar
4. Matikan spindle sebelum mengganti tool
5. Ketahui lokasi emergency stop
6. Jangan tinggalkan mesin tanpa pengawasan

---

*Modul Praktikum CAD/CAM — Modul 13: CAM Router Milling*
*Disusun untuk keperluan pendidikan*
