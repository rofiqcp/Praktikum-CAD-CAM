# PROJECT MODUL 2: GAMBAR TEKNIK 2D — DESAIN PANEL KONTROL

## Praktikum CAD/CAM — Pertemuan 2

---

## Deskripsi Project

Buat **gambar teknik 2D lengkap panel kontrol mesin** yang merangkum semua teknik dari Percobaan 1-10. Panel kontrol ini menggabungkan: rectangle, circle, arc, polygon, slot, spline, mirror, pattern, trim, offset, fillet, chamfer, dan semua jenis constraint.

---

## Spesifikasi Panel Kontrol

### Dimensi Utama:
- Ukuran panel: **200 x 150 mm**
- Fillet sudut panel: **R10**
- 4 lubang mounting di sudut: **Ø6mm**, jarak **10mm** dari tepi

### Komponen Panel:
1. **Display Cutout** (kanan atas):
   - Rectangle dengan sudut radius: 60 x 30 mm, R3
   - Posisi: 20mm dari tepi kanan, 15mm dari tepi atas

2. **Lubang Tombol** (3 buah, tengah bawah):
   - Ø22mm (standar push button)
   - Jarak antar center: 35mm
   - Jarak dari tepi bawah: 30mm
   - Label slot di bawah tiap tombol: 15 x 3mm

3. **Lubang Selector Switch** (kiri atas):
   - Ø22mm dengan flat (D-cut) 19mm
   - Posisi: 30mm dari tepi kiri, 30mm dari tepi atas

4. **Lubang Emergency Stop** (kanan bawah):
   - Ø40mm (mushroom button)
   - Posisi: 35mm dari tepi kanan, 35mm dari tepi bawah
   - Marking zone: lingkaran Ø55mm (construction line)

5. **Ventilasi Slots** (kiri bawah):
   - 5 slot paralel: 25 x 3mm
   - Jarak antar slot: 6mm
   - Fillet ujung slot: R1.5

6. **Label Engraving Area** (tengah atas):
   - Rectangle: 50 x 8mm
   - Teks area (ditandai dengan centerline)

### Constraints yang WAJIB digunakan:
- Symmetric (panel simetris pada sumbu vertikal untuk mounting holes)
- Equal (slot ventilasi sama panjang)
- Concentric (lingkaran marking dengan emergency stop)
- Perpendicular, Horizontal, Vertical
- Pattern (slot ventilasi)
- Mirror (mounting holes)

### Deliverables:
1. File .sldprt (sketch Fully Defined)
2. Screenshot sketch dengan dimensi terlihat
3. Screenshot constraints yang digunakan (Display/Delete Relations)

---

## Kriteria Penilaian

| No | Kriteria | Bobot |
|----|----------|-------|
| 1 | Semua komponen panel tergambar | 25% |
| 2 | Dimensi akurat sesuai spesifikasi | 20% |
| 3 | Sketch Fully Defined | 20% |
| 4 | Penggunaan constraints beragam & benar | 20% |
| 5 | Penggunaan Mirror/Pattern/Offset | 15% |

---

*Project Praktikum CAD/CAM — Modul 2*
