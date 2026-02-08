# JOBSHEET MODUL 11: PROJECT CAD — ROBOT LENGAN 3-DOF

## Praktikum CAD/CAM — Pertemuan 11

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mendesain robot lengan 3-DOF menggunakan servo SG90
2. Mahasiswa mampu menerapkan Design for 3D Printing pada setiap part
3. Mahasiswa mampu mendesain huruf timbul (embossed text) untuk 3D print
4. Mahasiswa mampu membuat assembly dengan hinge mate dan angle limits
5. Mahasiswa mampu meng-export STL dan mempersiapkan file untuk 3D printing

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + SolidWorks | Semua modul |
| 2 | Cura / PrusaSlicer | Preview & estimasi print |
| 3 | Datasheet Servo SG90 | Dimensi mounting |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 11 untuk:
- Konsep robot lengan 3-DOF dan kinematika
- Spesifikasi servo SG90 dan dimensi mounting
- Design rules untuk 3D printing (FDM)
- Teknik huruf timbul di SolidWorks
- Koneksi realisasi ke Modul 12

---

## IV. Langkah Percobaan
| No | Komponen | Teknik | Export |
|----|----------|--------|--------|
| 1 | Base Plate | Extrude + Pattern | **STL** |
| 2 | Turntable | Extrude + Pocket | **STL** |
| 3 | Shoulder Bracket (U-shape) | Extrude + Pocket SG90 | **STL** |
| 4 | Shoulder Link (Upper Arm) | Extrude + Hole + Fillet | **STL** |
| 5 | Elbow Bracket | Extrude + Pocket SG90 | **STL** |
| 6 | Forearm Link (Lower Arm) | Extrude + Hole + Fillet | **STL** |
| 7 | Gripper | Extrude / Assembly | **STL** |
| 8 | Servo Horn Adapter + **Huruf Timbul** | Extrude + **Text Boss** | **STL** |
| 9 | Assembly + Motion Study | Assembly + Hinge Mate | — |
| 10 | Export STL + Print Preparation | Export + Slicer | **G-code** |

---

## V. Analisa dan Pembahasan
1. Hitung jangkauan (reach) robot berdasarkan panjang link L1 dan L2
2. Jelaskan mengapa SG90 cukup untuk robot ini — hitung torsi yang dibutuhkan
3. Diskusikan orientasi print optimal untuk setiap part — mengapa?
4. Analisis toleransi servo pocket (clearance 0.2mm) — apa efeknya jika terlalu kecil/besar?
5. Jelaskan teknik pembuatan huruf timbul — mengapa gunakan Extruded Boss, bukan Cut?
6. Estimasi total waktu print dan filamen — apakah feasible di 1 sesi praktikum?

---

## VI. Kesimpulan
Rangkum proses desain robot lengan dari konsep 3-DOF → CAD → DfAM → STL → siap 3D print.

---

## VII. Tugas

### Video (10–15 menit):
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Penjelasan Konsep | 2–3 menit | 3-DOF, SG90, kinematika sederhana |
| 2. Demo SolidWorks | 5–7 menit | Screen record: bracket, link, huruf timbul |
| 3. Demo Slicer | 2–3 menit | Orientasi, parameter, estimasi |
| 4. Analisa & Kesimpulan | 2–3 menit | DfAM, toleransi, feasibility |

### Pengumpulan:
```
NIM_Nama_Modul11/
├── SolidWorks/ (semua .sldprt + .sldasm)
├── STL/ (semua part .stl)
├── Slicer/ (screenshot parameter + estimasi)
├── Drawing/ (.slddrw / .pdf)
├── Video/ (NIM_Nama_Modul11.mp4)
└── BOM.xlsx atau BOM.pdf
```
Kompres → `NIM_Nama_Modul11.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 11*
