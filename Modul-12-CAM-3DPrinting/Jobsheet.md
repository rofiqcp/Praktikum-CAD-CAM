# JOBSHEET MODUL 12: CAM — 3D PRINTING (FDM)

## Praktikum CAD/CAM — Pertemuan 12

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mengoperasikan slicer (Cura/PrusaSlicer) untuk mempersiapkan file STL
2. Mahasiswa mampu menentukan orientasi print optimal untuk setiap part robot lengan
3. Mahasiswa mampu mengatur parameter print (layer height, infill, support, dll.)
4. Mahasiswa mampu mencetak part robot lengan dan huruf timbul menggunakan printer FDM
5. Mahasiswa mampu melakukan post-processing dan assembly fisik robot lengan 3-DOF

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + Cura/PrusaSlicer | Slicer software |
| 2 | 3D Printer FDM | Ender 3 / Prusa i3 / sejenis |
| 3 | Filamen PLA 1.75mm | Warna sesuai ketersediaan |
| 4 | SD Card / USB | Transfer G-code |
| 5 | Spatula, tang, amplas | Post-processing |
| 6 | File STL dari Modul 11 | Semua part robot + huruf timbul |
| 7 | Servo SG90 × 3 unit | Assembly fisik |
| 8 | Jangka sorong | Pengukuran toleransi |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 12 untuk:
- Prinsip kerja FDM dan anatomi printer
- Parameter slicer dan pengaruhnya
- Orientasi print dan support strategy
- Troubleshooting masalah umum
- G-code dasar untuk 3D printing

---

## IV. Langkah Percobaan

### Bagian A: Persiapan & Kalibrasi
| No | Langkah | Detail |
|----|---------|--------|
| 1 | Kalibrasi printer | Bed leveling, load filamen, test extrude |
| 2 | Setup profil printer di slicer | Pilih printer, nozzle 0.4mm, bed size |
| 3 | Import STL dari Modul 11 | Semua part robot + huruf timbul |

### Bagian B: Slice Part Robot
| No | Part | Layer Height | Infill | Support | Orientasi |
|----|------|-------------|--------|---------|-----------|
| 4 | Base Plate | 0.2mm | 30% grid | Tidak | Flat face down |
| 5 | Turntable | 0.2mm | 25% gyroid | Tidak | Circle down |
| 6 | Shoulder Bracket | 0.2mm | 40% cubic | Minimal | U horizontal |
| 7 | Upper Arm Link | 0.2mm | 30% gyroid | Cek | Flat lying |
| 8 | Elbow Bracket | 0.2mm | 40% cubic | Minimal | U horizontal |
| 9 | Forearm Link | 0.2mm | 30% gyroid | Cek | Flat lying |
| 10 | Gripper | 0.2mm | 30% gyroid | Mungkin | Custom |
| 11 | Servo Horn Adapter ×3 | 0.12mm | 50% cubic | Tidak | Flat down |

### Bagian C: Huruf Timbul
| No | Langkah | Detail |
|----|---------|--------|
| 12 | Import STL huruf timbul | Text menghadap atas |
| 13 | Set parameter detail | Layer 0.12mm, wall 3, top 5 |
| 14 | (Opsional) Setup filament change | M600 di layer huruf |

### Bagian D: Print & Assembly
| No | Langkah | Detail |
|----|---------|--------|
| 15 | Print batch 1 | Part-part kecil dulu (adapter, plate) |
| 16 | Print batch 2 | Bracket + link |
| 17 | Print huruf timbul | High detail mode |
| 18 | Post-processing | Lepas, buang support, amplas |
| 19 | Test fit servo SG90 | Cek pocket, ukur dengan jangka sorong |
| 20 | Assembly robot lengan | Pasang servo + semua part |

---

## V. Analisa dan Pembahasan
1. Bandingkan dimensi part yang dicetak vs desain CAD — berapa deviasi (mm)?
2. Apakah servo SG90 masuk ke pocket dengan baik? Jika tidak, apa penyebabnya?
3. Evaluasi orientasi print — adakah part yang seharusnya di-orientasi berbeda?
4. Bandingkan estimasi waktu slicer vs waktu print aktual — berapa perbedaannya?
5. Jelaskan masalah yang terjadi selama print dan solusi yang dilakukan
6. Bagaimana kualitas huruf timbul — apakah huruf terbaca jelas?
7. Hitung total filamen (gram) dan biaya material keseluruhan

---

## VI. Kesimpulan
Rangkum proses dari STL → Slicer → Print → Assembly:
- Pembelajaran utama tentang parameter 3D print
- Pentingnya orientasi dan support
- Evaluasi kualitas part yang dihasilkan

---

## VII. Tugas

### Video (10–15 menit):
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Penjelasan Slicer | 2–3 menit | Demonstrasi import, orientasi, parameter |
| 2. Proses Print | 3–5 menit | Time-lapse / record proses print |
| 3. Post-Processing | 2–3 menit | Lepas support, test fit servo |
| 4. Assembly & Demo | 2–3 menit | Assembly robot + gerakan manual |
| 5. Analisa | 1–2 menit | Toleransi, masalah, solusi |

### Pengumpulan:
```
NIM_Nama_Modul12/
├── Slicer/
│   ├── Screenshot_orientasi_tiap_part/
│   ├── Screenshot_parameter/
│   └── Screenshot_preview_layer/
├── Gcode/ (semua .gcode)
├── Foto/
│   ├── Proses_print.jpg
│   ├── Part_hasil.jpg
│   ├── Huruf_timbul.jpg
│   ├── Test_fit_servo.jpg
│   └── Assembly_robot.jpg
├── Pengukuran/
│   └── Tabel_dimensi_CAD_vs_aktual.xlsx
├── Video/ (NIM_Nama_Modul12.mp4)
└── Laporan.pdf
```
Kompres → `NIM_Nama_Modul12.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 12*
