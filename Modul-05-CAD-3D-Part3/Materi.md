# MODUL 5: CAD GAMBAR 3D — PART 3 (TEKNIK LANJUTAN)

## Praktikum CAD/CAM — Pertemuan 5

---

## 5.1 Pendahuluan
Modul ini membahas teknik-teknik lanjutan dalam pemodelan 3D SolidWorks, termasuk Design Table, Configurations, Surfaces, dan fitur produktivitas tinggi lainnya yang digunakan dalam industri.

---

## 5.2 Design Table dan Configurations

### 5.2.1 Configurations
**Configurations** memungkinkan pembuatan variasi model dengan dimensi atau feature berbeda dalam satu file.

**Cara Membuat Configuration:**
1. Klik kanan pada part name → `Add Configuration`
2. Beri nama configuration (misal: "Small", "Medium", "Large")
3. Ubah dimensi atau feature sesuai kebutuhan
4. Setiap perubahan tersimpan dalam configuration aktif

**Penggunaan:**
- Variasi ukuran produk (S, M, L, XL)
- Versi komponen berbeda (with hole / without hole)
- Simplifikasi model untuk assembly besar

**Percobaan 1: Bolt Multi-Size**
```
Buat Bolt M6, M8, M10 dalam satu file
1. Part → Add Configuration → "M6"
2. Buat model bolt M6
3. Add Configuration → "M8"
4. Double-click dimensi → Link Values → ubah ke ukuran M8
5. Repeat untuk M10
```

---

### 5.2.2 Design Table
**Design Table** adalah Excel spreadsheet embedded dalam SolidWorks untuk mengontrol multiple configurations secara sistematis.

**Membuat Design Table:**
1. Insert → Tables → Design Table
2. Pilih "Auto-create" untuk otomatis menambah dimensi yang sudah ada
3. Atau "Blank" untuk membuat manual
4. Edit di Excel dalam SolidWorks

**Format Design Table:**
```
| (Header)      | Configuration1 | Configuration2 | Configuration3 |
|---------------|----------------|----------------|----------------|
| $PRP@Description | Bolt M6     | Bolt M8        | Bolt M10       |
| D1@Sketch1    | 6              | 8              | 10             |
| D2@Sketch1    | 10             | 13             | 16             |
| D1@Extrude1   | 20             | 25             | 30             |
```

**Percobaan 2: Profil Aluminium dengan Design Table**
```
Buat variasi profil aluminium 2020, 3030, 4040, 5050 dalam satu file
Design Table columns:
- Profile Width (20, 30, 40, 50)
- T-Slot Width (6, 8, 8, 8)
- Corner Radius (1.5, 2, 2.5, 3)
- Hole Diameter (4.2, 5.3, 6.8, 9)
```

---

## 5.3 Equations dan Link Values

### 5.3.1 Advanced Equations
Selain equations dasar, SolidWorks mendukung:
- **Conditional Equations**: `IF(condition, true_value, false_value)`
- **Math Functions**: `sin()`, `cos()`, `tan()`, `sqrt()`, `abs()`
- **Linked Dimensions**: Dimensi yang terikat ke dimensi lain

**Percobaan 3: Parametric Enclosure**
```
Membuat enclosure box parametrik:
"Length" = 100mm (drivung)
"Width" = "Length" * 0.6
"Height" = "Length" * 0.4
"Wall_Thickness" = IF("Length" > 150, 3, 2)
"Corner_Radius" = "Wall_Thickness" * 2
```

---

## 5.4 Surfaces (Permukaan)

### 5.4.1 Pengantar Surface Modeling
**Surface modeling** menggunakan permukaan tanpa ketebalan untuk membuat bentuk kompleks yang sulit dengan solid modeling.

**Surface Tools:**
- **Extruded Surface**: Surface dari sketch yang di-extrude
- **Revolved Surface**: Surface dari sketch yang diputar
- **Lofted Surface**: Surface dari beberapa profil
- **Swept Surface**: Surface sepanjang path
- **Boundary Surface**: Surface dengan boundary conditions
- **Planar Surface**: Surface datar untuk menutup lubang
- **Knit Surface**: Menggabungkan beberapa surface

### 5.4.2 Surface Operations
- **Trim Surface**: Memotong surface dengan surface/sketch lain
- **Untrim Surface**: Mengembalikan surface yang sudah di-trim
- **Extend Surface**: Memperpanjang edge surface
- **Offset Surface**: Membuat surface offset dari surface asli
- **Thicken**: Mengubah surface menjadi solid dengan ketebalan

**Percobaan 4: Mouse Housing dengan Surface**
```
1. Lofted Surface untuk body atas
2. Lofted Surface untuk body bawah
3. Knit Surface untuk menggabungkan
4. Thicken untuk memberikan ketebalan 2mm
5. Shell untuk membuat hollow
```

---

## 5.5 Mold Tools

### 5.5.1 Pengantar Mold Design
**Mold Tools** di SolidWorks membantu desain cetakan plastik (injection mold).

**Workflow Mold Design:**
1. **Draft Analysis**: Analisis sudut draft untuk ejection
2. **Scale**: Scaling untuk shrinkage kompensasi
3. **Parting Line**: Garis pembatas core dan cavity
4. **Shut-off Surfaces**: Permukaan penutup lubang
5. **Parting Surface**: Permukaan pemisah mold
6. **Tooling Split**: Memisahkan core dan cavity

**Percobaan 5: Simple Mold Design**
```
Membuat mold untuk tutup botol sederhana:
1. Draft Analysis → 2° minimum
2. Scale Factor: 1.006 (0.6% shrinkage untuk PP)
3. Parting Line pada perimeter
4. Parting Surface → extrude 50mm
5. Tooling Split → Core, Cavity, Parting Surface
```

