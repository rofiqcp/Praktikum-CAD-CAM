# JOBSHEET MODUL 14: CAM — LASER CUTTING AKRILIK + THERMAL BENDING

## Praktikum CAD/CAM — Pertemuan 14

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mendesain casing box akrilik dengan tab-slot interlocking
2. Mahasiswa mampu menggunakan fitur Sheet Metal SolidWorks untuk desain casing melengkung
3. Mahasiswa mampu melakukan Flatten dan export DXF dari Sheet Metal part
4. Mahasiswa mampu mengatur layer scoring dan cutting di CorelDRAW
5. Mahasiswa mampu melakukan laser cutting dan scoring pada akrilik
6. Mahasiswa mampu melakukan **thermal bending** akrilik menggunakan pemanas untuk membuat casing melengkung

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + SolidWorks | Sheet Metal design |
| 2 | CorelDRAW | Layout DXF, layer management |
| 3 | Mesin Laser Cutter CO2 | Potong + scoring akrilik |
| 4 | Akrilik Cast 3mm | Material utama |
| 5 | Heat Gun / Strip Heater | Thermal bending |
| 6 | Sarung tangan tahan panas | Safety bending |
| 7 | Jig / cetakan kurva | Dari MDF/kayu |
| 8 | Lem akrilik (solvent cement) | Assembly casing box |
| 9 | Jangka sorong | Pengukuran |
| 10 | Safety glasses, mask | Laser + bending safety |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 14 untuk:
- Konsep casing box flat-pack dan tab-slot
- Sheet Metal → Flatten → DXF workflow
- Teknik scoring untuk bend lines
- Prinsip thermal bending akrilik (kurva, bukan satu titik)
- Perbedaan bending akrilik vs bending sheet metal
- Troubleshooting dan safety

---

## IV. Langkah Percobaan

### Bagian A: Desain Casing Box
| No | Langkah | Detail |
|----|---------|--------|
| 1 | Desain 3D casing box | SolidWorks, dimensi 100×80×60mm |
| 2 | Buat panel terpisah | 6 panel (top, bottom, 4 sides) |
| 3 | Tambahkan tab-slot | Tab 10mm, slot 3.1mm (clearance 0.1mm) |
| 4 | Export DXF setiap panel | Save As → DXF |
| 5 | Nesting di CorelDRAW | Merah = cut, hijau = engrave |

### Bagian B: Desain Casing Melengkung (Sheet Metal)
| No | Langkah | Detail |
|----|---------|--------|
| 6 | Sheet Metal Base Flange | Thickness 3mm, bend radius 20mm |
| 7 | Desain curved profile | Profil samping dengan arc/spline |
| 8 | Edge Flange / fitur tambahan | Tepi, lubang ventilasi, dll. |
| 9 | **Flatten** | Klik Flatten → flat pattern 2D |
| 10 | Export DXF flat pattern | Termasuk bend lines |

### Bagian C: Layout & Laser
| No | Langkah | Detail |
|----|---------|--------|
| 11 | Import DXF ke CorelDRAW | Flat pattern + casing box panels |
| 12 | Assign warna layer | Merah=cut, Biru=scoring, Hijau=engrave |
| 13 | Setup laser cutter | Focus, air assist, parameter per layer |
| 14 | Engrave dulu (jika ada) | Power 20–30%, speed 300 mm/s |
| 15 | Scoring bend lines | Power 15–25%, speed 30–50 mm/s |
| 16 | Cutting kontur | Power 70–90%, speed 8–15 mm/s |

### Bagian D: Assembly Casing Box
| No | Langkah | Detail |
|----|---------|--------|
| 17 | Rakit panel casing box | Tab-slot → press fit |
| 18 | Lem jika perlu | Solvent cement pada sambungan |
| 19 | Evaluasi | Cek alignment, gap, kekuatan |

### Bagian E: Thermal Bending ⭐
| No | Langkah | Detail |
|----|---------|--------|
| 20 | **Test bending** pada sisa akrilik | Latihan sebelum part final! |
| 21 | Siapkan jig kurva | Profil sesuai desain, dari MDF/kayu |
| 22 | Panaskan bend area | Heat gun, jarak 10–15cm, gerak merata |
| 23 | Test fleksibilitas | Tekan perlahan — sudah lentur? |
| 24 | **Bengkokkan pada jig** | Perlahan, ikuti kurva, hold 30 detik |
| 25 | Dinginkan & lepas | Periksa bentuk vs desain |
| 26 | Assembly casing melengkung | Pasang base + side panels |

---

## V. Analisa dan Pembahasan
1. Bandingkan dimensi casing box aktual vs desain — apakah tab-slot fit?
2. Jelaskan proses Flatten di SolidWorks — apa peran bend radius dan bend allowance?
3. Bandingkan parameter scoring vs cutting — mengapa power scoring harus jauh lebih rendah?
4. Evaluasi hasil thermal bending — apakah kurva sesuai desain? Apakah smooth?
5. Apa perbedaan mendasar antara bending sheet metal (logam) dan thermal bending akrilik?
6. Jelaskan pentingnya jig dalam thermal bending — apa yang terjadi tanpa jig?
7. Diskusikan test bending pada sisa akrilik — parameter apa yang perlu diubah?
8. Identifikasi masalah dan solusi selama proses keseluruhan

---

## VI. Kesimpulan
Rangkum seluruh proses:
- Sheet Metal 3D → Flatten → DXF → Laser (Cut + Score) → Thermal Bending → Casing 3D
- Pembelajaran utama tentang transformasi 3D → 2D → 3D
- Perbandingan teknik manufaktur: laser cutting, bending, assembly

---

## VII. Tugas

### Video (10–15 menit):
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Desain Sheet Metal | 2–3 menit | Demo flatten, export DXF |
| 2. CorelDRAW Layout | 1–2 menit | Layer scoring + cutting |
| 3. Laser Cutting | 2–3 menit | Rekaman proses potong + scoring |
| 4. Assembly Casing Box | 1–2 menit | Rakit tab-slot |
| 5. **Thermal Bending** | 3–4 menit | **Proses bending + hasil** |
| 6. Analisa & Kesimpulan | 2–3 menit | Evaluasi kualitas, review praktikum |

### Pengumpulan:
```
NIM_Nama_Modul14/
├── SolidWorks/
│   ├── CasingBox/ (.sldprt per panel)
│   └── CasingMelengkung/ (.sldprt sheet metal)
├── DXF/ (semua flat pattern + panel)
├── CorelDRAW/ (.cdr layout)
├── Foto/
│   ├── LaserCutting_proses.jpg
│   ├── Scoring_detail.jpg
│   ├── CasingBox_assembly.jpg
│   ├── Bending_proses.jpg
│   ├── Bending_hasil.jpg
│   └── CasingMelengkung_final.jpg
├── Video/ (NIM_Nama_Modul14.mp4)
└── Laporan.pdf
```
Kompres → `NIM_Nama_Modul14.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 14*
