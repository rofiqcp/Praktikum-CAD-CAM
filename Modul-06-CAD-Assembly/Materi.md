# MODUL 6: CAD ASSEMBLY — SEMUA TEKNIK ASSEMBLY

## Praktikum CAD/CAM — Pertemuan 6

---

## 6.1 Pendahuluan

Assembly adalah proses menggabungkan beberapa part menjadi satu rakitan menggunakan **Mates** (hubungan posisional). SolidWorks Assembly environment memungkinkan simulasi gerakan, interference detection, dan pembuatan exploded view.

---

## 6.2 Konsep Dasar Assembly

### Membuat Assembly Baru:
1. `File → New → Assembly`
2. Insert komponen pertama (biasanya base/fixed part)
3. Komponen pertama otomatis **Fixed** (tidak bergerak)

### Insert Component:
- `Insert → Component → Existing Part/Assembly`
- Drag dari File Explorer / Task Pane

### Assembly Approach:
1. **Bottom-Up**: Buat semua part dulu → rakit di assembly
2. **Top-Down**: Buat part di dalam assembly (in-context design)
3. **Hybrid**: Kombinasi keduanya

---

## 6.3 Standard Mates

| No | Mate | Deskripsi | Degrees of Freedom Removed |
|----|------|-----------|----------------------------|
| 1 | **Coincident** | 2 face/plane/point bertemu | Menghilangkan 1 translasi |
| 2 | **Parallel** | 2 face/plane sejajar | Menghilangkan 2 rotasi |
| 3 | **Perpendicular** | 2 face/plane tegak lurus | Menghilangkan 1 rotasi |
| 4 | **Tangent** | 2 surface bersinggungan | Menghilangkan 1 translasi |
| 5 | **Concentric** | 2 cylindrical face sesumbu | Menghilangkan 2 translasi |
| 6 | **Distance** | Jarak tertentu antar face | Menghilangkan 1 translasi |
| 7 | **Angle** | Sudut tertentu antar face | Menghilangkan 1 rotasi |
| 8 | **Lock** | Mengunci posisi relatif | Menghilangkan semua DOF |

### Mate Alignment:
- **Aligned**: Face menghadap arah sama
- **Anti-Aligned**: Face menghadap berlawanan

---

## 6.4 Advanced Mates

| No | Mate | Deskripsi |
|----|------|-----------|
| 1 | **Width** | Menempatkan komponen di tengah slot/channel |
| 2 | **Path Mate** | Komponen mengikuti path |
| 3 | **Linear/Linear Coupler** | Menghubungkan gerakan linear 2 komponen |
| 4 | **Symmetric** | Komponen simetris terhadap plane |
| 5 | **Profile Center** | Menengahkan profil non-silindris |

---

## 6.5 Mechanical Mates

| No | Mate | Deskripsi |
|----|------|-----------|
| 1 | **Gear** | Simulasi pasangan gear (rasio putar) |
| 2 | **Rack and Pinion** | Konversi rotasi ke translasi |
| 3 | **Cam** | Follower mengikuti profil cam |
| 4 | **Hinge** | Engsel (rotasi pada sumbu) |
| 5 | **Screw** | Hubungan ulir (rotasi → translasi) |
| 6 | **Universal Joint** | Sambungan universal |
| 7 | **Slot** | Komponen bergerak dalam slot |

---

## 6.6 Fitur Assembly Lainnya

### Exploded View:
- Menampilkan assembly dengan komponen terpisah
- `Insert → Exploded View`
- Drag komponen untuk mengatur posisi exploded

### Section View:
- Memotong assembly untuk melihat bagian dalam
- `View → Section View`

### Interference Detection:
- Mendeteksi tabrakan antar komponen
- `Evaluate → Interference Detection`

### Mass Properties:
- Menghitung massa, volume, center of mass assembly
- `Evaluate → Mass Properties`

### Bill of Materials (BOM):
- Daftar komponen dalam assembly
- Dibuat di Drawing environment

### Component Pattern:
- Linear/Circular pattern komponen dalam assembly

---

## 6.7 Percobaan 1-10

### Percobaan 1: Assembly Bolt-Nut-Washer (Coincident + Concentric)
```
Part yang dibuat/digunakan:
- Plat dengan lubang Ø10mm (dari Toolbox atau buat sendiri)
- Bolt M10x30 (dari Toolbox)
- Nut M10 (dari Toolbox)
- Washer M10 (dari Toolbox)

Mates:
- Concentric: Bolt shaft ↔ Plat hole
- Coincident: Bolt head bottom face ↔ Plat top face
- Concentric: Nut ↔ Bolt shaft
- Coincident: Washer ↔ Plat bottom face
- Coincident: Nut ↔ Washer
```

