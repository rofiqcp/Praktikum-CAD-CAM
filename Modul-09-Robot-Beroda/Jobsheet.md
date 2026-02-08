# JOBSHEET MODUL 9: PROJECT CAD — ROBOT BERODA FLAT-PACK AKRILIK

## Praktikum CAD/CAM — Pertemuan 9

---

## I. Tujuan Praktikum
1. Mahasiswa mampu mengkonsep desain robot beroda dengan pendekatan flat-pack (2D → 3D)
2. Mahasiswa mampu mendesain panel-panel akrilik dengan interlocking tab-slot
3. Mahasiswa mampu mengintegrasikan desain mekanik dengan komponen elektronik
4. Mahasiswa mampu membuat nesting layout DXF untuk laser cutting
5. Mahasiswa memahami konsep Design for Manufacturing (DFM) dan Design for Assembly (DFA)

---

## II. Alat dan Bahan
| No | Alat/Bahan | Keterangan |
|----|------------|------------|
| 1 | Laptop/PC + SolidWorks | Semua modul |
| 2 | CorelDRAW | Layout nesting DXF |
| 3 | Datasheet motor DC N20/130 | Dimensi mounting |
| 4 | Datasheet Arduino Uno | Mounting holes pattern |
| 5 | Datasheet sensor HC-SR04 | Dimensi sensor |

---

## III. Landasan Teori
Lihat **Materi.md** Modul 9 untuk:
- Konsep differential drive dan kinematika
- Desain flat-pack akrilik (2D → 3D balok)
- Teknik interlocking tab-slot dan toleransi
- Komponen & BOM robot beroda
- Koneksi realisasi ke Modul 10 (Laser Cutting)

---

## IV. Langkah Percobaan
| No | Komponen | Teknik | Export |
|----|----------|--------|--------|
| 1 | Bottom Panel / Chassis | Extrude + Tab Pattern | **DXF** |
| 2 | Side Panel L & R | Extrude + Cutout + Tab | **DXF** |
| 3 | Front Panel | Extrude + Hole + Tab | **DXF** |
| 4 | Back Panel | Extrude + Cutout + Tab | **DXF** |
| 5 | Top Panel + **Engrave Nama** | Extrude + Text + Tab | **DXF** (multi-layer) |
| 6 | Motor Mount Panel (internal) | Extrude + Tab | **DXF** |
| 7 | PCB Shelf + Battery Bracket | Extrude + Tab | **DXF** |
| 8 | Sensor Bracket | Extrude + Tab | **DXF** |
| 9 | Assembly + Nesting DXF | Assembly + CorelDRAW | **CDR** |
| 10 | Drawing Package + Export Final | Drawing + BOM | **PDF** |

---

## V. Analisa dan Pembahasan
1. Jelaskan kelebihan desain flat-pack akrilik (2D → 3D) dibanding chassis monolit (1 piece)
2. Analisis toleransi tab-slot: berapa toleransi optimal untuk akrilik 3mm agar press-fit tanpa lem?
3. Diskusikan pengaruh posisi center of gravity terhadap stabilitas robot (posisi baterai!)
4. Bagaimana desain mengakomodasi proses laser cutting? (kerf, tab-slot, nesting)
5. Jelaskan pentingnya engraving nama/identitas pada produk — dan mengapa laser engrave cocok
6. Analisis berapa banyak akrilik yang dibutuhkan (hitung total area flat pattern vs ukuran sheet)

---

## VI. Kesimpulan
Rangkum proses desain robot beroda dari konsep flat-pack → CAD → DXF → nesting → siap laser cut.

---

## VII. Tugas

### Video (10–15 menit):
| Segmen | Durasi | Isi |
|--------|--------|-----|
| 1. Penjelasan Konsep | 2–3 menit | Flat-pack 2D→3D, differential drive |
| 2. Demo SolidWorks | 5–7 menit | Screen record: panel design + tab-slot + assembly |
| 3. Demo Nesting | 2–3 menit | CorelDRAW: nesting layout + layer warna |
| 4. Analisa & Kesimpulan | 2–3 menit | DFM, toleransi, material usage |

### Pengumpulan:
```
NIM_Nama_Modul09/
├── SolidWorks/ (semua .sldprt + .sldasm)
├── DXF/ (semua panel flat pattern)
├── CorelDRAW/ (nesting layout .cdr)
├── Drawing/ (.slddrw / .pdf)
├── Video/ (NIM_Nama_Modul09.mp4)
└── BOM.xlsx atau BOM.pdf
```
Kompres → `NIM_Nama_Modul09.zip`

---

*Jobsheet Praktikum CAD/CAM — Modul 9*
