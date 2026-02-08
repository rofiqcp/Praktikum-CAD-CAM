# JOBSHEET MODUL 1: PERKENALAN CAD/CAM & INSTALASI SOLIDWORKS

## Praktikum CAD/CAM — Pertemuan 1

---

## I. Tujuan Praktikum

1. Mahasiswa mampu memahami konsep dasar CAD/CAM dan penerapannya dalam industri
2. Mahasiswa mampu mengenali dan memahami istilah-istilah dalam CAD/CAM
3. Mahasiswa mampu mengidentifikasi software dan hardware yang digunakan dalam praktikum
4. Mahasiswa mampu menginstal dan mengkonfigurasi SolidWorks beserta software pendukung
5. Mahasiswa mampu menavigasi antarmuka dasar SolidWorks
6. Mahasiswa mampu memahami alur kerja (workflow) CAD dan CAM
7. Mahasiswa mampu membuat dan menyimpan file project pertama di SolidWorks

---

## II. Alat dan Bahan

### Perangkat Keras:
| No | Alat/Bahan | Spesifikasi | Jumlah |
|----|------------|-------------|--------|
| 1 | Laptop/PC | Min. i5, 8GB RAM, GPU dedicated | 1 unit |
| 2 | Mouse | 3-button mouse (scroll wheel) | 1 unit |
| 3 | USB Flash Drive | Min. 8GB (backup file) | 1 unit |
| 4 | Headset/Earphone | Untuk video tutorial | 1 unit |

### Perangkat Lunak:
| No | Software | Versi | Keterangan |
|----|----------|-------|------------|
| 1 | SolidWorks | 2021/2022/2023/2024 | Software CAD utama |
| 2 | CorelDRAW | 2021+ | Pendukung laser cutting |
| 3 | Fusion 360 | Latest | CAM router milling |
| 4 | Ultimaker Cura | 5.x | Slicer 3D printing |
| 5 | OBS Studio | Latest | Screen recording |
| 6 | Web Browser | Chrome/Firefox | Akses referensi online |

### Bahan Pendukung:
| No | Bahan | Keterangan |
|----|-------|------------|
| 1 | Modul Praktikum (digital) | File PDF/MD |
| 2 | Internet | Untuk download dan aktivasi |
| 3 | Serial Number SolidWorks | Dari asisten/lisensi kampus |

---

## III. Landasan Teori

### 3.1 Computer-Aided Design (CAD)
CAD adalah teknologi yang menggunakan sistem komputer untuk membantu proses desain, mulai dari pembuatan konsep, perancangan, analisis, hingga pembuatan gambar teknik. Dalam konteks manufaktur, CAD memungkinkan insinyur untuk membuat model digital yang akurat sebelum produk fisik dibuat.

**Keuntungan CAD:**
- Presisi tinggi dalam perancangan
- Mudah dimodifikasi dan direvisi
- Dapat disimulasikan sebelum produksi
- Dokumentasi otomatis (gambar teknik)
- Kolaborasi tim yang lebih baik
- Mengurangi biaya prototipe fisik

### 3.2 Computer-Aided Manufacturing (CAM)
CAM adalah penggunaan software komputer untuk mengendalikan mesin perkakas dan peralatan produksi. CAM mengambil output dari CAD dan mengubahnya menjadi instruksi mesin.

**Proses CAM meliputi:**
- Tool path generation (pembuatan jalur pahat)
- Simulasi proses manufaktur
- Post-processing (konversi ke G-code)
- Optimasi parameter pemotongan

### 3.3 SolidWorks
SolidWorks adalah software CAD 3D parametrik yang dikembangkan oleh Dassault Systèmes. SolidWorks menggunakan pendekatan feature-based modeling dan parametric design, di mana model 3D dibangun dari serangkaian feature yang dapat dimodifikasi melalui parameter (dimensi).

### 3.4 Workflow CAD/CAM
Alur kerja dalam CAD/CAM mengikuti tahapan:
1. **Conceptual Design** — Menentukan konsep dan spesifikasi
2. **Detailed Design (CAD)** — Membuat model 3D detail
3. **Analysis** — Simulasi dan validasi desain
4. **Manufacturing Planning (CAM)** — Merencanakan proses produksi
5. **Production** — Eksekusi di mesin

