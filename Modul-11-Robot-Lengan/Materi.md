# MODUL 11: PROJECT CAD — ROBOT LENGAN (ROBOT ARM)

## Praktikum CAD/CAM — Pertemuan 11

---

## 11.1 Pendahuluan

Robot lengan (robot arm/manipulator) adalah robot dengan struktur serial yang terdiri dari beberapa link dan joint. Desain robot lengan memerlukan pemahaman kinematika, material, dan proses manufaktur.

---

## 11.2 Komponen Robot Lengan

| No | Komponen | Fungsi |
|----|----------|--------|
| 1 | **Base** | Alas/pondasi robot |
| 2 | **Turntable/Waist** | Rotasi pada sumbu vertikal |
| 3 | **Shoulder Link** | Link pertama (bahu) |
| 4 | **Elbow Link** | Link kedua (siku) |
| 5 | **Wrist Link** | Link ketiga (pergelangan) |
| 6 | **End Effector/Gripper** | Penjepit/alat di ujung |
| 7 | **Servo Motors** (4-6x) | Aktuator sendi |
| 8 | **Servo Bracket** | Bracket mounting servo |
| 9 | **Bearing** | Penunjang rotasi |
| 10 | **Fasteners** | Baut, mur, spacer |

---

## 11.3 Konfigurasi Robot Arm (4 DOF)
```
Base (Yaw) → Shoulder (Pitch) → Elbow (Pitch) → Gripper (Open/Close)
```
- **DOF 1**: Base rotation (0-180°)
- **DOF 2**: Shoulder up/down (0-180°)
- **DOF 3**: Elbow up/down (0-180°)
- **DOF 4**: Gripper open/close

---

## 11.4 Percobaan 1-10

### Percobaan 1: Base Platform
```
Spesifikasi:
- Material: Akrilik 5mm (laser cut) atau 3D print
- Diameter base: Ø100mm atau persegi 100x100mm
- Lubang mounting ke meja: 4x Ø4mm
- Bearing seat untuk turntable: Ø50mm bore
- Lubang kabel pass-through di tengah
- Lubang mounting servo base: sesuai servo SG90/MG996R
```

### Percobaan 2: Turntable (Rotating Platform)
```
Spesifikasi:
- Platform rotasi di atas base
- Diameter: Ø80mm
- Bearing interface: outer race seat
- Hub di atas untuk mounting shoulder bracket
- Gear teeth di bawah (opsional) atau direct drive
- Material: Akrilik 5mm atau Aluminum 3mm
```

### Percobaan 3: Shoulder Bracket (Servo Bracket U-shape)
```
Spesifikasi:
- Bracket U untuk servo shoulder
- Material: Aluminum 2mm (sheet metal) atau Akrilik 3mm
- Dimensi sesuai servo MG996R (40.7 x 19.7 x 42.9mm)
- Lubang shaft servo di kedua sisi
- Lubang mounting ke turntable di bawah
- Sheet Metal design → Flatten → DXF
```

### Percobaan 4: Shoulder Link (Upper Arm)
```
Spesifikasi:
- Link penghubung shoulder ke elbow
- Panjang: 100mm (center to center)
- Material: Aluminum plate 3mm atau Akrilik 5mm
- 2 buah plat parallel (sandwich servo)
- Lubang bearing/servo di kedua ujung
- Slot untuk weight reduction (opsional)
- Fillet pada semua sudut
```

### Percobaan 5: Elbow Bracket
```
Spesifikasi:
- Bracket untuk servo elbow
- Desain mirip shoulder bracket (U-shape)
- Lebih kecil untuk servo SG90
- Mounting ke ujung shoulder link
```

### Percobaan 6: Forearm Link (Lower Arm)
```
Spesifikasi:
- Link penghubung elbow ke wrist/gripper
- Panjang: 80mm (center to center)
- Material: Akrilik 3mm atau Aluminum 2mm
- Lebih ringan dari shoulder link
- Lubang di kedua ujung
- Desain streamlined
```

### Percobaan 7: Gripper Mechanism
```
Spesifikasi:
- Gripper 2-finger parallel
- Servo driven: SG90 micro servo
- Jaw opening: 0-40mm
- Material: Akrilik 3mm
- Komponen:
  - Gripper base
  - Left jaw
  - Right jaw
  - Linkage bars (4-bar mechanism)
  - Servo mount
- Grip force cukup untuk benda ringan (<100g)
```

### Percobaan 8: Servo Horn Adapter
```
Spesifikasi:
- Adapter antara servo horn standard dan link
- Material: Aluminum 3mm
- Pola holes sesuai servo horn
- Lubang center untuk shaft
- Set screw hole
- Buat untuk beberapa ukuran servo (SG90, MG996R)
```

### Percobaan 9: Cable Management dan Cover
```
Spesifikasi:
- Cable guide clips (3D printable)
- Cover/shroud untuk link (opsional, estetika)
- Cable routing channel
- Material: PLA (3D print)
```

### Percobaan 10: Assembly Robot Lengan Lengkap
```
Rakit semua komponen:
1. Base (P1) + Turntable (P2) + Bearing
2. Shoulder Bracket (P3) + Servo MG996R
3. Shoulder Link (P4)
4. Elbow Bracket (P5) + Servo SG90
5. Forearm Link (P6)
6. Gripper Assembly (P7) + Servo SG90
7. Servo Horn Adapters (P8)
8. Cable Management (P9)
9. Fasteners (M3 bolts, nuts, spacers)

Assembly Mates:
- Concentric untuk semua sendi rotasi
- Hinge Mate untuk gerakan pitch
- Angle limits pada setiap sendi
- Buat Exploded View
- Buat Motion Study (sederhana)
- Buat BOM
```

---

*Modul Praktikum CAD/CAM — Modul 11: Project Robot Lengan*
*Disusun untuk keperluan pendidikan*
