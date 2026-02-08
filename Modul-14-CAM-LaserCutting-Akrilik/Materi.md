# MATERI MODUL 14: CAM — LASER CUTTING AKRILIK + THERMAL BENDING

## Praktikum CAD/CAM — Pertemuan 14

---

## 1. Pendahuluan & Konteks

### Koneksi dari Modul Sebelumnya
Modul ini merupakan **penutup seri praktikum CAD/CAM** yang menggabungkan teknik laser cutting akrilik dengan thermal bending (pembengkokan menggunakan pemanas). Mahasiswa akan membuat:

1. **Casing Box** — kotak akrilik yang dipotong laser dan dirakit (tab-slot / lem)
2. **Casing Body Melengkung** — desain 3D yang di-flatten menjadi 2D (teknik sheet metal), dipotong laser, lalu dibengkokkan dengan pemanas (heat gun/strip heater) sehingga membentuk kurva

```
Alur Kerja Modul 14:
──────────────────────────────────────────────
A. CASING BOX (Kotak Datar):
   SolidWorks 3D → Flatten manual/otomatis → DXF → CorelDRAW → Laser Cut → Assembly

B. CASING MELENGKUNG (Curved Bending):
   SolidWorks Sheet Metal → Flatten → DXF → Laser Cut → Scoring → Thermal Bending → Curved Casing
──────────────────────────────────────────────
```

### Perbedaan dengan Modul 10
| Aspek | Modul 10 (Laser Cutting) | Modul 14 (Laser Cutting Akrilik) |
|-------|--------------------------|----------------------------------|
| Material | Akrilik 3mm | Akrilik 3mm–5mm |
| Fokus | Potong panel 2D flat | Potong + **bending melengkung** |
| Desain | Panel flat-pack robot beroda | **Sheet metal → flatten → bend** |
| Tambahan | Engrave nama | **Scoring + thermal bending** |
| Kompleksitas | Sedang | Tinggi (3D → 2D → 3D) |

---

## 2. Teknik A: Casing Box Akrilik (Flat-Pack)

### Konsep Casing Box
Casing box dibuat dari panel-panel akrilik 2D yang dipotong laser, kemudian dirakit menjadi kotak 3D menggunakan:
- **Tab-slot interlocking** (tanpa lem)
- **Lem akrilik (solvent cement)** untuk sambungan permanen
- Atau **kombinasi** keduanya

### Desain di SolidWorks
```
Desain 3D Casing Box:
┌──────────────┐
│              │ ← Top
│   ┌──────┐   │
│   │      │   │ ← Side (×4)
│   │      │   │
│   └──────┘   │
│              │ ← Bottom
└──────────────┘

Flatten menjadi panel 2D:
┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
│Top │ │Bot │ │Left│ │Rght│ │Frnt│ │Back│
│    │ │    │ │    │ │    │ │    │ │    │
└──┬─┘ └──┬─┘ └──┬─┘ └──┬─┘ └──┬─┘ └──┬─┘
   └── Tabs ──┘   └── Tabs ──┘   └── Tabs
```

### Parameter Tab-Slot untuk Akrilik
| Parameter | Nilai (akrilik 3mm) |
|-----------|---------------------|
| Material Thickness (t) | 3.0mm |
| Tab Width | 8–10mm |
| Slot Width | t + 0.1mm = **3.1mm** (clearance) |
| Tab Spacing | 2× tab width |
| Corner Treatment | Dog-bone fillet (radius 0.5mm) |

### Langkah Desain Casing Box
1. **Desain 3D** kotak di SolidWorks (Extrude + Shell)
2. **Buat panel terpisah** — setiap face menjadi part tersendiri
3. **Tambahkan tab-slot** pada edge yang bersambungan
4. **Export DXF** setiap panel
5. **Layout di CorelDRAW** — nesting di atas sheet akrilik

---

## 3. Teknik B: Casing Melengkung (Thermal Bending) ⭐

### Konsep Utama
Berbeda dengan bending sheet metal yang membengkokkan pada **satu titik/garis lipat** (press brake), thermal bending akrilik membengkokkan material secara **melengkung (curved)** menggunakan pemanas, menghasilkan bentuk kurva yang smooth.