---

## IV. Langkah Percobaan

### Percobaan 1: Instalasi SolidWorks
**Tujuan**: Menginstal SolidWorks di komputer masing-masing

**Langkah-langkah:**
1. Buka folder installer SolidWorks
2. Klik kanan `setup.exe` → **Run as Administrator**
3. Pilih **Individual Installation** → Next
4. Masukkan Serial Number yang diberikan
5. Pilih komponen: SolidWorks, Toolbox, eDrawings
6. Tentukan lokasi instalasi
7. Klik **Install Now**
8. Tunggu hingga selesai → Restart komputer
9. Buka SolidWorks dan verifikasi aktivasi
10. Screenshot halaman utama SolidWorks yang berhasil dibuka

### Percobaan 2: Konfigurasi Awal SolidWorks
**Tujuan**: Mengatur konfigurasi dasar SolidWorks

**Langkah-langkah:**
1. Buka SolidWorks
2. Pergi ke `Tools → Options → System Options`
3. Set **Default Templates** → pilih template ISO
4. Pergi ke `Document Properties → Units`
5. Set unit ke **MMGS** (millimeter, gram, second)
6. Set drafting standard ke **ISO**
7. Pergi ke `System Options → Colors` → atur warna background
8. Pergi ke `System Options → Performance` → atur sesuai spesifikasi komputer
9. Simpan konfigurasi
10. Screenshot halaman konfigurasi unit

### Percobaan 3: Mengenal Antarmuka SolidWorks
**Tujuan**: Memahami setiap komponen antarmuka

**Langkah-langkah:**
1. Buka SolidWorks → New → Part
2. Identifikasi dan screenshot **Menu Bar**
3. Identifikasi dan screenshot **Command Manager** — catat semua tab yang ada
4. Identifikasi **Feature Manager Design Tree** — catat item default
5. Identifikasi **Graphics Area**
6. Identifikasi **Status Bar** — catat informasi yang ditampilkan
7. Buka **Task Pane** (klik panah di sisi kanan)
8. Identifikasi **Heads-Up View Toolbar**
9. Coba semua tab di Command Manager: Features, Sketch, Evaluate, DimXpert, Sheet Metal
10. Screenshot keseluruhan interface dengan label setiap komponen

### Percobaan 4: Navigasi 3D
**Tujuan**: Menguasai navigasi dalam ruang 3D

**Langkah-langkah:**
1. Buka file part baru atau contoh part dari Toolbox
2. Praktikkan **Rotate** — Middle Mouse Button + geser
3. Praktikkan **Pan** — Ctrl + Middle Mouse Button + geser
4. Praktikkan **Zoom In/Out** — Scroll wheel
5. Praktikkan **Zoom to Fit** — Tekan F
6. Praktikkan **View Orientation** — Ctrl+1 (Front), Ctrl+5 (Top), Ctrl+7 (Isometric)
7. Gunakan **View Orientation Cube** (klik sudut/sisi)
8. Coba **Section View** dari View menu
9. Coba **Display Style**: Wireframe, Hidden Lines, Shaded, Shaded with Edges
10. Screenshot masing-masing tampilan view orientation

### Percobaan 5: Membuat File Baru dan Menyimpan
**Tujuan**: Memahami pembuatan dan pengelolaan file

