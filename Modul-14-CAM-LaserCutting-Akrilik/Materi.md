# MATERI MODUL 14: CAM LASER CUTTING — SHEET METAL DRAWING & TEKNIK BENDING AKRILIK

## Praktikum CAD/CAM — Pertemuan 14

---

## Daftar Isi
1. [Pendahuluan](#1-pendahuluan)
2. [Sheet Metal Drawing untuk Laser Cutting](#2-sheet-metal-drawing-untuk-laser-cutting)
3. [Flat Pattern & DXF Export Lanjutan](#3-flat-pattern--dxf-export-lanjutan)
4. [Akrilik: Sifat Material dan Jenis](#4-akrilik-sifat-material-dan-jenis)
5. [Teknik Bending Akrilik](#5-teknik-bending-akrilik)
6. [Desain untuk Bending (DFB)](#6-desain-untuk-bending-dfb)
7. [Jig dan Fixture Bending](#7-jig-dan-fixture-bending)
8. [Workflow Lengkap: SolidWorks → Laser → Bending](#8-workflow-lengkap-solidworks--laser--bending)
9. [Teknik Joining Akrilik](#9-teknik-joining-akrilik)
10. [Percobaan 1–10](#10-percobaan-110)
11. [Keselamatan Kerja](#11-keselamatan-kerja)

---

## 1. Pendahuluan

Modul ini membahas workflow lanjutan **CAM Laser Cutting** yang dikombinasikan dengan **sheet metal drawing** dan **teknik bending akrilik**. Berbeda dengan Modul 10 (laser cutting dasar pada material datar), modul ini fokus pada pembuatan produk **3D dari lembaran akrilik** melalui proses potong laser + bending termal.

### Mengapa Sheet Metal + Laser + Bending?
- Sheet metal drawing di SolidWorks memungkinkan desain 3D yang bisa di-**flatten** (dibentangkan)
- Flat pattern → DXF → laser cut → bending → produk 3D
- Workflow ini sangat umum di industri untuk: casing, display, signage, enclosure, rak

### Posisi Modul dalam Alur Praktikum
```
Modul 7 (Sheet Metal) → Modul 10 (Laser Cutting) → Modul 14 (Gabungan + Bending)
```

---

## 2. Sheet Metal Drawing untuk Laser Cutting

### 2.1 Konsep Sheet Metal untuk Akrilik
Meskipun fitur Sheet Metal di SolidWorks awalnya dirancang untuk logam, konsepnya bisa diaplikasikan untuk **lembaran akrilik**:

| Aspek | Logam | Akrilik |
|-------|-------|---------|
| Ketebalan umum | 0.5 – 6 mm | 2 – 10 mm |
| Bend radius | 0.5–2× tebal | 1–3× tebal |
| K-factor | 0.3 – 0.5 | 0.3 – 0.4 (approx.) |
| Metode bending | Press brake / roll | Heat bending (hot air/strip heater) |
| Spring-back | Ya (signifikan) | Minimal (jika pemanasan cukup) |
| Bend line marking | Tidak perlu di part | **Perlu** (sebagai garis engraving di DXF) |

### 2.2 Setup Sheet Metal untuk Akrilik di SolidWorks
1. **New Part → Sheet Metal tab**
2. **Default Gauge Table**: Tidak pakai (Custom)
3. **Thickness**: Sesuai ketebalan akrilik (misal 3mm, 5mm)
4. **Default Bend Radius**: 1.5× tebal (misal 4.5mm untuk akrilik 3mm)
5. **K-Factor**: 0.35 (approksimasi untuk akrilik)
6. **Auto Relief**: None (akrilik tidak perlu relief pada bend)

### 2.3 Mendesain dengan Bend Line
Saat mendesain sheet metal untuk akrilik:
- **Bend line** = lokasi di mana akrilik akan dipanaskan dan dilipat
- Di flat pattern, bend line ini harus menjadi **garis engraving** (bukan cutting)
- Engraving berfungsi sebagai:
  - Penanda posisi bending
  - Penipisan lokal (memudahkan bending)
  - Panduan visual saat proses bending manual

### 2.4 Fitur Sheet Metal yang Relevan
| Fitur | Fungsi untuk Akrilik |
|-------|---------------------|
| Base Flange | Panel utama (dasar/sisi) |
| Edge Flange | Sisi yang akan di-bend |
| Miter Flange | Sudut/corner yang di-bend |
| Sketched Bend | Bend pada posisi custom |
| Flat Pattern | Bentangan → DXF untuk laser |
| Forming Tool | **Tidak relevan** (hanya untuk logam) |
| Hem | **Tidak relevan** |
| Jog | Bisa dipakai (step bend) |

---

## 3. Flat Pattern & DXF Export Lanjutan

### 3.1 Flat Pattern Configuration
Konfigurasi flat pattern untuk akrilik:
1. Buka flat pattern → **Flatten** fitur di feature tree
2. Pastikan semua bend ter-unfold dengan benar
3. Cek dimensi flat pattern — bandingkan dengan material akrilik yang tersedia

### 3.2 DXF Export dengan Layer Terpisah
Kunci workflow akrilik + laser adalah **pemisahan layer** dalam DXF:

| Layer | Warna | Fungsi | Setting Laser |
|-------|-------|--------|---------------|
| CUT (kontur luar) | Merah | Cutting through | Power tinggi, speed rendah |
| CUT_INTERNAL (lubang, slot) | Biru | Cutting internal | Sama dengan CUT |
| ENGRAVE_BEND | Hijau | Bend line marking | Power rendah, speed tinggi |
| ENGRAVE_TEXT | Kuning | Teks/logo | Power rendah, speed tinggi |
| SCORE (v-groove) | Magenta | Garis lipat (scoring) | Power sedang, speed sedang |

### 3.3 Cara Export DXF Multi-Layer dari SolidWorks
1. **Feature Tree → Flat-Pattern** → klik kanan → **Export to DXF/DWG**
2. Pada dialog Export:
   - ✅ **Geometry** → include bend lines
   - ✅ **Bend lines** → export as separate layer
   - Sheet Metal Options → **Include flat-pattern geometry**
3. Buka DXF di **CorelDRAW**:
   - Pisahkan objek per layer (cut, engrave, bend)
   - Assign warna sesuai tabel di atas
   - Set hairline (0.001mm) untuk cutting
4. Atur **urutan operasi**:
   - Engrave bend lines dulu
   - Internal cuts
   - External contour terakhir

### 3.4 Perhitungan Dimensi Flat Pattern
Untuk akrilik, rumus bend allowance yang disederhanakan:

```
Bend Allowance (BA) = π/180 × Bend Angle × (R + K × T)

Di mana:
R = Bend Radius (inner)
K = K-Factor (0.33–0.40 untuk akrilik)
T = Thickness (ketebalan akrilik)
```

**Contoh Perhitungan:**
- Akrilik 3mm, bend 90°, radius dalam 5mm, K=0.35
- BA = π/180 × 90 × (5 + 0.35 × 3)
- BA = 1.5708 × 6.05 = 9.50 mm
- Artinya flat pattern harus menyediakan 9.50mm di area bend tersebut

---

## 4. Akrilik: Sifat Material dan Jenis

### 4.1 Apa itu Akrilik?
**Akrilik (Acrylic / PMMA — Polymethyl Methacrylate)** adalah thermoplastic transparan yang sering disebut "kaca plastik". Nama dagang: Plexiglass, Perspex, Lucite.

### 4.2 Sifat Mekanik & Termal
| Properti | Nilai | Satuan |
|----------|-------|--------|
| Densitas | 1.17 – 1.20 | g/cm³ |
| Tensile Strength | 55 – 75 | MPa |
| Flexural Strength | 90 – 130 | MPa |
| Modulus Elastisitas | 2.4 – 3.3 | GPa |
| **Glass Transition (Tg)** | **105 – 115** | **°C** |
| **Softening Point** | **130 – 140** | **°C** |
| **Bending Temperature** | **150 – 170** | **°C** |
| Melting Point | ~160 (decompose) | °C |
| Max Service Temp | 80 – 90 | °C |
| Thermal Expansion | 70 – 80 | ×10⁻⁶/°C |

### 4.3 Jenis Akrilik
| Jenis | Proses Produksi | Sifat Bending | Harga |
|-------|----------------|---------------|-------|
| **Cast Acrylic** | Dicetak/dituang | Lebih tahan retak, bending bagus | Mahal |
| **Extruded Acrylic** | Diekstrusi | Lebih mudah retak saat bending | Murah |

> ⚠️ **PENTING**: Untuk bending, selalu gunakan **Cast Acrylic**. Extruded acrylic sangat mudah retak saat dibending.

### 4.4 Ketebalan Umum dan Aplikasi
| Tebal (mm) | Kemudahan Bending | Aplikasi |
|------------|-------------------|----------|
| 2 | Sangat mudah | Label, small parts |
| 3 | Mudah | Casing kecil, display stand |
| 5 | Sedang | Enclosure, rak, signage |
| 8 | Sulit | Box besar, furniture |
| 10 | Sangat sulit | Struktural, aquarium mini |

---

## 5. Teknik Bending Akrilik

### 5.1 Prinsip Dasar
Akrilik adalah **thermoplastic** → bisa dilunakkan dengan panas dan dibentuk. Setelah dingin, bentuk baru menjadi permanen.

**Suhu ideal bending**: 150–170°C (di atas Tg, di bawah titik dekomposisi)

### 5.2 Metode Bending

#### A. Strip Heater / Line Bender
Metode paling umum untuk **bending lurus (straight bend)**.

**Komponen:**
- Elemen pemanas (nichrome wire) dalam profil aluminium
- Lebar pemanasan: 10-20mm (sesuai ketebalan akrilik)
- Termokopel / termometer infrared

**Prosedur:**
1. Lepaskan film pelindung di area bend (±20mm dari garis bend)
2. Letakkan akrilik di atas strip heater
3. Posisikan garis bend **tepat di atas** elemen pemanas
4. Panaskan **kedua sisi** (bolak-balik tiap 30–60 detik untuk akrilik >3mm)
5. Tes kelenturan: tekan pelan, jika mulai lentur → siap bend
6. **Waktu pemanasan**: ~1 menit per mm ketebalan
7. Angkat, posisikan di jig/mal, tekuk ke sudut yang diinginkan
8. Tahan posisi hingga dingin (2–5 menit)

**Waktu Pemanasan Referensi:**
| Tebal Akrilik | Waktu Pemanasan | Catatan |
|---------------|----------------|---------|
| 2 mm | 2–3 menit | Bolak-balik 1× |
| 3 mm | 3–4 menit | Bolak-balik 2× |
| 5 mm | 5–7 menit | Bolak-balik 3–4× |
| 8 mm | 8–12 menit | Bolak-balik 5–6× |

#### B. Heat Gun / Hot Air
Untuk **bending kurva** atau area yang lebih luas.

**Prosedur:**
1. Set heat gun ke 150–170°C
2. Jaga jarak 5–10 cm dari permukaan akrilik
3. Gerakkan heat gun **maju-mundur** secara merata (jangan diam di satu titik!)
4. Panaskan area selebar 2–3× ketebalan akrilik
5. Tes kelenturan secara berkala
6. Bend menggunakan jig/template

> ⚠️ Heat gun lebih sulit dikontrol — risiko overheating dan gelembung (bubble) lebih tinggi

#### C. Oven Bending
Untuk **forming 3D** (bukan hanya line bend).

**Prosedur:**
1. Panaskan oven ke 150–160°C
2. Masukkan akrilik di atas wire rack (bukan langsung di rak solid)
3. Panaskan hingga seluruh sheet lunak (~10–15 menit untuk 3mm)
4. Keluarkan dengan sarung tangan tahan panas
5. Draping/forming di atas mold/jig
6. Biarkan dingin di posisi

### 5.3 Masalah Umum Bending

| Masalah | Penyebab | Solusi |
|---------|----------|-------|
| **Retak / Crack** | Suhu terlalu rendah, bending terlalu cepat | Panaskan lebih lama, bend pelan |
| **Gelembung (Bubble)** | Suhu terlalu tinggi | Kurangi suhu, jaga jarak heat gun |
| **Warna kekuningan** | Overheating | Kurangi waktu/suhu pemanasan |
| **Bend tidak lurus** | Pemanasan tidak merata | Gunakan strip heater, bolak-balik |
| **Spring-back** | Pendinginan terlalu cepat | Tahan di jig sampai benar-benar dingin |
| **Permukaan kasar** | Film pelindung tidak dilepas di area bend | Lepas film 20mm di sekitar bend line |
| **Radius terlalu besar** | Pemanasan terlalu lebar | Persempit area pemanasan |

### 5.4 Minimum Bend Radius
| Tebal Akrilik | Min. Radius Dalam | Rekomendasi |
|---------------|-------------------|-------------|
| 2 mm | 2 mm | 3–4 mm |
| 3 mm | 3 mm | 5–6 mm |
| 5 mm | 5 mm | 8–10 mm |
| 8 mm | 8 mm | 12–15 mm |

**Aturan umum**: Minimum bend radius = 1× tebal akrilik, rekomendasi 1.5–2× tebal.

---

## 6. Desain untuk Bending (DFB — Design for Bending)

### 6.1 Aturan Desain
1. **Jarak bend ke tepi**: Minimum 3× tebal dari tepi terdekat
2. **Jarak antar bend**: Minimum 4× tebal
3. **Lubang/slot dekat bend**: Minimum 2× tebal dari bend line
4. **Arah bend**: Hindari bend yang memotong lubang/slot
5. **Bend sequence**: Rencanakan urutan bending (dalam → luar)

### 6.2 Scoring (V-Groove) untuk Bend Line
Teknik scoring menggunakan laser:
- Laser menggores **v-groove** di sepanjang garis bend
- Kedalaman: 30–50% ketebalan akrilik
- Membantu bending lebih presisi dan mengurangi radius
- **Hati-hati**: Terlalu dalam → lemah, bisa patah

```
Setting Laser untuk Scoring (akrilik 3mm):
- Power: 40-50% (dari max)
- Speed: 15-25 mm/s
- Passes: 1-2
- Target depth: 1.0-1.5 mm (30-50% dari 3mm)
```

### 6.3 Template Desain Sheet Metal → Akrilik di SolidWorks
```
Parameter Sheet Metal untuk Akrilik 3mm:
├── Thickness: 3.00 mm
├── Default Bend Radius: 5.00 mm (inside)
├── K-Factor: 0.35
├── Bend Allowance: Calculated
├── Auto Relief: None
└── Gauge Table: None (Custom)
```

---

## 7. Jig dan Fixture Bending

### 7.1 Mengapa Perlu Jig?
- Memastikan **sudut bend** konsisten dan akurat
- Membantu **menahan** akrilik saat pendinginan
- **Reprodusibilitas** — bisa membuat banyak part identik

### 7.2 Jenis Jig Bending

#### A. Jig Sudut Sederhana (V-Block)
- Dua papan MDF/kayu dihubungkan dengan engsel
- Sudut diatur sesuai kebutuhan (90°, 120°, dll.)
- Cocok untuk: bend tunggal, sudut tetap

#### B. Jig Profil/Template
- Dibuat dari MDF/kayu tebal
- Profil dipotong menggunakan CNC Router atau laser
- Akrilik panas ditekan/dilipat mengikuti profil
- Cocok untuk: bend kurva, multi-bend

#### C. Jig Multi-Bend
- Untuk part dengan beberapa bend
- Memiliki stopper dan guide untuk setiap tahap bend
- Urutan bend ditentukan di desain jig

### 7.3 Desain Jig di SolidWorks
1. Desain part akrilik (sheet metal) terlebih dahulu
2. Buat assembly → posisikan part dalam keadaan ter-bend
3. Desain jig yang mengikuti kontur luar part
4. Flat pattern jig → laser cut dari MDF
5. Assembly jig → tes dengan part akrilik

### 7.4 Contoh Jig 90° untuk Akrilik 3mm
```
Komponen Jig:
├── Base plate: MDF 6mm, 150×100mm
├── Stop block A: MDF 6mm, 100×50mm (vertikal)
├── Stop block B: MDF 6mm, 100×50mm (horizontal)
├── Guide slot: Untuk positioning akrilik
├── Clamp: Binder clip atau spring clamp
└── Semua part laser cut → assembly slot/tab
```

---

## 8. Workflow Lengkap: SolidWorks → Laser → Bending

### 8.1 Flowchart Workflow
```
┌─────────────────────────────────────┐
│ 1. SolidWorks - Sheet Metal Design  │
│    (3D → Flat Pattern)              │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│ 2. DXF Export (Multi-Layer)         │
│    Cut + Engrave + Bend Lines       │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│ 3. CorelDRAW - Layout & Nesting    │
│    Assign warna, hairline, urutan   │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│ 4. Software Laser (RDWorks/LB)     │
│    Set parameter per layer          │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│ 5. LASER CUTTING + ENGRAVING       │
│    (Engrave bend lines → Cut)       │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│ 6. BENDING                          │
│    Strip heater / heat gun          │
│    + Jig/fixture                    │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│ 7. ASSEMBLY & FINISHING             │
│    Lem akrilik + pembersihan        │
└─────────────────────────────────────┘
```

### 8.2 Parameter Laser Cutting untuk Akrilik
| Tebal (mm) | Power (%) | Speed (mm/s) | Passes | Gas |
|------------|-----------|--------------|--------|-----|
| 2 | 45–55 | 12–18 | 1 | Air |
| 3 | 55–65 | 8–14 | 1 | Air |
| 5 | 70–80 | 5–10 | 1–2 | Air |
| 8 | 85–95 | 3–6 | 2–3 | Air |

> Catatan: Parameter sangat bergantung pada mesin laser (watt, jenis, usia tabung). Selalu lakukan test cut!

### 8.3 Parameter Engraving untuk Bend Line
| Ketebalan | Power (%) | Speed (mm/s) | Kedalaman Target |
|-----------|-----------|--------------|-----------------|
| 2 mm | 20–25 | 50–80 | 0.5–0.7 mm |
| 3 mm | 25–35 | 40–60 | 0.8–1.2 mm |
| 5 mm | 35–45 | 30–50 | 1.5–2.0 mm |

---

## 9. Teknik Joining Akrilik

### 9.1 Lem Akrilik (Solvent Cement)
- **Jenis**: Acrifix, Weld-On #3, #4, #16
- **Prinsip**: Melarutkan permukaan → fusi kimia (bukan adhesive biasa)
- **Kekuatan**: Sangat kuat (hampir seamless)

**Prosedur Pengeleman:**
1. Pastikan permukaan bersih dan rata
2. Posisikan part → tahan dengan jig/tape
3. Aplikasikan lem menggunakan **syringe/applicator bottle**
4. Lem akan mengalir masuk ke celah (kapiler)
5. Tahan posisi 2–5 menit (initial set)
6. Curing penuh: 24–48 jam

### 9.2 Teknik Tab-Slot (Interlocking)
- Desain tab dan slot di SolidWorks (pada flat pattern)
- Laser cut → assembly tanpa lem (press-fit) atau dengan lem
- **Toleransi slot**: +0.1mm dari ketebalan akrilik
- **Kerf compensation**: Sesuaikan slot width = thickness + kerf

### 9.3 Teknik Gabungan: Bend + Tab-Slot
Untuk produk kompleks:
- Bagian yang bisa dibend → gunakan sheet metal bend
- Bagian yang harus di-join → gunakan tab-slot + lem
- Contoh: Box akrilik → 3 sisi dari 1 sheet (bend), 2 sisi terpisah (tab-slot)

---

## 10. Percobaan 1–10

---

### Percobaan 1: Sheet Metal Akrilik — Base Flange & Edge Flange

**Tujuan**: Membuat desain sheet metal sederhana untuk akrilik dengan base flange dan edge flange.

**Langkah-langkah:**
1. Buka SolidWorks → New Part
2. Pilih **Sheet Metal** tab
3. Set parameter:
   - Thickness: 3.00 mm
   - Default Bend Radius: 5.00 mm
   - K-Factor: 0.35
4. **Base Flange/Tab**:
   - Front Plane → Sketch → Rectangle 100×60 mm → Exit Sketch
   - Klik **Base Flange/Tab** → pilih sketch → Direction: Mid Plane
5. **Edge Flange** (sisi panjang):
   - Klik edge 100mm → **Edge Flange**
   - Angle: 90° (Up)
   - Flange Length: 30 mm
6. **Edge Flange** (sisi pendek):
   - Klik edge 60mm → **Edge Flange**
   - Angle: 90° (Up)
   - Flange Length: 30 mm
7. Perhatikan **Relief Cut** otomatis di corner
8. Klik **Flatten** → lihat flat pattern
9. Catat dimensi flat pattern (panjang × lebar total)
10. **Save** → `Percobaan1_SheetMetal_Akrilik.SLDPRT`

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Dimensi base (L×W) | 100 × 60 mm |
| Jumlah edge flange | ... |
| Tinggi flange | 30 mm |
| Dimensi flat pattern (total) | ... × ... mm |
| Bend Allowance per bend | ... mm |

---

### Percobaan 2: DXF Export Multi-Layer dengan Bend Lines

**Tujuan**: Mengekspor flat pattern sebagai DXF dengan layer terpisah untuk cut dan bend lines.

**Langkah-langkah:**
1. Buka file dari Percobaan 1
2. Pastikan dalam mode **Flat Pattern** (Flatten aktif)
3. Tambahkan teks pada permukaan: **Insert → Annotations → Note** atau **Sketch Text**
   - Tulis: Nama + NIM
   - Posisi: di tengah base flange
4. Klik kanan **Flat-Pattern** di Feature Tree → **Export to DXF/DWG**
5. Pada dialog:
   - Format: DXF
   - ✅ Include flat-pattern geometry
   - ✅ Include bend lines
   - Klik **Options**:
     - Export bend lines → ✅
     - Merge coplanar faces → ✅ (jika ada)
   - Simpan → `Percobaan2_FlatPattern.DXF`
6. Buka DXF di **CorelDRAW**:
   - Import → pilih DXF
   - Scale: 1:1 (mm)
7. **Pisahkan layer** di CorelDRAW:
   - Kontur luar → warna **Merah** (Cut)
   - Bend lines → warna **Hijau** (Engrave)
   - Teks → warna **Kuning** (Engrave)
8. Set semua outline ke **Hairline** (0.001mm)
9. Simpan sebagai `.CDR` dan ekspor `.DXF` baru (multi-layer)

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Jumlah layer di DXF | ... |
| Jenis garis kontur | ... |
| Jenis garis bend line | ... |
| Total panjang cutting path | ... mm |
| Jumlah bend lines | ... |

---

### Percobaan 3: Perhitungan Bend Allowance Akrilik

**Tujuan**: Memahami dan memverifikasi perhitungan bend allowance untuk akrilik.

**Langkah-langkah:**
1. Hitung **Bend Allowance manual** untuk konfigurasi berikut:

| Kasus | Tebal (T) | Radius (R) | Sudut | K-Factor |
|-------|-----------|------------|-------|----------|
| A | 3 mm | 5 mm | 90° | 0.35 |
| B | 3 mm | 5 mm | 120° | 0.35 |
| C | 5 mm | 8 mm | 90° | 0.35 |
| D | 5 mm | 10 mm | 45° | 0.40 |

2. Gunakan rumus:
   ```
   BA = π/180 × Angle × (R + K × T)
   ```

3. Hitung untuk setiap kasus:
   - Kasus A: BA = π/180 × 90 × (5 + 0.35 × 3) = ?
   - Kasus B: BA = ?
   - Kasus C: BA = ?
   - Kasus D: BA = ?

4. Bandingkan dengan **nilai SolidWorks**:
   - Buat sheet metal part untuk setiap kasus
   - Lihat flat pattern → ukur jarak di area bend
   - Catat bend allowance dari SolidWorks

5. Hitung **% error** antara manual vs SolidWorks

**Data Percobaan:**
| Kasus | BA Manual (mm) | BA SolidWorks (mm) | Error (%) |
|-------|---------------|-------------------|-----------|
| A | | | |
| B | | | |
| C | | | |
| D | | | |

---

### Percobaan 4: Desain Tray Akrilik (Multi-Bend)

**Tujuan**: Mendesain tray/nampan akrilik menggunakan sheet metal dengan 4 bend.

**Langkah-langkah:**
1. New Part → Sheet Metal
   - Thickness: 3 mm, Bend Radius: 5 mm, K=0.35
2. **Base Flange**: Rectangle 150 × 100 mm
3. **Edge Flange** × 4 sisi:
   - Panjang 100mm: flange 25mm, 90°
   - Panjang 150mm: flange 25mm, 90°
4. **Corner Treatment**:
   - Klik kanan pada corner → pilih treatment
   - Coba: **Closed Corner** → Overlap / Butt
   - Atau biarkan gap (untuk akrilik, gap OK karena di-lem)
5. Tambahkan **lubang** di base:
   - Pattern lubang Ø5mm, 4×, di area tengah (dekorasi / ventilasi)
   - Pastikan lubang tidak terlalu dekat dengan bend line (min. 2×T = 6mm)
6. Flatten → cek dimensi total flat pattern
7. Export DXF (dengan bend lines)
8. Verifikasi di CorelDRAW
9. Cek apakah flat pattern **muat** di lembaran akrilik 300×200mm

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Dimensi base tray | 150 × 100 mm |
| Tinggi sisi | 25 mm |
| Jumlah bend | 4 |
| Corner treatment | ... |
| Dimensi flat pattern | ... × ... mm |
| Muat di sheet 300×200? | Ya / Tidak |

---

### Percobaan 5: Desain Phone Stand dengan Bend & Tab-Slot

**Tujuan**: Mendesain phone stand dari akrilik yang menggabungkan bending dan tab-slot joint.

**Langkah-langkah:**
1. **Desain Konsep** (2 part):
   - **Part A** (Support/badan): Sheet metal dengan 1 bend (sudut 60–70°)
     - Dimensi: 80 × 120 mm (flat)
     - Bend di posisi 40mm dari bawah → angle 65°
     - Tab di bawah: 2× tab 10×3mm
   - **Part B** (Base/alas): Flat piece
     - Dimensi: 80 × 60 mm
     - Slot: 2× slot 10.2 × 3.2 mm (toleransi +0.2mm)
     - Lip/penahan depan: tinggi 10mm

2. **SolidWorks — Part A**:
   - Sheet Metal → Base Flange 80×120mm
   - Sketched Bend → posisi 40mm dari bawah, angle 65°
   - Cut → tab shape di bagian bawah
   - Flatten → Export DXF

3. **SolidWorks — Part B**:
   - Normal sketch (bukan sheet metal, karena flat)
   - Rectangle 80×60mm
   - Slot cut: 2× slot 10.2 × 3.2mm
   - Lip: rectangle 80×10mm di satu edge
   - Export DXF

4. **CorelDRAW**: Gabungkan kedua DXF, nesting di sheet
5. **Assembly di SolidWorks**: Gabungkan Part A + B → verifikasi fit

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Sudut bend Part A | ...° |
| Toleransi tab-slot | ... mm |
| Dimensi total flat (A) | ... × ... mm |
| Dimensi flat (B) | ... × ... mm |
| Total area material | ... mm² |

---

### Percobaan 6: Scoring / V-Groove Bend Line dengan Laser

**Tujuan**: Mempraktikkan teknik scoring (garis alur V) menggunakan laser untuk membantu bending presisi.

**Langkah-langkah:**
1. **Buat test piece** di SolidWorks:
   - Rectangle 200 × 50 mm, tebal 3mm
   - Buat **5 garis scoring** dengan jarak 40mm
   - Setiap garis memiliki setting scoring yang berbeda

2. **DXF Export** — semua garis scoring sebagai layer SCORE (Magenta)

3. **Parameter Scoring Test** (di software laser):

| Garis | Power (%) | Speed (mm/s) | Kedalaman Target |
|-------|-----------|--------------|-----------------|
| 1 | 20 | 60 | ~0.5 mm (ringan) |
| 2 | 25 | 50 | ~0.7 mm |
| 3 | 30 | 40 | ~1.0 mm (sedang) |
| 4 | 35 | 30 | ~1.2 mm |
| 5 | 40 | 25 | ~1.5 mm (dalam) |

4. **Eksekusi laser scoring** pada akrilik 3mm
5. **Ukur kedalaman** setiap garis scoring (menggunakan caliper/microscope)
6. **Test bending** setiap garis → catat:
   - Kemudahan bending (mudah/sedang/sulit)
   - Radius bend yang dihasilkan
   - Ada/tidaknya crack

**Data Percobaan:**
| Garis | Power | Speed | Kedalaman Aktual | Bending | Crack? |
|-------|-------|-------|-----------------|---------|--------|
| 1 | 20% | 60 | ... mm | | |
| 2 | 25% | 50 | ... mm | | |
| 3 | 30% | 40 | ... mm | | |
| 4 | 35% | 30 | ... mm | | |
| 5 | 40% | 25 | ... mm | | |

---

### Percobaan 7: Bending Akrilik dengan Strip Heater

**Tujuan**: Mempraktikkan bending akrilik menggunakan strip heater/line bender.

**Langkah-langkah:**
1. **Siapkan test piece**: 4 potongan akrilik 100 × 50 × 3mm (sudah laser cut)
2. **Setup strip heater**:
   - Nyalakan strip heater
   - Tunggu 5–10 menit hingga stabil
   - Cek suhu dengan infrared thermometer → target 150–170°C

3. **Test Bend (4 variasi)**:

| Test | Target Sudut | Metode | Jig |
|------|-------------|--------|-----|
| A | 90° | Strip heater | Jig 90° |
| B | 120° | Strip heater | Jig 120° |
| C | 45° | Strip heater | Jig 45° |
| D | 90° | Tanpa jig (manual) | Tidak ada |

4. **Prosedur per test**:
   - Lepas film pelindung di area bend (±15mm)
   - Letakkan akrilik di strip heater, garis bend di atas elemen
   - Panaskan selama 3–4 menit (bolak-balik tiap 60 detik)
   - Test kelenturan → jika mulai lentur, angkat
   - Posisikan di jig → tekuk ke sudut target
   - Tahan 2–3 menit → lepas

5. **Ukur hasil**:
   - Sudut aktual (menggunakan protractor/angle gauge)
   - Kualitas permukaan di area bend
   - Ada/tidaknya crack, bubble, discoloration

**Data Percobaan:**
| Test | Target | Sudut Aktual | Error | Kualitas | Crack/Bubble |
|------|--------|-------------|-------|----------|-------------|
| A | 90° | ...° | ...° | | |
| B | 120° | ...° | ...° | | |
| C | 45° | ...° | ...° | | |
| D | 90° | ...° | ...° | | |

---

### Percobaan 8: Desain & Laser Cut Jig Bending

**Tujuan**: Mendesain dan memfabrikasi jig bending dari MDF menggunakan laser cutting.

**Langkah-langkah:**
1. **Desain Jig 90° di SolidWorks**:
   - **Base plate**: MDF 6mm, 150 × 100 mm
   - **Block A (vertikal)**: 100 × 50 mm, MDF 6mm
   - **Block B (horizontal)**: 100 × 50 mm, MDF 6mm
   - **Joint**: Tab-slot 10 × 6.2mm (toleransi +0.2mm)
   - **Guide slot**: 3.2 × 60 mm (untuk posisi akrilik)
   - **Stopper**: notch 20 × 6 mm di base

2. **Assembly di SolidWorks**:
   - Gabungkan semua part → verifikasi sudut 90°
   - Pastikan akrilik bisa masuk guide slot
   - Cek clearance dan interferensi

3. **Export DXF** setiap part (flat, karena MDF = flat pieces)

4. **CorelDRAW**: Nesting semua part → 1 sheet MDF

5. **Laser cut MDF** → assembly jig

6. **Test jig**: Gunakan untuk bending akrilik test piece → ukur presisi sudut

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Jumlah part jig | ... |
| Material jig | MDF 6mm |
| Total area MDF | ... × ... mm |
| Sudut jig (target) | 90° |
| Sudut bend (aktual) | ...° |
| Repeatability (3× test) | ...° ± ...° |

---

### Percobaan 9: Desain Produk: Display Stand Akrilik dengan Bending

**Tujuan**: Mendesain display stand/product display dari akrilik yang melibatkan multiple bends dan tab-slot joints.

**Langkah-langkah:**
1. **Spesifikasi Display Stand**:
   - Fungsi: Display untuk HP / produk kecil
   - Material: Akrilik bening (clear) 3mm
   - Ukuran keseluruhan: ~120 × 80 × 100mm (P×L×T)

2. **Komponen Desain** (3 part):
   - **Part 1 — Main Body**: Sheet metal, 2 bends
     - Base horizontal → bend 80° → riser → bend 10° (back lean)
     - Total flat length: ~250mm
   - **Part 2 — Side Support** (×2): Flat piece
     - Profil segitiga/trapezoid
     - Tab: 2× per sisi
   - **Part 3 — Lip/Stopper**: Flat piece kecil
     - 80 × 15 mm, tab di bawah

3. **SolidWorks Sheet Metal**:
   - Part 1: Base Flange + Sketched Bend × 2
   - Pastikan bend direction dan angle benar
   - Tambahkan tab di sisi untuk side support

4. **Assembly**: Gabungkan semua → verifikasi

5. **Export DXF** (semua part) → CorelDRAW → nesting

6. Tentukan **urutan fabrikasi**:
   - Laser cut semua part
   - Bending Part 1 (bend 1 dulu, lalu bend 2)
   - Assembly: Side support → base → lip
   - Lem akrilik di joint tab-slot

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Jumlah part total | ... |
| Jumlah bend | ... |
| Sudut bend 1 | ...° |
| Sudut bend 2 | ...° |
| Total flat area | ... mm² |
| Estimasi waktu fabrikasi | ... menit |

---

### Percobaan 10: Eksekusi Lengkap — Laser Cut + Bending + Assembly

**Tujuan**: Melaksanakan seluruh workflow dari desain hingga produk jadi.

**Langkah-langkah:**
1. **Finalisasi desain** dari Percobaan 9 (atau modifikasi)
2. **Prepare DXF file** di CorelDRAW:
   - Layer Cut (Merah) → semua kontur potong
   - Layer Engrave_Bend (Hijau) → semua bend lines
   - Layer Engrave_Text (Kuning) → teks/logo jika ada
   - Pastikan urutan: Engrave → Internal Cut → External Cut

3. **Setup Mesin Laser**:
   - Material: Akrilik 3mm (clear atau warna)
   - Posisikan material, fokus laser
   - Set parameter cutting dan engraving

4. **EKSEKUSI LASER CUTTING**:
   - ⚠️ **Rekam dengan HP** dari awal sampai selesai
   - Jalankan engrave bend lines
   - Jalankan internal cuts (lubang, slot)
   - Jalankan external contour
   - Lepaskan part dari sheet → bersihkan edge

5. **EKSEKUSI BENDING**:
   - ⚠️ **Rekam dengan HP**
   - Setup strip heater
   - Posisikan Part 1 di strip heater (bend line 1)
   - Panaskan → bend menggunakan jig → tahan → dinginkan
   - Ulangi untuk bend line 2
   - Cek sudut dengan protractor

6. **ASSEMBLY**:
   - Dry fit semua part (tanpa lem)
   - Jika OK → aplikasikan lem akrilik
   - Tahan dengan jig/tape selama curing
   - Bersihkan excess lem

7. **Quality Check**:
   - Cek sudut bend (±2° toleransi)
   - Cek gap pada joint tab-slot
   - Cek kekuatan (uji tekan ringan)
   - Cek estetika (bersih, transparan, rata)
   - Dokumentasi foto dari semua sisi

**Data Percobaan:**
| Parameter | Nilai |
|-----------|-------|
| Waktu laser cutting | ... menit |
| Waktu bending total | ... menit |
| Waktu assembly | ... menit |
| Waktu total fabrikasi | ... menit |
| Sudut bend 1 (aktual vs target) | ...° vs ...° |
| Sudut bend 2 (aktual vs target) | ...° vs ...° |
| Gap tab-slot | ... mm |
| Overall quality (1-10) | ... |

---

## 11. Keselamatan Kerja

### 11.1 Keselamatan Laser Cutting Akrilik
| Bahaya | Risiko | Pencegahan |
|--------|--------|-----------|
| Asap/gas toksik | Iritasi pernapasan | Pastikan exhaust/ventilasi aktif |
| Nyala api | Material terbakar | Monitor, siapkan pemadam |
| Sinar laser | Cedera mata | Jangan lihat langsung, pakai kacamata laser |
| Edge tajam | Luka gores | Hati-hati handling, amplas edge |

### 11.2 Keselamatan Bending
| Bahaya | Risiko | Pencegahan |
|--------|--------|-----------|
| Permukaan panas | Luka bakar | Sarung tangan tahan panas |
| Strip heater | Kontak langsung | Jangan sentuh elemen |
| Heat gun | Luka bakar, overheating | Jaga jarak, jangan arahkan ke orang |
| Akrilik patah | Serpihan tajam | Kacamata pelindung |
| Lem akrilik (solvent) | Iritasi kulit/mata, inhalasi | Sarung tangan, ventilasi, hindari kontak |

### 11.3 APD (Alat Pelindung Diri)
- ✅ Kacamata pelindung (wajib)
- ✅ Sarung tangan tahan panas (saat bending)
- ✅ Sarung tangan nitril (saat menggunakan lem)
- ✅ Masker (saat laser cutting dan lem)
- ✅ Sepatu tertutup

---

## Referensi
1. SolidWorks Help — Sheet Metal Features
2. CorelDRAW Documentation — DXF Import/Export
3. PMMA/Acrylic Material Data Sheet
4. Thermoforming & Bending Acrylic — Best Practices
5. Laser Cutting Parameters Database
6. Acrifix Technical Data Sheets

---

*Materi Praktikum CAD/CAM — Modul 14 — CAM Laser Cutting, Sheet Metal & Bending Akrilik*
