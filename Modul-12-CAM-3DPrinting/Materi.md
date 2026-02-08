# MODUL 12: CAM 3D PRINTING — SolidWorks → Slicer Software (STL Export)

## Praktikum CAD/CAM — Pertemuan 12

---

## 12.1 Pendahuluan

3D Printing (Additive Manufacturing) adalah proses manufaktur yang membuat objek 3D dari model digital dengan menambahkan material layer per layer. Teknologi paling umum untuk desktop adalah **FDM (Fused Deposition Modeling)**.

---

## 12.2 Alur Kerja 3D Printing

```
SolidWorks (Part 3D) → Export STL → Slicer (Cura/PrusaSlicer) → 
G-code → 3D Printer → Post-Processing
```

---

## 12.3 Prinsip FDM 3D Printing

### Cara Kerja:
1. Filamen plastik (PLA/ABS/PETG) dipanaskan di **hotend**
2. Material cair diekstrusi melalui **nozzle** (umumnya Ø0.4mm)
3. Material diletakkan **layer per layer** di atas **build plate**
4. Setiap layer mengeras dan menyatu dengan layer sebelumnya

### Parameter Penting:

| Parameter | Deskripsi | Nilai Umum |
|-----------|-----------|------------|
| **Layer Height** | Ketebalan per layer | 0.1-0.3mm |
| **Nozzle Diameter** | Diameter nozzle | 0.4mm |
| **Infill Density** | Kepadatan pengisian internal | 15-100% |
| **Infill Pattern** | Pola pengisian | Grid, Gyroid, Cubic |
| **Wall Thickness** | Ketebalan dinding | 0.8-1.6mm (2-4 walls) |
| **Print Speed** | Kecepatan cetak | 40-80 mm/s |
| **Temperature (Hotend)** | Suhu nozzle | PLA: 200-220°C |
| **Temperature (Bed)** | Suhu bed | PLA: 50-60°C |
| **Support** | Penyangga overhang | Yes/No |
| **Adhesion** | Tipe adhesi bed | Skirt/Brim/Raft |

---

## 12.4 Design for 3D Printing (Df3DP)

### Aturan Desain:

| Aturan | Nilai | Keterangan |
|--------|-------|------------|
| **Minimum Wall Thickness** | ≥ 0.8mm | 2x nozzle diameter |
| **Minimum Feature Size** | ≥ 0.4mm | = nozzle diameter |
| **Overhang Angle** | ≤ 45° tanpa support | Di atas 45° perlu support |
| **Bridge Distance** | ≤ 10mm | Jarak spanning tanpa support |
| **Minimum Hole Size** | ≥ 2mm | Lubang kecil bisa tertutup |
| **Tolerance** | ±0.2-0.5mm | Tergantung printer |
| **Clearance** | ≥ 0.3mm | Jarak antar part yang bergerak |
| **Text Height** | ≥ 6mm | Agar terbaca |

### Orientasi Print:
- **Orientasi mempengaruhi**: Kekuatan, kualitas permukaan, waktu cetak, support
- **Layer lines**: Lemah di arah Z (antar layer)
- **Kuat di arah X-Y**: Searah layer

---

## 12.5 Export STL dari SolidWorks

### Langkah Export:
1. `File → Save As → STL (*.stl)`
2. Klik **Options**:
   - Output as: Binary (file lebih kecil)
   - Resolution: Fine (deviation 0.02mm, angle 5°)
   - Atau Custom sesuai kebutuhan
3. **Save**

### Quality Settings:
| Setting | Deviation | Angle | File Size | Kualitas |
|---------|-----------|-------|-----------|----------|
| Coarse | 0.1mm | 30° | Kecil | Rendah |
| Fine | 0.02mm | 5° | Medium | Bagus |
| Custom | User-defined | User-defined | Varies | Custom |

---

## 12.6 Percobaan 1-10

### Percobaan 1: Export STL dan Import ke Slicer
```
Langkah:
1. Buat balok sederhana 30x20x15mm di SolidWorks
2. Tambahkan fillet R3 pada edge atas
3. Export ke STL (Fine quality)
4. Buka Cura / PrusaSlicer
5. Import STL file
6. Atur posisi pada build plate
7. Atur parameter: Layer 0.2mm, Infill 20%, No Support
8. Slice → preview layer by layer
9. Catat: waktu cetak, penggunaan filamen, jumlah layer
10. Export G-code (belum print)
```

### Percobaan 2: Pengaruh Orientasi Print
```
Langkah:
1. Buat L-bracket sederhana dari SolidWorks
2. Export STL
3. Import ke Cura → slice dengan 3 orientasi berbeda:
   a. Flat (lengan horizontal di bed)
   b. Upright (lengan vertikal)
   c. Side (miring 45°)
4. Untuk setiap orientasi, catat:
   - Waktu cetak
   - Penggunaan filamen
   - Volume support
   - Kualitas permukaan (estimasi)
5. Bandingkan dan tentukan orientasi optimal
6. Screenshot preview setiap orientasi
```

