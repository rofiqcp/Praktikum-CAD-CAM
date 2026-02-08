# MODUL 10: CAM LASER CUTTING — SolidWorks → CorelDRAW → Software Laser

## Praktikum CAD/CAM — Pertemuan 10

---

## 10.1 Pendahuluan

Laser cutting adalah proses pemotongan material menggunakan sinar laser yang difokuskan. Proses ini sangat presisi dan dapat memotong berbagai material seperti akrilik, MDF, kayu, kain, dan logam tipis.

---

## 10.2 Alur Kerja Laser Cutting

```
SolidWorks (Desain) → Export DXF → CorelDRAW (Edit/Layout) → 
Software Laser (RDWorks/LightBurn) → Mesin Laser (Eksekusi)
```

### Langkah Detail:
1. **SolidWorks**: Buat desain 2D (sketch) atau flat pattern (sheet metal)
2. **Export DXF**: `File → Save As → DXF (*.dxf)`
3. **CorelDRAW**: Import DXF → edit/layout → atur warna (cut vs engrave)
4. **Software Laser**: Import dari CorelDRAW → atur parameter laser
5. **Mesin Laser**: Eksekusi pemotongan

---

## 10.3 Pengaturan Warna di CorelDRAW untuk Laser

| Warna | Fungsi | Parameter |
|-------|--------|-----------|
| **Merah** (RGB 255,0,0) | Cutting | Power tinggi, speed rendah |
| **Biru** (RGB 0,0,255) | Engraving (vektor) | Power rendah, speed tinggi |
| **Hitam** (RGB 0,0,0) | Raster Engraving | Power rendah, speed tinggi |
| **Hijau** (RGB 0,255,0) | Scoring/marking | Power rendah |
| **Kuning** | Cutting priority 2 | |

### Tips CorelDRAW:
- Gunakan **Hairline** width untuk cutting (bukan outline tebal)
- Pastikan semua objek dalam mode **Wireframe**
- Konversi text ke **Curves** sebelum export
- Atur ukuran kerja sesuai bed laser

---

## 10.4 Parameter Laser Cutting

### Parameter Umum Akrilik:

| Material | Tebal | Power (%) | Speed (mm/s) | Hasil |
|----------|-------|-----------|--------------|-------|
| Akrilik | 2mm | 40-50 | 15-20 | Cut through |
| Akrilik | 3mm | 50-60 | 10-15 | Cut through |
| Akrilik | 5mm | 70-80 | 5-10 | Cut through |
| Akrilik | 2mm | 15-20 | 200-300 | Engrave |
| MDF | 3mm | 50-60 | 15-20 | Cut through |
| MDF | 6mm | 70-80 | 5-10 | Cut through |
| Kayu | 3mm | 40-50 | 15-20 | Cut through |

> ⚠️ Parameter di atas adalah perkiraan. **Selalu lakukan test cut** pada material sebenarnya!

---

## 10.5 Konsep Kerf dan Kompensasi

### Kerf:
- Lebar material yang hilang akibat laser beam (~0.1-0.3mm)
- Perlu kompensasi untuk part yang butuh presisi fit
- **Inside cut**: Offset ke dalam sebesar kerf/2
- **Outside cut**: Offset ke luar sebesar kerf/2

### Nesting:
- Mengatur layout potongan untuk **efisiensi material**
- Minimalkan jarak antar part (2-3mm minimum)
- Pertimbangkan arah serat (untuk kayu)

---

## 10.6 Percobaan 1-10

### Percobaan 1: Export DXF dari SolidWorks (Sketch)
```
Langkah:
1. Buka SolidWorks → buat sketch 2D sederhana (kotak 50x50mm dengan lingkaran Ø20 di tengah)
2. File → Save As → pilih DXF (*.dxf)
3. Pilih "Faces/Loops/Edges" atau "Sketch Entities"
4. Klik Options → DXF/DWG Output
5. Pilih versi DXF: R14 atau R2000 (kompatibilitas terbaik)
6. Save
7. Buka CorelDRAW → Import DXF
8. Verifikasi dimensi benar
9. Atur warna garis: Merah untuk cut
10. Screenshot proses dan hasil
```

### Percobaan 2: Export DXF dari Sheet Metal Flat Pattern
```
Langkah:
1. Buka part sheet metal dari Modul 7 (misal: Box Sederhana)
2. Klik Flatten (bentangkan)
3. File → Save As → DXF
4. Pilih "Sheet Metal" pada DXF export options
5. Centang "Geometry" dan "Bend Lines"
6. Save
7. Buka di CorelDRAW
8. Atur warna: Merah (cut), Biru (bend lines/score)
9. Verifikasi dimensi
10. Screenshot
```

