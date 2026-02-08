# MODUL 4: CAD GAMBAR 3D — PART 2 (FEATURE LANJUTAN)

## Praktikum CAD/CAM — Pertemuan 4

---

## 4.1 Pendahuluan
Modul ini membahas feature 3D lanjutan yang memungkinkan pembuatan bentuk-bentuk kompleks yang tidak bisa dicapai dengan feature dasar saja.

---

## 4.2 Feature Lanjutan

### 5.2.1 Loft
Membuat bentuk 3D dari beberapa profil sketch pada plane berbeda.
- **Minimum 2 profil** pada plane yang berbeda
- Bisa menggunakan **Guide Curves** untuk mengontrol bentuk transisi
- Opsi: Start/End constraints, Tangency

### 5.2.2 Sweep
Menarik profil sketch sepanjang jalur (path).
- **Profile**: Sketch profil penampang
- **Path**: Sketch jalur yang diikuti
- Opsi: Follow Path, Keep Normal Constant, Twist Along Path

### 5.2.3 Boundary Boss/Base
Mirip Loft tetapi menggunakan 2 arah (Direction 1 dan Direction 2).
- Lebih presisi dari Loft untuk permukaan kompleks
- Menggunakan kurva batas di 2 arah

### 5.2.4 Wrap
Membungkus sketch 2D pada permukaan silindris atau kerucut.
- **Emboss**: Menambah material
- **Deboss**: Mengurangi material
- **Scribe**: Garis pada permukaan

### 5.2.5 Flex
Melenturkan/menekuk solid body.
- Tipe: Bending, Twisting, Tapering, Stretching

### 5.2.6 Dome
Membuat permukaan cembung/cekung pada face datar.

### 5.2.7 Indent
Membuat cekungan pada satu body berdasarkan bentuk body lain.

### 5.2.8 Deform
Mendeformasi solid body dengan point, curve, atau surface.

### 5.2.9 Split / Split Line
- **Split Line**: Membagi face menjadi beberapa region
- **Split**: Memotong body menjadi beberapa body terpisah

### 5.2.10 Combine (Multibody)
Menggabungkan beberapa solid body dalam satu part file.
- **Add**: Menggabungkan
- **Subtract**: Mengurangi
- **Common**: Irisan (intersection)

---

## 5.3 Reference Geometry

### Plane (Bidang Referensi Tambahan)
- **Offset from Plane**: Plane paralel dengan jarak tertentu
- **Through Line/Point**: Plane melalui garis/titik
- **Parallel to Plane through Point**: Plane paralel melalui titik
- **Angle to Plane**: Plane dengan sudut tertentu
- **Normal to Curve**: Plane tegak lurus terhadap kurva

### Axis (Sumbu Referensi)
- Dari 2 plane, cylindrical face, atau 2 point

### Coordinate System
- Sistem koordinat kustom untuk analisis dan export

---

## 5.4 Percobaan 1-10

### Percobaan 1: Vase (Loft)
```
Spesifikasi:
- 4 profil pada plane berbeda:
  - Base: Circle Ø60mm (z=0)
  - Mid-low: Circle Ø40mm (z=30)
  - Mid-high: Circle Ø50mm (z=60)
  - Top: Circle Ø70mm (z=90)
- Loft melalui 4 profil
- Shell: 2mm (remove face atas)
- Fillet R2 pada edge bawah
```

### Percobaan 2: Pipe Bend (Sweep)
```
Spesifikasi:
- Profile: Circle Ø20mm (OD), Ø16mm (ID) → Thin feature
- Path: L-shape dengan fillet R40 (sweep path)
- Total length: 150mm horizontal + 100mm vertikal
- Ketebalan pipa: 2mm
```

### Percobaan 3: Spring (Sweep Helix)
```
Spesifikasi:
- Profile: Circle Ø3mm (wire diameter)
- Path: Helix → Pitch 10mm, Diameter Ø25mm, 8 turns
- Flat pada kedua ujung (ground ends)
```

### Percobaan 4: Bottle (Loft + Revolve)
```
Spesifikasi:
- Body botol: Revolve Ø60mm → neck Ø25mm
- Thread pada neck: Sweep helix
- Loft transisi body → neck
- Shell 1.5mm
- Total tinggi: 150mm
```

### Percobaan 5: Propeller (Loft + Pattern)
```
Spesifikasi:
- Hub: Ø20mm, panjang 15mm
- Blade: Loft dari 3 profil (airfoil) pada plane angled
- 3 blades → Circular Pattern 120°
- Lubang poros: Ø6mm
```

### Percobaan 6: Handle/Grip (Sweep + Loft)
```
Spesifikasi:
- Handle berbentuk D-shape
- Profil: Oval 30x20mm → transisi ke Circle Ø20mm
- Path: Curved path mengikuti kontur tangan
- Texture grooves: Wrap deboss pada permukaan
```

### Percobaan 7: Cam 3D (Loft + Sweep)
```
Spesifikasi:
- Base: Circle Ø40mm
- Cam profile dari Modul 2 (Percobaan 6) sebagai profil atas
- Loft antara base circle dan cam profile
- Lubang shaft: Ø12mm + keyway
- Ketebalan: 15mm
```

### Percobaan 8: Enclosure Ergonomis (Loft + Shell + Dome)
```
Spesifikasi:
- Bottom: Rectangle 80x50mm, fillet R10
- Middle: Rectangle 85x55mm, fillet R15 (z=20mm)
- Top: Rectangle 75x45mm, fillet R10 (z=35mm)
- Loft ketiga profil
- Shell: 2mm, remove bottom
- Dome pada face atas: height 3mm
- Cutout untuk USB port: 12x5mm pada sisi
```

### Percobaan 9: Text Emboss pada Silinder (Wrap)
```
Spesifikasi:
- Silinder: Ø40mm, panjang 100mm
- Text "CADCAM LAB" di-wrap pada permukaan silinder
- Emboss depth: 1mm
- Font: Arial Bold, height 8mm
- Posisi: di tengah silinder
```

### Percobaan 10: Multi-Body Part (Combine)
```
Spesifikasi:
- Body 1: Balok 60x60x40mm
- Body 2: Silinder Ø40mm tinggi 60mm, posisi offset
- Combine Subtract: Balok dikurangi silinder
- Tambahkan pattern lubang pada hasil
- Fillet pada semua edge tajam
```

---

*Modul Praktikum CAD/CAM — Modul 5: CAD Gambar 3D Part 2*
*Disusun untuk keperluan pendidikan*