### Percobaan 3: Pengaruh Infill
```
Langkah:
1. Buat kubus 40x40x40mm (SolidWorks → STL)
2. Slice dengan variasi infill:
   a. 0% (hollow + wall)
   b. 10% Grid
   c. 20% Grid
   d. 50% Grid
   e. 100% Solid
3. Untuk masing-masing, catat: waktu, filamen, estimasi kekuatan
4. Slice juga dengan infill pattern berbeda (20%):
   a. Grid
   b. Gyroid
   c. Cubic
   d. Lines
5. Bandingkan semua parameter
```

### Percobaan 4: Custom Support dan Overhang Test
```
Spesifikasi:
- Desain test piece overhang di SolidWorks:
  - Balok base 40x40x5mm
  - 5 overhang tab pada sudut: 20°, 30°, 45°, 60°, 75°
  - Setiap tab: 15x10x3mm
- Export STL
- Slice TANPA support → preview overhang
- Slice DENGAN support → preview support structure
- Bandingkan waktu dan filamen
- PRINT test piece ini (pilih salah satu)
```

### Percobaan 5: Desain Box dengan Snap Fit (DfAM)
```
Spesifikasi:
- Box: 50x40x30mm
- Lid (tutup) terpisah
- Snap-fit mechanism: Cantilever snap
- Clearance snap: 0.3mm
- Wall thickness: 2mm
- No support required (design for printability)
- Export STL terpisah (box + lid)
- Slice keduanya → posisikan pada build plate
```

### Percobaan 6: Desain Phone Stand (3D Printable)
```
Spesifikasi:
- Stand HP yang dicetak tanpa support
- Sudut kemiringan: 60° dari horizontal
- Base: stabil, tidak mudah jatuh
- Kabel charging port: ada channel/slot
- Material: PLA
- Max print time: 4 jam
- Orientasi: desain agar tidak butuh support
```

### Percobaan 7: Desain Bearing/Bushing
```
Spesifikasi:
- Bushing: OD Ø15mm, ID Ø8mm (sesuai shaft), panjang 10mm
- Clearance fit: +0.3mm pada ID
- Flange bushing: flange Ø20mm, tebal 2mm
- Tolerance test: buat 3 versi dengan ID berbeda (7.5, 8.0, 8.3mm)
- Print ketiga versi → test fit dengan shaft
- Tentukan clearance optimal
```

### Percobaan 8: Desain Gear 3D Printable
```
Spesifikasi:
- Spur gear: Module 2, Z=20
- Dimodifikasi dari Modul 3
- Bore: Ø6mm + D-cut (flat)
- Hub: Ø12mm, tinggi 3mm
- Lebar gigi: 8mm
- Tip: Atur clearance + 0.1mm pada tooth profile
- Print → test mesh dengan gear lain
```

### Percobaan 9: Part Robot (dari Modul 9 atau 11)
```
Langkah:
1. Pilih 1-2 part dari robot beroda/lengan yang cocok di-3D print
   (misal: wheel hub, sensor bracket, gripper jaws)
2. Modifikasi desain jika perlu untuk printability
3. Atur orientasi optimal
4. Slice dengan parameter sesuai
5. PRINT part ini
6. Test fit dengan komponen lain
7. Rekam proses printing dengan HP
```

### Percobaan 10: Eksekusi 3D Printing
```
Langkah:
1. Pilih 2-3 part terbaik dari percobaan sebelumnya
2. Nesting pada build plate (print sekaligus)
3. Final check parameter:
   - Layer height: 0.2mm
   - Infill: 20-30%
   - Support: sesuai kebutuhan
   - Adhesion: Brim (3mm)
4. Export G-code
5. Transfer ke 3D printer (USB/SD/WiFi)
6. Prepare printer: level bed, load filament
7. Start print
8. Rekam proses dengan HP (time-lapse jika bisa)
9. Monitor print → troubleshoot jika ada masalah
10. Post-process: remove support, clean up
```

---

## 12.7 Troubleshooting 3D Print

| Masalah | Penyebab | Solusi |
|---------|----------|-------|
| Warping | Bed temp rendah, no adhesion | Brim/raft, naikkan bed temp |
| Stringing | Retraction kurang | Naikkan retraction (6-7mm) |
| Layer shift | Belt loose, speed terlalu tinggi | Kencangkan belt, kurangi speed |
| Under-extrusion | Nozzle clog, temp rendah | Bersihkan nozzle, naikkan temp |
| Elephant foot | Bed temp terlalu tinggi, nozzle terlalu dekat | Kurangi bed temp, naikkan Z-offset |

---

*Modul Praktikum CAD/CAM — Modul 12: CAM 3D Printing*
*Disusun untuk keperluan pendidikan*
