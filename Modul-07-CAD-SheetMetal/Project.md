# PROJECT MODUL 7: SHEET METAL ENCLOSURE + AKSESORIS ALUMINIUM

## Praktikum CAD/CAM — Pertemuan 7

---

## Project A: Enclosure Elektronik Sheet Metal

### Deskripsi
Desain **Enclosure/Casing elektronik** lengkap dari sheet metal yang siap diproduksi.

### Komponen:
1. **Main Body** — Box utama dengan ventilasi dan cable entry
2. **Cover/Lid** — Penutup atas dengan snap-fit tabs
3. **Front Panel** — Panel depan dengan cutout display, tombol, dan LED
4. **Mounting Bracket** — Bracket untuk mounting ke dinding/rak
5. **Internal Bracket** — Bracket PCB holder di dalam

### Spesifikasi Keseluruhan:
- Material: Aluminum 1.5mm
- Ukuran: 150 x 100 x 50mm
- K-Factor: 0.33
- Bend Radius: 1.5mm
- Semua komponen harus bisa di-Flatten
- Export semua Flat Pattern ke DXF

### Deliverables Project A:
1. 5 file .sldprt (sheet metal)
2. 5 file .dxf (flat pattern)
3. 1 file .sldasm (assembly)
4. Exploded View
5. Drawing dengan Flat Pattern view

---

## Project B: Aksesoris Aluminium Sheet Metal

### Deskripsi
Desain **aksesoris sheet metal** untuk sistem profil aluminium yang siap diproduksi dengan laser cutting atau CNC bending.

### Komponen Sheet Metal untuk Profil Aluminium:

#### 1. Mounting Plate untuk Profil 4040
```
Spesifikasi:
- Material: Aluminum 3mm
- Ukuran: 80 x 80mm
- 4x slot untuk T-nut (8mm width x 12mm length)
- 1x center hole Ø8mm untuk cable routing
- K-Factor: 0.40
- Bend: 2x lip 10mm 90° untuk rigidity

Feature:
- Base Flange 80x80mm
- Edge Flange 10mm pada 2 sisi
- Cut-Extrude untuk slots
- Flat Pattern untuk laser cutting
```

#### 2. L-Bracket Sheet Metal untuk Profil 3030
```
Spesifikasi:
- Material: Aluminum 2mm
- Dimensi: 60 x 60mm x 30mm (L-shape)
- 2x slot pada masing-masing sisi (6mm width untuk slot 8)
- Bend Radius: 2mm
- K-Factor: 0.35

Feature:
- Base Flange 60x30mm
- Edge Flange 60mm pada satu sisi (90°)
- Cut-Extrude untuk T-slot holes
- Relief otomatis di corner
```

#### 3. Gusset Plate Triangular
```
Spesifikasi:
- Material: Aluminum 4mm (flat, no bends)
- Shape: Right triangle 50x50mm
- 2x slot per sisi (8mm width)
- Fillet R8 pada corner hypotenuse

Feature:
- Base Flange (flat plate mode)
- Cut-Extrude untuk slots
- DXF export untuk laser cutting
```

#### 4. Cable Tray Bracket
```
Spesifikasi:
- Material: Aluminum 1.5mm
- Ukuran: 100mm panjang, 40mm lebar tray
- Bentuk: U-channel dengan mounting tabs
- 2x slot mounting ke profil 4040

Feature:
- Base Flange 100x40mm
- Edge Flange 15mm pada kedua sisi panjang (90°)
- Tab dan slot untuk interlocking
- Flat Pattern siap laser cutting
```

#### 5. End Cap Metal dengan Ventilasi
```
Spesifikasi:
- Material: Aluminum 1.5mm
- Ukuran: 40x40mm (untuk profil 4040)
- Cutout ventilasi pattern (perforated)
- Lip untuk snap-fit ke profil

Feature:
- Base Flange 40x40mm
- Hem pada 4 sisi (3mm lip for snap)
- Perforated pattern untuk ventilasi
- Flat Pattern
```

---

## Kriteria Penilaian

| Kriteria | Bobot |
|----------|-------|
| Project A: Kelengkapan 5 komponen enclosure | 20% |
| Project A: Kebenaran sheet metal features | 15% |
| Project A: Flat Pattern benar (no overlaps) | 10% |
| Project B: 5 komponen aksesoris aluminium | 20% |
| Project B: Dimensi sesuai profil standar | 10% |
| Project B: DXF export siap manufaktur | 10% |
| Assembly kedua project dengan mate benar | 10% |
| Drawing dengan Flat Pattern view | 5% |

---

## Total Deliverables

**Project A (Enclosure):**
1. M07_A1_MainBody.sldprt + .dxf
2. M07_A2_Cover.sldprt + .dxf
3. M07_A3_FrontPanel.sldprt + .dxf
4. M07_A4_MountingBracket.sldprt + .dxf
5. M07_A5_InternalBracket.sldprt + .dxf
6. M07_A_Enclosure.sldasm

**Project B (Aksesoris Aluminium):**
7. M07_B1_MountingPlate4040.sldprt + .dxf
8. M07_B2_LBracket3030.sldprt + .dxf
9. M07_B3_GussetPlate.sldprt + .dxf
10. M07_B4_CableTrayBracket.sldprt + .dxf
11. M07_B5_EndCapVentilasi.sldprt + .dxf

**Drawing:**
12. M07_Drawing_FlatPatterns.slddrw (semua flat pattern dalam 1 drawing)

---

## Tips Sheet Metal untuk Aksesoris Aluminium

1. **T-Slot Compatibility**: Slot width harus 8mm untuk profil 30/40/45/50 series, 6mm untuk 20 series
2. **Material Thickness**: Jangan terlalu tebal (max 4mm) agar bisa di-bend
3. **K-Factor**: Gunakan 0.33-0.40 untuk aluminum
4. **Relief**: Auto Relief untuk corner bends
5. **DXF Export**: Pastikan export flat pattern, bukan folded
6. **Bend Sequence**: Pertimbangkan urutan bending saat desain

---

## Referensi
- Aluminium Catalog 2020.pdf (folder Referensi)
- Halaman profil: 6-17 (untuk dimensi T-slot)
- Halaman accessories: 55-96

---

*Project Praktikum CAD/CAM — Modul 7*