### Percobaan 2: Engsel / Hinge (Hinge Mate)
```
Part yang dibuat:
- Hinge Plate A: plat dengan 3 knuckle
- Hinge Plate B: plat dengan 2 knuckle (interleave)
- Pin: silinder Ø5 x 50mm

Mates:
- Concentric: Pin ↔ Knuckle holes
- Hinge Mate: Plate A ↔ Plate B (axis = pin)
- Angle limit: 0° - 180°
```

### Percobaan 3: Slider-Crank Mechanism (Distance + Concentric)
```
Part yang dibuat:
- Crank: lengan pendek 30mm dengan lubang di kedua ujung
- Connecting Rod: lengan panjang 80mm dengan lubang di kedua ujung
- Slider Block: balok 30x20x15mm dengan lubang
- Base Frame: plat dengan slider slot

Mates:
- Concentric: Crank pin ↔ Frame pivot
- Concentric: Crank end ↔ ConRod end
- Concentric: ConRod end ↔ Slider pin
- Slot mate: Slider ↔ Frame slot
- Simulasikan gerakan dengan drag
```

### Percobaan 4: Gear Pair (Gear Mate)
```
Part yang dibuat:
- Gear 1: Z=20, Module 2 (dari Modul 3 Percobaan 7)
- Gear 2: Z=30, Module 2 (buat baru)
- 2 Shaft: Ø10mm
- Frame/Housing

Mates:
- Concentric: Gear ↔ Shaft
- Gear Mate: Gear 1 ↔ Gear 2 (ratio 20:30)
- Distance: Center distance = (20+30)/2 × 2 = 50mm
```

### Percobaan 5: Pulley-Belt System (Path Mate)
```
Part:
- Pulley 1: Ø80mm (dari Modul 3)
- Pulley 2: Ø40mm
- Belt (profil persegi panjang, swept along path)
- Frame

Mates:
- Concentric: Pulley ↔ Shaft
- Distance: Center distance
- Belt: Tangent constraints
```

### Percobaan 6: Clamp Assembly (dari Project Modul 3)
```
Rakit semua part dari Project Modul 3:
- Base Clamp
- Clamp Arm
- Pressure Pad
- Pivot Pin
- Knob

Mates: Coincident, Concentric, Tangent, Angle
Buat Exploded View
```

### Percobaan 7: Motor + Gear Reducer Assembly
```
Part:
- Motor body (silinder Ø40 x 60mm)
- Motor shaft (Ø5mm)
- Gear 1 (pinion Z=12)
- Gear 2 (Z=36)
- Output shaft
- Housing box

Mates: Standard + Gear Mate
Gear ratio: 1:3
```

### Percobaan 8: Linear Guide Assembly (Width Mate)
```
Part:
- Rail profil (V-groove atau prismatik)
- Carriage/slider block
- Mounting bolts

Mates:
- Width mate: Carriage centered on rail
- Coincident: Carriage ↔ Rail (kontak permukaan)
- Carriage harus bisa slide sepanjang rail
```

### Percobaan 9: Cam-Follower Mechanism (Cam Mate)
```
Part:
- Cam (dari Modul 5 atau Modul 2)
- Cam shaft
- Follower (flat atau roller)
- Follower guide
- Frame

Mates:
- Cam Mate: Follower ↔ Cam profile
- Concentric: Shaft ↔ Cam bore
```

### Percobaan 10: Complete Mechanism Assembly
```
Gabungkan beberapa mekanisme sebelumnya menjadi
"Teaching Model Mechanism":
- 1 motor (driver)
- 1 gear pair
- 1 crank-slider
- Frame/base
- Semua saling terhubung secara kinematik

Mates: Kombinasi semua jenis mate
Buat Exploded View + Animation (Motion Study basics)
```

---

## 6.8 Motion Study (Pengenalan)

### Basic Motion:
1. Klik tab **Motion Study 1** di bawah Graphics Area
2. Pilih **Basic Motion** dari dropdown
3. Atur **Motor** pada shaft: rotary, 30 RPM
4. Klik **Play** → amati gerakan mekanisme
5. **Record** untuk membuat video animasi

---

*Modul Praktikum CAD/CAM — Modul 6: CAD Assembly*
*Disusun untuk keperluan pendidikan*
