# MODUL 1: PERKENALAN CAD/CAM & INSTALASI SOLIDWORKS

## Praktikum CAD/CAM — Pertemuan 1

---

## 1.1 Pendahuluan

### Apa itu CAD?
**CAD (Computer-Aided Design)** adalah penggunaan perangkat lunak komputer untuk membuat, memodifikasi, menganalisis, dan mengoptimasi desain. CAD digunakan secara luas di berbagai industri seperti otomotif, aerospace, manufaktur, arsitektur, dan robotika.

### Apa itu CAM?
**CAM (Computer-Aided Manufacturing)** adalah penggunaan perangkat lunak dan mesin yang dikontrol komputer untuk mengotomatisasi proses manufaktur. CAM mengambil desain dari CAD dan mengubahnya menjadi instruksi mesin (G-code) untuk proses produksi.

### Hubungan CAD dan CAM
```
[Desain (CAD)] → [Proses (CAM)] → [Produksi (Mesin CNC/3D Printer/Laser)]
```

---

## 1.2 Istilah-Istilah Penting dalam CAD/CAM

### Istilah CAD Dasar:

| No | Istilah | Definisi |
|----|---------|----------|
| 1 | **Sketch** | Gambar 2D dasar yang menjadi fondasi pembuatan model 3D |
| 2 | **Feature** | Operasi 3D yang diterapkan pada sketch (extrude, revolve, dll.) |
| 3 | **Part** | File tunggal yang berisi satu komponen 3D (.sldprt) |
| 4 | **Assembly** | File yang menggabungkan beberapa part menjadi satu rakitan (.sldasm) |
| 5 | **Drawing** | File gambar teknik 2D dari part/assembly (.slddrw) |
| 6 | **Plane** | Bidang referensi untuk membuat sketch (Front, Top, Right) |
| 7 | **Origin** | Titik asal (0,0,0) dalam ruang 3D |
| 8 | **Constraint** | Hubungan geometris antar entitas sketch (horizontal, vertical, coincident, dll.) |
| 9 | **Dimension** | Ukuran yang diberikan pada entitas sketch |
| 10 | **Fully Defined** | Kondisi sketch yang semua geometri dan posisinya sudah terdefinisi |
| 11 | **Under Defined** | Kondisi sketch yang masih memiliki derajat kebebasan |
| 12 | **Over Defined** | Kondisi sketch yang memiliki constraint berlebihan |
| 13 | **Extrude** | Menarik sketch 2D menjadi bentuk 3D |
| 14 | **Revolve** | Memutar sketch 2D mengelilingi sumbu menjadi bentuk 3D |
| 15 | **Fillet** | Pembulatan pada sudut/tepi |
| 16 | **Chamfer** | Potongan miring pada sudut/tepi |
| 17 | **Shell** | Membuat benda menjadi berongga |
| 18 | **Pattern** | Pengulangan feature secara linear atau circular |
| 19 | **Mirror** | Pencerminan feature atau sketch |
| 20 | **Loft** | Membuat bentuk 3D dari beberapa profil sketch |

### Istilah CAM:

| No | Istilah | Definisi |
|----|---------|----------|
| 1 | **Toolpath** | Jalur yang diikuti oleh alat potong pada proses manufaktur |
| 2 | **G-code** | Bahasa pemrograman untuk mesin CNC |
| 3 | **Feed Rate** | Kecepatan pergerakan alat potong |
| 4 | **Spindle Speed** | Kecepatan putaran spindle (RPM) |
| 5 | **DOC (Depth of Cut)** | Kedalaman pemotongan per pass |
| 6 | **WOC (Width of Cut)** | Lebar pemotongan |
| 7 | **Post Processor** | Software yang mengubah toolpath menjadi G-code spesifik mesin |
| 8 | **Stock** | Material mentah yang akan diproses |
| 9 | **Fixture** | Alat penjepit/penahan benda kerja |
| 10 | **STL** | Format file standar untuk 3D printing (STereoLithography) |
| 11 | **DXF/DWG** | Format file untuk laser cutting |
| 12 | **Kerf** | Lebar material yang hilang akibat pemotongan |
| 13 | **Nesting** | Pengaturan layout potongan untuk efisiensi material |
| 14 | **Slicing** | Proses memotong model 3D menjadi layer untuk 3D printing |
| 15 | **Infill** | Pengisian internal pada 3D printing |