```
BENDING SHEET METAL (Satu Titik):        THERMAL BENDING AKRILIK (Kurva):
          │                                         ╭──────╮
    ┌─────┤                                    ╭────╯      ╰────╮
    │     │ ← Satu titik lipat              ╭──╯                ╰──╮
    │     │                                 │      Kurva smooth      │
    │     │                                 │                        │
```

### Prinsip Thermal Bending Akrilik
| Aspek | Detail |
|-------|--------|
| **Material** | Akrilik cast (bukan extruded) — lebih mudah dibending |
| **Suhu Bending** | 150–170°C (glass transition temperature akrilik) |
| **Alat Pemanas** | Heat gun, strip heater, atau oven |
| **Teknik** | Panaskan area yang lebar → bengkokkan perlahan pada cetakan/jig |
| **Hasil** | Kurva smooth, bukan lipatan tajam |
| **Ketebalan** | 3–5mm optimal untuk bending |

### Perbedaan dengan Sheet Metal Bending
| Aspek | Sheet Metal (Logam) | Thermal Bending (Akrilik) |
|-------|--------------------|-----------------------------|
| Proses | Press brake, tekanan mekanis | Pemanasan + pembengkokan manual |
| Titik Lipat | Satu garis lipat tajam | Area lebar, kurva gradual |
| Suhu | Dingin (cold forming) | Panas (150–170°C) |
| Hasil | Sudut tajam (90°, 45°, dll.) | **Kurva smooth/melengkung** |
| Radius | K-factor, bend radius | Radius besar, gradual |
| Springback | Ada (logam elastis) | Minimal (akrilik thermoplastik) |
| Reversible | Tidak | Bisa dipanaskan ulang dan dibentuk lagi |

---

## 4. Workflow: 3D → Flatten → Laser Cut → Bending

### Step 1: Desain 3D di SolidWorks (Sheet Metal Mode)

#### Mengapa Sheet Metal?
SolidWorks Sheet Metal memiliki fitur **Flatten** yang bisa membuka desain 3D menjadi 2D secara otomatis. Ini menghemat waktu dan menghindari kesalahan manual saat membuat pola 2D.

```
SolidWorks Sheet Metal Workflow:
1. Insert → Sheet Metal → Base Flange
2. Set thickness = 3mm (akrilik)
3. Set default bend radius = 15mm (kurva smooth)
4. Model bentuk casing 3D dengan Edge Flange, Miter Flange, dll.
5. Flatten → menghasilkan pola 2D otomatis
6. Export DXF dari Flatten
```

#### Parameter Sheet Metal untuk Akrilik
| Parameter | Nilai |
|-----------|-------|
| Thickness | 3mm (sesuai akrilik) |
| Default Bend Radius | 15–30mm (kurva smooth, BUKAN kecil) |
| K-Factor | 0.33–0.44 (untuk estimasi, akrilik berbeda dari logam) |
| Bend Allowance | Perlu ditest pada sampel akrilik |
| Relief Type | Rectangular / None |

> **CATATAN PENTING:** K-factor pada akrilik **tidak seakurat** pada logam karena akrilik thermal bending tidak mengikuti hukum plastisitas yang sama. **Selalu buat test bend** pada sampel material sebelum produksi final.

### Step 2: Flatten di SolidWorks
```
1. Di Sheet Metal part → klik "Flatten" di toolbar
2. SolidWorks membuka desain 3D menjadi flat pattern
3. Bend lines ditampilkan sebagai garis putus-putus
4. Verify dimensi flat pattern dengan perhitungan manual

SEBELUM FLATTEN:              SETELAH FLATTEN:
    ╭──────╮                  ┌─────────────────────────┐
╭───╯      ╰───╮             │   │         │   │       │
│               │             │   │         │   │       │
│   Casing 3D   │             │   bend line │   │       │
│               │             │   (scoring) │   │       │
└───────────────┘             └─────────────────────────┘
                              ← Flat Pattern (untuk laser) →
```

