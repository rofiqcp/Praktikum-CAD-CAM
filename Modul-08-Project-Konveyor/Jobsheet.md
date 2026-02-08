# JOBSHEET MODUL 8: PROJECT CAD — DESAIN KONVEYOR BELT MINI

## Praktikum CAD/CAM — Pertemuan 8

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mengkonsep dan mendesain sistem konveyor belt mini lengkap
2. Mahasiswa mampu mengintegrasikan part dari berbagai teknik (extrude, revolve, assembly)
3. Mahasiswa mampu mendesain part sesuai proses manufaktur target (laser cut, CNC milling)
4. Mahasiswa mampu membuat BOM, exploded view, dan gambar teknik assembly
5. Mahasiswa mampu mengeksport file dalam format yang sesuai (DXF, STEP, STL)

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + SolidWorks | Semua modul |
| 2 | Datasheet NEMA 17 | Dimensi mounting motor |
| 3 | Datasheet Bearing 608ZZ | Dimensi bearing |
| 4 | Katalog profil aluminium 2020/2040 | Dimensi cross-section |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 8 untuk:
- Konsep konveyor belt dan parameter desain
- Spesifikasi NEMA 17 dan dimensi mounting
- Part akrilik (laser cut) dan part milling (CNC router)
- Sistem transmisi dan roller
- Peta koneksi realisasi ke Modul 10, 13, dan 14

---

## IV. Langkah Percobaan
| No | Komponen | Teknik | Export |
|----|----------|--------|--------|
| 1 | Frame Samping (Profil Al 2040) | Extrude + Assembly | — |
| 2 | Cross Member, Legs & Rangka | Extrude + Assembly | — |
| 3 | End Plate Motor Side (Akrilik) | Extrude + Pattern | **DXF** |
| 4 | End Plate Idler Side (Akrilik) | Extrude + Slot | **DXF** |
| 5 | Bearing Housing (Akrilik stack) | Extrude + Config | **DXF** |
| 6 | Drive & Idler Roller | Revolve + Extrude | — |
| 7 | Motor Bracket NEMA 17 (Akrilik) | Extrude + Tab-Slot | **DXF** |
| 8 | Bearing Block (MDF — utk Milling) | Extrude + Pocket | **STEP** |
| 9 | Side Guide + Name Plate | Extrude + Text Wrap | **DXF + STEP** |
| 10 | Full Assembly + BOM + Drawing | Assembly + Exploded | — |

---

## V. Analisa dan Pembahasan
1. Jelaskan mengapa konveyor ini menggunakan kombinasi 3 proses manufaktur (laser, milling, beli). Apa kelebihan dan kekurangan masing-masing?
2. Hitung torsi yang dibutuhkan untuk menggerakkan belt dengan beban 500g. Apakah NEMA 17 cukup?
3. Jelaskan fungsi tensioning system pada idler roller dan mengapa menggunakan slot, bukan lubang bulat
4. Diskusikan toleransi yang diperlukan untuk bearing housing akrilik (press-fit 608ZZ)
5. Analisis kesesuaian part milling (bearing block) — mengapa tidak bisa dibuat dengan laser cut?
6. Jelaskan strategi export file: kapan gunakan DXF, kapan STEP, kapan STL?

---

## VI. Kesimpulan
Rangkum proses desain konveyor dari konsep → pemilihan komponen → desain CAD → DFM (Design for Manufacturing) → export file untuk fabrikasi.

---

## VII. Tugas

### Video (10–15 menit):
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Penjelasan Konsep | 3–4 menit | Konsep konveyor, komponen, NEMA 17 |
| 2. Demo SolidWorks | 5–7 menit | Screen record percobaan 1–10 (highlight) |
| 3. Analisa & Kesimpulan | 2–3 menit | Pembahasan DFM, export strategy |

### Pengumpulan:
```
NIM_Nama_Modul08/
├── SolidWorks/ (semua .sldprt + .sldasm)
├── DXF/ (semua part akrilik untuk laser cut)
├── STEP/ (semua part untuk CNC milling)
├── Drawing/ (.slddrw / .pdf)
├── Video/ (NIM_Nama_Modul08.mp4)
└── BOM.xlsx atau BOM.pdf
```
Kompres → `NIM_Nama_Modul08.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 8*