### Istilah Assembly:

| No | Istilah | Definisi |
|----|---------|----------|
| 1 | **Mate** | Hubungan posisional antar komponen dalam assembly |
| 2 | **Coincident** | Mate yang membuat dua permukaan/titik/sumbu bertemu |
| 3 | **Concentric** | Mate yang membuat dua silinder/lingkaran sesumbu |
| 4 | **Distance** | Mate yang memberikan jarak tertentu antar komponen |
| 5 | **Angle** | Mate yang memberikan sudut tertentu antar komponen |
| 6 | **BOM (Bill of Materials)** | Daftar komponen dalam assembly |
| 7 | **Exploded View** | Tampilan assembly yang komponen-komponennya terpisah |
| 8 | **Sub-assembly** | Assembly yang menjadi bagian dari assembly lain |
| 9 | **Interference Detection** | Pengecekan tabrakan antar komponen |

### Istilah Sheet Metal:

| No | Istilah | Definisi |
|----|---------|----------|
| 1 | **Gauge** | Ketebalan plat logam |
| 2 | **Bend Radius** | Jari-jari tekukan |
| 3 | **K-Factor** | Faktor koreksi untuk perhitungan panjang tekukan |
| 4 | **Bend Allowance** | Panjang material pada daerah tekukan |
| 5 | **Flat Pattern** | Pola bentangan plat sebelum ditekuk |
| 6 | **Hem** | Tekukan 180° pada tepi plat |
| 7 | **Flange** | Bagian plat yang ditekuk |
| 8 | **Tab** | Bagian plat yang menonjol |
| 9 | **Relief** | Potongan pada sudut untuk memudahkan tekukan |

---

## 1.3 Software yang Digunakan dalam Praktikum

### Software Utama:

#### 1. SolidWorks (CAD Utama)
- **Versi**: SolidWorks 2021/2022/2023/2024
- **Fungsi**: Desain 2D, 3D, Assembly, Drawing, Sheet Metal, Simulation
- **Format file**: .sldprt, .sldasm, .slddrw
- **Lisensi**: Educational License

#### 2. CorelDRAW (Pendukung Laser Cutting)
- **Versi**: CorelDRAW 2021 atau lebih baru
- **Fungsi**: Persiapan file untuk laser cutting, editing vektor
- **Format file**: .cdr, .dxf, .ai
- **Alur**: SolidWorks → Export DXF → CorelDRAW → Laser Cutter

#### 3. Fusion 360 (CAM Router Milling)
- **Versi**: Fusion 360 (Cloud-based, free for education)
- **Fungsi**: CAM untuk router milling, toolpath generation
- **Format file**: .f3d, .step, .iges
- **Alur**: SolidWorks → Export STEP → Fusion 360 → G-code → CNC Router

#### 4. Software 3D Printer (Slicer)
- **Pilihan**: Cura / PrusaSlicer / Bambu Studio
- **Fungsi**: Slicing model 3D menjadi G-code untuk 3D printer
- **Format input**: .stl, .3mf, .obj
- **Alur**: SolidWorks → Export STL → Slicer → G-code → 3D Printer

#### 5. Software Laser Cutting
- **Pilihan**: RDWorks / LightBurn / LaserCAD
- **Fungsi**: Kontrol mesin laser cutting
- **Format input**: .dxf, .ai, .rd

### Software Pendukung:

| No | Software | Fungsi |
|----|----------|--------|
| 1 | OBS Studio | Screen recording untuk dokumentasi |
| 2 | HandBrake | Kompresi video |
| 3 | Paint/GIMP | Screenshot dan editing gambar |
| 4 | Google Drive | Pengumpulan tugas |

---

## 1.4 Hardware/Mesin yang Digunakan

### Mesin Produksi:

| No | Mesin | Spesifikasi | Software Terkait |
|----|-------|-------------|------------------|
| 1 | **Laser Cutter CO2** | Area kerja 600x400mm, 60-80W | RDWorks/CorelDRAW |
| 2 | **3D Printer FDM** | PLA/PETG, nozzle 0.4mm | Cura/PrusaSlicer |
| 3 | **CNC Router** | 3-axis, area kerja 600x900mm | Fusion 360 CAM |

### Material:

| No | Material | Penggunaan |
|----|----------|------------|
| 1 | Akrilik 2-5mm | Laser cutting |
| 2 | MDF 3-6mm | Laser cutting |
| 3 | Filamen PLA 1.75mm | 3D printing |
| 4 | Kayu/MDF tebal | CNC Router milling |
| 5 | Profil Aluminium | Konstruksi mekanik |

---

## 1.5 Antarmuka SolidWorks

### Area Kerja SolidWorks:

```
┌─────────────────────────────────────────────────────┐
│  Menu Bar   │ File │ Edit │ View │ Insert │ Tools  │
├─────────────────────────────────────────────────────┤
│  Command Manager (Tab: Features, Sketch, dll.)      │
├──────────┬──────────────────────────────────────────┤
│          │                                          │
│ Feature  │                                          │
│ Manager  │        Graphics Area                     │
│ Design   │        (Area Gambar Utama)                │
│ Tree     │                                          │
│          │                                          │
│          │                                          │
├──────────┴──────────────────────────────────────────┤
│  Status Bar  │ Units │ Sketch Status │              │
└─────────────────────────────────────────────────────┘
```

### Komponen Utama Interface:

1. **Menu Bar** — Akses semua fungsi melalui menu dropdown
2. **Command Manager** — Tab berisi tool yang dikelompokkan (Features, Sketch, Evaluate, dll.)
3. **Feature Manager Design Tree** — Menampilkan struktur/hierarki model
4. **Graphics Area** — Area kerja utama untuk menampilkan model
5. **Property Manager** — Panel untuk mengatur properti tool yang aktif
6. **Status Bar** — Informasi status sketch dan unit
7. **Task Pane** — Panel samping kanan untuk Design Library, File Explorer, dll.
8. **Heads-Up View Toolbar** — Kontrol tampilan (zoom, rotate, view orientation)

### Navigasi Dasar:

| Aksi | Mouse/Keyboard |
|------|----------------|
| **Rotate** | Middle Mouse Button (tekan & geser) |
| **Pan** | Ctrl + Middle Mouse Button |
| **Zoom** | Scroll Wheel |
| **Zoom to Fit** | F (keyboard) |
| **Front View** | Ctrl + 1 |
| **Back View** | Ctrl + 2 |
| **Left View** | Ctrl + 3 |
| **Right View** | Ctrl + 4 |
| **Top View** | Ctrl + 5 |
| **Bottom View** | Ctrl + 6 |
| **Isometric View** | Ctrl + 7 |

### Shortcut Keyboard Penting:

| Shortcut | Fungsi |
|----------|--------|
| S | Shortcut Bar |
| L | Line |
| C | Circle |
| R | Rectangle |
| D | Smart Dimension |
| Ctrl+Z | Undo |
| Ctrl+Y | Redo |
| Ctrl+S | Save |
| Ctrl+N | New |
| Ctrl+O | Open |
| Ctrl+Q | Rebuild All |
| Ctrl+B | Rebuild |
| Esc | Cancel/Deselect |

---

## 1.6 Tipe File SolidWorks

| Ekstensi | Deskripsi |
|----------|-----------|
| .sldprt | SolidWorks Part — File komponen tunggal |
| .sldasm | SolidWorks Assembly — File rakitan |
| .slddrw | SolidWorks Drawing — File gambar teknik 2D |
| .sldlfp | SolidWorks Library Feature Part |
| .sldbom | SolidWorks Bill of Materials |

### Format Ekspor Umum:

| Format | Ekstensi | Penggunaan |
|--------|----------|------------|
| STEP | .step, .stp | Pertukaran antar software CAD |
| IGES | .iges, .igs | Pertukaran data geometri |
| STL | .stl | 3D Printing |
| DXF | .dxf | Laser cutting, CNC 2D |
| PDF | .pdf | Dokumentasi gambar teknik |
| eDrawings | .edrw | Review desain |
| Parasolid | .x_t, .x_b | Pertukaran data solid |
| 3MF | .3mf | 3D Printing (format baru) |

---

## 1.7 Unit dan Standar

### Sistem Unit dalam SolidWorks:

| Sistem | Unit Panjang | Penggunaan |
|--------|-------------|------------|
| **MMGS** | Milimeter, Gram, Second | **Standar praktikum ini** |
| IPS | Inch, Pound, Second | Standar Amerika |
| CGS | Centimeter, Gram, Second | Ilmiah |
| MKS | Meter, Kilogram, Second | SI |

### Mengatur Unit:
```
Tools → Options → Document Properties → Units → MMGS
```

### Standar Gambar Teknik:
- **ISO** (International Organization for Standardization) — **Digunakan dalam praktikum**
- ANSI (American National Standards Institute)
- DIN (Deutsches Institut für Normung)
- JIS (Japanese Industrial Standards)

### Proyeksi:
- **First Angle Projection** (ISO/Eropa) — **Digunakan dalam praktikum**
- Third Angle Projection (ANSI/Amerika)

---

## 1.8 Instalasi SolidWorks

### Spesifikasi Minimum Komputer:

| Komponen | Minimum | Rekomendasi |
|----------|---------|-------------|
| **OS** | Windows 10 64-bit | Windows 10/11 64-bit |
| **CPU** | Intel/AMD 64-bit | Intel Core i7 / AMD Ryzen 7 |
| **RAM** | 8 GB | 16 GB atau lebih |
| **GPU** | OpenGL 4.5 capable | NVIDIA Quadro / GeForce GTX/RTX |
| **Storage** | 10 GB free | SSD 256 GB+ |
| **Display** | 1920x1080 | 1920x1080 atau lebih |

### Langkah Instalasi SolidWorks:

#### Langkah 1: Persiapan
1. Pastikan komputer memenuhi spesifikasi minimum
2. Matikan antivirus sementara
3. Pastikan koneksi internet stabil
4. Siapkan serial number / license key

#### Langkah 2: Download
1. Akses portal SolidWorks (student portal atau media instalasi)
2. Download SolidWorks Installation Manager
3. Pilih versi yang sesuai (2021/2022/2023/2024)

#### Langkah 3: Instalasi
1. Jalankan setup.exe sebagai Administrator (Klik kanan → Run as Administrator)
2. Pilih **Individual Installation**
3. Masukkan Serial Number
4. Pilih produk yang akan diinstal:
   - ✅ SolidWorks
   - ✅ SolidWorks Toolbox
   - ✅ SolidWorks Simulation (opsional)
   - ✅ SolidWorks eDrawings
5. Tentukan lokasi instalasi (default: C:\Program Files\SolidWorks Corp)
6. Klik **Install Now**
7. Tunggu proses instalasi selesai (±30-60 menit)
8. Restart komputer

#### Langkah 4: Aktivasi
1. Buka SolidWorks
2. Pilih metode aktivasi:
   - Online Activation (jika ada internet)
   - Email Activation (offline)
3. Masukkan serial number jika diminta
4. Verifikasi aktivasi berhasil

#### Langkah 5: Konfigurasi Awal
1. Buka SolidWorks
2. Pilih unit system: **MMGS (millimeter, gram, second)**
3. Set dimensioning standard: **ISO**
4. Konfigurasi template:
   ```
   Tools → Options → System Options → Default Templates
   ```
5. Buat folder kerja praktikum:
   ```
   D:\Praktikum-CADCAM\
   ├── Modul-01\
   ├── Modul-02\
   ├── ...
   └── Modul-14\
   ```

---

## 1.9 Instalasi Software Pendukung

### Instalasi CorelDRAW:
1. Download CorelDRAW dari situs resmi
2. Jalankan installer
3. Ikuti wizard instalasi
4. Aktifkan dengan lisensi/trial

