# PROJECT MODUL 6: ASSEMBLY MEKANIK + FRAME ALUMINIUM

## Praktikum CAD/CAM — Pertemuan 6

---

## Project A: Mekanisme Press Tool Sederhana

### Deskripsi
Desain dan rakit **Press Tool sederhana** yang menggunakan semua jenis mate.

### Komponen:
1. Base Frame — Plat tebal sebagai alas
2. Guide Pillars (2x) — Silinder vertikal sebagai guide
3. Guide Bushings (2x) — Bushing di upper plate
4. Upper Plate — Plat bergerak naik-turun
5. Punch — Profil potong yang turun
6. Die — Cetakan di base
7. Stripper — Plat penekan material
8. Spring (4x) — Pegas penekan
9. Handle — Tuas untuk menggerakkan

### Deliverables Project A:
1. Semua part .sldprt (9 parts)
2. Assembly .sldasm dengan mate benar
3. Exploded View
4. Motion Study (Basic Motion)
5. BOM (Bill of Materials)

---

## Project B: Assembly Frame Aluminium dengan Komponen Lengkap

### Deskripsi
Rakit **frame workstation** dari profil aluminium dengan semua aksesoris standar menggunakan part yang sudah dibuat di modul sebelumnya.

### Komponen Assembly:
```
Frame Structure (dari Modul 5 atau buat baru):
- 4x Profil 4040 @ 1200mm (horizontal panjang)
- 4x Profil 4040 @ 800mm (horizontal pendek)
- 4x Profil 4040 @ 710mm (vertikal/kaki)

Connectors (dari Modul 4 atau buat baru):
- 8x Corner Bracket 4040 (untuk corner atas)
- 8x Corner Bracket 4040 (untuk corner bawah)
- 16x T-Nut M8 (2 per bracket)
- 16x Hex Bolt M8x16 (untuk bracket)

Accessories:
- 4x Adjustable Foot M10 (untuk kaki)
- 4x End Cap 4040 (untuk ujung atas vertikal)

Optional (bonus):
- 2x Gusset Plate 40 (penguat diagonal)
- 4x Handle Plastic (untuk pegangan)
```

### Teknik Assembly:
1. **Insert** profil aluminium pertama (fixed)
2. **Mate** profil kedua dengan Coincident + Parallel
3. **Pattern** untuk profil repetitif
4. **Insert** corner bracket, posisikan dengan Coincident ke T-slot
5. **Smart Fastener** atau manual insert untuk bolt & T-nut
6. **Limit Mate** untuk adjustable foot (range 0-20mm)
7. **Exploded View** dengan step configuration

### Deliverables Project B:
```
Parts (jika belum ada dari modul sebelumnya):
- Profil_4040.sldprt (atau gunakan dari M05)
- CornerBracket_4040.sldprt (atau gunakan dari M04)
- TNut_M8.sldprt
- HexBolt_M8x16.sldprt (atau dari Toolbox)
- AdjustableFoot_M10.sldprt
- EndCap_4040.sldprt

Assembly:
- M06_B_AluminiumFrame.sldasm
- M06_B_BOM.xlsx (exported Bill of Materials)

Views:
- Exploded View configuration
- Drawing dengan Exploded + BOM
```

---

## Kriteria Penilaian

| Kriteria | Bobot |
|----------|-------|
| Project A: Kelengkapan komponen | 10% |
| Project A: Kebenaran mate | 15% |
| Project A: Motion Study berjalan | 10% |
| Project B: Assembly frame lengkap | 15% |
| Project B: Semua connector & fastener ter-assembly | 15% |
| Project B: Mate tanpa error (fully defined) | 10% |
| Exploded View (A & B) | 10% |
| BOM & Drawing | 10% |
| Video demo assembly process | 5% |

---

## Total Deliverables

**Project A (Press Tool):**
1. M06_A1_BaseFrame.sldprt
2. M06_A2_GuidePillar.sldprt
3. M06_A3_GuideBushing.sldprt
4. M06_A4_UpperPlate.sldprt
5. M06_A5_Punch.sldprt
6. M06_A6_Die.sldprt
7. M06_A7_Stripper.sldprt
8. M06_A8_Spring.sldprt
9. M06_A9_Handle.sldprt
10. M06_A_PressTool.sldasm

**Project B (Aluminium Frame):**
11. M06_B_AluminiumFrame.sldasm
12. M06_B_BOM.xlsx
13. M06_B_Drawing.slddrw

---

## Referensi
- Aluminium Catalog 2020.pdf (folder Referensi)
- Halaman connector: 18-26
- Halaman fastener: 23-25
- Halaman foot/accessories: 26-28

---

*Project Praktikum CAD/CAM — Modul 6*