### Step 3: Tambahkan Scoring Lines (Garis Bantu Bending)
**Scoring** adalah garis tipis yang di-engrave (bukan dipotong penuh) pada permukaan akrilik untuk menandai lokasi bending dan memudahkan pembengkokan yang tepat.

```
Laser Scoring pada Akrilik:
┌──────────────────────────────────┐
│          │            │          │
│          │ ← Scoring  │          │
│  Panel A │   (engrave) │  Panel B │
│          │    garis    │          │
│          │            │          │
└──────────────────────────────────┘

Parameter Scoring:
- Power: 15–25% (JANGAN sampai potong penuh!)
- Speed: 30–50 mm/s
- Kedalaman: ~0.3–0.5mm (1/6 sampai 1/10 ketebalan)
- Tujuan: menandai bend line, BUKAN memperlemah
```

### Step 4: Export DXF & Layout di CorelDRAW
```
1. Dari SolidWorks Flat Pattern → Save As → DXF
2. Buka di CorelDRAW
3. Assign warna layer:
   ├── MERAH (RGB 255,0,0): Cutting — potong keliling
   ├── BIRU (RGB 0,0,255): Scoring — garis bending (engrave)
   └── HIJAU (RGB 0,255,0): Engraving — dekorasi/teks (opsional)
4. Nesting pada sheet akrilik
5. Export ke software laser (RDWorks/LightBurn)
```

### Step 5: Laser Cutting + Scoring
```
Urutan Operasi Laser:
1. ENGRAVE (dekorasi/teks) → power rendah, area
2. SCORING (bend lines) → power rendah, line
3. CUTTING (kontur luar) → power tinggi, line

Parameter Laser untuk Akrilik 3mm:
┌────────────┬───────────┬───────────┬────────────┐
│ Operasi    │ Power (%) │ Speed     │ Kedalaman  │
├────────────┼───────────┼───────────┼────────────┤
│ Engraving  │ 20–30%    │ 300 mm/s  │ ~0.2mm     │
│ Scoring    │ 15–25%    │ 30–50 mm/s│ ~0.3–0.5mm │
│ Cutting    │ 70–90%    │ 8–15 mm/s │ Through    │
└────────────┴───────────┴───────────┴────────────┘
```

### Step 6: Thermal Bending
```
Alat yang Dibutuhkan:
├── Heat gun (500–600°C output, tapi jarak jauh → 150–170°C di permukaan)
│   ATAU Strip heater (lebih terkontrol untuk garis lipat)
├── Sarung tangan tahan panas
├── Jig / cetakan (dari kayu/MDF — bentuk kurva yang diinginkan)
├── Timer / termometer infrared (opsional)
└── Kain basah (untuk mendinginkan area yang tidak dibending)

Prosedur Bending:
1. Letakkan akrilik yang sudah di-scoring pada jig
2. Panaskan area bending dengan heat gun:
   ├── Jarak ±10–15 cm dari permukaan
   ├── Gerakkan heat gun bolak-balik (jangan diam di satu titik!)
   ├── Panaskan KEDUA sisi (bolak-balik)
   └── Waktu: 1–3 menit tergantung ketebalan
3. Test fleksibilitas — tekan perlahan
   ├── Jika sudah lentur → mulai bengkokkan
   └── Jika masih kaku → panaskan lagi
4. Bengkokkan perlahan mengikuti jig
   ├── Jangan terlalu cepat → pecah!
   ├── Bengkokkan bertahap, bukan sekaligus
   └── Pegang posisi sampai dingin (~30 detik)
5. Jika perlu kurva gradual:
   ├── Panaskan area yang LEBAR (bukan titik)
   ├── Gunakan jig dengan kurva smooth
   └── Bengkokkan bertahap dari tengah ke tepi

PENTING:
- BUKAN seperti press brake yang membengkokkan satu titik tajam!
- Panaskan area LEBAR → menghasilkan kurva SMOOTH
- Scoring membantu mengarahkan bending ke posisi yang tepat
- Akrilik CAST lebih mudah dibending daripada EXTRUDED
```