### Instalasi Fusion 360:
1. Kunjungi https://www.autodesk.com/products/fusion-360
2. Buat akun Autodesk (gunakan email .edu untuk lisensi education)
3. Download installer
4. Jalankan instalasi
5. Login dengan akun Autodesk

### Instalasi Cura (3D Printer Slicer):
1. Kunjungi https://ultimaker.com/software/ultimaker-cura
2. Download versi terbaru
3. Jalankan installer
4. Pilih printer yang tersedia di lab
5. Konfigurasi profil cetak default

### Instalasi OBS Studio (Screen Recording):
1. Kunjungi https://obsproject.com
2. Download untuk Windows
3. Jalankan instalasi
4. Konfigurasi:
   - Video: 1920x1080, 30fps
   - Audio: Desktop Audio + Microphone
   - Output: MP4/MKV format

---

## 1.10 Alur Kerja Praktikum (Workflow)

### Alur CAD:
```
Sketch 2D → Feature 3D → Part → Assembly → Drawing
```

### Alur CAM Laser Cutting:
```
SolidWorks (Part/Drawing) → Export DXF → CorelDRAW (Edit/Layout) → 
Software Laser (RDWorks) → Laser Cutter (Eksekusi)
```

### Alur CAM 3D Printing:
```
SolidWorks (Part 3D) → Export STL → Slicer (Cura/PrusaSlicer) → 
Export G-code → 3D Printer (Eksekusi)
```

### Alur CAM Router Milling:
```
SolidWorks (Part 3D) → Export STEP → Fusion 360 (Setup CAM) → 
Generate Toolpath → Post Process (G-code) → CNC Router (Eksekusi)
```

---

## 1.11 Aturan dan Ketentuan Praktikum

### Ketentuan Umum:
1. Praktikan **wajib** hadir tepat waktu
2. Membawa laptop dengan software terinstal
3. Memakai jas lab saat menggunakan mesin
4. Menyimpan file dengan format penamaan: `NIM_Nama_ModulXX_PercobaanYY`
5. Mengumpulkan tugas sebelum deadline

### Format Pengumpulan:
- **File CAD**: .sldprt, .sldasm, .slddrw
- **Video**: .mp4 (maksimal 500MB per video)
- **Laporan**: .pdf
- **Platform**: Google Classroom / Google Drive (link disediakan asisten)

### Komponen Penilaian:

| Komponen | Bobot |
|----------|-------|
| Kehadiran & Keaktifan | 10% |
| Percobaan 1-10 (per modul) | 30% |
| Project (per modul) | 25% |
| Video Penjelasan | 20% |
| Laporan (Jobsheet) | 15% |

---

## 1.12 Referensi dan Sumber Belajar

### Buku:
1. *SolidWorks 2024 Tutorial* — David Planchard
2. *Engineering Design with SolidWorks* — David Planchard
3. *Exploring Finite Element Simulations with SolidWorks* — Khairul Alam

### Online:
1. SolidWorks Help: help.solidworks.com
2. MySolidWorks Training: my.solidworks.com
3. YouTube Channel: SolidWorks Official
4. GrabCAD Library: grabcad.com (referensi model 3D)

### Forum & Komunitas:
1. SolidWorks Forum: forum.solidworks.com
2. Reddit: r/SolidWorks
3. Eng-Tips Forums

---

## Catatan Penting

> ⚠️ **PENTING**: Pastikan semua software terinstal dan berjalan dengan baik sebelum pertemuan ke-2. Jika ada kendala instalasi, segera hubungi asisten praktikum.

> 💡 **TIPS**: Biasakan menyimpan file secara berkala (Ctrl+S) dan membuat backup di cloud storage.

> 📌 **REMINDER**: Setiap pertemuan akan ada 10 percobaan + 1 project. Praktikan diharapkan sudah membaca materi sebelum praktikum dimulai.

---

*Modul Praktikum CAD/CAM — Modul 1: Perkenalan & Instalasi*
*Disusun untuk keperluan pendidikan*
