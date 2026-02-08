# JOBSHEET MODUL 5: CAD GAMBAR 3D — PART 3

## Praktikum CAD/CAM — Pertemuan 5

---

## I. Tujuan Praktikum
1. Mahasiswa mampu membuat Configurations untuk variasi produk
2. Mahasiswa mampu menggunakan Design Table dengan Excel
3. Mahasiswa mampu membuat model parametrik dengan Advanced Equations
4. Mahasiswa mampu menggunakan Surface Modeling dasar
5. Mahasiswa mampu membuat struktur frame dengan Weldments
6. Mahasiswa mampu membuat Library Feature untuk reuse
7. Mahasiswa mampu melakukan Import/Export file CAD
8. Mahasiswa mampu mendesain seri profil aluminium dengan Design Table

---

## II. Alat dan Bahan
| No | Alat/Bahan | Jumlah |
|----|------------|--------|
| 1 | Laptop/PC dengan SolidWorks | 1 unit |
| 2 | Mouse 3-button | 1 unit |
| 3 | Microsoft Excel | 1 unit |
| 4 | Referensi: Aluminium Catalog 2020.pdf | 1 file |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 5 untuk teori lengkap teknik lanjutan.

---

## IV. Langkah Percobaan

| No | Percobaan | Feature Utama | Keterangan |
|----|-----------|---------------|------------|
| 1 | Bolt Multi-Size | Configurations | M6, M8, M10 dalam 1 file |
| 2 | Profil Aluminium Series | Design Table | 2020, 3030, 4040, 5050 |
| 3 | Parametric Enclosure | Advanced Equations | IF conditions |
| 4 | Mouse Housing | Surface Modeling | Loft Surface + Thicken |
| 5 | Simple Mold Design | Mold Tools | Core & Cavity split |
| 6 | Aluminium Frame | Weldments | Struktur meja dengan Cut List |
| 7 | T-Slot Library Feature | Library Feature | Reusable T-slot cut |
| 8 | Excel-Driven Bracket | External Link | Parameter dari Excel |
| 9 | In-Context Bracket | In-Context Design | Reference ke assembly |
| 10 | Import & Repair | Import Diagnostics | STEP import + STL export |

---

### Percobaan 1: Bolt Multi-Size dengan Configurations

**Langkah:**
1. New Part → Front Plane
2. Sketch Circle D=6mm (untuk M6)
3. Extrude: 20mm untuk shank
4. Sketch Hexagon untuk head, Extrude 4mm
5. Chamfer edge head dan tip
6. Klik kanan Part Name → Add Configuration → "M6"
7. Add Configuration → "M8"
8. Aktivkan M8, double-click dimensi, ubah sesuai M8
9. Repeat untuk M10

**Output:** M05_P01_BoltMultiSize.sldprt (3 configurations)

---

### Percobaan 2: Profil Aluminium dengan Design Table

**Langkah:**
1. Buat sketch profil aluminium 2020:
   - Square 20x20mm
   - T-slot 6mm pada 4 sisi
   - Center hole Ø4.2mm
2. Extrude: 100mm
3. Insert → Tables → Design Table → Auto-create
4. Edit Design Table di Excel:

```
|               | 2020  | 3030  | 4040  | 5050  |
|---------------|-------|-------|-------|-------|
| D1@Sketch1    | 20    | 30    | 40    | 50    |
| D2@Sketch1    | 6     | 8     | 8     | 8     |
| D3@Sketch1    | 4.2   | 5.3   | 6.8   | 9     |
| D1@Extrude1   | 100   | 100   | 100   | 100   |
```

5. Close Excel, konfigurasi otomatis terbuat

**Output:** M05_P02_ProfilAluminium_Series.sldprt (4 configurations)

---

### Percobaan 3: Parametric Enclosure dengan Equations

**Langkah:**
1. Tools → Equations → Add
2. Global Variables:
   - "Length" = 100
   - "Width" = "Length" * 0.6
   - "Height" = "Length" * 0.4
   - "Wall" = IF("Length" > 150, 3, 2)
   - "Radius" = "Wall" * 2
3. Buat sketch dengan Link to Global Variable
4. Extrude dengan "Height"
5. Shell dengan "Wall"
6. Fillet dengan "Radius"
7. Test: Ubah Length ke 200, lihat perubahan otomatis

**Output:** M05_P03_ParametricEnclosure.sldprt

---

### Percobaan 4: Mouse Housing dengan Surface

**Langkah:**
1. Buat 3 sketch pada 3 plane berbeda (Top, Offset 30mm, Offset 50mm)
2. Sketch 1: Ellipse 80x50mm (base)
3. Sketch 2: Ellipse 70x45mm (middle)
4. Sketch 3: Ellipse 30x20mm (top)
5. Insert → Surface → Lofted Surface → Select 3 profiles
6. Insert → Surface → Planar Surface → tutup base
7. Knit Surface untuk menggabungkan
8. Insert → Boss/Base → Thicken → 2mm (outward)

**Output:** M05_P04_MouseHousing.sldprt

---

### Percobaan 5: Simple Mold Design