### Diagram Proses Thermal Bending
```
Tahap 1: FLAT (setelah laser cut)
┌──────────────────────────┐
│     │ scoring │           │
│     │  lines  │           │
└──────────────────────────┘

Tahap 2: PEMANASAN (heat gun / strip heater)
┌──────────────────────────┐
│     │≈≈≈≈≈≈≈│            │  ← Area dipanaskan (150-170°C)
│     │ PANAS │            │
└──────────────────────────┘

Tahap 3: BENDING pada jig
      ╭──────────╮
 ╭────╯ ≈≈ panas ╰────╮
 │     ≈≈ area ≈≈      │  ← Bengkokkan perlahan
 │                      │
 └──────────────────────┘

Tahap 4: DINGINKAN (hold posisi)
      ╭──────────╮
 ╭────╯          ╰────╮
 │                      │  ← Tahan sampai dingin
 │                      │     (~30 detik)
 └──────────────────────┘

Tahap 5: CASING MELENGKUNG (selesai)
      ╭──────────╮
 ╭────╯          ╰────╮
 │    Curved Casing    │
 │                      │
 └──────────────────────┘
```

---

## 5. Contoh Desain Casing Melengkung

### Casing Body Sederhana
```
Desain 3D (perspektif):
         ╭───────────────╮
    ╭────╯               ╰────╮
    │                          │
    │    Curved top cover       │
    │                          │
    ├──────────────────────────┤
    │    Base (flat bottom)    │
    └──────────────────────────┘

Dipecah menjadi:
A. Top Cover → Sheet Metal → Flatten → Laser Cut → Thermal Bend
B. Base Plate → Flat panel → Laser Cut → Flat (tidak dibend)
C. Side Panels (×2) → Flat → Laser Cut → Flat
D. Front/Back → Flat (atau curved juga)
```

### Konfigurasi Sheet Metal di SolidWorks
```
Part: Top Cover (Curved)
─────────────────────────
1. Insert → Sheet Metal → Base Flange
   ├── Thickness: 3mm
   ├── Bend Radius: 20mm (radius besar untuk kurva smooth)
   └── Sketch: profil samping (arc/spline + garis lurus)

2. Tambahkan Edge Flange jika perlu tepi vertikal
3. Tambahkan fitur lain (lubang, slot, dll.)
4. FLATTEN → pola 2D otomatis
5. Klik kanan pada Flat Pattern → Export DXF

Perhatikan:
- Bend radius BESAR (≥15mm) → kurva smooth saat bending
- Bend radius KECIL (<5mm) → risiko pecah saat bending
- SolidWorks menambahkan bend allowance pada flat pattern
```

---

## 6. Jig/Cetakan untuk Thermal Bending

### Mengapa Perlu Jig?
Jig/cetakan memastikan bentuk kurva yang **konsisten dan akurat**. Tanpa jig, bending manual akan menghasilkan bentuk yang tidak presisi.

### Material Jig
| Material | Kelebihan | Kekurangan |
|----------|-----------|------------|
| MDF | Murah, mudah dibentuk | Tidak tahan panas tinggi |
| Kayu solid | Kuat, tahan panas sedang | Lebih mahal |
| Plaster/Gypsum | Tahan panas baik | Rapuh |
| Aluminium | Tahan panas sangat baik | Mahal, sulit dibentuk |

### Desain Jig
```
Jig untuk Curved Bending:
┌────────────────────────────┐
│         ╭────────╮         │
│    ╭────╯        ╰────╮    │
│    │    Permukaan      │    │ ← Profil kurva
│    │    cetakan jig    │    │    sesuai desain
│    │                   │    │
│    └───────────────────┘    │
│    [   BASE JIG (flat)  ]   │
└────────────────────────────┘

Jig bisa dibuat dari:
- CNC Router (Modul 13!) → milling kontur kurva dari MDF
- 3D Print (Modul 12!) → print profil kurva
- Manual (amplas/rasp) → untuk bentuk sederhana
```

---

## 7. Troubleshooting