### Percobaan 3: Desain Name Tag (SolidWorks + CorelDRAW)
```
Spesifikasi:
- Ukuran: 80 x 30mm
- Material: Akrilik 3mm
- Outline: Cut (merah)
- Text nama: Engrave (hitam, raster)
- Logo/motif: Engrave vektor (biru)
- Lubang gantungan: Ø3mm
- Fillet sudut: R5

Langkah di SolidWorks:
1. Buat sketch name tag → Export DXF (outline saja)
Langkah di CorelDRAW:
2. Import DXF → tambahkan text nama (font: Arial)
3. Tambahkan logo/motif dekoratif
4. Atur warna sesuai layer (cut/engrave)
5. Convert text to curves
```

### Percobaan 4: Desain Gantungan Kunci (Keychain)
```
Spesifikasi:
- Material: Akrilik 3mm
- Bentuk: Custom shape (inisial nama, bentuk hewan, dll)
- Ukuran max: 50 x 50mm
- Lubang keyring: Ø4mm
- Engraving: Nama atau pattern
- Desain lengkap di SolidWorks → Export DXF → CorelDRAW
```

### Percobaan 5: Desain Coaster (Alas Gelas)
```
Spesifikasi:
- Material: MDF 3mm
- Diameter: Ø90mm
- Pattern engraving: Geometric pattern (mandala, hexagonal, dll.)
- Desain pattern menggunakan Circular Pattern di SolidWorks
- Export DXF → CorelDRAW → atur Cut dan Engrave
```

### Percobaan 6: Desain Stand HP (Phone Stand) — 2D Flat Pack
```
Spesifikasi:
- Material: Akrilik 3mm
- Desain interlocking (tanpa lem/sekrup)
- 2 part: Base + Support
- Slot interlocking: lebar = 3mm (sesuai material thickness)
- HP bisa berdiri vertikal (portrait)
- Desain di SolidWorks → DXF → CorelDRAW
```

### Percobaan 7: Nesting Layout di CorelDRAW
```
Langkah:
1. Kumpulkan semua DXF dari Percobaan 3-6
2. Import semua ke 1 file CorelDRAW
3. Atur bed size sesuai laser cutter (600 x 400mm)
4. Layout semua part untuk efisiensi material (nesting)
5. Atur jarak antar part: min 3mm
6. Atur urutan cutting: engrave dulu, cut terakhir
7. Atur urutan cut: inside holes dulu, outline terakhir
8. Verifikasi semua warna benar
9. Save sebagai .cdr dan .pdf
10. Screenshot layout
```

### Percobaan 8: Import ke Software Laser (RDWorks/LightBurn)
```
Langkah:
1. Buka RDWorks / LightBurn
2. Import file dari CorelDRAW (.dxf atau via clipboard)
3. Atur parameter laser per layer/warna:
   - Cut: Power, Speed, jumlah pass
   - Engrave: Power, Speed, DPI (untuk raster)
4. Verifikasi ukuran di software laser
5. Atur posisi origin/home
6. Preview toolpath / simulasi
7. Atur urutan proses
8. Screenshot parameter settings
9. Screenshot preview/simulasi
10. Siap untuk eksekusi (akan dilakukan saat eksekusi mesin)
```

### Percobaan 9: Test Cut dan Parameter Tuning
```
Langkah (di mesin laser):
1. Siapkan material test (akrilik kecil 100x100mm)
2. Buat grid test: kotak 10x10mm dengan parameter berbeda
   - Variasi Power: 30%, 40%, 50%, 60%, 70%
   - Variasi Speed: 5, 10, 15, 20 mm/s
3. Eksekusi test grid
4. Evaluasi hasil: cut through? clean edge? burning?
5. Tentukan parameter optimal untuk material
6. Dokumentasikan dengan foto
7. Catat parameter terbaik
8. Rekam proses dengan HP
9. Buat tabel hasil test
10. Simpan sebagai referensi
```

### Percobaan 10: Eksekusi Laser Cutting Proyek
```
Langkah:
1. Load file nesting (Percobaan 7) ke software laser
2. Set parameter sesuai hasil test (Percobaan 9)
3. Pasang material (akrilik/MDF) pada bed laser
4. Set focus laser (adjust Z-height)
5. Set origin point
6. Run preview/boundary check (laser menelusuri batas tanpa cutting)
7. Nyalakan exhaust fan
8. Start cutting!
9. Rekam proses dengan HP (VIDEO WAJIB)
10. Ambil hasil, bersihkan, dan dokumentasikan
```

---

## 10.7 Keselamatan Kerja Laser Cutting

⚠️ **WAJIB DIPATUHI:**
1. Jangan pernah meninggalkan mesin laser tanpa pengawasan saat beroperasi
2. Selalu gunakan exhaust/ventilasi
3. Jangan memotong material PVC/vinil (menghasilkan gas beracun HCl)
4. Gunakan kacamata pelindung jika diperlukan
5. Ketahui lokasi dan cara menggunakan alat pemadam api
6. Jangan melihat langsung ke sinar laser

---

*Modul Praktikum CAD/CAM — Modul 10: CAM Laser Cutting*
*Disusun untuk keperluan pendidikan*
