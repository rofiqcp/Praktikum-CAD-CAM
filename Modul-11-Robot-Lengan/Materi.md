# MODUL 11: PROJECT CAD — ROBOT LENGAN 3-DOF (SERVO SG90)

## Praktikum CAD/CAM — Pertemuan 11

---

## Daftar Isi
1. [Pendahuluan](#111-pendahuluan)
2. [Konsep Robot Lengan 3-DOF](#112-konsep-robot-lengan-3-dof)
3. [Servo Motor SG90](#113-servo-motor-sg90)
4. [Komponen & BOM](#114-komponen--bom)
5. [Desain untuk 3D Printing](#115-desain-untuk-3d-printing)
6. [Kinematika Sederhana](#116-kinematika-sederhana)
7. [Koneksi ke Modul Realisasi](#117-koneksi-ke-modul-realisasi)
8. [Percobaan 1–10](#118-percobaan-110)

---

## 11.1 Pendahuluan

Robot lengan (robot arm / manipulator) adalah robot dengan struktur serial yang terdiri dari beberapa link dan joint. Dalam praktikum ini, kita mendesain **Robot Lengan 3-DOF** menggunakan servo motor **SG90** sebagai aktuator. Desain ini dirancang agar **semua part custom bisa di-3D print** dan direalisasikan di **Modul 12 (CAM 3D Printing)**.

### Mengapa 3-DOF?
- **Cukup** untuk demonstrasi pick-and-place sederhana
- **3 servo SG90** = murah dan mudah didapat
- **Ringan** — SG90 cocok untuk beban ringan (< 100g di ujung)
- **Sederhana** untuk dipelajari — kinematika 3-DOF lebih mudah dipahami
- **Printable** — semua part bisa dicetak dalam 1 sesi 3D printing

### Konfigurasi 3-DOF
```
DOF 1: Base Rotation (Yaw)    — servo SG90 di base → rotasi horizontal 0–180°
DOF 2: Shoulder (Pitch)       — servo SG90 di bahu → angkat/turunkan lengan
DOF 3: Elbow (Pitch)          — servo SG90 di siku → angkat/turunkan forearm
       + Gripper sederhana    — servo SG90 ke-4 (opsional) atau passive gripper
```

---

## 11.2 Konsep Robot Lengan 3-DOF

### 11.2.1 Arsitektur Robot
```
        ┌─────────┐
        │ Gripper │    DOF 3: Elbow (Pitch)
        └────┬────┘         │
             │              ▼
        ┌────┴────┐    ┌──────────┐
        │Forearm  │────│ Servo 3  │
        │ Link    │    │ (SG90)   │
        └────┬────┘    └──────────┘
             │
        ┌────┴────┐    ┌──────────┐
        │Shoulder │    │ Servo 2  │    DOF 2: Shoulder (Pitch)
        │ Link    │────│ (SG90)   │         │
        └────┬────┘    └──────────┘         ▼
             │
        ┌────┴────────────────────┐
        │    Turntable / Base     │    DOF 1: Base Rotation (Yaw)
        │    ┌──────────┐        │         │
        │    │ Servo 1  │        │         ▼
        │    │ (SG90)   │        │
        └────┴──────────┴────────┘
        ┌─────────────────────────┐
        │      Base Plate         │
        └─────────────────────────┘
```

### 11.2.2 Dimensi Desain
| Parameter | Nilai |
|-----------|-------|
| Base diameter | Ø70–80mm |
| Shoulder link length | 80mm (center-to-center) |
| Forearm link length | 70mm (center-to-center) |
| Total reach (max) | ~150mm dari center base |
| Total height (max) | ~180mm dari meja |
| Payload | < 50 gram (ringan) |
| Material part custom | **PLA (3D Print)** |

---

## 11.3 Servo Motor SG90

### 11.3.1 Spesifikasi SG90
| Parameter | Nilai |
|-----------|-------|
| Tipe | Micro servo, analog |
| Berat | 9 gram |
| Torsi | 1.2–1.8 kg·cm (4.8V–6V) |
| Speed | 0.1 s/60° (tanpa beban) |
| Rotation angle | 0–180° |
| Tegangan operasi | 4.8–6.0 V |
| Ukuran body | 22.2 × 11.8 × 22.7 mm |
| Shaft | Gear shaft, Ø-cut |
| Wire | 3 pin: Signal (orange), VCC (red), GND (brown) |

### 11.3.2 Dimensi Mounting SG90
```
Tampak Depan:              Tampak Samping:
   ┌────┐                      ┌────┐
   │gear│                      │    │ 22.7mm
   ├────┤                      │    │
   │    │ 22.2mm               │    │
   │    │                      ├────┤
┌──┤    ├──┐  ← mounting tabs  │tab │ 2.5mm (tab thickness)
│  │    │  │  32.5mm total     └────┘
└──┤    ├──┘  (body + tabs)
   │    │
   └────┘
   11.8mm

Mounting Tab Details:
- Tab lebar total: 32.5mm (body 22.2mm + 2×5.15mm tab)
- Tab thickness: 2.5mm
- Mounting hole: Ø2mm (atau self-tapping)
- Hole spacing: 27.5mm (center-to-center)
- Shaft center dari mounting surface: ~5mm ke atas

Servo Horn (Cross-shape):
- Ø single arm: Ø18mm (radius from center)
- Hub: Ø7mm
- Screw: M2 (center)
```

### 11.3.3 Kontrol SG90 dengan Arduino
```
Wiring:
- Orange (Signal) → Arduino PWM pin (D9, D10, D11)
- Red (VCC) → 5V (atau external 5V PSU jika banyak servo)
- Brown (GND) → GND

Kode Arduino (Servo library):
  #include <Servo.h>
  Servo base, shoulder, elbow;
  
  void setup() {
    base.attach(9);      // DOF 1
    shoulder.attach(10); // DOF 2
    elbow.attach(11);    // DOF 3
  }
  
  void loop() {
    base.write(90);      // center position
    shoulder.write(45);  // 45° up
    elbow.write(90);     // straight
    delay(1000);
  }
```

---

## 11.4 Komponen & BOM

| No | Part | Qty | Material | Proses | STL? |
|----|------|-----|----------|--------|------|
| 1 | Base Plate | 1 | PLA | **3D Print** | ✅ |
| 2 | Turntable | 1 | PLA | **3D Print** | ✅ |
| 3 | Shoulder Bracket | 1 | PLA | **3D Print** | ✅ |
| 4 | Shoulder Link (Upper Arm) | 1 | PLA | **3D Print** | ✅ |
| 5 | Elbow Bracket | 1 | PLA | **3D Print** | ✅ |
| 6 | Forearm Link (Lower Arm) | 1 | PLA | **3D Print** | ✅ |
| 7 | Gripper (sederhana) | 1 | PLA | **3D Print** | ✅ |
| 8 | Servo Horn Adapter | 2–3 | PLA | **3D Print** | ✅ |
| 9 | **Huruf Timbul / Name Plate** | 1 | PLA | **3D Print** | ✅ |
| 10 | Servo SG90 | 3 (+ 1 opsional gripper) | Motor | Beli | — |
| 11 | Arduino Uno / Nano | 1 | PCB | Beli | — |
| 12 | Fasteners M2×8 | 12+ | Hardware | Beli | — |
| 13 | Jumper wires | 12+ | Kabel | Beli | — |

---

## 11.5 Desain untuk 3D Printing

### 11.5.1 Design Rules (FDM Printing)
| Aturan | Nilai | Keterangan |
|--------|-------|------------|
| Min wall thickness | ≥ 1.2mm | 3× nozzle (0.4mm) |
| Min feature size | ≥ 0.8mm | 2× nozzle |
| Overhang angle | ≤ 45° tanpa support | Di atas 45° perlu support |
| Hole clearance | +0.3mm dari nominal | Compensate shrinkage |
| Shaft hole SG90 | Ø5.3mm (5mm + 0.3mm) | Clearance fit |
| Screw hole M2 | Ø1.7mm (self-tap) atau Ø2.3mm (clearance) | |
| Layer orientation | Kuat di X-Y, lemah di Z | Orient part accordingly |
| Bridge max | ≤ 10mm tanpa support | |

### 11.5.2 Servo Pocket Design
```
Setiap bracket yang memegang servo SG90 membutuhkan pocket/slot:

Pocket dimensi:
- Width: 12.0mm (body 11.8mm + 0.2mm clearance)
- Length: 22.5mm (body 22.2mm + 0.3mm clearance)
- Depth: 22.7mm (full body) atau lebih tipis jika perlu
- Tab slot: 2.7mm (tab 2.5mm + 0.2mm clearance)
- Tab slot width: 5.3mm (tab 5.15mm + 0.15mm)

Mounting strategy:
- Servo masuk dari atas, tab menahan di slot
- Atau servo masuk dari samping (slide-in)
- Sekrup M2 melalui tab hole untuk mengunci
```

### 11.5.3 Huruf Timbul (3D Print)
Salah satu part yang di-3D print adalah **huruf timbul / name plate**:
```
Huruf Timbul:
- Base plate: 60 × 20 × 3mm
- Huruf: tinggi 10mm, tebal 2mm, menonjol dari base
- Teks: Nama / Inisial / "ARM BOT"
- Teknik SolidWorks: Sketch Text → Extruded Boss 2mm
- Mounting: clip/slot ke base robot atau standalone display

Tips 3D Print huruf:
- Font: Sans-serif tebal (Arial Bold, Impact)
- Min stroke width: 1.5mm (agar kuat di cetak)
- Orientasi print: huruf menghadap atas (best surface quality)
- Layer height: 0.1–0.15mm (untuk detail halus)
- Infill: 100% (solid, karena tipis)
```

---

## 11.6 Kinematika Sederhana

### Forward Kinematics (3-DOF)
```
Posisi ujung lengan (x, y, z) berdasarkan sudut joint (θ1, θ2, θ3):

x = cos(θ1) × [L1 × cos(θ2) + L2 × cos(θ2 + θ3)]
y = sin(θ1) × [L1 × cos(θ2) + L2 × cos(θ2 + θ3)]
z = L1 × sin(θ2) + L2 × sin(θ2 + θ3) + h_base

Di mana:
- θ1 = sudut base (yaw, 0–180°)
- θ2 = sudut shoulder (pitch)
- θ3 = sudut elbow (pitch)
- L1 = panjang shoulder link (80mm)
- L2 = panjang forearm link (70mm)
- h_base = tinggi base + turntable (~30mm)
```

### Workspace (Jangkauan)
```
Max reach = L1 + L2 = 80 + 70 = 150mm (horizontal, dari center base)
Max height = L1 + L2 + h_base = 80 + 70 + 30 = 180mm (vertikal)
Min reach = |L1 - L2| = |80 - 70| = 10mm (lengan terlipat hampir habis)
```

---

## 11.7 Koneksi ke Modul Realisasi

### Peta Fabrikasi
```
┌──────────────────────────────┐
│ MODUL 11 (ini)               │
│ Robot Lengan 3-DOF — CAD     │
│ Desain semua part 3D print   │
│ Export: STL semua part       │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ MODUL 12 — 3D Printing       │
│                              │
│ • 3D print semua bracket     │
│ • 3D print link (arm)        │
│ • 3D print gripper           │
│ • 3D print HURUF TIMBUL      │
│ • Assembly robot lengan      │
│ • Test fungsional             │
└──────────────────────────────┘
```

### Yang Harus Disiapkan untuk Modul 12:
1. **STL semua part** (8–10 files) — exported dengan Fine quality
2. **Orientasi print** — tentukan orientasi terbaik per part
3. **Estimasi**: waktu print, filamen, support yang dibutuhkan
4. **Assembly guide** — urutan perakitan

---

## 11.8 Percobaan 1–10

### Percobaan 1: Base Plate
```
Spesifikasi:
- Material: PLA (3D Print)
- Bentuk: Lingkaran Ø80mm atau persegi 80×80mm, tinggi 8mm
- Lubang mounting: 4× Ø3mm (untuk dipasang di meja/surface)
- Center bore: Ø5.3mm (untuk shaft servo base)
- Recessed area: Ø15mm, depth 2mm (untuk servo horn hub)
- Cable channel: slot 5×3mm (untuk kabel servo)
- Rubber pad recess: 4× Ø10mm, depth 1mm (anti-slip)

Langkah:
1. Sketch circle Ø80mm → Extrude 8mm
2. Center bore Ø5.3mm → Extrude Cut through
3. Recessed area Ø15mm → Cut 2mm dari atas
4. Mounting holes: Circular Pattern 4× Ø3mm, PCD Ø65mm
5. Cable channel: Sketch slot → Cut
6. Export STL (Fine: deviation 0.02mm, angle 5°)
```

### Percobaan 2: Turntable (Platform Rotasi)
```
Spesifikasi:
- Material: PLA
- Platform atas: Ø60mm, tinggi total 15mm
- Servo horn pocket: recess untuk menempel servo horn cross
  - Pocket: sesuai servo horn cross-shape
  - Depth: 2mm
  - Center screw hole: Ø2.3mm
- Lubang mounting bracket shoulder: 2× Ø2mm
- Step/collar bawah: Ø30mm × 5mm (masuk ke base plate bore)

Langkah:
1. Sketch Ø60mm → Extrude 10mm (platform)
2. Sketch Ø30mm → Extrude 5mm ke bawah (step collar)
3. Pocket servo horn: sketch cross-shape horn → Cut 2mm
4. Mounting holes untuk shoulder bracket
5. Export STL
```

### Percobaan 3: Shoulder Bracket (U-shape)
```
Spesifikasi:
- Material: PLA
- Bracket bentuk U untuk menahan servo SG90 (DOF 2)
- Dimensi luar: 35 × 25 × 30mm (W×D×H)
- Servo pocket: 12.0 × 22.5 × 23mm (servo masuk dari atas)
- Tab slot: 2× (2.7 × 5.3mm) di kedua sisi
- Mounting holes servo: 2× Ø2mm (melalui tab)
- Mounting ke turntable: 2× Ø2mm di base bracket
- Shaft hole (kedua sisi U): Ø5.3mm (untuk servo shaft)

Langkah:
1. Sketch profil U → Extrude 25mm
2. Pocket servo: Extruded Cut sesuai dimensi SG90
3. Tab slots di kedua sisi
4. Drill holes
5. Shaft holes di kedua sisi
6. Export STL
```

### Percobaan 4: Shoulder Link (Upper Arm)
```
Spesifikasi:
- Material: PLA
- Panjang: 80mm (center-to-center antara shoulder dan elbow)
- Desain: 2 plate parallel (sandwich) atau single arm
- Lebar: 15mm
- Tebal: 5mm per plate (atau 10mm single arm)
- Hole ujung shoulder: Ø5.3mm (servo shaft)
- Hole ujung elbow: Ø5.3mm (servo shaft elbow)
- Hub pocket servo horn: di ujung shoulder
- Weight reduction: oval slots atau cutouts (opsional)
- Fillet semua sudut: R3mm

Langkah:
1. Sketch profil arm → 80mm long, 15mm wide
2. Extrude 5mm
3. Holes di kedua ujung Ø5.3mm
4. Hub pocket untuk servo horn di ujung shoulder
5. Weight reduction cutouts (opsional)
6. Fillet semua edge
7. Export STL
```

### Percobaan 5: Elbow Bracket (Compact)
```
Spesifikasi:
- Material: PLA
- Bracket kecil untuk servo SG90 (DOF 3) di siku
- Dimensi: 30 × 22 × 25mm
- Servo pocket: sama dengan shoulder bracket (SG90)
- Mounting: menyatu/terintegrasi dengan ujung shoulder link
  — Atau sebagai part terpisah yang di-bolt ke shoulder link
- Shaft hole: Ø5.3mm di kedua sisi

Langkah:
1. Desain bracket compact untuk SG90
2. Integrasi dengan shoulder link atau desain terpisah
3. Servo pocket + tab slot
4. Export STL
```

### Percobaan 6: Forearm Link (Lower Arm)
```
Spesifikasi:
- Material: PLA
- Panjang: 70mm (center-to-center)
- Lebar: 12mm (lebih ramping dari shoulder link)
- Tebal: 5mm
- Hole ujung elbow: Ø5.3mm
- Hole ujung gripper: Ø5.3mm atau slot mounting
- Hub pocket servo horn: di ujung elbow
- Lebih ringan dari shoulder link (torsi SG90 terbatas)
- Fillet R3mm

Langkah:
1. Sketch profil arm → 70mm long, 12mm wide
2. Extrude 5mm
3. Holes + hub pocket
4. Fillet
5. Export STL
```

### Percobaan 7: Gripper Sederhana
```
Spesifikasi:
- Material: PLA
- Tipe: Fork gripper atau finger gripper passive
- Desain sederhana:

Opsi A — Fork Gripper (Tanpa servo):
  - 2 prong/fork: gap 20mm
  - Mounting ke ujung forearm
  - Untuk mendorong/menyendok benda ringan

Opsi B — Finger Gripper (Dengan servo SG90 ke-4 — opsional):
  - 2 finger parallel motion
  - Servo driven via linkage atau rack-pinion
  - Opening: 0–30mm
  - Grip force: cukup untuk benda < 50g

Langkah:
1. Desain gripper sesuai opsi yang dipilih
2. Mounting interface ke forearm (hole/slot)
3. Pastikan printable tanpa support (orient dengan baik)
4. Export STL
```

### Percobaan 8: Servo Horn Adapter & Huruf Timbul
```
Servo Horn Adapter (2–3 pcs):
- Material: PLA
- Adapter antara servo horn dan link
- Pola holes sesuai servo horn cross
- Center hole: Ø2.3mm (untuk screw M2)
- Outer profile: sesuai hub pocket di link

★ HURUF TIMBUL / NAME PLATE:
- Material: PLA
- Base plate: 60 × 20 × 3mm (atau sesuai kebutuhan)
- Huruf: Nama / Inisial / "ARM BOT"
- Tinggi huruf: 10mm
- Tebal huruf (menonjol): 2mm dari base
- Font: Arial Bold atau Impact
- Min stroke width: 1.5mm
- Mounting: 2× Ø2mm hole atau clip ke base robot

Langkah Huruf Timbul:
1. Sketch rectangle base → Extrude 3mm
2. Front Plane → Sketch → Text tool → ketik nama/inisial
3. Font: Arial Bold, size ~10mm
4. Extruded Boss/Base → 2mm (huruf menonjol ke depan)
5. Opsional: Fillet pada huruf 0.3mm (halus)
6. Export STL
7. Orientasi print: huruf menghadap atas (best quality)
```

### Percobaan 9: Assembly Robot Lengan + Motion Study
```
Assembly:
1. Base Plate (P1)
2. Servo 1 (SG90) masuk ke base plate
3. Turntable (P2) terhubung ke servo horn 1
4. Shoulder Bracket (P3) di atas turntable
5. Servo 2 (SG90) masuk ke shoulder bracket
6. Shoulder Link (P4) terhubung ke servo horn 2
7. Elbow Bracket (P5) di ujung shoulder link
8. Servo 3 (SG90) masuk ke elbow bracket
9. Forearm Link (P6) terhubung ke servo horn 3
10. Gripper (P7) di ujung forearm
11. Servo Horn Adapters (P8) di setiap joint
12. Huruf Timbul (P8) di base atau display
13. Fasteners M2

Assembly Mates:
- Concentric: semua shaft ke holes
- Coincident: bracket ke turntable/link
- Hinge Mate: untuk rotasi joint (DOF 1, 2, 3)
- Angle Limits: 0–180° per joint

Motion Study (sederhana):
- Rotate base 0→90→180→90→0°
- Shoulder 90→45→90°
- Elbow 90→135→45→90°
```

### Percobaan 10: Export STL + Print Preparation
```
Export semua part ke STL:
1. Setiap part → File → Save As → STL (Fine quality)
2. Buat folder: STL/ → semua file .stl

Print Preparation (untuk Modul 12):
3. Buka Cura / PrusaSlicer
4. Import semua STL
5. Untuk setiap part, tentukan:
   - Orientasi print optimal (minimize support)
   - Layer height (0.2mm standard, 0.1mm untuk huruf timbul)
   - Infill (20% standard, 100% untuk huruf timbul)
   - Support (yes/no per part)
6. Buat tabel estimasi:

| Part | Orientasi | Layer | Infill | Support | Waktu Est. | Filamen Est. |
|------|-----------|-------|--------|---------|------------|--------------|
| Base Plate | Flat | 0.2mm | 20% | No | ... | ... |
| Turntable | Flat | 0.2mm | 20% | No | ... | ... |
| Shoulder Bracket | Upright | 0.2mm | 25% | Yes | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |
| Huruf Timbul | Flat (huruf up) | 0.1mm | 100% | No | ... | ... |

7. Screenshot slicer preview per part
8. Hitung total waktu print dan total filamen
9. Tentukan apakah bisa print semua sekaligus (nesting di bed)
10. Save G-code (belum print — akan diprint di Modul 12)
```

---

## 11.9 Tips Desain Robot Lengan
1. **Ringan di ujung** — forearm dan gripper harus lebih ringan dari shoulder link (torsi SG90 terbatas)
2. **Clearance servo** — beri toleransi 0.2–0.3mm pada pocket servo
3. **Self-tapping holes** — untuk M2: buat hole Ø1.7mm (screw tap sendiri ke PLA)
4. **Orient print** — bracket U-shape: print upright (kekuatan antar layer di arah beban)
5. **Avoid thin walls** — minimum 1.2mm (3 × nozzle 0.4mm)
6. **Test fit** — print 1 bracket dulu, test servo masuk/tidak, adjust toleransi
7. **Huruf timbul** — print flat (huruf menghadap atas) untuk kualitas terbaik

---

*Modul Praktikum CAD/CAM — Modul 11: Project Robot Lengan*
*Disusun untuk keperluan pendidikan*