**Langkah:**
1. Buat tutup botol sederhana (cylinder Ø30mm, H=15mm, hollow)
2. View → Draft Analysis → 2° draft minimum
3. Tambahkan draft angle pada model jika perlu
4. Insert → Molds → Scale → 1.006 (PP shrinkage)
5. Insert → Molds → Parting Line → select edge
6. Insert → Molds → Parting Surface → 50mm extend
7. Insert → Molds → Tooling Split → Define mold size
8. Result: Core, Cavity, dan Parting Surface bodies

**Output:** M05_P05_MoldDesign.sldprt

---

### Percobaan 6: Aluminium Frame dengan Weldments

**Langkah:**
1. New Part → Insert → Weldments → 3D Sketch aktif
2. Buat kerangka meja:
   - Rectangle 800x500mm pada Top Plane
   - 4 garis vertikal turun 700mm dari 4 corner
3. Insert → Weldments → Structural Member
4. Pilih profil: Square Tube 40x40x3 (atau custom 4040)
5. Select semua horizontal lines → Apply
6. Select semua vertical lines → Apply
7. Insert → Weldments → Trim/Extend → Trim corner
8. Insert → Weldments → End Cap → tutup ujung
9. Lihat Cut List di Feature Tree

**Output:** M05_P06_AluminiumFrame.sldprt

---

### Percobaan 7: T-Slot Library Feature

**Langkah:**
1. New Part → buat T-slot profile cut
   - Rectangle 6x6mm (slot opening)
   - Rectangle 10x4mm (T portion)
2. Cut-Extrude → Through All Both Sides
3. File → Save As → Type: "Lib Feat Part (*.sldlfp)"
4. Name: "TSlot_6mm.sldlfp"
5. Specify References: Face for placement
6. Save to Design Library folder
7. Test: Drag ke part baru

**Output:** TSlot_6mm.sldlfp + M05_P07_TestLibFeature.sldprt

---

### Percobaan 8: Excel-Driven Bracket

**Langkah:**
1. Buat file Excel "Bracket_Params.xlsx":
   | Cell | Parameter | Value |
   |------|-----------|-------|
   | A2   | Length    | 100   |
   | B2   | Width     | 50    |
   | C2   | Thickness | 5     |
   | D2   | Holes     | 4     |

2. New Part SolidWorks
3. Tools → Equations → Link to External File
4. Browse "Bracket_Params.xlsx"
5. Map: "Length" = Cell A2, dst.
6. Buat model dengan dimensi linked
7. Test: Ubah nilai di Excel, rebuild SolidWorks

**Output:** M05_P08_ExcelBracket.sldprt + Bracket_Params.xlsx

---

### Percobaan 9: In-Context Bracket

**Langkah:**
1. Buka assembly dari Modul 6 (atau buat simple assembly)
2. Insert → Component → New Part
3. Pilih face pada part existing sebagai sketch plane
4. Buat sketch bracket yang mengikuti kontur part
5. Extrude → part baru dengan external reference
6. Check Feature Tree: ada "->..." indicating external ref
7. Ubah part referensi → bracket auto update

**Output:** M05_P09_InContextBracket.sldprt (dengan assembly)

---

### Percobaan 10: Import dan Repair STEP File

**Langkah:**
1. Download sample STEP file (atau gunakan STEP dari Modul sebelumnya export)
2. File → Open → Pilih file .stp/.step
3. Check for errors di Feature Tree
4. Tools → Evaluate → Import Diagnostics
5. Repair: Knit gaps, Heal edges, Fill holes
6. File → Save As → STL → Fine resolution
7. Verify di STL viewer

**Output:** M05_P10_ImportRepair.sldprt + M05_P10_Export.stl

---

## V. Analisa dan Pembahasan
1. Jelaskan keuntungan menggunakan Configurations vs membuat file terpisah
2. Kapan menggunakan Design Table vs manual Configurations?
3. Bandingkan Surface Modeling vs Solid Modeling: kelebihan/kekurangan
4. Bagaimana Weldments mempercepat desain struktur frame?
5. Analisis manfaat Library Features untuk produktivitas
6. Jelaskan risiko External References dalam In-Context Design
7. Format file apa yang paling cocok untuk berbagi dengan vendor berbeda CAD?

---

## VI. Kesimpulan
Rangkum semua teknik lanjutan dan kapan menggunakan masing-masing dalam workflow desain profesional.

---

## VII. Tugas

### Video (12-15 menit):
- Penjelasan materi Design Table, Configurations, dan Weldments
- Demo lengkap Percobaan 2 (Profil Aluminium Design Table) dan Percobaan 6 (Aluminium Frame)
- Analisa perbandingan metode

### Pengumpulan:
Total deliverables: 12 file + 1 Excel + Project
- M05_P01_BoltMultiSize.sldprt
- M05_P02_ProfilAluminium_Series.sldprt
- M05_P03_ParametricEnclosure.sldprt
- M05_P04_MouseHousing.sldprt
- M05_P05_MoldDesign.sldprt
- M05_P06_AluminiumFrame.sldprt
- TSlot_6mm.sldlfp
- M05_P07_TestLibFeature.sldprt
- M05_P08_ExcelBracket.sldprt
- Bracket_Params.xlsx
- M05_P09_InContextBracket.sldprt (+ assembly jika diperlukan)
- M05_P10_ImportRepair.sldprt
- M05_P10_Export.stl
- Project files (lihat Project.md)

→ Kompres semua: `NIM_Nama_Modul05.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 5*
