"""
VISUALISASI MODUL 7: CAD SHEET METAL
Generate ilustrasi untuk Materi dan Project:
- image/m01_deskripsi.png : Ringkasan materi Sheet Metal
- image/p01_deskripsi.png : Ringkasan project Enclosure + Aksesoris Aluminium
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, FancyArrowPatch
import os
import warnings
warnings.filterwarnings('ignore')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'image')
os.makedirs(IMG_DIR, exist_ok=True)

# WARNA
BG = '#F8F9FA'
C_TITLE = '#1A237E'
C_ACCENT = '#0D47A1'
C_BLUE = '#1565C0'
C_RED = '#C62828'
C_GREEN = '#2E7D32'
C_PURPLE = '#6A1B9A'
C_ORANGE = '#E65100'
C_TEAL = '#00695C'
C_LB = '#BBDEFB'
C_LG = '#C8E6C9'
C_LO = '#FFE0B2'
C_LR = '#FFCDD2'
C_LP = '#E1BEE7'


# ============================================================================
# HELPER: draw simple isometric
# ============================================================================
def iso(x, y, z):
    return x - 0.5*z, y + 0.35*z


def draw_flat_pattern(ax, cx, cy, w, h, flange_h, label='', color=C_BLUE):
    """Draw simplified flat pattern"""
    # Main body
    ax.add_patch(patches.Rectangle((cx-w/2, cy-h/2), w, h,
                                    facecolor='#ECEFF1', edgecolor=color, linewidth=1.5))
    # Flanges (dashed fold lines)
    for side in ['top', 'bottom', 'left', 'right']:
        if side == 'top':
            ax.add_patch(patches.Rectangle((cx-w/2, cy+h/2), w, flange_h,
                                            facecolor='#CFD8DC', edgecolor=color, linewidth=1, linestyle='--'))
        elif side == 'bottom':
            ax.add_patch(patches.Rectangle((cx-w/2, cy-h/2-flange_h), w, flange_h,
                                            facecolor='#CFD8DC', edgecolor=color, linewidth=1, linestyle='--'))
        elif side == 'left':
            ax.add_patch(patches.Rectangle((cx-w/2-flange_h, cy-h/2), flange_h, h,
                                            facecolor='#CFD8DC', edgecolor=color, linewidth=1, linestyle='--'))
        elif side == 'right':
            ax.add_patch(patches.Rectangle((cx+w/2, cy-h/2), flange_h, h,
                                            facecolor='#CFD8DC', edgecolor=color, linewidth=1, linestyle='--'))
    # Fold lines
    ax.plot([cx-w/2, cx+w/2], [cy+h/2, cy+h/2], color=color, linewidth=1.5, linestyle=':')
    ax.plot([cx-w/2, cx+w/2], [cy-h/2, cy-h/2], color=color, linewidth=1.5, linestyle=':')
    ax.plot([cx-w/2, cx-w/2], [cy-h/2, cy+h/2], color=color, linewidth=1.5, linestyle=':')
    ax.plot([cx+w/2, cx+w/2], [cy-h/2, cy+h/2], color=color, linewidth=1.5, linestyle=':')
    if label:
        ax.text(cx, cy, label, ha='center', va='center', fontsize=7, fontweight='bold', color=color)


# ============================================================================
# 1. MATERI DESKRIPSI (m01_deskripsi.png)
# ============================================================================
def generate_materi_image():
    fig = plt.figure(figsize=(18, 24), facecolor=BG)

    # HEADER
    fig.text(0.5, 0.975, 'MODUL 7: CAD SHEET METAL', ha='center', va='top',
             fontsize=24, fontweight='bold', color=C_TITLE,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#E3F2FD', edgecolor=C_ACCENT, linewidth=2))
    fig.text(0.5, 0.953, 'Desain Komponen Plat Logam — Bend, Flange, Flat Pattern & DXF Export',
             ha='center', va='top', fontsize=13, color='#546E7A', style='italic')

    # ==== SECTION 1: Konsep Dasar Sheet Metal ====
    ax1 = fig.add_axes([0.02, 0.78, 0.47, 0.16])
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 6)
    ax1.axis('off')
    ax1.set_title('1. PARAMETER SHEET METAL', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    params = [
        ('Thickness', 'Ketebalan plat (mm)', C_BLUE),
        ('Bend Radius', 'Jari-jari tekukan\n(umumnya = thickness)', C_GREEN),
        ('K-Factor', 'Posisi neutral axis\n0.33-0.45', C_PURPLE),
        ('Bend Allow.', 'Panjang material\npada daerah bend', C_ORANGE),
        ('Bend Deduct.', 'Pengurangan panjang\nakibat bend', C_TEAL),
        ('Relief Type', 'Rectangular / Oblong\n/ Tear', C_RED),
    ]
    for i, (title, desc, col) in enumerate(params):
        row = i // 3; ci = i % 3
        cx = 0.15 + ci * 3.3; cy = 4.5 - row * 2.8
        ax1.add_patch(FancyBboxPatch((cx, cy-0.4), 2.9, 2.2, boxstyle="round,pad=0.05",
                                      facecolor='white', edgecolor=col, linewidth=1.5))
        ax1.text(cx+1.45, cy+1.2, title, ha='center', fontsize=9, fontweight='bold', color=col)
        ax1.text(cx+1.45, cy+0.2, desc, ha='center', fontsize=7.5, color='#616161')

    # K-Factor values
    ax1.text(5, 0.3, 'K-Factor: Aluminum ≈ 0.33 | Mild Steel ≈ 0.40 | Stainless ≈ 0.45',
             ha='center', fontsize=8, style='italic', color='#424242',
             bbox=dict(boxstyle='round,pad=0.2', facecolor=C_LO, edgecolor=C_ORANGE, linewidth=1))

    # ==== SECTION 2: Sheet Metal Features ====
    ax2 = fig.add_axes([0.52, 0.78, 0.47, 0.16])
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 6)
    ax2.axis('off')
    ax2.set_title('2. SHEET METAL FEATURES (Utama)', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    features_main = [
        ('Base Flange', 'Profil utama\nsheet metal', C_BLUE),
        ('Edge Flange', 'Tekukan pada edge\nAngle, Length, Position', C_GREEN),
        ('Miter Flange', 'Flange dengan\nmiter joint', C_PURPLE),
        ('Hem', '180° tekukan\n(pengaman tepi)', C_ORANGE),
        ('Jog', 'Offset/step\npada permukaan', C_TEAL),
        ('Sketched Bend', 'Bend pada lokasi\ndari sketch line', C_RED),
    ]
    for i, (title, desc, col) in enumerate(features_main):
        row = i // 3; ci = i % 3
        cx = 0.15 + ci * 3.3; cy = 4.5 - row * 2.8
        ax2.add_patch(FancyBboxPatch((cx, cy-0.4), 2.9, 2.2, boxstyle="round,pad=0.05",
                                      facecolor='white', edgecolor=col, linewidth=1.5))
        ax2.text(cx+1.45, cy+1.2, title, ha='center', fontsize=9, fontweight='bold', color=col)
        ax2.text(cx+1.45, cy+0.2, desc, ha='center', fontsize=7.5, color='#616161')

    # ==== SECTION 3: More Features ====
    ax3 = fig.add_axes([0.02, 0.62, 0.47, 0.14])
    ax3.set_xlim(0, 10); ax3.set_ylim(0, 5)
    ax3.axis('off')
    ax3.set_title('3. FEATURES TAMBAHAN', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    features_extra = [
        ('Cross Break', 'X-pattern bend\nuntuk kekakuan', C_BLUE),
        ('Closed Corner', 'Tutup celah di\nsudut 2 flange', C_GREEN),
        ('Rip', 'Pisahkan/robek\nedge tersambung', C_PURPLE),
        ('Forming Tools', 'Louver, Lance,\nRib, Emboss (Library)', C_ORANGE),
        ('Flat Pattern', 'Bentangkan → pola\ndatar (DXF export)', C_RED),
    ]
    for i, (title, desc, col) in enumerate(features_extra):
        cx = 0.1 + i * 1.96; cy = 2.5
        ax3.add_patch(FancyBboxPatch((cx, cy-0.6), 1.76, 2.8, boxstyle="round,pad=0.04",
                                      facecolor='white', edgecolor=col, linewidth=1.3))
        ax3.text(cx+0.88, cy+1.5, title, ha='center', fontsize=8.5, fontweight='bold', color=col)
        ax3.text(cx+0.88, cy+0.2, desc, ha='center', fontsize=7, color='#616161')

    # ==== SECTION 4: Hem Types ====
    ax4 = fig.add_axes([0.52, 0.62, 0.47, 0.14])
    ax4.set_xlim(0, 10); ax4.set_ylim(0, 5)
    ax4.axis('off')
    ax4.set_title('4. TIPE HEM & EDGE FLANGE', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    # Hem types
    hems = [
        ('Closed Hem', C_BLUE, 0.5),
        ('Open Hem', C_GREEN, 2.5),
        ('Tear Drop', C_PURPLE, 4.5),
        ('Rolled Hem', C_ORANGE, 6.5),
    ]
    for name, col, cx in hems:
        ax4.add_patch(FancyBboxPatch((cx, 2.5), 1.7, 1.8, boxstyle="round,pad=0.04",
                                      facecolor='white', edgecolor=col, linewidth=1.5))
        ax4.text(cx+0.85, 3.4, name, ha='center', fontsize=8, fontweight='bold', color=col)
        # Simple illustration
        ax4.plot([cx+0.2, cx+1.5], [3.0, 3.0], color=col, linewidth=2)
        if 'Closed' in name:
            ax4.plot([cx+1.5, cx+1.5, cx+0.9], [3.0, 2.7, 2.7], color=col, linewidth=2)
        elif 'Open' in name:
            ax4.plot([cx+1.5, cx+1.5, cx+1.0], [3.0, 2.8, 2.8], color=col, linewidth=2)
        elif 'Tear' in name:
            theta = np.linspace(0, np.pi, 20)
            ax4.plot(cx+1.4+0.15*np.cos(theta), 2.85+0.15*np.sin(theta), color=col, linewidth=2)
        elif 'Rolled' in name:
            theta = np.linspace(0, 1.5*np.pi, 30)
            ax4.plot(cx+1.4+0.15*np.cos(theta), 2.85+0.15*np.sin(theta), color=col, linewidth=2)

    # Edge Flange Position
    ax4.add_patch(FancyBboxPatch((0.2, 0.3), 9.3, 1.8, boxstyle="round,pad=0.06",
                                  facecolor=C_LB, edgecolor=C_BLUE, linewidth=1.2))
    ax4.text(5, 1.6, 'Edge Flange Position:', ha='center', fontsize=9, fontweight='bold', color=C_BLUE)
    ax4.text(5, 0.8, 'Material Inside  |  Material Outside  |  Bend Outside  |  Bend from Virtual Sharp',
             ha='center', fontsize=8, color='#424242')

    # ==== SECTION 5: Flat Pattern & Workflow ====
    ax5 = fig.add_axes([0.02, 0.42, 0.47, 0.18])
    ax5.set_xlim(0, 12); ax5.set_ylim(0, 7)
    ax5.axis('off')
    ax5.set_title('5. FLAT PATTERN & WORKFLOW', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    # Workflow: 3D → Flatten → DXF
    # 3D box (folded)
    ax5.add_patch(FancyBboxPatch((0.3, 3.5), 2.5, 1.8, boxstyle="round,pad=0.05",
                                  facecolor='#B0BEC5', edgecolor='#455A64', linewidth=2))
    ax5.add_patch(patches.Rectangle((0.3, 5.3), 2.5, 0.5,
                                     facecolor='#90A4AE', edgecolor='#455A64', linewidth=1.5))
    ax5.add_patch(patches.Rectangle((2.8, 3.5), 0.5, 1.8,
                                     facecolor='#78909C', edgecolor='#455A64', linewidth=1.5))
    ax5.text(1.55, 4.4, '3D Model\n(Folded)', ha='center', fontsize=9, fontweight='bold', color='white')

    # Arrow
    ax5.annotate('', xy=(4.5, 4.5), xytext=(3.8, 4.5),
                 arrowprops=dict(arrowstyle='->', lw=2.5, color=C_RED))
    ax5.text(4.15, 5.2, 'Flatten', fontsize=8, fontweight='bold', color=C_RED)

    # Flat pattern
    draw_flat_pattern(ax5, 6, 4.5, 2.0, 1.2, 0.4, 'Flat\nPattern', C_BLUE)

    # Arrow
    ax5.annotate('', xy=(8.5, 4.5), xytext=(7.8, 4.5),
                 arrowprops=dict(arrowstyle='->', lw=2.5, color=C_RED))
    ax5.text(8.15, 5.2, 'Export', fontsize=8, fontweight='bold', color=C_RED)

    # DXF file
    ax5.add_patch(FancyBboxPatch((8.8, 3.5), 2.2, 2.0, boxstyle="round,pad=0.08",
                                  facecolor='#E8F5E9', edgecolor=C_GREEN, linewidth=2))
    ax5.text(9.9, 4.5, '.DXF\nFile', ha='center', fontsize=10, fontweight='bold', color=C_GREEN)

    # Workflow steps
    ax5.add_patch(FancyBboxPatch((0.2, 0.3), 10.8, 2.5, boxstyle="round,pad=0.08",
                                  facecolor=C_LG, edgecolor=C_GREEN, linewidth=1.2))
    ax5.text(5.6, 2.3, 'Sheet Metal Design Workflow', ha='center', fontsize=10, fontweight='bold', color=C_GREEN)
    wf = "1. Base Flange (profil utama) → 2. Edge Flange / Miter → 3. Hem (pengaman tepi)\n" \
         "→ 4. Cut-Extrude (lubang/slot) → 5. Forming Tools → 6. Flat Pattern → 7. Export DXF"
    ax5.text(5.6, 1.2, wf, ha='center', fontsize=8.5, color='#424242')

    # ==== SECTION 6: Percobaan 1-10 ====
    ax6 = fig.add_axes([0.52, 0.42, 0.47, 0.18])
    ax6.set_xlim(0, 10); ax6.set_ylim(0, 7)
    ax6.axis('off')
    ax6.set_title('6. PERCOBAAN 1-10', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    percobaan = [
        ("1.  Box Sederhana", "Base + 4 Edge Flange", C_BLUE),
        ("2.  U-Channel", "Base Flange + Hem", C_BLUE),
        ("3.  L-Bracket", "Edge Flange + Slot", C_GREEN),
        ("4.  Cover/Lid", "Edge Flange + Hem + Hole", C_GREEN),
        ("5.  Enclosure Box", "Tab & Slot + Ventilasi", C_PURPLE),
        ("6.  Bracket + Jog", "Jog offset + Edge Flange", C_PURPLE),
        ("7.  Fan Guard", "Forming Tool (Louver)", C_ORANGE),
        ("8.  Cable Tray", "Edge Flange + Lip + Pattern", C_ORANGE),
        ("9.  Multi-Body", "Tab-Slot interlocking", C_TEAL),
        ("10. Panel Elektrik", "Full SM + DXF Export", C_TEAL),
    ]
    for i, (name, desc, col) in enumerate(percobaan):
        cy = 6.3 - i * 0.6
        ax6.text(0.2, cy, name, fontsize=8.5, fontweight='bold', color=col)
        ax6.text(5.0, cy, desc, fontsize=8, color='#616161')

    # ==== SECTION 7: Tips ====
    ax7 = fig.add_axes([0.02, 0.22, 0.96, 0.18])
    ax7.set_xlim(0, 20); ax7.set_ylim(0, 6)
    ax7.axis('off')
    ax7.set_title('7. TIPS SHEET METAL DESIGN', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    ax7.add_patch(FancyBboxPatch((0.2, 0.3), 9.2, 5.0, boxstyle="round,pad=0.08",
                                  facecolor='#E8F5E9', edgecolor=C_GREEN, linewidth=1.5))
    ax7.text(4.8, 4.8, '💡 BEST PRACTICES', ha='center', fontsize=11, fontweight='bold', color=C_GREEN)
    tips = [
        "✅ Selalu mulai dari Base Flange (menetapkan thickness & parameter)",
        "✅ Perhatikan K-Factor sesuai material yang digunakan",
        "✅ Cek Flat Pattern reguler (pastikan bisa dibentangkan)",
        "✅ Perhatikan minimum bend radius (umumnya ≥ thickness)",
        "✅ Gunakan Forming Tools untuk fitur standar (louver, lance)",
        "✅ Export DXF dari Flat Pattern untuk proses laser cutting",
        "✅ Auto Relief untuk corner bends",
    ]
    for i, t in enumerate(tips):
        ax7.text(0.5, 4.0 - i*0.52, t, fontsize=8.5, color='#2E7D32')

    ax7.add_patch(FancyBboxPatch((10.0, 0.3), 9.5, 5.0, boxstyle="round,pad=0.08",
                                  facecolor='#FFEBEE', edgecolor=C_RED, linewidth=1.5))
    ax7.text(14.75, 4.8, '⚠️ PERHATIKAN', ha='center', fontsize=11, fontweight='bold', color=C_RED)
    cautions = [
        "❌ Jangan ketebalan > 4mm (sulit di-bend)",
        "❌ Jangan abaikan gauge table untuk standar",
        "❌ Jangan lupa cek interference pada bend",
        "❌ Jangan export folded (harus flat pattern)",
        "❌ Perhatikan bend sequence saat desain",
        "❌ Jangan bend radius terlalu kecil (< thickness)",
        "❌ Perhatikan grain direction material",
    ]
    for i, c in enumerate(cautions):
        ax7.text(10.3, 4.0 - i*0.52, c, fontsize=8.5, color=C_RED)

    # FOOTER
    fig.text(0.5, 0.19, 'Modul Praktikum CAD/CAM — Modul 7: CAD Sheet Metal — Bend, Flange, Flat Pattern & DXF',
             ha='center', fontsize=10, color='#9E9E9E', style='italic')

    plt.savefig(os.path.join(IMG_DIR, 'm01_deskripsi.png'), dpi=150, bbox_inches='tight', facecolor=BG)
    print("✓ image/m01_deskripsi.png")
    plt.close()


# ============================================================================
# 2. PROJECT DESKRIPSI (p01_deskripsi.png)
# ============================================================================
def generate_project_image():
    fig = plt.figure(figsize=(18, 24), facecolor=BG)

    # HEADER
    fig.text(0.5, 0.975, 'PROJECT MODUL 7: SHEET METAL ENCLOSURE + AKSESORIS', ha='center', va='top',
             fontsize=22, fontweight='bold', color=C_TITLE,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3E0', edgecolor=C_ORANGE, linewidth=2))
    fig.text(0.5, 0.953, 'Enclosure Elektronik + Aksesoris Aluminium Sheet Metal',
             ha='center', va='top', fontsize=13, color='#546E7A', style='italic')

    # ==== PROJECT A: Enclosure Elektronik ====
    ax_a = fig.add_axes([0.02, 0.52, 0.96, 0.42])
    ax_a.set_xlim(0, 20); ax_a.set_ylim(0, 15)
    ax_a.axis('off')
    ax_a.set_title('PROJECT A: ENCLOSURE ELEKTRONIK SHEET METAL', fontweight='bold',
                    fontsize=16, color=C_RED, loc='left', pad=10)

    # Enclosure illustration (isometric-like)
    # Main body (open-top box)
    ax_a.add_patch(FancyBboxPatch((1, 2.5), 8, 4, boxstyle="round,pad=0.05",
                                   facecolor='#B0BEC5', edgecolor='#37474F', linewidth=2.5))
    # Side wall left
    ax_a.add_patch(patches.Polygon([(1, 2.5), (1, 6.5), (2.5, 8), (2.5, 4)],
                                    facecolor='#90A4AE', edgecolor='#37474F', linewidth=2))
    # Top face
    ax_a.add_patch(patches.Polygon([(1, 6.5), (9, 6.5), (10.5, 8), (2.5, 8)],
                                    facecolor='#CFD8DC', edgecolor='#37474F', linewidth=2))

    ax_a.text(5, 4.5, 'MAIN BODY\n150×100×50mm', ha='center', fontsize=10, fontweight='bold', color='#37474F')

    # Cover/Lid
    ax_a.add_patch(FancyBboxPatch((1, 8.5), 8, 0.6, boxstyle="round,pad=0.02",
                                   facecolor='#64B5F6', edgecolor=C_BLUE, linewidth=2))
    ax_a.text(5, 8.8, 'COVER/LID (snap-fit tabs)', ha='center', fontsize=8, fontweight='bold', color=C_BLUE)

    # Front Panel
    ax_a.add_patch(FancyBboxPatch((9.2, 2.5), 0.5, 4, boxstyle="round,pad=0.02",
                                   facecolor='#A5D6A7', edgecolor=C_GREEN, linewidth=2))
    ax_a.text(10.5, 4.5, 'FRONT\nPANEL', ha='center', fontsize=8, fontweight='bold', color=C_GREEN)

    # Display cutout on front panel
    ax_a.add_patch(patches.Rectangle((9.3, 5.0), 0.3, 1.0,
                                      facecolor='#263238', edgecolor='#1B5E20', linewidth=1))
    # Button holes
    for by in [3.5, 4.0]:
        ax_a.add_patch(Circle((9.45, by), 0.1, facecolor='white', edgecolor=C_GREEN, linewidth=1))

    # Ventilasi slots
    for vy in np.linspace(3.0, 5.5, 5):
        ax_a.plot([2, 4], [vy, vy], color='#546E7A', linewidth=1.5)
    ax_a.text(3, 2.0, 'Ventilasi', ha='center', fontsize=7, color='#546E7A')

    # Cable entry
    ax_a.add_patch(Circle((6, 2.5), 0.3, facecolor='white', edgecolor='#37474F', linewidth=1.5))
    ax_a.text(6, 1.8, 'Cable Entry\nØ25mm', ha='center', fontsize=7, color='#37474F')

    # Mounting Bracket
    ax_a.add_patch(patches.Polygon([(0, 3), (0, 5), (1, 6.5), (1, 2.5)],
                                    facecolor='#FFB74D', edgecolor=C_ORANGE, linewidth=2, alpha=0.7))
    ax_a.text(-0.3, 4.2, 'MOUNT\nBRACKET', ha='center', fontsize=7, fontweight='bold', color=C_ORANGE, rotation=90)

    # Internal Bracket (PCB)
    ax_a.plot([3, 7], [3.5, 3.5], color=C_PURPLE, linewidth=2, linestyle='--')
    ax_a.text(5, 3.0, 'Internal PCB Bracket', ha='center', fontsize=7, color=C_PURPLE, style='italic')

    # Komponen list
    ax_a.add_patch(FancyBboxPatch((12, 1.5), 7.5, 8.5, boxstyle="round,pad=0.15",
                                   facecolor='#FFF8E1', edgecolor=C_ORANGE, linewidth=1.5))
    ax_a.text(15.75, 9.5, 'KOMPONEN (5 Parts)', ha='center', fontsize=11, fontweight='bold', color=C_ORANGE)

    comp_a = [
        ("1. Main Body", "Box + ventilasi + cable entry"),
        ("2. Cover/Lid", "Snap-fit tabs"),
        ("3. Front Panel", "Cutout display + tombol + LED"),
        ("4. Mounting Bracket", "Bracket untuk dinding/rak"),
        ("5. Internal Bracket", "PCB holder"),
        ("", ""),
        ("Spesifikasi:", ""),
        ("  Material", "Aluminum 1.5mm"),
        ("  K-Factor", "0.33"),
        ("  Bend Radius", "1.5mm"),
        ("  Ukuran", "150×100×50mm"),
        ("", ""),
        ("Deliverables:", ""),
        ("  5× .sldprt", "(sheet metal)"),
        ("  5× .dxf", "(flat pattern)"),
        ("  1× .sldasm", "(assembly)"),
    ]
    for i, (name, desc) in enumerate(comp_a):
        is_header = name.endswith(':')
        ax_a.text(12.3, 8.8 - i*0.47, name, fontsize=8.5,
                  fontweight='bold' if is_header else 'normal',
                  color=C_ORANGE if is_header else '#424242')
        if desc:
            ax_a.text(16.5, 8.8 - i*0.47, desc, fontsize=8, color='#757575')

    # ==== PROJECT B: Aksesoris Aluminium ====
    ax_b = fig.add_axes([0.02, 0.06, 0.96, 0.44])
    ax_b.set_xlim(0, 20); ax_b.set_ylim(0, 15)
    ax_b.axis('off')
    ax_b.set_title('PROJECT B: AKSESORIS ALUMINIUM SHEET METAL', fontweight='bold',
                    fontsize=16, color=C_TEAL, loc='left', pad=10)

    # 5 aksesoris illustrations
    # 1. Mounting Plate 4040
    ax_b.add_patch(FancyBboxPatch((0.5, 10.0), 3.5, 3.5, boxstyle="round,pad=0.1",
                                   facecolor='#ECEFF1', edgecolor=C_BLUE, linewidth=1.5))
    ax_b.add_patch(patches.Rectangle((0.8, 10.3), 2.9, 2.9,
                                      facecolor='#B0BEC5', edgecolor='#455A64', linewidth=2))
    # Slots
    for sy in [10.8, 12.5]:
        for sx in [1.3, 3.0]:
            ax_b.add_patch(patches.Rectangle((sx-0.15, sy-0.1), 0.3, 0.2,
                                              facecolor='white', edgecolor='#616161', linewidth=1))
    ax_b.add_patch(Circle((2.25, 11.75), 0.15, facecolor='white', edgecolor='#424242', linewidth=1))
    ax_b.text(2.25, 14.0, '1. Mounting Plate\n4040', ha='center', fontsize=9, fontweight='bold', color=C_BLUE)
    ax_b.text(2.25, 9.6, '80×80mm, Al 3mm\n4 T-slot + lip', ha='center', fontsize=7.5, color='#616161')

    # 2. L-Bracket 3030
    ax_b.add_patch(FancyBboxPatch((4.5, 10.0), 3.5, 3.5, boxstyle="round,pad=0.1",
                                   facecolor='#ECEFF1', edgecolor=C_GREEN, linewidth=1.5))
    ax_b.add_patch(patches.Polygon([(5.0, 10.5), (7.5, 10.5), (7.5, 12.0), (6.5, 12.0), (6.5, 13.0), (5.0, 13.0)],
                                    facecolor='#B0BEC5', edgecolor='#455A64', linewidth=2))
    ax_b.text(6.25, 14.0, '2. L-Bracket\n3030', ha='center', fontsize=9, fontweight='bold', color=C_GREEN)
    ax_b.text(6.25, 9.6, '60×60×30mm, Al 2mm\n4 T-slot holes', ha='center', fontsize=7.5, color='#616161')

    # 3. Gusset Plate Triangular
    ax_b.add_patch(FancyBboxPatch((8.5, 10.0), 3.5, 3.5, boxstyle="round,pad=0.1",
                                   facecolor='#ECEFF1', edgecolor=C_PURPLE, linewidth=1.5))
    ax_b.add_patch(patches.Polygon([(9.0, 10.5), (11.5, 10.5), (9.0, 13.0)],
                                    facecolor='#B0BEC5', edgecolor='#455A64', linewidth=2))
    for sx, sy in [(9.5, 10.8), (9.5, 11.5), (9.8, 10.8), (10.5, 10.8)]:
        ax_b.add_patch(patches.Rectangle((sx-0.08, sy-0.05), 0.16, 0.1,
                                          facecolor='white', edgecolor='#616161', linewidth=0.8))
    ax_b.text(10.25, 14.0, '3. Gusset Plate\nTriangular', ha='center', fontsize=9, fontweight='bold', color=C_PURPLE)
    ax_b.text(10.25, 9.6, '50×50mm, Al 4mm\n2 slot/sisi, R8', ha='center', fontsize=7.5, color='#616161')

    # 4. Cable Tray Bracket
    ax_b.add_patch(FancyBboxPatch((12.5, 10.0), 3.5, 3.5, boxstyle="round,pad=0.1",
                                   facecolor='#ECEFF1', edgecolor=C_ORANGE, linewidth=1.5))
    ax_b.add_patch(patches.Polygon([(13.0, 10.5), (15.5, 10.5), (15.5, 11.0), (15.0, 11.0),
                                     (15.0, 12.5), (15.5, 12.5), (15.5, 13.0), (13.0, 13.0),
                                     (13.0, 12.5), (13.5, 12.5), (13.5, 11.0), (13.0, 11.0)],
                                    facecolor='#B0BEC5', edgecolor='#455A64', linewidth=2))
    ax_b.text(14.25, 14.0, '4. Cable Tray\nBracket', ha='center', fontsize=9, fontweight='bold', color=C_ORANGE)
    ax_b.text(14.25, 9.6, '100×40mm, Al 1.5mm\nU-channel + tabs', ha='center', fontsize=7.5, color='#616161')

    # 5. End Cap Ventilasi
    ax_b.add_patch(FancyBboxPatch((16.5, 10.0), 3.0, 3.5, boxstyle="round,pad=0.1",
                                   facecolor='#ECEFF1', edgecolor=C_RED, linewidth=1.5))
    ax_b.add_patch(patches.Rectangle((17.0, 10.5), 2.0, 2.0,
                                      facecolor='#B0BEC5', edgecolor='#455A64', linewidth=2))
    # Perforated pattern
    for px in np.linspace(17.3, 18.7, 4):
        for py in np.linspace(10.8, 12.2, 4):
            ax_b.add_patch(Circle((px, py), 0.08, facecolor='white', edgecolor='#616161', linewidth=0.8))
    ax_b.text(18.0, 14.0, '5. End Cap\nVentilasi', ha='center', fontsize=9, fontweight='bold', color=C_RED)
    ax_b.text(18.0, 9.6, '40×40mm, Al 1.5mm\nHem snap + perf.', ha='center', fontsize=7.5, color='#616161')

    # Spesifikasi & Constraints
    ax_b.add_patch(FancyBboxPatch((0.3, 4.0), 9.5, 5.0, boxstyle="round,pad=0.15",
                                   facecolor='#E0F2F1', edgecolor=C_TEAL, linewidth=1.5))
    ax_b.text(5.05, 8.5, 'TEKNIK & CONSTRAINTS', ha='center', fontsize=12, fontweight='bold', color=C_TEAL)

    teknik = [
        "SETIAP KOMPONEN WAJIB:",
        "• Base Flange sebagai awal (set thickness & K-Factor)",
        "• Edge Flange / Miter Flange untuk tekukan",
        "• Cut-Extrude untuk slot/lubang",
        "• Flat Pattern harus valid (no overlaps)",
        "• Export DXF dari Flat Pattern",
        "",
        "T-SLOT COMPATIBILITY:",
        "• Slot 8mm → Profil 30/40/45/50 series",
        "• Slot 6mm → Profil 20 series",
    ]
    for i, t in enumerate(teknik):
        is_header = t.endswith(':')
        ax_b.text(0.6, 7.8 - i*0.4, t, fontsize=8.5,
                  fontweight='bold' if is_header else 'normal',
                  color=C_TEAL if is_header or t.startswith('•') else '#424242')

    # Penilaian
    ax_b.add_patch(FancyBboxPatch((10.5, 4.0), 9.0, 5.0, boxstyle="round,pad=0.15",
                                   facecolor='#FFF3E0', edgecolor=C_ORANGE, linewidth=1.5))
    ax_b.text(15.0, 8.5, 'KRITERIA PENILAIAN', ha='center', fontsize=12, fontweight='bold', color=C_ORANGE)

    penilaian = [
        ("A: 5 komponen enclosure", "20%"),
        ("A: Sheet metal features benar", "15%"),
        ("A: Flat Pattern valid", "10%"),
        ("B: 5 komponen aksesoris", "20%"),
        ("B: Dimensi sesuai profil standar", "10%"),
        ("B: DXF siap manufaktur", "10%"),
        ("Assembly + mate benar", "10%"),
        ("Drawing + Flat Pattern view", "5%"),
    ]
    for i, (crit, bobot) in enumerate(penilaian):
        ax_b.text(10.8, 7.8 - i*0.42, f"• {crit}", fontsize=8.5, color='#424242')
        ax_b.text(18.8, 7.8 - i*0.42, bobot, fontsize=9, fontweight='bold', color=C_ORANGE, ha='center')

    # Deliverables
    ax_b.add_patch(FancyBboxPatch((0.3, 0.3), 19.2, 3.2, boxstyle="round,pad=0.12",
                                   facecolor=C_LR, edgecolor=C_RED, linewidth=1.5))
    ax_b.text(10, 3.0, 'TOTAL DELIVERABLES', ha='center', fontsize=12, fontweight='bold', color=C_RED)

    delivs_a = [
        "PROJECT A: M07_A1_MainBody.sldprt/.dxf | M07_A2_Cover.sldprt/.dxf",
        "M07_A3_FrontPanel.sldprt/.dxf | M07_A4_MountingBracket.sldprt/.dxf | M07_A5_InternalBracket.sldprt/.dxf",
        "M07_A_Enclosure.sldasm",
    ]
    delivs_b = [
        "PROJECT B: M07_B1_MountingPlate4040 | M07_B2_LBracket3030 | M07_B3_GussetPlate",
        "M07_B4_CableTrayBracket | M07_B5_EndCapVentilasi (semua .sldprt + .dxf)",
        "M07_Drawing_FlatPatterns.slddrw",
    ]
    for i, d in enumerate(delivs_a):
        ax_b.text(10, 2.4 - i*0.35, d, ha='center', fontsize=7.5, color='#424242', family='monospace')
    for i, d in enumerate(delivs_b):
        ax_b.text(10, 1.3 - i*0.35, d, ha='center', fontsize=7.5, color='#616161', family='monospace')

    # FOOTER
    fig.text(0.5, 0.035, 'Project Praktikum CAD/CAM — Modul 7: Sheet Metal Enclosure + Aksesoris Aluminium',
             ha='center', fontsize=10, color='#9E9E9E', style='italic')

    plt.savefig(os.path.join(IMG_DIR, 'p01_deskripsi.png'), dpi=150, bbox_inches='tight', facecolor=BG)
    print("✓ image/p01_deskripsi.png")
    plt.close()


# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("GENERATING IMAGES FOR MODUL 7 - CAD SHEET METAL")
    print("="*60)

    generate_materi_image()
    generate_project_image()

    print("\n✓ Semua gambar Modul 7 berhasil dibuat!")
    print(f"  Lokasi: {IMG_DIR}/")
    print("="*60 + "\n")
