# PROJECT MODUL 14: DISPLAY PRODUK AKRILIK — Laser Cut + Bending + Assembly

## Praktikum CAD/CAM — Pertemuan 14

---

## Deskripsi Project
Desain dan fabrikasi **Display Produk Akrilik** yang fungsional dan estetis menggunakan workflow lengkap: SolidWorks Sheet Metal → DXF Export → CorelDRAW → Laser Cutting → Scoring → Bending → Tab-Slot Assembly + Lem Akrilik.

Project ini menggabungkan **seluruh 10 percobaan**: sheet metal design, DXF multi-layer, bend allowance, multi-bend, tab-slot joint, scoring, bending, jig, dan eksekusi lengkap.

---

## Spesifikasi Teknis

| Parameter | Nilai |
|-----------|-------|
| Material | Akrilik Cast 3mm (Clear / Warna pilihan) |
| Dimensi keseluruhan | ~150 × 100 × 120 mm (P×L×T) |
| Jumlah part minimum | 3 part |
| Jumlah bend minimum | 2 bend |
| Jumlah tab-slot joint minimum | 4 joint |
| Teknik scoring | Wajib (bend line marking) |
| Engraving | Nama + NIM + Logo (opsional) |
| Finishing | Bersih, transparan, presisi |

---

## Opsi Desain (Pilih Salah Satu atau Modifikasi)

### Opsi A: Phone/Tablet Stand
- 2–3 part, 2 bend pada body utama
- Side support dengan tab-slot
- Lip penahan di depan

### Opsi B: Business Card Holder
- 3 part, 2 bend pada holder
- Base dengan tab-slot
- Kompartemen kartu nama

### Opsi C: Cosmetic/Stationery Organizer
- 4–5 part, 2–3 bend
- Multiple kompartemen
- Tiered display (bertingkat)

### Opsi D: Mini Display Shelf
- 3–4 part, 3 bend
- 2 tingkat/rak
- Side panel + back panel

### Opsi E: Custom Design
- Desain bebas sesuai kreativitas
- Harus memenuhi spesifikasi minimum di atas

---

## Workflow

### Tahap 1 — SolidWorks (Desain)
1. Tentukan konsep dan sketsa kasar (di kertas)
2. Buat setiap part sebagai **Sheet Metal** (untuk part yang di-bend) atau **Normal Part** (flat)
3. Parameter sheet metal: T=3mm, R=5mm, K=0.35
4. Tambahkan tab dan slot pada joint interface
5. Toleransi slot: +0.15–0.20mm dari ketebalan
6. Buat **Assembly** → verifikasi fit dan clearance
7. **Flatten** semua sheet metal part
8. Eksport DXF per part (include bend lines)

### Tahap 2 — CorelDRAW (Layout)
1. Import semua DXF
2. Pisahkan layer:
   - CUT (Merah) — kontur potong
   - ENGRAVE_BEND (Hijau) — bend line scoring
   - ENGRAVE_TEXT (Kuning) — teks/logo
3. Set semua outline ke hairline
4. Nesting optimal di sheet akrilik (hemat material)
5. Atur urutan: Engrave → Internal Cut → External Cut

### Tahap 3 — Laser Cutting
1. Setup mesin laser, fokus, origin
2. Load file → set parameter per layer
3. **Eksekusi** (rekam dengan HP):
   - Scoring bend lines
   - Engraving teks
   - Internal cutting (lubang, slot)
   - External contour cutting
4. Lepas part → bersihkan edge → lepas film pelindung (di area bend)

### Tahap 4 — Bending
1. Setup strip heater / heat gun
2. **Eksekusi per bend** (rekam dengan HP):
   - Posisikan di strip heater (bend line tepat di atas elemen)
   - Panaskan (3–4 menit untuk 3mm, bolak-balik)
   - Bend di jig → tahan 2–3 menit
   - Cek sudut dengan protractor
3. Ulangi untuk semua bend

### Tahap 5 — Assembly & Finishing
1. Dry fit (tanpa lem) → verifikasi semua part fit
2. Aplikasikan lem akrilik:
   - Posisikan → syringe → lem mengalir kapiler
   - Tahan dengan tape/jig → 5 menit initial set
3. Curing 24 jam untuk kekuatan penuh
4. Bersihkan sisa lem, poles jika perlu
5. Quality check → foto dokumentasi

---

## Deliverables
| No | Item | Format |
|----|------|--------|
| 1 | File SolidWorks (semua part + assembly) | .SLDPRT / .SLDASM |
| 2 | File DXF (flat pattern per part) | .DXF |
| 3 | File CorelDRAW (layout nesting) | .CDR |
| 4 | Perhitungan bend allowance | Tabel di laporan |
| 5 | Foto proses (laser, bending, assembly) | JPG/PNG |
| 6 | Video proses (rekaman HP) | MP4 |
| 7 | **Produk fisik display akrilik** | **Fisik** |

---

## Kriteria Penilaian (Lihat Rubrik Penilaian Project — Modul 01)
- **Pemahaman konsep** (25%): Sheet metal, bend allowance, DFB rules, workflow
- **Kualitas desain** (25%): Estetika, proporsi, fungsionalitas display
- **Kompleksitas** (20%): Jumlah part, bend, joint, teknik gabungan
- **Kelengkapan** (15%): Semua deliverables lengkap dan rapi
- **Feasibility & Hasil** (15%): Produk jadi, presisi, kekuatan, finishing

---

## Tips
- Gunakan **cast acrylic** (bukan extruded) untuk menghindari crack saat bending
- Lepaskan **film pelindung** hanya di area bend, sisanya tetap terpasang sampai selesai
- Lakukan **test piece** dulu sebelum memotong part final
- Buat **jig bending** untuk presisi dan repeatability
- Urutan bending: **dalam ke luar** (bend yang paling sulit diakses duluan)
- Lem akrilik menggunakan **syringe** → hasil lebih rapi dan presisi
- **Jangan terburu-buru** saat bending — pemanasan merata = kunci kualitas
- Dokumentasikan **setiap tahap** dengan foto dan video

---

*Project Praktikum CAD/CAM — Modul 14*
