# PROJECT MODUL 5: SISTEM PROFIL ALUMINIUM MODULAR

## Praktikum CAD/CAM — Pertemuan 5

---

## Project A: Library Profil Aluminium Lengkap

### Deskripsi
Buat **library profil aluminium lengkap** menggunakan Design Table dan Configurations untuk seluruh seri profil yang umum digunakan di industri.

### Deliverables:

#### 1. Master Profile dengan Design Table
```
File: M05_A1_ProfilAluminium_Master.sldprt

Configurations (minimal 8):
- 2020 (20x20mm, T-slot 6mm)
- 2040 (20x40mm, T-slot 6mm)
- 3030 (30x30mm, T-slot 8mm)
- 3060 (30x60mm, T-slot 8mm)
- 4040 (40x40mm, T-slot 8mm)
- 4080 (40x80mm, T-slot 8mm)
- 4545 (45x45mm, T-slot 8mm)
- 5050 (50x50mm, T-slot 8mm)

Design Table harus include:
- Profile Width
- Profile Height
- T-Slot Width
- T-Slot Depth
- Center Hole Diameter
- Corner Radius
- Default Length (100mm)
```

#### 2. Connector Series dengan Design Table
```
File: M05_A2_ConnectorSeries.sldprt

Configurations:
- Corner Bracket 2020
- Corner Bracket 3030
- Corner Bracket 4040
- Corner Bracket 4545
- Gusset Plate 20
- Gusset Plate 30
- Gusset Plate 40

Design Table harus include:
- Bracket Size
- Hole Size
- Hole Spacing
- Thickness
```

---

## Project B: Aluminium Frame Workstation dengan Weldments

### Deskripsi
Desain **meja kerja modular** menggunakan profil aluminium 4040 dengan Weldments feature.

### Spesifikasi:
```
Dimensi Overall:
- Panjang: 1200mm
- Lebar: 800mm
- Tinggi: 750mm

Profil:
- Frame utama: 4040 (40x40mm)
- Cross support: 3030 (30x30mm)
- Tinggi adjustable foot: 20mm range

Fitur tambahan:
- 4 adjustable feet (M10)
- Cross brace diagonal pada sisi belakang
- Mount points untuk PC holder (optional)
```

### Deliverables:
```
M05_B1_WorkstationFrame.sldprt (Weldments part)
M05_B2_WorkstationFrame_CutList.xlsx (exported Cut List)
```

### Cut List harus berisi:
| Item | Description | Qty | Length |
|------|-------------|-----|--------|
| 1 | 4040 Horizontal Long | 4 | 1200mm |
| 2 | 4040 Horizontal Short | 4 | 800mm |
| 3 | 4040 Vertical | 4 | 710mm |
| 4 | 3030 Cross Support | 2 | 760mm |
| 5 | 3030 Diagonal Brace | 2 | ~850mm |

---

## Project C: Parametric Mounting Bracket

### Deskripsi
Desain **mounting bracket parametrik** yang bisa menyesuaikan berbagai ukuran profil aluminium menggunakan Excel-linked equations.

### Spesifikasi:
```
File Excel "BracketParameters.xlsx":
| Parameter       | Value_20 | Value_30 | Value_40 |
|-----------------|----------|----------|----------|
| Profile_Width   | 20       | 30       | 40       |
| Slot_Width      | 6        | 8        | 8        |
| Bracket_Length  | 60       | 90       | 120      |
| Bracket_Width   | 30       | 45       | 60       |
| Hole_Diameter   | 5.5      | 6.8      | 9        |
| Thickness       | 3        | 4        | 5        |
| Fillet_Radius   | 2        | 3        | 4        |

SolidWorks akan membaca parameter dari Excel
dan auto-update bracket sesuai profil yang dipilih.
```

### Deliverables:
```
M05_C1_ParametricBracket.sldprt
BracketParameters.xlsx
```

---

## Kriteria Penilaian

| Kriteria | Bobot |
|----------|-------|
| Project A: Design Table dengan 8+ configurations | 25% |
| Project A: Dimensi akurat sesuai katalog | 10% |
| Project B: Weldments frame lengkap | 20% |
| Project B: Cut List tereksport dengan benar | 10% |
| Project C: Excel-linked parametric bracket | 20% |
| Project C: Parameter update otomatis | 10% |
| Dokumentasi dan kerapihan model | 5% |

---

## Deliverables Summary

**Project A:**
1. M05_A1_ProfilAluminium_Master.sldprt
2. M05_A2_ConnectorSeries.sldprt

**Project B:**
3. M05_B1_WorkstationFrame.sldprt
4. M05_B2_WorkstationFrame_CutList.xlsx

**Project C:**
5. M05_C1_ParametricBracket.sldprt
6. BracketParameters.xlsx

---

## Referensi
- Aluminium Catalog 2020.pdf (folder Referensi)
- Halaman profil: 6-17
- Halaman connector: 18-26
- Halaman fastener: 23-25

---

*Project Praktikum CAD/CAM — Modul 5*
