# PROJECT MODUL 3: DESAIN CLAMP ASSEMBLY PART + PROFIL ALUMINIUM 3D

## Praktikum CAD/CAM — Pertemuan 3

---

## Project A: Clamp Assembly Parts

### Deskripsi Project
Desain **Clamp (penjepit) mekanik** yang terdiri dari beberapa part menggunakan semua feature dari Percobaan 1-10. Setiap part mendemonstrasikan penguasaan feature berbeda.

---

### Part yang Harus Dibuat:

#### 1. Base Clamp (Extrude + Shell + Pattern)
- Base plate 100x60x10mm dengan 4 lubang mounting Ø8mm
- Raised boss Ø30mm tinggi 5mm untuk pivot

#### 2. Clamp Arm (Extrude + Fillet + Chamfer)
- Lengan penjepit 120x20x10mm
- Lubang pivot Ø12mm di satu ujung
- Slot adjustment 30x8mm di ujung lain
- Fillet R5 pada semua edge

#### 3. Pressure Pad (Revolve)
- Pad penjepit silindris Ø20mm tinggi 10mm
- Fillet R3 pada tepi bawah (kontak permukaan)
- Lubang berulir M6 di atas

#### 4. Pivot Pin (Revolve + Chamfer)
- Pin Ø12mm x 25mm
- Chamfer 1x45° pada kedua ujung
- Groove untuk circlip: lebar 1.5mm, kedalaman 0.5mm

#### 5. Knob (Revolve + Knurling Pattern)
- Knob putar Ø25mm untuk mengencangkan
- Knurling pattern pada sisi luar

---

## Project B: Profil Aluminium 3D (EXTRUDE dari Modul 2)

### Deskripsi
Ubah sketch profil aluminium dari Modul 2 menjadi **model 3D** menggunakan Extrude. Ini adalah komponen struktural yang akan digunakan di Project Konveyor, Robot, dan proyek lainnya.

### Profil yang Harus Di-Extrude:

#### 1. Profil 2020 — Panjang 200mm
```
Referensi: Aluminium Catalog halaman 5
- Gunakan sketch dari Modul 2 Project B
- Extrude: Blind, 200mm
- Chamfer ujung: 0.5x45° pada semua edge luar
- Material: Aluminum 6063-T5
- Simpan: M03_Profil2020_200mm.sldprt
```

#### 2. Profil 3030 — Panjang 300mm
```
Referensi: Aluminium Catalog halaman 14
- Extrude: 300mm
- Chamfer ujung: 0.5x45°
- Center bore: Through All
- Material: Aluminum 6063-T5
- Simpan: M03_Profil3030_300mm.sldprt
```

#### 3. Profil 4040 Standard — Panjang 400mm
```
Referensi: Aluminium Catalog halaman 38
- Extrude: 400mm
- Chamfer ujung: 1x45°
- Center bore: Through All
- Material: Aluminum 6063-T5
- Simpan: M03_Profil4040_400mm.sldprt
```

#### 4. Profil 4080 — Panjang 500mm
```
Referensi: Aluminium Catalog halaman 39
- Penampang: 40 x 80 mm
- 6 slot total (2 sisi pendek, 4 sisi panjang)
- 2 center bore
- Extrude: 500mm
- Material: Aluminum 6063-T5
- Simpan: M03_Profil4080_500mm.sldprt
```

### Teknik Membuat Profil 3D:
1. **Import/Copy sketch** dari Modul 2 atau gambar ulang
2. **Extrude Boss/Base** dengan panjang sesuai spesifikasi
3. **Tambahkan Chamfer** pada edge ujung
4. **Cut Extrude Through All** untuk center bore (jika belum)
5. **Assign Material**: Edit Material → Aluminum Alloys → 6063-T5
6. **Cek Mass Properties**: `Evaluate → Mass Properties`

---

## Kriteria Penilaian

| Kriteria | Bobot |
|----------|-------|
| Clamp: Kelengkapan 5 part | 20% |
| Clamp: Ketepatan dimensi | 15% |
| Clamp: Variasi feature yang digunakan | 15% |
| Profil Aluminium: 4 profil 3D sesuai katalog | 25% |
| Profil Aluminium: Dimensi presisi | 15% |
| Material assignment benar | 10% |

---

### Deliverables:
**Project A (Clamp):**
1. M03_A1_BaseClamp.sldprt
2. M03_A2_ClampArm.sldprt
3. M03_A3_PressurePad.sldprt
4. M03_A4_PivotPin.sldprt
5. M03_A5_Knob.sldprt

**Project B (Profil Aluminium):**
6. M03_B1_Profil2020_200mm.sldprt
7. M03_B2_Profil3030_300mm.sldprt
8. M03_B3_Profil4040_400mm.sldprt
9. M03_B4_Profil4080_500mm.sldprt

---

*Project Praktikum CAD/CAM — Modul 3*
