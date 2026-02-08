# PROJECT MODUL 13: PAPAN NAMA MEJA 3D — CNC Router Milling

## Praktikum CAD/CAM — Pertemuan 13

---

## Deskripsi Project
Desain dan fabrikasi **Papan Nama Meja (Desk Nameplate) 3D** menggunakan CNC Router. Project ini menggabungkan seluruh 10 percobaan: face milling permukaan rata, kontur luar bentuk profil, pocket untuk relief, drilling lubang mounting, engraving teks nama/logo, dan finishing 3D untuk permukaan sculpted.

---

## Spesifikasi Teknis

| Parameter | Nilai |
|-----------|-------|
| Material | MDF/Kayu 18-20 mm |
| Dimensi Stock | 200 × 100 × 20 mm |
| Profil Luar | Kontur custom (bukan kotak biasa) |
| Pocket Teks | Kedalaman 3-5 mm |
| Engraving | Nama + NIM + Logo Prodi |
| Lubang Mounting | 2× Ø5 mm (untuk baut/stand) |
| Relief 3D | Pola dekoratif sculpted |
| Finishing | Amplas + cat/pernis |

---

## Workflow

### Tahap 1 — SolidWorks (Desain)
1. Buat Part baru → dimensi 200×100×20 mm
2. Sketch profil luar (bisa lengkung, chamfer, fillet)
3. Sketch pocket area untuk teks
4. Sketch relief/pola 3D (menggunakan Loft/Freeform/Sculpt jika perlu)
5. Sketch posisi lubang mounting
6. Tambah teks (nama, NIM, logo) menggunakan Sketch Text / Wrap
7. Simpan sebagai .SLDPRT dan ekspor .STEP

### Tahap 2 — Fusion 360 CAM
1. Import STEP → CAM Setup (stock 200×100×20)
2. WCS origin di pojok kiri depan atas

**Operasi CAM (urut):**

| No | Operasi | Tool | Detail |
|----|---------|------|--------|
| 1 | Face | End Mill Ø10mm | Ratakan permukaan atas, DOC 1mm |
| 2 | 2D Contour | End Mill Ø6mm | Profil luar, tabs 3-4 buah |
| 3 | 2D Pocket | End Mill Ø6mm | Area pocket teks, depth 3-5mm |
| 4 | Engraving | V-bit 60° | Teks nama + NIM + logo |
| 5 | Drilling | Drill Ø5mm | 2× lubang mounting |
| 6 | 3D Adaptive | End Mill Ø6mm | Roughing relief 3D |
| 7 | 3D Contour/Parallel | Ball End Ø6mm | Finishing relief 3D, stepover 0.3mm |

3. Simulate semua toolpath → cek collision
4. Post Process → G-code (.nc / .gcode)

### Tahap 3 — Eksekusi CNC Router
1. Pasang material MDF/Kayu di meja CNC
2. Clamp dengan benar (hindari area kerja)
3. Set Work Zero (X, Y, Z) → probe Z jika tersedia
4. Load G-code → jalankan per operasi
5. Monitor proses (speed, feed, suara)
6. Lepas tabs, amplas, finishing

---

## Deliverables
| No | Item | Format |
|----|------|--------|
| 1 | File SolidWorks (.SLDPRT) | Digital |
| 2 | File STEP (.step) | Digital |
| 3 | File Fusion 360 (.f3d) | Digital |
| 4 | G-code (.nc/.gcode) | Digital |
| 5 | Foto setup CNC + hasil | JPG/PNG |
| 6 | Video proses CNC (HP) | MP4 |
| 7 | Produk fisik papan nama | Fisik |

---

## Kriteria Penilaian (Lihat Rubrik Penilaian Project — Modul 01)
- Pemahaman konsep CAM workflow (25%)
- Kualitas desain dan estetika papan nama (25%)
- Kompleksitas operasi CAM (20%)
- Kelengkapan deliverables (15%)
- Feasibility dan hasil eksekusi (15%)

---

## Tips
- Gunakan **tabs** pada kontur luar agar part tidak terlepas
- Pastikan **urutan operasi** benar: face → pocket → drill → engrave → 3D → contour
- Lakukan **air cut** (tanpa material) dulu jika ragu
- Perhatikan **arah serat kayu** untuk hasil finishing yang baik
- Dokumentasikan setiap tahap dengan foto/video

---

*Project Praktikum CAD/CAM — Modul 13*
