# MODUL 9: PROJECT CAD — ROBOT BERODA (DIFFERENTIAL DRIVE, 2 RODA)

## Praktikum CAD/CAM — Pertemuan 9

---

## 9.1 Pendahuluan

Robot beroda differential drive menggunakan **2 roda penggerak independen** dan **1 atau 2 castor wheel** untuk stabilitas. Dengan mengatur kecepatan masing-masing roda, robot dapat bergerak maju, mundur, belok, dan berputar di tempat.

---

## 9.2 Konsep Differential Drive

### Kinematika:
- **Maju lurus**: Kedua roda berputar sama arah, kecepatan sama
- **Belok kiri**: Roda kanan lebih cepat dari roda kiri
- **Belok kanan**: Roda kiri lebih cepat dari roda kanan
- **Putar di tempat**: Roda berputar berlawanan arah, kecepatan sama

### Komponen Utama:
1. **Chassis** — Rangka utama robot
2. **Drive Wheels** (2x) — Roda penggerak
3. **DC Motors** (2x) — Motor penggerak roda
4. **Motor Bracket** — Penahan motor ke chassis
5. **Castor Wheel** — Roda pasif untuk stabilitas
6. **Battery Holder** — Tempat baterai
7. **Controller Mount** — Tempat Arduino/ESP32
8. **Sensor Bracket** — Bracket sensor (ultrasonic, IR)
9. **Bumper** — Pelindung depan
10. **Top Plate** — Plat atas untuk komponen tambahan

---

## 9.3 Percobaan 1-10

### Percobaan 1: Chassis Base Plate
```
Spesifikasi:
- Material: Akrilik 5mm atau Aluminum 3mm
- Bentuk: Rounded rectangle 200 x 150mm, R20
- Lubang mounting motor: sesuai bracket motor (2 set)
- Lubang castor wheel: di depan dan/atau belakang
- Lubang mounting PCB: 4x Ø3mm (standar mounting holes)
- Slot kabel: 2 slot 10x5mm
- Simetris terhadap sumbu longitudinal
```

### Percobaan 2: Drive Wheel
```
Spesifikasi (berbeda dari wheel standar):
- Diameter roda: Ø65mm
- Lebar roda: 20mm
- Hub bore: Ø5mm (sesuai motor shaft) atau Ø6mm
- Hub keyway/flat: D-shape
- Tread pattern: V-groove atau flat rubber
- Buat 2 tipe wheel berbeda (rubber grip vs smooth)
```

### Percobaan 3: Motor Bracket (Sheet Metal)
```
Spesifikasi:
- Material: Aluminum 2mm
- Bracket untuk DC motor Ø25mm (130-size motor) atau N20 motor
- Clamp style atau tab-mount style
- Lubang mounting ke chassis: 2x Ø3mm
- Adjustable slot untuk alignment
- Sheet metal → Flatten → DXF
```

### Percobaan 4: Castor Wheel Assembly
```
Spesifikasi:
- Ball castor type:
  - Housing: Ø20mm ball, Cup Ø25mm
  - Mounting plate: 30x30mm, 4 lubang Ø3mm
  - Tinggi total: 15mm (adjustable dengan spacer)
- Atau Swivel castor mini
```

### Percobaan 5: Battery Holder
```
Spesifikasi:
- Holder untuk 4x AA battery (atau Li-Po pack)
- Material: ABS plastic (3D printable)
- Dimensi sesuai ukuran baterai
- Clip/snap-fit mechanism
- Lubang kabel output
- Mounting holes untuk chassis: 2x Ø3mm
```

### Percobaan 6: Controller Board Mount (Arduino Uno)
```
Spesifikasi:
- Mounting plate untuk Arduino Uno (68.6 x 53.4mm)
- 4 standoff pillars: Ø6mm luar, Ø3mm dalam, tinggi 8mm
- Posisi holes sesuai Arduino Uno mounting pattern
- Material: Akrilik 3mm
- Slot untuk kabel
```

### Percobaan 7: Sensor Bracket (Ultrasonic HC-SR04)
```
Spesifikasi:
- Bracket untuk sensor ultrasonic HC-SR04
- 2 lubang sensor: Ø16mm, jarak center 26mm
- Adjustable angle: 0-30° (slot atau hinge)
- Mounting ke depan chassis
- Material: Akrilik 3mm atau 3D print
```

### Percobaan 8: Front Bumper
```
Spesifikasi:
- Material: Rubber/TPU (3D print flex) atau Akrilik 3mm
- Bentuk: Arc mengikuti kontur depan chassis
- Mounting brackets ke chassis
- Bisa menampung micro switch (bump sensor)
- Cutout untuk sensor ultrasonic
```

### Percobaan 9: Top Plate / Second Deck
```
Spesifikasi:
- Material: Akrilik 3mm
- Dimensi: sama dengan chassis atau lebih kecil
- Spacer/standoff: 4x Ø8mm luar, Ø4mm dalam, tinggi 30mm
- Lubang untuk kabel pass-through
- Mounting untuk komponen tambahan (sensor, display)
```

### Percobaan 10: Assembly Robot Beroda Lengkap
```
Rakit semua komponen:
1. Chassis (Percobaan 1)
2. 2x Drive Wheel (Percobaan 2)
3. 2x Motor + Bracket (Percobaan 3)
4. 1-2x Castor Wheel (Percobaan 4)
5. Battery Holder (Percobaan 5)
6. Arduino Mount (Percobaan 6)
7. Sensor Bracket + Sensor (Percobaan 7)
8. Bumper (Percobaan 8)
9. Top Plate + Standoffs (Percobaan 9)

Assembly Mates:
- Concentric: Wheel ↔ Motor shaft
- Coincident: Brackets ↔ Chassis
- Distance: Castor wheel height
- Buat Exploded View
- Buat BOM
```

---

## 9.4 Variasi Wheel Design (Different Wheels)
Eksplorasi tipe roda berbeda:
1. **Omni Wheel** — Bisa bergerak ke segala arah
2. **Mecanum Wheel** — Roller pada sudut 45°
3. **Standard Rubber Wheel** — Traksi tinggi
4. **Track/Caterpillar** — Untuk terrain kasar

---

*Modul Praktikum CAD/CAM — Modul 9: Project Robot Beroda*
*Disusun untuk keperluan pendidikan*
