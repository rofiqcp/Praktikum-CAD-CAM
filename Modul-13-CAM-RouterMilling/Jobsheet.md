# JOBSHEET MODUL 13: CAM — CNC ROUTER MILLING

## Praktikum CAD/CAM — Pertemuan 13

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mengimport file STEP ke Fusion 360 dan melakukan setup CAM
2. Mahasiswa mampu membuat toolpath: face, pocket, contour (dengan tabs), drill, dan engrave
3. Mahasiswa mampu mensimulasikan toolpath dan mendeteksi collision/gouging
4. Mahasiswa mampu melakukan post-processing untuk menghasilkan G-code (GRBL)
5. Mahasiswa mampu mengeksekusi G-code pada mesin CNC router
6. Mahasiswa mampu membuat **ukiran nama** menggunakan V-bit engraving

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + Fusion 360 | CAM software |
| 2 | CNC Router | Mesin pengeksekusi |
| 3 | End Mill 6mm flat, 2-flute | Pocket, contour |
| 4 | End Mill 3mm flat, 2-flute | Detail |
| 5 | V-Bit 60° | Ukiran nama / engraving |
| 6 | Drill Bit 3mm, 5mm | Lubang baut |
| 7 | MDF / Kayu | Material benda kerja |
| 8 | Clamp, wrench, jangka sorong | Setup & pengukuran |
| 9 | Safety glasses, mask, ear plug | Keselamatan |
| 10 | File STEP dari Modul 08 | Part konveyor |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 13 untuk:
- Anatomi mesin CNC router dan komponen
- Jenis cutting tool dan fungsinya
- Parameter feeds & speeds + rumus
- Workflow CAM di Fusion 360
- G-code dasar untuk CNC router

---

## IV. Langkah Percobaan

### Bagian A: Setup Fusion 360
| No | Langkah | Detail |
|----|---------|--------|
| 1 | Import STEP | File → Open → .STEP bearing block |
| 2 | MANUFACTURE workspace | Switch dari DESIGN |
| 3 | New Setup | WCS origin: top-left corner, Z top of stock |
| 4 | Stock definition | Fixed Size Box, ketebalan sesuai MDF |

### Bagian B: Toolpath Part Konveyor
| No | Operasi | Tool | Keterangan |
|----|---------|------|------------|
| 5 | Face | 6mm flat | Ratakan permukaan, 0.5mm depth |
| 6 | 2D Pocket — bearing | 6mm flat → 3mm flat | Pocket untuk bearing, DOC 3mm |
| 7 | 2D Contour + Tabs | 6mm flat | Profil luar, 4 tabs per part |
| 8 | Drill — lubang baut | 3mm/5mm drill | Peck drilling |
| 9 | (Ulangi 5–8 untuk part lain) | — | Motor mount, side plate |

### Bagian C: Ukiran Nama
| No | Langkah | Detail |
|----|---------|--------|
| 10 | Sketch Text | Tulis nama + NIM di permukaan stock |
| 11 | Explode Text | Klik kanan → Explode Text |
| 12 | Engrave toolpath | V-bit 60°, depth 0.5–1mm, feed 800 |
| 13 | Preview | Cek kualitas tulisan di simulasi |

### Bagian D: Simulasi & Post-Process
| No | Langkah | Detail |
|----|---------|--------|
| 14 | Simulate semua toolpath | Cek collision, gouging, remaining stock |
| 15 | Post-process | GRBL post-processor → export .nc |
| 16 | Review G-code | Buka di text editor, cek header |

### Bagian E: Eksekusi CNC
| No | Langkah | Detail |
|----|---------|--------|
| 17 | Setup mesin | Pasang material, clamp, end mill |
| 18 | Set origin | Jog → X0 Y0 Z0 (paper test untuk Z) |
| 19 | Dry run | Jalankan tanpa spindle → cek movement |
| 20 | Execute | Spindle ON → jalankan program |
| 21 | Monitor | JANGAN tinggalkan mesin |
| 22 | Finishing | Lepas tabs, amplas tepi |
| 23 | Pengukuran | Dimensi aktual vs CAD (jangka sorong) |

---

## V. Analisa dan Pembahasan
1. Bandingkan dimensi part CNC vs desain CAD — berapa deviasi? Apa penyebabnya?
2. Evaluasi kualitas permukaan pocket vs contour — mana yang lebih halus? Mengapa?
3. Apakah ukiran nama terbaca jelas? Apa yang menentukan kualitas V-carving?
4. Jelaskan fungsi tabs dan apa yang terjadi jika tidak menggunakan tabs
5. Bandingkan estimasi waktu Fusion 360 vs waktu aktual machining
6. Diskusikan feeds & speeds — apa yang terjadi jika feed terlalu cepat vs terlalu lambat?
7. Identifikasi masalah selama proses CNC dan solusi yang diterapkan

---

## VI. Kesimpulan
Rangkum proses dari STEP → Fusion 360 CAM → G-code → CNC Router → Part fisik:
- Pembelajaran utama tentang CNC machining
- Pentingnya simulasi sebelum eksekusi
- Evaluasi kualitas part yang dihasilkan

---

## VII. Tugas

### Video (10–15 menit):
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Setup CAM | 3–4 menit | Import STEP, setup, toolpath di Fusion 360 |
| 2. Simulasi | 1–2 menit | Preview simulasi, identifikasi masalah |
| 3. Eksekusi CNC | 3–5 menit | Rekaman proses milling + engraving |
| 4. Hasil & Analisa | 2–3 menit | Part jadi, pengukuran, evaluasi kualitas |

### Pengumpulan:
```
NIM_Nama_Modul13/
├── Fusion360/
│   ├── Project_file (.f3d)
│   ├── Screenshot_setup/
│   ├── Screenshot_toolpath/
│   └── Screenshot_simulasi/
├── Gcode/ (.nc files)
├── Foto/
│   ├── Setup_mesin.jpg
│   ├── Proses_milling.jpg
│   ├── Part_hasil.jpg
│   ├── Ukiran_nama.jpg
│   └── Pengukuran.jpg
├── Pengukuran/
│   └── Tabel_dimensi_CAD_vs_aktual.xlsx
├── Video/ (NIM_Nama_Modul13.mp4)
└── Laporan.pdf
```
Kompres → `NIM_Nama_Modul13.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 13*
