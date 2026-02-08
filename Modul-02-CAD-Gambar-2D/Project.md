# PROJECT MODUL 2: GAMBAR TEKNIK 2D — DESAIN PANEL KONTROL + PROFIL ALUMINIUM

## Praktikum CAD/CAM — Pertemuan 2

---

## Project A: Panel Kontrol

### Deskripsi Project

Buat **gambar teknik 2D lengkap panel kontrol mesin** yang merangkum semua teknik dari Percobaan 1-10. Panel kontrol ini menggabungkan: rectangle, circle, arc, polygon, slot, spline, mirror, pattern, trim, offset, fillet, chamfer, dan semua jenis constraint.

---

### Spesifikasi Panel Kontrol

#### Dimensi Utama:

- Ukuran panel: **200 x 150 mm**
- Fillet sudut panel: **R10**
- 4 lubang mounting di sudut: **Ø6mm**, jarak **10mm** dari tepi

#### Komponen Panel:

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

#### Constraints yang WAJIB digunakan:

- Symmetric (panel simetris pada sumbu vertikal untuk mounting holes)
- Equal (slot ventilasi sama panjang)
- Concentric (lingkaran marking dengan emergency stop)
- Perpendicular, Horizontal, Vertical
- Pattern (slot ventilasi)
- Mirror (mounting holes)

---

## Project B: Sketch Profil Aluminium

### Deskripsi

Buat **sketch 2D penampang profil aluminium** dari katalog Connect Automation. Ini adalah latihan presisi sketching untuk profil industri yang akan digunakan di modul-modul selanjutnya.

### Profil yang Harus Digambar:

#### 1. Profil 2020 (20x20mm, 4 Slot)

```
Referensi: Aluminium Catalog halaman 5
- Penampang: 20 x 20 mm
- T-slot: 6mm width setiap sisi
- Center bore: Ø5mm
- Ix = Iy = 7023.91 mm⁴
- TIPS: Gambar 1/4 profil → Mirror 2x (manfaatkan simetri 4 arah)
```

#### 2. Profil 2040 (20x40mm, 6 Slot)

```
Referensi: Aluminium Catalog halaman 5
- Penampang: 20 x 40 mm
- T-slot: 6mm pada sisi pendek (2 slot), 6mm pada sisi panjang (2x2 slot)
- Center bore: 2x Ø5mm
- Sketch harus Fully Defined
```

#### 3. Profil 3030 (30x30mm, 4 Slot)

```
Referensi: Aluminium Catalog halaman 14
- Penampang: 30 x 30 mm
- T-slot: 8mm width setiap sisi
- Center bore: Ø12mm
- Ketebalan dinding: ~2mm
```

#### 4. Profil 4040 Standard (40x40mm, 4 Slot)

```
Referensi: Aluminium Catalog halaman 38
- Penampang: 40 x 40 mm
- T-slot: 8mm width, ~10mm depth
- Center bore: Ø12mm
- Internal cross ribs 4 arah
- Ix = Iy = 95526.88 mm⁴
```

### Teknik Sketching Profil:

1. **Gambar 1/4 profil** dari Origin (manfaatkan simetri)
2. **Gunakan Centerline** sebagai sumbu simetri
3. **Gambar T-Slot detail**: perhatikan undercut dan dimensi kritis
4. **Mirror horizontal** → Mirror vertikal → profil lengkap
5. **Tambahkan center bore** di Origin
6. **Pastikan Fully Defined**

### Constraints Wajib:

- **Symmetric** (profil simetris terhadap kedua sumbu)
- **Equal** (semua T-slot identik)
- **Perpendicular** (sudut-sudut 90°)
- **Concentric** (center bore di origin)

---

## Kriteria Penilaian

| No | Kriteria                                         | Bobot |
| -- | ------------------------------------------------ | ----- |
| 1  | Panel Kontrol: Semua komponen tergambar          | 20%   |
| 2  | Panel Kontrol: Dimensi akurat                    | 15%   |
| 3  | Panel Kontrol: Fully Defined + constraints benar | 15%   |
| 4  | Profil Aluminium: 4 profil tergambar akurat      | 25%   |
| 5  | Profil Aluminium: Detail T-slot presisi          | 15%   |
| 6  | Teknik efisien (Mirror/Pattern)                  | 10%   |

---

### Deliverables:

1. `M02_ProjectA_PanelKontrol.sldprt` — Panel kontrol Fully Defined
2. `M02_ProjectB_Profil2020.sldprt` — Sketch profil 2020
3. `M02_ProjectB_Profil2040.sldprt` — Sketch profil 2040
4. `M02_ProjectB_Profil3030.sldprt` — Sketch profil 3030
5. `M02_ProjectB_Profil4040.sldprt` — Sketch profil 4040
6. Screenshot constraints yang digunakan

---

*Project Praktikum CAD/CAM — Modul 2*
