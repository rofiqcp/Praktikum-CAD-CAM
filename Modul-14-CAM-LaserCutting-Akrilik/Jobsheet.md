# JOBSHEET MODUL 14: CAM LASER CUTTING — SHEET METAL & BENDING AKRILIK

## Praktikum CAD/CAM — Pertemuan 14

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mendesain sheet metal di SolidWorks untuk fabrikasi akrilik
2. Mahasiswa mampu mengekspor DXF multi-layer (cut, engrave, bend line)
3. Mahasiswa mampu menghitung bend allowance untuk akrilik
4. Mahasiswa mampu melakukan scoring/engraving bend line dengan laser
5. Mahasiswa mampu melakukan bending akrilik menggunakan strip heater
6. Mahasiswa mampu mendesain dan memfabrikasi jig bending
7. Mahasiswa mampu melakukan assembly produk akrilik (tab-slot + lem)
8. Mahasiswa mampu mengeksekusi workflow lengkap: desain → laser → bending → assembly

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + SolidWorks + CorelDRAW | Software |
| 2 | Mesin Laser CO₂ | Di lab |
| 3 | Strip Heater / Line Bender | Bending akrilik |
| 4 | Infrared Thermometer | Cek suhu |
| 5 | Akrilik Cast 3mm (Clear/Warna) | Material utama |
| 6 | MDF 6mm | Material jig |
| 7 | Lem akrilik (Acrifix/Weld-On) | Joining |
| 8 | Syringe/applicator bottle | Aplikasi lem |
| 9 | Jangka sorong / Protractor | Pengukuran |
| 10 | Sarung tangan tahan panas | Keselamatan |
| 11 | Kacamata pelindung + Masker | Keselamatan |
| 12 | HP/Smartphone | Rekaman |

---

## III. Landasan Teori
Lihat **Materi.md — Modul 14** untuk pembahasan lengkap tentang:
- Sheet metal design untuk akrilik
- Flat pattern & DXF export multi-layer
- Sifat material akrilik (PMMA)
- Teknik bending akrilik (strip heater, heat gun, oven)
- Desain untuk bending (DFB)
- Jig dan fixture bending
- Teknik joining akrilik

---

## IV. Percobaan

| No | Percobaan | Software/Alat | Estimasi Waktu |
|----|-----------|---------------|----------------|
| 1 | Sheet Metal Akrilik — Base & Edge Flange | SolidWorks | 20 menit |
| 2 | DXF Export Multi-Layer dengan Bend Lines | SolidWorks + CorelDRAW | 20 menit |
| 3 | Perhitungan Bend Allowance Akrilik | SolidWorks + Manual | 15 menit |
| 4 | Desain Tray Akrilik (Multi-Bend) | SolidWorks | 25 menit |
| 5 | Desain Phone Stand (Bend + Tab-Slot) | SolidWorks | 30 menit |
| 6 | Scoring / V-Groove Bend Line dengan Laser | Laser + Akrilik | 25 menit |
| 7 | Bending Akrilik dengan Strip Heater | Strip Heater | 30 menit |
| 8 | Desain & Laser Cut Jig Bending | SolidWorks + Laser | 30 menit |
| 9 | Desain Produk: Display Stand Akrilik | SolidWorks | 30 menit |
| 10 | Eksekusi Lengkap: Laser + Bending + Assembly | Laser + Heater + Lem | 45 menit |

Lihat **Materi.md — Bagian 10 (Percobaan 1–10)** untuk langkah-langkah detail setiap percobaan.

---

## V. Analisa
Jawab pertanyaan berikut berdasarkan hasil percobaan:

1. Bandingkan nilai bend allowance perhitungan manual dengan SolidWorks. Mengapa bisa berbeda?
2. Bagaimana pengaruh kedalaman scoring terhadap kemudahan bending dan kekuatan part?
3. Berapa kedalaman scoring optimal untuk akrilik 3mm? Jelaskan alasannya.
4. Apa perbedaan hasil bending dengan jig vs tanpa jig? (Presisi sudut, repeatability)
5. Bagaimana pengaruh waktu pemanasan terhadap kualitas bend? (Kurang panas vs cukup vs berlebih)
6. Jelaskan pentingnya urutan bending pada part dengan multiple bends.
7. Bandingkan kekuatan joint tab-slot (tanpa lem) vs tab-slot + lem akrilik.
8. Apa perbedaan cast acrylic vs extruded acrylic untuk bending?
9. Jelaskan pengaruh arah scoring (sisi dalam vs sisi luar bend) terhadap hasil bend.
10. Berapa toleransi yang tepat untuk tab-slot joint pada akrilik 3mm? Mengapa?

---

## VI. Kesimpulan
Tuliskan kesimpulan berdasarkan:
1. Workflow sheet metal → DXF → laser cut → bending → assembly
2. Parameter optimal scoring dan bending untuk akrilik 3mm
3. Pentingnya jig dalam menjaga presisi dan repeatability
4. Teknik joining yang paling efektif (tab-slot + lem)
5. Tantangan dan solusi yang ditemukan selama praktikum

---

## VII. Tugas Video (15–20 Menit)

### Konten Video:
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Penjelasan Materi | 3–4 menit | Sheet metal untuk akrilik, DFB rules, bend allowance |
| 2. Demo SolidWorks | 4–5 menit | Screen record: desain sheet metal + flat pattern + DXF export |
| 3. Demo CorelDRAW | 2–3 menit | Screen record: layout multi-layer, nesting |
| 4. **Eksekusi Laser** | 3–4 menit | **Rekaman HP**: scoring + cutting akrilik |
| 5. **Eksekusi Bending** | 3–4 menit | **Rekaman HP**: strip heater + bending + assembly |
| 6. Analisa & Kesimpulan | 2–3 menit | Pembahasan hasil, quality check |

### Format Video:
- Resolusi minimum: 720p (1280×720)
- Audio: Narasi jelas sepanjang video
- Screen record: OBS Studio / screen recorder lainnya
- **HP record: Wajib untuk proses laser cutting dan bending**
- Tunjukkan produk akhir dari semua sisi

---

## VIII. Format Pengumpulan

### Struktur Folder:
```
NIM_Nama_Modul14/
├── SolidWorks/
│   ├── Percobaan1_SheetMetal.SLDPRT
│   ├── Percobaan4_Tray.SLDPRT
│   ├── Percobaan5_PhoneStand_A.SLDPRT
│   ├── Percobaan5_PhoneStand_B.SLDPRT
│   ├── Percobaan8_Jig_*.SLDPRT
│   ├── Percobaan9_DisplayStand_*.SLDPRT
│   └── Assembly_DisplayStand.SLDASM
├── DXF/
│   ├── FlatPattern_Tray.DXF
│   ├── FlatPattern_PhoneStand.DXF
│   ├── FlatPattern_Jig.DXF
│   └── FlatPattern_DisplayStand.DXF
├── CorelDRAW/
│   ├── Layout_Scoring_Test.CDR
│   ├── Layout_Jig.CDR
│   └── Layout_DisplayStand.CDR
├── Foto/
│   ├── Scoring_Results.jpg
│   ├── Bending_Process.jpg
│   ├── Jig_Assembly.jpg
│   └── Final_Product_*.jpg
├── Video/
│   └── NIM_Nama_Modul14.mp4
├── Laporan/
│   └── Jobsheet_Modul14.pdf
└── README.md
```

### Kompres dan upload: `NIM_Nama_Modul14.zip`

---

## IX. Rubrik Penilaian
Lihat **Rubrik Penilaian Video** dan **Rubrik Penilaian Project** di Modul 01 (berlaku untuk semua modul).

---

*Jobsheet Praktikum CAD/CAM — Modul 14*
