# PROJECT MODUL 11: ROBOT LENGAN 3-DOF (SG90)

## Deskripsi
Desain robot lengan sederhana 3-DOF menggunakan servo SG90 — seluruh part dirancang untuk realisasi melalui **3D printing** di Modul 12. Termasuk desain **huruf timbul** (embossed text) sebagai name plate 3D print.

---

## Koneksi Antar Modul
| Dari Modul 11 | Ke Modul 12 (CAM 3D Printing) |
|---------------|-------------------------------|
| STL semua part robot | 3D print PLA semua bracket & link |
| STL huruf timbul | 3D print multi-color / emboss |
| Slicer parameter preset | Langsung print di mesin FDM |

---

## Spesifikasi Project

### Robot Lengan 3-DOF
| Parameter | Spesifikasi |
|-----------|-------------|
| DOF | 3 (Base Rotation + Shoulder + Elbow) |
| Servo | SG90 × 3 unit |
| Bahan Part | PLA filament (3D print) |
| Reach | ≥ 15 cm |
| End-effector | Gripper sederhana (manual/servo) |

### Huruf Timbul
| Parameter | Spesifikasi |
|-----------|-------------|
| Isi Teks | Nama + NIM mahasiswa |
| Tinggi huruf | ≥ 5 mm |
| Ketebalan emboss | 1.0–2.0 mm |
| Base plate | 80 × 30 mm minimum |

---

## Part List (Minimum)
| No | Nama Part | Fungsi | Teknik CAD | Export |
|----|-----------|--------|------------|--------|
| 1 | Base Plate | Alas + penahan servo base | Extrude, CutExtrude | STL |
| 2 | Turntable | Rotasi base | Revolve, CutExtrude | STL |
| 3 | Shoulder Bracket | Dudukan servo shoulder (U-shape) | Extrude, Pocket | STL |
| 4 | Upper Arm Link | Penghubung shoulder-elbow | Extrude, Fillet | STL |
| 5 | Elbow Bracket | Dudukan servo elbow | Extrude, Pocket | STL |
| 6 | Forearm Link | Penghubung elbow-gripper | Extrude, Fillet | STL |
| 7 | Gripper / End-effector | Pencengkeram | Extrude, Assembly | STL |
| 8 | Servo Horn Adapter (×3) | Koneksi servo → part | Extrude, toleransi | STL |
| 9 | Name Plate (Huruf Timbul) | Identitas mahasiswa | Text + Boss Extrude | STL |

---

## Deliverables

### File Digital
- [ ] SolidWorks files (.sldprt + .sldasm)
- [ ] STL semua part (≥9 file)
- [ ] Drawing: exploded view + BOM (.slddrw/.pdf)
- [ ] Screenshot slicer: orientasi + parameter + estimasi waktu
- [ ] BOM lengkap dengan dimensi per part

### Dokumentasi Video (10–15 menit)
- [ ] Penjelasan konsep 3-DOF dan pilihan SG90
- [ ] Screen recording proses desain minimum 3 part kunci
- [ ] Demo huruf timbul (text → sketch → boss extrude)
- [ ] Demo assembly + motion study
- [ ] Demo slicer: orientasi, support, parameter
- [ ] Analisa: DfAM, toleransi, estimasi

---

## Rubrik Penilaian
| Aspek | Bobot | Kriteria |
|-------|-------|----------|
| Kelengkapan Part | 25% | ≥9 part, semua fungsional, SG90 fit |
| DfAM & Toleransi | 20% | Wall ≥1.2mm, pocket clearance 0.2mm, no overhang >45° tanpa support |
| Huruf Timbul | 15% | Text jelas, emboss ≥1mm, bisa diprint |
| Assembly & Motion | 15% | Hinge mate dengan limit, motion study berjalan |
| STL Export & Slicer Prep | 10% | Orientasi benar, estimasi realistis |
| Video & Dokumentasi | 15% | Jelas, runtut, analisa mendalam |

---

## Catatan Penting
- **Semua dimensi servo pocket** harus mengacu datasheet SG90 (22.2 × 11.8 × 25.4 mm) **+ clearance 0.2mm per sisi**
- **Toleransi servo horn adapter** sangat krusial — terlalu ketat akan pecah saat print, terlalu longgar akan wobble
- **Jangan gunakan chamfer tajam** pada bagian yang kontak dengan bed — gunakan fillet atau elephant foot compensation
- **STL harus watertight** — cek di SolidWorks (Tools → Check) sebelum export
- Part ini akan **dicetak nyata di Modul 12** — desain harus realistis dan printable

---

*Project Praktikum CAD/CAM — Modul 11*