### Masalah Laser Cutting Akrilik
| Masalah | Penyebab | Solusi |
|---------|----------|-------|
| Tepi kecoklatan | Power terlalu tinggi | ↓ Power, ↑ speed |
| Tidak terpotong | Power kurang / focus salah | ↑ Power, cek focus lens |
| Flash/api | Material kotor / power tinggi | Bersihkan, ↓ power, gunakan air assist |
| Scoring terlalu dalam | Power scoring berlebih | ↓ Power scoring ke 15–20% |
| Scoring tidak terlihat | Power terlalu rendah | ↑ Power scoring ke 20–25% |

### Masalah Thermal Bending
| Masalah | Penyebab | Solusi |
|---------|----------|-------|
| **Akrilik pecah** | Terlalu cepat dibending / kurang panas | Panaskan lebih lama, bending lebih perlahan |
| **Gelembung (bubble)** | Suhu terlalu tinggi | ↓ Suhu, jaga jarak heat gun |
| **Bending tidak rata** | Pemanasan tidak merata | Gerakkan heat gun merata, panaskan kedua sisi |
| **Springback** | Terlalu cepat dilepas | Hold posisi lebih lama sampai dingin |
| **Kurva tidak smooth** | Area pemanasan terlalu sempit | Panaskan area yang lebih lebar |
| **Warna berubah/kabur** | Overheating | ↓ Suhu, ↑ jarak, monitoring |
| **Posisi bend tidak tepat** | Scoring kurang jelas | Pastikan scoring visible sebelum bending |

### Tips Keberhasilan Bending
1. **Test dulu** pada potongan sisa akrilik sebelum bending part final
2. **Panaskan merata** — gerakkan heat gun, jangan diam di satu titik
3. **Akrilik CAST** (bukan extruded) — lebih mudah dibending
4. **Ketebalan 3mm** paling mudah — 5mm butuh waktu lebih lama
5. **Jig WAJIB** untuk hasil yang konsisten
6. **Sarung tangan tahan panas** — akrilik panas bisa membakar kulit
7. **Ventilasi** — panaskan di area terbuka / berventilasi

---

## 8. Safety

### Keselamatan Laser Cutting
| Wajib | Keterangan |
|-------|------------|
| 🥽 Laser Safety Glasses | Sesuai wavelength CO2 (10.6µm) |
| 🔒 Lid tertutup | Jangan buka saat laser aktif |
| 🫁 Ventilasi/Exhaust | Asap akrilik berbahaya |
| 🧯 Fire extinguisher | Akrilik bisa terbakar |
| 👀 Monitor terus | Jangan tinggalkan mesin |

### Keselamatan Thermal Bending
| Wajib | Keterangan |
|-------|------------|
| 🧤 Sarung tangan tahan panas | Akrilik dan heat gun SANGAT panas |
| 🥽 Safety glasses | Pecahan akrilik bisa terbang |
| 🌬️ Ventilasi | Akrilik yang dipanaskan mengeluarkan uap |
| 🪤 Area bersih | Hindari material mudah terbakar di sekitar |
| 🔥 Heat gun posisi aman | Jangan arahkan ke tangan/tubuh |

---

## 9. Percobaan

### Percobaan 1: Review Teknik Sheet Metal di SolidWorks
- Buka SolidWorks → Insert → Sheet Metal → Base Flange
- Set thickness 3mm, bend radius 20mm
- Buat profil sederhana (rectangle + edge flange)

### Percobaan 2: Desain Casing Box (6 Panel)
- Desain kotak 100×80×60mm dari panel akrilik 3mm
- Tambahkan tab-slot (tab 10mm, slot 3.1mm)
- Export DXF setiap panel

### Percobaan 3: Nesting Casing Box di CorelDRAW
- Import semua DXF panel
- Assign warna: merah = cut, hijau = engrave
- Nesting optimal pada sheet akrilik

### Percobaan 4: Desain Casing Body Melengkung (Sheet Metal)
- Buat sheet metal part: base + curved top cover
- Bend radius 20–30mm (kurva smooth)
- Gunakan Edge Flange / Sketched Bend

### Percobaan 5: Flatten & Export DXF
- Flatten sheet metal part → flat pattern
- Identifikasi bend lines pada flat pattern
- Export DXF → pastikan bend lines ter-export