**Langkah-langkah:**
1. Buat folder: `D:\Praktikum-CADCAM\Modul-01\`
2. Buat file **Part** baru (`Ctrl+N → Part`)
3. Simpan dengan nama: `NIM_Nama_M01_Part01.sldprt`
4. Buat file **Assembly** baru (`Ctrl+N → Assembly`)
5. Simpan dengan nama: `NIM_Nama_M01_Assembly01.sldasm`
6. Buat file **Drawing** baru (`Ctrl+N → Drawing`)
7. Simpan dengan nama: `NIM_Nama_M01_Drawing01.slddrw`
8. Coba **Save As** dengan format berbeda (.step, .stl)
9. Coba **Pack and Go** (`File → Pack and Go`)
10. Screenshot folder berisi semua file yang dibuat

### Percobaan 6: Mengenal Feature Manager Design Tree
**Tujuan**: Memahami struktur dan fungsi Design Tree

**Langkah-langkah:**
1. Buka file Part yang sudah dibuat
2. Perhatikan item default di Design Tree:
   - Sensors
   - Annotations
   - Material (not specified)
   - Front Plane
   - Top Plane
   - Right Plane
   - Origin
3. Klik kanan **Front Plane** → pilih **Sketch** → gambar kotak sederhana → Exit Sketch
4. Perhatikan perubahan di Design Tree (Sketch1 muncul)
5. Pilih Sketch1 → Features → **Extruded Boss/Base** → Depth 20mm → OK
6. Perhatikan perubahan di Design Tree (Boss-Extrude1 muncul)
7. Coba **expand** dan **collapse** item di Design Tree
8. Coba **Rename** feature (klik 2x pada nama)
9. Coba **Suppress** feature (klik kanan → Suppress)
10. Screenshot Design Tree yang menampilkan semua item

### Percobaan 7: Instalasi CorelDRAW
**Tujuan**: Menginstal CorelDRAW untuk keperluan laser cutting

**Langkah-langkah:**
1. Download installer CorelDRAW dari sumber yang disediakan
2. Jalankan installer
3. Ikuti wizard instalasi
4. Pilih komponen yang diperlukan
5. Tunggu instalasi selesai
6. Buka CorelDRAW dan verifikasi
7. Buat dokumen baru dengan ukuran A4
8. Coba import file DXF sederhana
9. Eksplorasi antarmuka dasar CorelDRAW
10. Screenshot halaman utama CorelDRAW

### Percobaan 8: Instalasi Fusion 360
**Tujuan**: Menginstal Fusion 360 untuk keperluan CAM

**Langkah-langkah:**
1. Buka https://www.autodesk.com/products/fusion-360
2. Buat akun Autodesk dengan email .edu
3. Download installer
4. Jalankan instalasi
5. Login ke Fusion 360
6. Verifikasi lisensi education
7. Eksplorasi antarmuka dasar Fusion 360
8. Coba membuat project baru
9. Identifikasi workspace: Design, Render, Animate, Manufacture
10. Screenshot halaman utama Fusion 360

### Percobaan 9: Instalasi Software 3D Printing (Cura)
**Tujuan**: Menginstal slicer software untuk 3D printing

**Langkah-langkah:**
1. Buka https://ultimaker.com/software/ultimaker-cura
2. Download Ultimaker Cura versi terbaru
3. Jalankan instalasi
4. Pilih printer: Generic FDM Printer (atau sesuai lab)
5. Konfigurasi profil default:
   - Layer height: 0.2mm
   - Infill: 20%
   - Support: None
6. Buka Cura dan verifikasi
7. Coba load file STL contoh
8. Eksplorasi pengaturan: Quality, Shell, Infill, Support
9. Coba slice file contoh dan lihat preview
10. Screenshot halaman utama Cura dengan file contoh

### Percobaan 10: Instalasi OBS Studio dan Percobaan Screen Recording
**Tujuan**: Menginstal OBS Studio untuk dokumentasi video praktikum

**Langkah-langkah:**
1. Buka https://obsproject.com
2. Download OBS Studio
3. Jalankan instalasi
4. Buka OBS Studio → Auto-Configuration Wizard
5. Pilih **Optimize for recording**
6. Set resolusi: 1920x1080
7. Set FPS: 30
8. Tambahkan **Display Capture** source
9. Tambahkan **Audio Input Capture** (Microphone)
10. Coba rekam 30 detik, putar video hasilnya, dan screenshot pengaturan OBS

---

## V. Analisa dan Pembahasan

Jawab pertanyaan-pertanyaan berikut secara lengkap:

### Analisa:
1. **Jelaskan perbedaan antara CAD dan CAM!** Berikan contoh penerapan masing-masing dalam industri manufaktur.

2. **Bandingkan kelebihan dan kekurangan** menggunakan SolidWorks dibandingkan software CAD lain yang Anda ketahui (AutoCAD, Inventor, Fusion 360).

3. **Jelaskan mengapa unit MMGS dan standar ISO** dipilih sebagai default dalam praktikum ini. Apa dampaknya jika menggunakan unit yang berbeda?

4. **Analisis alur kerja (workflow)** dari desain hingga produksi untuk masing-masing proses:
   - Laser Cutting
   - 3D Printing
   - Router Milling

5. **Identifikasi minimal 5 komponen antarmuka SolidWorks** dan jelaskan fungsi masing-masing beserta cara mengaksesnya.

### Pembahasan:
1. Diskusikan tantangan yang dihadapi selama proses instalasi dan bagaimana mengatasinya.
2. Jelaskan pentingnya konfigurasi awal (unit, template, standar) sebelum memulai desain.
3. Bandingkan navigasi 3D di SolidWorks dengan software 3D lain yang pernah Anda gunakan.
4. Jelaskan peran masing-masing software pendukung (CorelDRAW, Fusion 360, Cura) dalam workflow CAM.
5. Bagaimana pemahaman istilah-istilah CAD/CAM akan membantu dalam praktikum selanjutnya?

---

## VI. Kesimpulan

Tuliskan kesimpulan yang mencakup:
1. Pemahaman tentang konsep CAD/CAM secara keseluruhan
2. Kesiapan software dan hardware untuk praktikum selanjutnya
3. Penguasaan navigasi dasar SolidWorks
4. Pemahaman alur kerja CAD dan CAM
5. Kesiapan perangkat dokumentasi (OBS Studio)

---

## VII. Tugas

### Tugas Video:
Buat video **berdurasi 10-15 menit** yang mencakup:

1. **Penjelasan Materi** (5-7 menit):
   - Jelaskan apa itu CAD dan CAM
   - Sebutkan dan jelaskan minimal 10 istilah penting
   - Jelaskan software yang digunakan dan fungsinya
   - Jelaskan alur kerja CAD dan CAM

2. **Penjelasan Ulang Percobaan 1-10** (5-7 menit):
   - Rekam layar (screen record) saat menunjukkan:
     - SolidWorks yang sudah terinstal dan dikonfigurasi
     - Demonstrasi navigasi 3D
     - Pembuatan dan penyimpanan file
     - Semua software pendukung yang sudah terinstal
   - Jelaskan setiap langkah yang dilakukan

3. **Analisa dan Kesimpulan** (2-3 menit):
   - Sampaikan analisa dari hasil percobaan
   - Berikan kesimpulan

### Ketentuan Video:
- Format: MP4
- Resolusi: Minimal 720p (1280x720), direkomendasikan 1080p
- Audio: Jelas, narasi menggunakan bahasa Indonesia
- Wajah terlihat (menggunakan HP untuk merekam diri + screen record)
- Screen recording menggunakan OBS Studio
- **Penamaan file**: `NIM_Nama_Modul01_Video.mp4`

### Tugas Pengumpulan File:
Kumpulkan semua file berikut dalam satu folder terkompresi (.zip):
1. Screenshot semua percobaan (10 percobaan)
2. File SolidWorks (.sldprt, .sldasm, .slddrw)
3. Video penjelasan (.mp4)
4. Laporan jobsheet (.pdf)
5. **Penamaan folder**: `NIM_Nama_Modul01.zip`

---

## VIII. Rubrik Penilaian

### Penilaian Percobaan (30%):
| Kriteria | Bobot |
|----------|-------|
| Semua software terinstal dengan benar | 10% |
| Konfigurasi SolidWorks sesuai standar | 5% |
| Navigasi 3D dikuasai | 5% |
| File tersimpan dengan format penamaan benar | 5% |
| Screenshot lengkap dan jelas | 5% |

### Penilaian Video (20%):
| Kriteria | Bobot |
|----------|-------|
| Penjelasan materi lengkap dan benar | 8% |
| Demonstrasi percobaan jelas | 7% |
| Kualitas video dan audio | 5% |

### Penilaian Laporan (15%):
| Kriteria | Bobot |
|----------|-------|
| Kelengkapan laporan | 5% |
| Analisa dan pembahasan | 5% |
| Kesimpulan | 5% |

---

*Jobsheet Praktikum CAD/CAM — Modul 1: Perkenalan & Instalasi*
*Disusun untuk keperluan pendidikan*
