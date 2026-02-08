# MODUL 10: CAM LASER CUTTING — REALISASI ROBOT BERODA + TULISAN NAMA

## Praktikum CAD/CAM — Pertemuan 10

---

## Daftar Isi
1. [Pendahuluan](#101-pendahuluan)
2. [Alur Kerja Laser Cutting](#102-alur-kerja-laser-cutting)
3. [Pengaturan Warna Layer](#103-pengaturan-warna-layer)
4. [Parameter Laser Cutting Akrilik](#104-parameter-laser-cutting-akrilik)
5. [Kerf dan Kompensasi](#105-kerf-dan-kompensasi)
6. [Nesting untuk Efisiensi Material](#106-nesting-untuk-efisiensi-material)
7. [Engraving Tulisan Nama](#107-engraving-tulisan-nama)
8. [Percobaan 1–10](#108-percobaan-110)
9. [Keselamatan Kerja](#109-keselamatan-kerja)

---

## 10.1 Pendahuluan

Modul ini merealisasikan desain **Robot Beroda Flat-Pack** dari Modul 9 menggunakan **mesin laser cutting**. Selain memotong panel-panel robot, kita juga akan **mengengrave tulisan nama, NIM, dan logo** pada panel akrilik.

### Koneksi dari Modul Sebelumnya
```
Modul 9 (Robot Beroda CAD) → DXF files → Modul 10 (ini) → Laser Cut + Engrave → Robot Fisik
                                                          → Juga: part konveyor (Modul 8)
```

### Yang Akan Diproduksi di Modul Ini:
1. **Panel-panel robot beroda** (dari Modul 9) — semua panel akrilik
2. **Engraving nama + NIM** — pada panel robot
3. **Part konveyor** (dari Modul 8) — end plates, holders, bearing housing, side guide
4. **Tulisan nama terpisah** — name tag / label akrilik dengan engraving

---

## 10.2 Alur Kerja Laser Cutting

```
SolidWorks (Desain 3D) → Export DXF (2D flat) → CorelDRAW (Layout/Nesting) → 
Software Laser (RDWorks/LightBurn) → Mesin Laser CO₂ (Eksekusi)
```

### Langkah Detail:
1. **SolidWorks**: Desain part → sketch 2D atau flat pattern
2. **Export DXF**: `File → Save As → DXF (*.dxf)` — pilih versi R14/R2000
3. **CorelDRAW**: Import DXF → edit layout → atur warna layer → nesting
4. **Software Laser**: Import → atur parameter per warna → preview/simulate
5. **Mesin Laser**: Focus → origin → boundary check → EKSEKUSI

---

## 10.3 Pengaturan Warna Layer

| Warna | RGB | Fungsi | Parameter Laser |
|-------|-----|--------|-----------------|
| **Merah** | 255,0,0 | **Cutting** (potong tembus) | Power tinggi, speed rendah |
| **Biru** | 0,0,255 | **Engraving Vektor** (garis/logo) | Power rendah, speed tinggi |
| **Hitam** | 0,0,0 | **Raster Engraving** (teks/area fill) | Power rendah, speed tinggi |
| **Hijau** | 0,255,0 | **Scoring/Marking** (garis tipis) | Power rendah, speed tinggi |
| **Kuning** | 255,255,0 | **Cutting priority 2** (potong internal) | Sama dengan merah |

### Urutan Eksekusi (PENTING!)
```
1. Raster Engraving (Hitam) — engrave area/teks dulu
2. Vektor Engraving (Biru) — engrave garis/logo
3. Internal Cutting (Kuning) — potong lubang-lubang di dalam
4. External Cutting (Merah) — potong kontur luar TERAKHIR
```
> ⚠️ Selalu potong **kontur luar terakhir** agar part tidak bergeser saat proses berlangsung!

### Tips CorelDRAW:
- Gunakan **Hairline** width (0.001mm) untuk semua garis cutting
- Pastikan objek dalam mode **Outline/Wireframe**
- Konversi **text ke Curves** (`Ctrl+Q`) sebelum export ke software laser
- Atur ukuran page sesuai bed laser (600×400mm atau 900×600mm)

---

## 10.4 Parameter Laser Cutting Akrilik

### Parameter Cutting:
| Material | Tebal | Power (%) | Speed (mm/s) | Passes | Hasil |
|----------|-------|-----------|--------------|--------|-------|
| Akrilik | 2mm | 40–50 | 15–20 | 1 | Cut through |
| Akrilik | 3mm | 50–65 | 10–15 | 1 | Cut through |
| Akrilik | 5mm | 70–80 | 5–10 | 1–2 | Cut through |
| Akrilik | 2mm | 15–20 | 200–300 | 1 | Raster Engrave |
| Akrilik | 3mm | 15–25 | 200–300 | 1 | Raster Engrave |
| Akrilik | 3mm | 10–15 | 100–200 | 1 | Vektor Engrave |

> ⚠️ Parameter di atas adalah perkiraan untuk laser CO₂ 60–80W. **Selalu test cut** pada material sebenarnya!

### Parameter untuk Tulisan Nama (Engraving):
| Jenis | Power (%) | Speed (mm/s) | DPI | Keterangan |
|-------|-----------|--------------|-----|------------|
| Teks kecil (< 10mm) | 12–18 | 250–350 | 300 | Raster, detail halus |
| Teks besar (> 10mm) | 15–25 | 200–300 | 300 | Raster, lebih dalam |
| Logo/pattern vektor | 10–15 | 100–200 | — | Vektor, garis outline |
| Deep engrave (timbul) | 20–30 | 100–150 | 500 | Multi-pass, lebih dalam |

---

## 10.5 Kerf dan Kompensasi

### Kerf Width:
- Lebar material yang **hilang** akibat sinar laser ≈ 0.1–0.3mm
- Untuk akrilik 3mm dengan laser CO₂ 60W: kerf ≈ 0.15mm

### Kapan Perlu Kompensasi:
| Situasi | Kompensasi |
|---------|------------|
| Tab-slot interlocking | Kurangi slot width 0.1mm (kerf membuat slot lebih besar) |
| Press-fit bearing | Kurangi lubang 0.1mm (kerf membuat lubang lebih besar) |
| Loose fit (clearance) | Tidak perlu kompensasi |
| Part dekoratif | Tidak perlu kompensasi |

---

## 10.6 Nesting untuk Efisiensi Material

### Prinsip Nesting:
1. Susun semua part di 1 sheet akrilik (minimize waste)
2. Jarak antar part: minimum **3mm** (safety margin)
3. Jarak dari edge sheet: minimum **5mm**
4. Pertimbangkan urutan cutting (inside → outside)
5. Part kecil dulu, besar terakhir (mengurangi pergerakan material)

### Contoh Nesting Robot Beroda:
```
Sheet Akrilik 400 × 600 mm:
┌──────────────────────────────────────────────────────┐
│  ┌──────────┐  ┌──────────┐  ┌─────────┐            │
│  │ Bottom   │  │ Top      │  │ Front   │            │
│  │ 150×120  │  │ 150×120  │  │ 120×80  │            │
│  │          │  │ +engrave │  │         │            │
│  └──────────┘  └──────────┘  └─────────┘            │
│  ┌──────────┐  ┌──────────┐  ┌─────────┐ ┌────────┐│
│  │ Side L   │  │ Side R   │  │ Back    │ │MotorMt ││
│  │ 150×80   │  │ 150×80   │  │ 120×80  │ │120×50  ││
│  └──────────┘  └──────────┘  └─────────┘ └────────┘│
│  ┌──────┐ ┌──────┐ ┌────────┐ ┌──────┐ ┌──────────┐│
│  │PCB   │ │BattBr│ │SensrBr │ │Name  │ │Sisa area ││
│  │80×60 │ │60×40 │ │50×30   │ │tag   │ │          ││
│  └──────┘ └──────┘ └────────┘ └──────┘ └──────────┘│
└──────────────────────────────────────────────────────┘
```

---

## 10.7 Engraving Tulisan Nama

### 10.7.1 Jenis Engraving
| Jenis | Deskripsi | Cocok Untuk |
|-------|-----------|-------------|
| **Raster Engraving** | Area/fill — laser scan bolak-balik | Teks, foto, area shading |
| **Vektor Engraving** | Garis/outline — laser mengikuti path | Logo, pattern, border |
| **Deep Engraving** | Multi-pass raster — lebih dalam | Teks timbul (invert: area sekitar teks di-engrave) |

### 10.7.2 Desain Tulisan Nama
```
Konten yang di-engrave pada panel robot:
┌──────────────────────────────────┐
│                                  │
│    ██████╗  NAMA MAHASISWA       │  ← Raster engrave (hitam)
│    ██╔═══╝  NIM: 12345678       │  ← Raster engrave (hitam)
│    ██████╗  "ROBOT BERODA"       │  ← Raster engrave (hitam)
│    ╚═══██║                       │
│    ██████║  ┌──────┐             │  ← Logo vektor engrave (biru)
│    ╚═════╝  │ LOGO │             │
│             └──────┘             │
│    ═══════════════════════       │  ← Border vektor engrave (biru)
└──────────────────────────────────┘
```

### 10.7.3 Tips Engraving Teks
1. **Font**: Gunakan font sans-serif (Arial, Helvetica) untuk keterbacaan
2. **Ukuran minimum**: 5mm tinggi huruf (agar terbaca setelah engrave)
3. **Convert to Curves**: WAJIB di CorelDRAW sebelum export (`Ctrl+Q`)
4. **Warna background**: Akrilik warna gelap → engrave terlihat putih (kontras bagus)
5. **Akrilik bening**: Engrave terlihat frosted/buram — tetap estetis
6. **Multi-line**: Atur spacing antar baris ≥ 2mm

---

## 10.8 Percobaan 1–10

### Percobaan 1: Export DXF dari SolidWorks (Panel Robot)
```
Langkah:
1. Buka file panel robot dari Modul 9 (misal: Bottom Panel)
2. File → Save As → DXF (*.dxf)
3. Pilih "Faces/Loops/Edges" → pilih face atas
4. DXF Options: Version R14 atau R2000
5. Save
6. Buka CorelDRAW → Import DXF → verifikasi dimensi (1:1, mm)
7. Atur warna garis: Merah untuk cut
8. Set outline ke Hairline
9. Ulangi untuk semua panel robot (10+ files)
10. Screenshot proses dan hasil
```

### Percobaan 2: Setup Engraving Nama di CorelDRAW
```
Langkah:
1. Buka DXF top panel robot di CorelDRAW
2. Kontur panel → warna Merah (cut)
3. Lubang/slot → warna Merah atau Kuning (cut internal)
4. Tambahkan teks: Nama + NIM → font Arial Bold, size 8–12mm
5. Tambahkan teks: "ROBOT BERODA" → font Impact/Arial Black, size 15mm
6. Tambahkan logo (import vektor atau buat di CorelDRAW)
7. Teks → warna Hitam (raster engrave)
8. Logo/motif → warna Biru (vektor engrave)
9. Convert ALL text to Curves (Ctrl+Q)
10. Simpan .CDR
```

### Percobaan 3: Buat Name Tag / Label Terpisah (Engrave)
```
Spesifikasi:
- Ukuran: 80 × 35mm, fillet R5
- Material: Akrilik 3mm
- Lubang gantungan: Ø4mm
- Konten engrave:
  - Baris 1: Nama (bold, 8mm)
  - Baris 2: NIM (regular, 5mm)
  - Baris 3: "Praktikum CAD/CAM 2026" (italic, 4mm)
  - Logo/ikon kecil (vektor)
- Border dekoratif: garis double frame (vektor engrave)

Langkah:
1. SolidWorks: sketch name tag → Export DXF (outline saja)
2. CorelDRAW: Import DXF → Outline = Merah (cut)
3. Tambahkan teks → Hitam (raster engrave)
4. Tambahkan border → Biru (vektor engrave)
5. Convert to Curves → Save .CDR
```

### Percobaan 4: Nesting Semua Panel Robot + Name Tag
```
Langkah:
1. Buka CorelDRAW → New document, page = 400×600mm (atau sesuai bed laser)
2. Import semua DXF panel robot (10+ panel)
3. Import name tag (percobaan 3)
4. Import part konveyor (dari Modul 8): end plates, holders, bearing housing, side guide
5. NESTING: susun semua part → minimalisir waste
6. Atur jarak antar part: min 3mm
7. Verifikasi semua warna benar (merah=cut, hitam=engrave, biru=engrave vektor)
8. Verifikasi semua teks sudah Convert to Curves
9. Cek total area vs sheet size → hitung material efficiency
10. Save .CDR + Export .DXF
```

### Percobaan 5: Import ke Software Laser (RDWorks/LightBurn)
```
Langkah:
1. Buka RDWorks / LightBurn
2. Import file nesting (dari CorelDRAW)
3. Atur parameter per warna/layer:
   - Hitam (raster engrave): Power 18%, Speed 300mm/s, DPI 300
   - Biru (vektor engrave): Power 12%, Speed 150mm/s
   - Kuning (cut internal): Power 60%, Speed 12mm/s
   - Merah (cut external): Power 60%, Speed 12mm/s
4. Atur urutan: Hitam → Biru → Kuning → Merah
5. Verifikasi ukuran dan posisi
6. Set origin point
7. Preview toolpath / simulasi
8. Catat estimasi waktu total
9. Screenshot parameter settings
10. Screenshot preview
```

### Percobaan 6: Test Cut dan Parameter Tuning
```
Langkah:
1. Siapkan material test: akrilik kecil 100×100mm
2. Buat test grid di CorelDRAW:
   - 5 kotak 10×10mm → test CUT dengan Power variasi: 50%, 55%, 60%, 65%, 70%
   - Speed tetap 12mm/s
3. Buat test teks → test ENGRAVE:
   - 5 baris teks "TEST" → Power variasi: 12%, 15%, 18%, 20%, 25%
   - Speed tetap 250mm/s
4. Load ke software laser
5. Eksekusi test pada material
6. Evaluasi:
   - Cut: potong tembus? edge bersih? burning?
   - Engrave: terbaca? kedalaman? kontras?
7. Tentukan parameter optimal
8. Dokumentasikan dengan foto
9. Catat parameter terbaik di tabel
10. Simpan sebagai referensi
```

### Percobaan 7: Eksekusi Laser Cutting — Panel Robot
```
Langkah:
1. Pasang akrilik 3mm pada bed laser
2. Set focus laser (Z-height ke permukaan material)
3. Set origin point (sudut kiri bawah nesting)
4. Run boundary check (laser trace tanpa firing → cek semua muat)
5. Nyalakan exhaust/ventilasi
6. ★ MULAI REKAM VIDEO dengan HP ★
7. Start proses: Raster engrave (teks nama) — HP rekam
8. Proses: Vektor engrave (logo/motif) — HP rekam
9. Proses: Internal cutting (lubang, slot) — HP rekam
10. Proses: External cutting (kontur luar) — HP rekam
```

### Percobaan 8: Eksekusi Laser Engraving — Tulisan Nama
```
Langkah:
1. Pastikan engraving sudah tereksekusi pada percobaan 7
   (raster + vektor engrave berjalan sebelum cutting)
2. Jika belum, jalankan terpisah:
   - Name tag: engrave dulu, kemudian cut
   - Panel top: engrave nama, NIM, logo
3. Evaluasi hasil engraving:
   - Teks terbaca? Kontras cukup?
   - Logo terlihat jelas?
   - Kedalaman engrave konsisten?
4. Foto close-up hasil engraving
5. Jika kurang → adjust parameter → re-engrave pada test piece
```

### Percobaan 9: Assembly Robot Beroda Fisik
```
Langkah:
1. Lepaskan semua part dari sheet akrilik
2. Bersihkan edge (amplas halus jika perlu)
3. Lepas film pelindung
4. Ikuti assembly sequence dari Modul 9:
   a. Pasang motor pada motor mount panel
   b. Rakit bottom panel + motor mount panel
   c. Pasang side panels (kiri + kanan)
   d. Pasang front panel + back panel
   e. Pasang PCB shelf + Arduino
   f. Pasang battery holder + baterai
   g. Pasang sensor bracket + sensor
   h. Pasang wheels pada motor shaft
   i. Pasang castor wheel
   j. Pasang top cover (dengan engraving nama)
5. Test tab-slot fit:
   - Terlalu loose? → catat, adjust toleransi untuk iterasi berikutnya
   - Terlalu tight? → amplas sedikit
6. Cek stabilitas → robot berdiri tegak?
7. Opsional: lem akrilik pada joint yang longgar
8. FOTO dari semua sisi (6 sisi + 2 perspektif)
9. ★ REKAM VIDEO HP: proses assembly
10. Test fungsional (jika sudah wiring): motor berputar?
```

### Percobaan 10: Dokumentasi & Quality Check
```
Langkah:
1. Quality check final:
   - Semua panel terpasang? ✅/❌
   - Tab-slot fit baik? ✅/❌
   - Engraving terbaca? ✅/❌
   - Robot stabil berdiri? ✅/❌
   - Roda berputar bebas? ✅/❌
   - Sensor terlihat dari depan? ✅/❌
2. Ukur dimensi aktual vs desain (caliper)
3. Foto produk final dari semua sisi
4. Foto detail engraving nama (close-up)
5. Foto name tag terpisah
6. Compile semua foto
7. Compile semua video (proses laser + assembly)
8. Hitung sisa material akrilik (waste percentage)
9. Buat tabel evaluasi:
   | Panel | Fit | Quality | Notes |
10. Tulis analisa dan kesimpulan
```

---

## 10.9 Keselamatan Kerja Laser Cutting

⚠️ **WAJIB DIPATUHI:**
1. **Jangan tinggalkan** mesin laser tanpa pengawasan saat beroperasi
2. Selalu **nyalakan exhaust/ventilasi** sebelum cutting
3. **Jangan memotong PVC/vinil** — menghasilkan gas beracun HCl
4. Gunakan **kacamata pelindung** jika tersedia
5. Ketahui lokasi **pemadam api** dan cara menggunakannya
6. **Jangan melihat langsung** ke sinar laser
7. Pastikan **material rata** di bed (tidak melengkung)
8. Jangan buka cover mesin saat laser aktif

---

*Modul Praktikum CAD/CAM — Modul 10: CAM Laser Cutting*
*Disusun untuk keperluan pendidikan*