### Percobaan 6: Layout Scoring + Cutting di CorelDRAW
- Import DXF flat pattern
- Assign: merah = cutting, biru = scoring (bend lines)
- Cek parameter scoring (power rendah!)

### Percobaan 7: Laser Cutting Akrilik
- Setup laser cutter → focus, air assist
- Potong casing box panels
- Potong flat pattern casing melengkung + scoring bend lines

### Percobaan 8: Assembly Casing Box
- Rakit panel casing box → tab-slot / lem akrilik
- Evaluasi fit dan alignment
- Dokumentasi foto

### Percobaan 9: Thermal Bending Casing Melengkung ⭐
- Siapkan jig dengan profil kurva
- Panaskan flat pattern pada bend area
- Bengkokkan perlahan → ikuti jig
- Hold sampai dingin → evaluasi bentuk

### Percobaan 10: Assembly Final & Evaluasi
- Assembly casing melengkung (pasang side panel, base)
- Bandingkan bentuk aktual vs desain 3D
- Ukur radius bending aktual vs desain
- Dokumentasi foto seluruh produk

---

## 10. Peta Koneksi Modul
```
┌─────────────────────────────────────────────┐
│              MODUL 14 (Final)               │
│     CAM Laser Cutting Akrilik +             │
│     Thermal Bending                         │
│                                             │
│     INPUT:                                  │
│     ├── Teknik Sheet Metal (Modul 07)       │
│     ├── Teknik Laser Cutting (Modul 10)     │
│     └── DXF workflow CorelDRAW              │
│                                             │
│     PROSES:                                 │
│     ├── A. Casing Box:                      │
│     │   └── Panel 2D → Cut → Assembly       │
│     └── B. Casing Melengkung:               │
│         ├── Sheet Metal 3D                  │
│         ├── Flatten → DXF                   │
│         ├── Laser Cut + Scoring             │
│         └── Thermal Bending → Curved 3D     │
│                                             │
│     OUTPUT:                                 │
│     ├── Casing box jadi                     │
│     └── Casing melengkung jadi              │
└─────────────────────────────────────────────┘
```

---

## 11. Ringkasan Seluruh Seri Praktikum
```
MODUL 01–07: Fondasi CAD
├── SolidWorks 2D, 3D Part, Assembly, Sheet Metal

MODUL 08–09, 11: Project CAD (Desain)
├── Modul 08: Konveyor → STEP (ke Modul 13)
├── Modul 09: Robot Beroda → DXF (ke Modul 10)
└── Modul 11: Robot Lengan → STL (ke Modul 12)

MODUL 10, 12, 13, 14: Realisasi CAM
├── Modul 10: Laser Cut → Robot Beroda + Nama
├── Modul 12: 3D Print → Robot Lengan + Huruf Timbul
├── Modul 13: CNC Router → Part Konveyor + Ukiran Nama
└── Modul 14: Laser Cut Akrilik → Casing Box + Bending
```

---

## 12. Checklist Kesiapan
- [ ] SolidWorks dengan fitur Sheet Metal
- [ ] CorelDRAW untuk layout DXF
- [ ] Mesin laser cutter siap (CO2, untuk akrilik)
- [ ] Sheet akrilik cast 3mm (ukuran cukup)
- [ ] Heat gun atau strip heater
- [ ] Sarung tangan tahan panas
- [ ] Jig/cetakan untuk bending (MDF/kayu)
- [ ] Lem akrilik (solvent cement) untuk casing box
- [ ] Safety equipment (glasses, mask, gloves)
- [ ] Potongan sisa akrilik untuk test bending

---

## Referensi
1. SolidWorks Sheet Metal Documentation — help.solidworks.com
2. Acrylic Bending Guide — https://www.eplastics.com/bending-acrylic
3. TAP Plastics Heating Guide — https://www.tapplastics.com
4. CorelDRAW + Laser Cutting Workflow
5. RDWorks / LightBurn Documentation

---

*Materi Praktikum CAD/CAM — Modul 14*
