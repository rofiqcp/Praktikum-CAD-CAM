# MODUL 8: PROJECT CAD — DESAIN KONVEYOR DENGAN PROFIL ALUMINIUM

## Praktikum CAD/CAM — Pertemuan 8

---

## 8.1 Pendahuluan

Konveyor (conveyor) adalah sistem transportasi material yang banyak digunakan di industri. Dalam praktikum ini, kita akan mendesain **Belt Conveyor sederhana** menggunakan profil aluminium sebagai rangka struktur.

---

## 8.2 Komponen Konveyor

| No | Komponen | Fungsi |
|----|----------|--------|
| 1 | **Frame (Rangka)** | Struktur penopang dari profil aluminium |
| 2 | **Drive Roller** | Roller penggerak (terhubung motor) |
| 3 | **Idler Roller** | Roller pembalik (ujung lain) |
| 4 | **Belt** | Sabuk konveyor (material transport) |
| 5 | **Motor + Gearbox** | Penggerak utama |
| 6 | **Bearing Housing** | Rumah bearing untuk roller |
| 7 | **Side Guide** | Pemandu material di atas belt |
| 8 | **Support Legs** | Kaki penyangga |
| 9 | **Tensioning Mechanism** | Pengatur tegangan belt |
| 10 | **End Plate** | Plat ujung (sheet metal) |

---

## 8.3 Percobaan 1-10: Desain Komponen Konveyor

### Percobaan 1: Frame Samping Konveyor (Profil Aluminium 2040)
```
Spesifikasi:
- 2 batang profil 2040 panjang 600mm (sisi atas)
- 2 batang profil 2040 panjang 600mm (sisi bawah)
- 2 batang profil 2040 panjang 200mm (tiang vertikal, masing-masing ujung)
- Corner bracket untuk sambungan
- Assembly satu frame sisi
```

### Percobaan 2: Frame Cross Member (Penghubung 2 Sisi)
```
Spesifikasi:
- 4 batang profil 2020 panjang 250mm (penghubung horizontal)
- Posisi: 2 di atas, 2 di bawah
- Assembly dengan frame samping → rangka lengkap
```

### Percobaan 3: Drive Roller
```
Spesifikasi:
- Roller tube: Ø50mm, panjang 250mm, wall thickness 3mm
- Shaft: Ø12mm, panjang 300mm (menonjol di kedua sisi)
- End cap / hub: penghubung tube ke shaft
- Keyway pada shaft: 4x4mm
```

### Percobaan 4: Idler Roller
```
Spesifikasi:
- Roller tube: Ø50mm, panjang 250mm (sama dengan drive roller)
- Shaft: Ø12mm, panjang 300mm
- Tanpa keyway (free spinning)
- Sistem tensioning: slot 20mm untuk adjust posisi
```

### Percobaan 5: Bearing Housing / Pillow Block
```
Spesifikasi:
- Housing untuk bearing Ø12mm (bore)
- Base mounting: 2 lubang Ø6mm
- Material: Aluminum atau Cast Iron
- Dimensi sesuai standar UCP201 (atau desain sendiri)
```

### Percobaan 6: End Plate (Sheet Metal)
```
Spesifikasi:
- Material: Steel 2mm
- Plat ujung berbentuk trapesoid
- Slot untuk shaft bearing housing
- Lubang mounting ke profil aluminium
- Flatten → DXF
```

### Percobaan 7: Side Guide
```
Spesifikasi:
- Material: Aluminum plate 3mm atau profil L
- Panjang: 500mm
- Tinggi: 30mm
- Slot untuk adjustment posisi
- Mounting ke profil atas menggunakan T-nut
```

### Percobaan 8: Motor Bracket
```
Spesifikasi:
- Bracket untuk mounting motor NEMA 23 / motor DC
- Material: Aluminum plate 5mm
- Mounting holes sesuai motor pattern
- Adjustable slot untuk belt tension
- Mounting ke frame profil aluminium
```

### Percobaan 9: Support Legs (Kaki Penyangga)
```
Spesifikasi:
- 4 kaki dari profil 2020 panjang 400mm
- Leveling foot (adjustable) di bawah
- Gusset plate penguat di sudut atas
- Cross brace (profil 2020) penghubung antar kaki
```

### Percobaan 10: Assembly Lengkap Konveyor
```
Rakit semua komponen menjadi konveyor lengkap:
1. Frame (Percobaan 1+2)
2. Drive Roller (Percobaan 3) + Bearing Housing (5)
3. Idler Roller (Percobaan 4) + Bearing Housing (5)
4. End Plates (Percobaan 6)
5. Side Guides (Percobaan 7)
6. Motor + Bracket (Percobaan 8)
7. Support Legs (Percobaan 9)
8. Belt (simplified as surface/sheet body)

Buat:
- Exploded View
- BOM (Bill of Materials)
- Drawing dengan dimensi keseluruhan
```

---

## 8.4 Tips Desain Konveyor
1. Pastikan semua komponen kompatibel dengan profil aluminium (T-slot mounting)
2. Perhatikan center distance roller untuk ukuran belt
3. Bearing housing harus accessible untuk maintenance
4. Motor bracket harus adjustable untuk belt tension
5. Side guide harus bisa diatur posisinya

---

*Modul Praktikum CAD/CAM — Modul 8: Project Konveyor*
*Disusun untuk keperluan pendidikan*
