# PROJECT MODUL 13: CAM — CNC ROUTER MILLING PART KONVEYOR + UKIRAN NAMA

## Deskripsi
Realisasi part-part konveyor dari Modul 08 menggunakan CNC router milling. Termasuk pembuatan **ukiran nama** (engraving) menggunakan V-bit pada material MDF/kayu.

---

## Koneksi Antar Modul
| Input (Modul 08) | Proses (Modul 13) | Output |
|-------------------|-------------------|--------|
| STEP Bearing Block | Pocket + Contour + Drill | Part fisik MDF |
| STEP Motor Mount | Pocket + Contour + Drill | Part fisik MDF |
| STEP Side Plate | Contour + Drill | Part fisik MDF |
| Teks Nama + NIM | V-bit Engrave | Ukiran nama |

---

## Spesifikasi Project

### CNC Router Part Konveyor
| Parameter | Spesifikasi |
|-----------|-------------|
| Material | MDF 18mm / kayu solid |
| Tools | 6mm flat, 3mm flat, V-bit 60°, drill 3mm & 5mm |
| Software CAM | Fusion 360 |
| Controller | GRBL |
| Toleransi target | ±0.3mm |

### Ukiran Nama
| Parameter | Spesifikasi |
|-----------|-------------|
| Tool | V-bit 60° |
| Kedalaman | 0.5–1.0mm |
| Isi | Nama + NIM mahasiswa |
| Ukuran huruf | Tinggi minimal 10mm |

---

## Part List
| No | Part | Operasi CAM | Tool |
|----|------|-------------|------|
| 1 | Bearing Block | Pocket + Contour + Drill | 6mm flat, 3mm flat, drill |
| 2 | Motor Mount Plate | Pocket + Contour + Drill | 6mm flat, drill |
| 3 | Side Plate | Contour + Drill | 6mm flat, drill |
| 4 | Ukiran Nama | Engrave | V-bit 60° |

---

## Deliverables

### Produk Fisik
- [ ] Part bearing block selesai di-milling (pocket akurat, lubang sesuai)
- [ ] Part motor mount plate selesai di-milling
- [ ] Part side plate selesai di-contour
- [ ] Ukiran nama — huruf terbaca jelas dan rapi
- [ ] Foto dokumentasi seluruh proses dan hasil

### File Digital
- [ ] Fusion 360 project file (.f3d)
- [ ] G-code semua operasi (.nc)
- [ ] Screenshot: setup, toolpath, simulasi per operasi
- [ ] Tabel pengukuran: dimensi CAD vs aktual (jangka sorong)
- [ ] Tabel feeds & speeds yang digunakan

### Dokumentasi Video (10–15 menit)
- [ ] Setup CAM di Fusion 360 (import, setup, toolpath)
- [ ] Simulasi toolpath (highlight engraving)
- [ ] Rekaman proses milling di mesin CNC
- [ ] Hasil part fisik + ukiran nama
- [ ] Analisa: dimensi, surface quality, troubleshooting

---

## Rubrik Penilaian
| Aspek | Bobot | Kriteria |
|-------|-------|----------|
| Setup & Toolpath | 20% | WCS benar, tools tepat, operasi lengkap |
| Simulasi & G-code | 15% | No collision/gouging, G-code valid |
| Kualitas Part Milling | 25% | Dimensi akurat (±0.3mm), surface halus |
| Ukiran Nama | 15% | Huruf jelas, V-carving rapi, depth konsisten |
| Safety & Prosedur | 10% | APD lengkap, prosedur diikuti, mesin terawat |
| Video & Analisa | 15% | Video jelas, analisa feeds/speeds & kualitas mendalam |

---

## Catatan Penting
- **SAFETY FIRST**: Kacamata, masker debu, dan ear protection WAJIB
- **Jangan tinggalkan mesin CNC** saat program berjalan — monitoring 100%
- **Cek clamp** sebelum mulai — material terbang = BAHAYA
- **Dry run dulu** sebelum spindle ON — pastikan gerakan benar
- **Tabs wajib** pada contour — potong tabs manual setelah selesai
- **Jangan potong terlalu dalam** — lindungi spoilboard (Z offset +0.3mm)
- **Simpan G-code** — jangan sampai hilang setelah post-process

---

*Project Praktikum CAD/CAM — Modul 13*