---

## 5.6 Weldments

### 5.6.1 Pengantar Weldments
**Weldments** untuk mendesain struktur welded dari profil standar (frame, rak, meja).

**Structural Member:**
1. Buat 3D Sketch sebagai kerangka (framework)
2. Insert → Weldments → Structural Member
3. Pilih profil (square tube, angle, channel, pipe)
4. Select path segments

**Trim/Extend:**
- Automatic trimming pada corner
- Manual trim dengan Trim/Extend tool

**Weld Beads:**
- Fillet bead
- Groove bead

**Percobaan 6: Aluminium Frame dengan Weldments**
```
Membuat frame meja dari profil aluminium 4040:
1. 3D Sketch: Rectangle 800x500mm + 4 vertical lines 700mm
2. Structural Member: Square Tube 40x40 (atau custom 4040 profile)
3. Trim corners
4. Add End Caps
5. Cut List untuk BOM
```

---

## 5.7 Library Features dan Design Library

### 5.7.1 Design Library
**Design Library** menyimpan feature, part, dan annotation untuk reuse.

**Lokasi:** Task Pane → Design Library

**Tipe Content:**
- **Toolbox**: Standard hardware (bolt, nut, washer, bearing)
- **Custom Features**: User-created features
- **Parts**: Reusable components
- **Assemblies**: Sub-assemblies

### 5.7.2 Library Feature
**Library Feature** adalah feature yang disimpan untuk digunakan berulang kali.

**Membuat Library Feature:**
1. Buat feature (misal: pocket dengan fillet tertentu)
2. File → Save As → Pilih "Lib Feat Part (*.sldlfp)"
3. Tentukan references (face, edge) untuk positioning

**Percobaan 7: Library Feature - T-Slot**
```
Membuat T-Slot sebagai library feature:
1. Buat cut-extrude profil T-slot 6mm
2. Save As → "TSlot_6mm.sldlfp"
3. Define references: Face untuk placement
4. Gunakan di part lain dengan drag & drop
```

---

## 5.8 Equations dengan External File

### 5.8.1 Link to External File
Equations dapat di-link ke file Excel eksternal untuk parametric design yang lebih kompleks.

**Cara Link:**
1. Tools → Equations
2. Klik icon "Link to external file"
3. Browse file Excel (.xlsx)
4. Map cell Excel ke dimension SolidWorks

**Percobaan 8: Excel-Driven Part**
```
File Excel "Bracket_Params.xlsx":
| Parameter | Value |
|-----------|-------|
| Length    | 100   |
| Width     | 50    |
| Thickness | 5     |
| Holes     | 4     |

SolidWorks Equations:
"Length" = [A2] from "Bracket_Params.xlsx"
"Width" = [B2] from "Bracket_Params.xlsx"
```

---

## 5.9 In-Context Design

### 5.9.1 Top-Down Design
**In-Context Design** memungkinkan pembuatan part dalam assembly dengan referensi ke part lain.

**External References:**
- Dimensi part mereferensikan geometry dari part lain
- Ditandai dengan "->..." di Feature Tree
- Update otomatis saat part referensi berubah

**Percobaan 9: In-Context Bracket**
```
1. Buka assembly dengan profil aluminium
2. Insert → Component → New Part
3. Sketch pada face profil aluminium
4. Extrude → bracket mengikuti kontur profil
5. Part memiliki external reference ke profil
```

---

## 5.10 Import dan Export

### 5.10.1 Import File CAD Lain
SolidWorks dapat import:
- **STEP** (.stp, .step) — paling direkomendasikan
- **IGES** (.igs, .iges)
- **Parasolid** (.x_t, .x_b)
- **ACIS** (.sat)
- **STL** (.stl) — mesh, bukan solid
- **DXF/DWG** — 2D AutoCAD

**Import Diagnostics:**
Setelah import, gunakan Import Diagnostics untuk repair:
1. Knit gaps
2. Heal edges
3. Fill holes

### 5.10.2 Export Formats
- **STEP**: Universal CAD exchange
- **STL**: 3D Printing
- **DXF**: 2D CNC/Laser cutting
- **eDrawings**: Viewer untuk review

**Percobaan 10: Import dan Repair**
```
1. Import file STEP dari vendor
2. Run Import Diagnostics
3. Repair faulty faces
4. Export sebagai STL untuk 3D printing
```

---

## 5.11 Best Practices Part Modeling

### Design Intent:
1. **Sketch Fully Defined**: Semua sketch harus fully defined (hitam)
2. **Use Relations**: Horizontal, Vertical, Tangent, Concentric
3. **Avoid Over-constraining**: Jangan pakai fix kecuali perlu
4. **Name Features**: Rename feature sesuai fungsi
5. **Design for Manufacturing (DFM)**: Pertimbangkan proses manufaktur

### Performance:
1. **Simplify complex models** dengan Configurations
2. **Use Lightweight mode** untuk assembly besar
3. **Avoid circular references** dalam equations
4. **Keep Feature Tree organized**

---

## 5.12 Ringkasan Modul 5

| No | Topik | Penggunaan |
|----|-------|------------|
| 1 | Configurations | Variasi ukuran dalam 1 file |
| 2 | Design Table | Manage configurations via Excel |
| 3 | Advanced Equations | Parametric dengan kondisional |
| 4 | Surfaces | Bentuk organik kompleks |
| 5 | Mold Tools | Desain injection mold |
| 6 | Weldments | Struktur frame welded |
| 7 | Library Features | Reusable custom features |
| 8 | External Links | Parameter dari Excel |
| 9 | In-Context | Top-down assembly design |
| 10 | Import/Export | Interoperability |

---

*Materi Praktikum CAD/CAM — Modul 5*
