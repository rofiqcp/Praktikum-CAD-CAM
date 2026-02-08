# PROJECT MODUL 12: CAM — 3D PRINTING ROBOT LENGAN + HURUF TIMBUL

## Deskripsi
Realisasi desain robot lengan 3-DOF dari Modul 11 menjadi objek fisik menggunakan 3D printer FDM. Termasuk pencetakan huruf timbul (embossed text) sebagai name plate.

---

## Koneksi Antar Modul
| Input (Modul 11) | Proses (Modul 12) | Output |
|-------------------|-------------------|--------|
| STL part robot | Slice + Print | Part fisik PLA |
| STL huruf timbul | Slice + Print (detail) | Name plate 3D |
| Assembly reference | Assembly fisik | Robot lengan jadi |

---

## Spesifikasi Project

### 3D Print Robot Lengan
| Parameter | Spesifikasi |
|-----------|-------------|
| Material | PLA 1.75mm |
| Nozzle | 0.4mm |
| Layer Height | 0.2mm (standar), 0.12mm (detail part) |
| Infill | 25–50% tergantung part |
| Servo | SG90 × 3 (assembly fisik) |

### 3D Print Huruf Timbul
| Parameter | Spesifikasi |
|-----------|-------------|
| Layer Height | 0.12–0.16mm |
| Orientasi | Text menghadap atas |
| Multi-color | Opsional (filament change) |

---

## Deliverables

### Produk Fisik
- [ ] Part robot lengan tercetak lengkap (≥9 part)
- [ ] Huruf timbul tercetak — nama dan NIM terbaca jelas
- [ ] Assembly robot lengan 3-DOF (servo terpasang, bisa digerakkan manual)
- [ ] Foto dokumentasi proses dan hasil

### File Digital
- [ ] G-code semua part
- [ ] Screenshot slicer (orientasi, parameter, preview per part)
- [ ] Tabel pengukuran: dimensi CAD vs aktual (jangka sorong)
- [ ] Estimasi vs aktual: waktu print dan filamen

### Dokumentasi Video (10–15 menit)
- [ ] Demo slicer: import, orientasi, parameter
- [ ] Rekaman/time-lapse proses print
- [ ] Post-processing dan test fit servo
- [ ] Assembly dan demo gerakan robot
- [ ] Analisa kualitas dan toleransi

---

## Rubrik Penilaian
| Aspek | Bobot | Kriteria |
|-------|-------|----------|
| Kualitas Print | 25% | Surface halus, dimensi akurat (±0.3mm), no defect besar |
| Parameter & Orientasi | 20% | Orientasi optimal, parameter sesuai fungsi part |
| Huruf Timbul | 15% | Huruf terbaca jelas, detail bagus |
| Assembly Robot | 15% | Semua part terpasang, servo fit, bisa gerak |
| Dokumentasi Print | 10% | Screenshot slicer lengkap, tabel pengukuran akurat |
| Video & Analisa | 15% | Video jelas, analisa mendalam (toleransi, troubleshooting) |

---

## Catatan Penting
- **Periksa STL watertight** sebelum import ke slicer — jika error, perbaiki di SolidWorks (Modul 11)
- **Monitor first 3 layers** — jika gagal adhesion, STOP dan re-level bed
- **Jangan tinggalkan printer tanpa pengawasan** — terutama saat print panjang
- **Siapkan filamen cadangan** — estimasi total usage sebelum mulai
- **Ukur dengan jangka sorong** setelah print — catat deviasi untuk laporan

---

*Project Praktikum CAD/CAM — Modul 12*
