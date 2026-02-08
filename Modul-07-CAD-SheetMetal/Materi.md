# MODUL 7: CAD SHEET METAL

## Praktikum CAD/CAM — Pertemuan 7

---

## 7.1 Pendahuluan

Sheet Metal adalah modul di SolidWorks untuk mendesain komponen dari plat logam yang dibentuk melalui proses bending (tekukan). Sheet Metal design memungkinkan pembuatan flat pattern (pola bentangan) yang digunakan untuk proses potong dan tekuk.

---

## 7.2 Konsep Dasar Sheet Metal

### Parameter Sheet Metal:
| Parameter | Deskripsi |
|-----------|-----------|
| **Thickness** | Ketebalan plat (mm) |
| **Bend Radius** | Jari-jari tekukan default (umumnya = thickness) |
| **K-Factor** | Faktor koreksi posisi neutral axis (0.3-0.5) |
| **Bend Allowance** | Panjang material pada daerah bend |
| **Bend Deduction** | Pengurangan panjang akibat bend |
| **Relief Type** | Tipe relief pada sudut bend (rectangular/oblong/tear) |

### K-Factor:
- K-Factor = jarak neutral axis dari permukaan dalam / thickness
- Soft material (aluminum): K ≈ 0.33
- Medium (mild steel): K ≈ 0.40
- Hard material (stainless): K ≈ 0.45

---

## 7.3 Sheet Metal Features

### 7.3.1 Base Flange/Tab
Membuat base feature sheet metal (profil utama).
- Sketch profil → Base Flange → tentukan direction dan distance

### 7.3.2 Edge Flange
Menambahkan flange (tekukan) pada edge yang ada.
- Parameter: Angle, Length, Position (Material Inside/Outside/Bend Outside)

### 7.3.3 Miter Flange
Membuat flange dengan miter joint pada sudut.

### 7.3.4 Hem
Membuat tekukan 180° pada edge (pengaman tepi).
- Tipe: Closed Hem, Open Hem, Tear Drop Hem, Rolled Hem

### 7.3.5 Jog
Membuat offset (step) pada permukaan sheet metal.

### 7.3.6 Sketched Bend
Menambahkan bend pada lokasi yang ditentukan oleh sketch line.

### 7.3.7 Cross Break
Menambahkan X-pattern sedikit bend untuk kekakuan.

### 7.3.8 Closed Corner
Menutup celah pada sudut yang terbentuk dari 2 edge flange.

### 7.3.9 Rip
Memisahkan (merobek) edge yang tersambung.

### 7.3.10 Forming Tools
Tool khusus untuk membuat bentuk standar pada sheet metal:
- Louver, Lance, Rib, Emboss, dll.
- Drag dari Design Library → Sheet Metal forming tools

### 7.3.11 Flat Pattern
Membentangkan sheet metal menjadi pola datar untuk manufaktur.
- `Insert → Sheet Metal → Flatten`
- Atau klik **Flatten** di Feature Manager
- Export DXF dari flat pattern untuk laser cutting

---

## 7.4 Percobaan 1-10

### Percobaan 1: Box Sederhana (Base Flange + Edge Flange)
```
Spesifikasi:
- Material: Aluminum 1mm
- Base: 100 x 60mm
- 4 Edge Flange: tinggi 30mm, angle 90°, bend radius 1mm
- Cek Flat Pattern
```

### Percobaan 2: U-Channel (Base Flange)
```
Spesifikasi:
- Material: Steel 1.5mm
- Profil U: lebar 50mm, tinggi sisi 25mm, panjang 150mm
- 2 lubang Ø6mm di base (jarak 100mm)
- Hem pada kedua ujung atas (Closed Hem)
```

### Percobaan 3: L-Bracket Sheet Metal
```
Spesifikasi:
- Material: Steel 2mm
- Lengan vertikal: 60 x 40mm, 2 lubang Ø8mm
- Lengan horizontal: 50 x 40mm, 2 slot 15x8mm
- Bend radius: 2mm
- Fillet pada edge luar bend
```

### Percobaan 4: Cover/Lid dengan Hem
```
Spesifikasi:
- Material: Aluminum 1mm
- Plat atas: 80 x 60mm
- 4 Edge Flange turun: 10mm
- Hem pada keempat tepi bawah (Closed Hem)
- 1 lubang Ø20mm di tengah atas
```

### Percobaan 5: Enclosure Box dengan Tab dan Slot
```
Spesifikasi:
- Material: Steel 1.5mm
- Box 100 x 80 x 50mm
- Salah satu sisi terbuka (untuk panel)
- Tab & Slot pada 3 sisi (untuk self-alignment saat welding)
- 4 lubang ventilasi Ø5mm di sisi atas
```

### Percobaan 6: Bracket dengan Jog
```
Spesifikasi:
- Material: Steel 2mm
- Plat dasar 80 x 40mm
- Jog (step) offset 10mm di tengah
- 2 lubang mounting di bagian bawah
- 2 lubang mounting di bagian atas (setelah jog)
- Edge flange 20mm pada satu sisi
```

### Percobaan 7: Fan Guard (Forming Tool)
```
Spesifikasi:
- Material: Steel 1mm
- Plat lingkaran Ø100mm
- Circular pattern louver (8 buah, dari Forming Tool)
- Lubang tengah Ø30mm
- 4 lubang mounting Ø4mm pada PCD Ø90mm
```

### Percobaan 8: Cable Tray
```
Spesifikasi:
- Material: Steel 1.5mm
- Base tray: 200 x 100mm
- Sisi kiri-kanan: Edge Flange 30mm ke atas
- Lip (bibir) ke dalam: Edge Flange 10mm, angle 90° ke dalam
- Lubang ventilasi: Pattern rectangular 10x5mm slot
```

### Percobaan 9: Multi-Body Sheet Metal (Welded Box)
```
Spesifikasi:
- Material: Steel 2mm
- Box dari 5 plat terpisah (multi-body sheet metal)
- Base + 4 sisi
- Tab-slot interlocking design
- Flatten setiap body secara terpisah
```

### Percobaan 10: Panel Elektrik (Sheet Metal Lengkap)
```
Spesifikasi:
- Material: Steel 1.5mm
- Box: 300 x 200 x 100mm
- Pintu dengan hinge cutout
- Ventilasi louver di sisi (Forming Tool)
- Cable entry knockout Ø25mm di bawah
- DIN rail mounting holes di dalam
- Grounding bolt Ø6mm
- Flatten → Export DXF
```

---

## 7.5 Tips Sheet Metal Design

1. **Selalu mulai dari Base Flange** — ini menetapkan ketebalan dan parameter
2. **Perhatikan K-Factor** — pastikan sesuai material yang digunakan
3. **Cek Flat Pattern** reguler — untuk memastikan bisa dibentangkan
4. **Perhatikan minimum bend radius** — umumnya ≥ thickness material
5. **Gunakan Forming Tools** untuk fitur standar (louver, lance, emboss)
6. **Export DXF** dari Flat Pattern untuk proses laser cutting

---

*Modul Praktikum CAD/CAM — Modul 7: CAD Sheet Metal*
*Disusun untuk keperluan pendidikan*
