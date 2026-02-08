# PROJECT MODUL 9: ROBOT BERODA FLAT-PACK AKRILIK — SIAP LASER CUT

## Deskripsi
Finalisasi desain robot beroda flat-pack dan buat **design package siap produksi** yang akan direalisasikan di **Modul 10 (Laser Cutting)**.

Seluruh bodi robot dibuat dari panel-panel akrilik 2D yang disusun menjadi struktur 3D (bentuk balok/kubus) menggunakan interlocking tab-slot.

---

## Konsep Kunci
- **Bodi = balok akrilik** dari panel 2D yang dirakit jadi 3D
- **Semua part = flat** → bisa laser cut dari 1 sheet akrilik
- **Engraving nama** pada panel top/front/side
- **Realisasi di Modul 10** — laser cut + engrave + assembly

---

## Deliverables

### 1. File CAD
| Item | Qty Min | Format |
|------|---------|--------|
| Part files — semua panel | 10+ unique parts | .sldprt |
| Assembly file — robot terakit | 1 | .sldasm |

### 2. Manufacturing Files
| Item | Format | Untuk |
|------|--------|-------|
| DXF semua panel (multi-layer: cut + engrave) | .dxf | Laser Cut (Modul 10) |
| CorelDRAW nesting layout (semua part di 1 sheet) | .cdr | Laser Cut (Modul 10) |

### 3. Dokumentasi
| Item | Format |
|------|--------|
| Exploded View | Di assembly / drawing |
| BOM dengan qty, material, sumber, proses | Excel / PDF |
| Assembly Sequence (urutan rakit) | Dokumen / diagram |
| Drawing Package (assembly + 3 part detail) | .slddrw / .pdf |
| Nesting Layout (semua muat di sheet akrilik) | .cdr / screenshot |

### 4. Engraving Content
| Item | Posisi | Jenis Engrave |
|------|--------|---------------|
| Nama Mahasiswa | Top / Front panel | Raster engrave (hitam) |
| NIM | Top / Front panel | Raster engrave (hitam) |
| "ROBOT BERODA" | Top panel | Raster engrave (hitam) |
| Logo/motif (opsional) | Top / Side panel | Vektor engrave (biru) |

---

## Spesifikasi Minimum
- Bodi bentuk **balok/kubus** dari panel akrilik 3mm
- Minimal **10 panel** (6 sisi + internal supports)
- Semua panel menggunakan **interlocking tab-slot**
- Slot toleransi: material thickness + 0.15mm
- **Engraving nama** wajib pada minimal 1 panel
- Semua part **muat di 1 sheet** akrilik (max 400×600mm)
- Komponen: 2× motor + 2× wheel + 1× castor + Arduino

---

## Kriteria Penilaian
| Kriteria | Bobot |
|----------|-------|
| Kelengkapan desain panel (10+ part) | 20% |
| Fungsionalitas mekanik (tab-slot fit, clearance) | 20% |
| Assembly benar (semua panel terhubung) | 15% |
| Design for Manufacturing (laser cut ready) | 15% |
| Nesting layout efisien | 15% |
| Engraving nama + estetika | 15% |

---

*Project Praktikum CAD/CAM — Modul 9*
