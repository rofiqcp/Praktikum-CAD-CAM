"""
VISUALISASI MODUL 6: CAD ASSEMBLY
Generate ilustrasi untuk Materi dan Project:
- image/m01_deskripsi.png : Ringkasan materi Assembly
- image/p01_deskripsi.png : Ringkasan project Press Tool + Frame Aluminium
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
# HELPER: isometric box
# ============================================================================
def iso(x, y, z):
    return x - 0.5*z, y + 0.35*z

def draw_box_iso(ax, ox, oy, w, h, d, fc='#B3E5FC', ec='#01579B', lw=1.5, alpha=0.6):
    """Draw a 3D box in simple isometric"""
    c = [iso(ox, oy, 0), iso(ox+w, oy, 0), iso(ox+w, oy+h, 0), iso(ox, oy+h, 0),
         iso(ox, oy, d), iso(ox+w, oy, d), iso(ox+w, oy+h, d), iso(ox, oy+h, d)]
    # top face
    ax.add_patch(Polygon([c[4], c[5], c[6], c[7]], facecolor=fc, edgecolor=ec, lw=lw, alpha=alpha))
    # front face
    ax.add_patch(Polygon([c[0], c[1], c[5], c[4]], facecolor=fc, edgecolor=ec, lw=lw, alpha=alpha*0.85))
    # right face
    ax.add_patch(Polygon([c[1], c[2], c[6], c[5]], facecolor=fc, edgecolor=ec, lw=lw, alpha=alpha*0.7))


# ============================================================================
# 1. MATERI DESKRIPSI (m01_deskripsi.png)
# ============================================================================
def generate_materi_image():
    fig = plt.figure(figsize=(18, 24), facecolor=BG)

    # HEADER
    fig.text(0.5, 0.975, 'MODUL 6: CAD ASSEMBLY', ha='center', va='top',
             fontsize=24, fontweight='bold', color=C_TITLE,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#E3F2FD', edgecolor=C_ACCENT, linewidth=2))
    fig.text(0.5, 0.953, 'Semua Teknik Assembly — Standard, Advanced & Mechanical Mates',
             ha='center', va='top', fontsize=13, color='#546E7A', style='italic')

    # ==== SECTION 1: Konsep Dasar Assembly ====
    ax1 = fig.add_axes([0.02, 0.78, 0.47, 0.16])
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 6)
    ax1.axis('off')
    ax1.set_title('1. KONSEP DASAR ASSEMBLY', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    approaches = [
        ('Bottom-Up', 'Buat semua part dulu\n→ rakit di Assembly', C_BLUE, 0.2, 4.0),
        ('Top-Down', 'Buat part di dalam\nAssembly (in-context)', C_GREEN, 3.5, 4.0),
        ('Hybrid', 'Kombinasi keduanya\n(paling umum)', C_PURPLE, 6.8, 4.0),
    ]
    for title, desc, col, cx, cy in approaches:
        ax1.add_patch(FancyBboxPatch((cx, cy-0.5), 2.8, 2.0, boxstyle="round,pad=0.06",
                                      facecolor='white', edgecolor=col, linewidth=1.5))
        ax1.text(cx+1.4, cy+1.0, title, ha='center', fontsize=10, fontweight='bold', color=col)
        ax1.text(cx+1.4, cy, desc, ha='center', fontsize=8, color='#616161')

    steps_text = "File → New → Assembly → Insert komponen pertama (Fixed) → Insert part lain → Tambah Mates"
    ax1.text(5, 1.5, steps_text, ha='center', fontsize=9, style='italic', color='#424242',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=C_LG, edgecolor=C_GREEN, linewidth=1))

    # ==== SECTION 2: Standard Mates ====
    ax2 = fig.add_axes([0.52, 0.78, 0.47, 0.16])
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 6)
    ax2.axis('off')
    ax2.set_title('2. STANDARD MATES', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    std_mates = [
        ('Coincident', '2 face bertemu\n(-1 translasi)', C_BLUE),
        ('Parallel', '2 face sejajar\n(-2 rotasi)', C_GREEN),
        ('Perpendicular', '2 face tegak lurus\n(-1 rotasi)', C_PURPLE),
        ('Tangent', '2 surface singgung\n(-1 translasi)', C_ORANGE),
        ('Concentric', '2 cylinder sesumbu\n(-2 translasi)', C_TEAL),
        ('Distance', 'Jarak tertentu\n(-1 translasi)', C_RED),
        ('Angle', 'Sudut tertentu\n(-1 rotasi)', '#757575'),
        ('Lock', 'Kunci semua DOF\n(-6 DOF)', '#424242'),
    ]
    for i, (name, desc, col) in enumerate(std_mates):
        row = i // 4; ci = i % 4
        cx = 0.1 + ci * 2.45; cy = 4.8 - row * 2.7
        ax2.add_patch(FancyBboxPatch((cx, cy-0.4), 2.2, 2.0, boxstyle="round,pad=0.04",
                                      facecolor='white', edgecolor=col, linewidth=1.4))
        ax2.text(cx+1.1, cy+1.1, name, ha='center', fontsize=8.5, fontweight='bold', color=col)
        ax2.text(cx+1.1, cy+0.2, desc, ha='center', fontsize=6.5, color='#616161')

    # ==== SECTION 3: Advanced Mates ====
    ax3 = fig.add_axes([0.02, 0.62, 0.47, 0.14])
    ax3.set_xlim(0, 10); ax3.set_ylim(0, 5)
    ax3.axis('off')
    ax3.set_title('3. ADVANCED MATES', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    adv_mates = [
        ('Width', 'Komponen di tengah\nslot/channel', C_BLUE),
        ('Path Mate', 'Komponen mengikuti\npath tertentu', C_GREEN),
        ('Linear Coupler', 'Hubungkan gerakan\nlinear 2 komponen', C_PURPLE),
        ('Symmetric', 'Komponen simetris\nterhadap plane', C_ORANGE),
        ('Profile Center', 'Menengahkan profil\nnon-silindris', C_TEAL),
    ]
    for i, (name, desc, col) in enumerate(adv_mates):
        cx = 0.1 + i * 1.96; cy = 2.5
        ax3.add_patch(FancyBboxPatch((cx, cy-0.6), 1.76, 2.8, boxstyle="round,pad=0.04",
                                      facecolor='white', edgecolor=col, linewidth=1.3))
        ax3.text(cx+0.88, cy+1.5, name, ha='center', fontsize=8.5, fontweight='bold', color=col)
        ax3.text(cx+0.88, cy+0.3, desc, ha='center', fontsize=7, color='#616161')

    # ==== SECTION 4: Mechanical Mates ====
    ax4 = fig.add_axes([0.52, 0.62, 0.47, 0.14])
    ax4.set_xlim(0, 10); ax4.set_ylim(0, 5)
    ax4.axis('off')
    ax4.set_title('4. MECHANICAL MATES', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    mech_mates = [
        ('Gear', 'Rasio putar\n2 gear', C_BLUE),
        ('Rack & Pinion', 'Rotasi →\ntranslasi', C_GREEN),
        ('Cam', 'Follower ikuti\nprofil cam', C_PURPLE),
        ('Hinge', 'Rotasi pada\nsumbu (engsel)', C_ORANGE),
        ('Screw', 'Ulir: rotasi\n→ translasi', C_TEAL),
        ('Universal Joint', 'Sambungan\nuniversal', C_RED),
        ('Slot', 'Komponen\ndalam slot', '#757575'),
    ]
    for i, (name, desc, col) in enumerate(mech_mates):
        cx = 0.05 + i * 1.4; cy = 2.5
        ax4.add_patch(FancyBboxPatch((cx, cy-0.6), 1.25, 2.8, boxstyle="round,pad=0.03",
                                      facecolor='white', edgecolor=col, linewidth=1.2))
        ax4.text(cx+0.625, cy+1.5, name, ha='center', fontsize=7.5, fontweight='bold', color=col)
        ax4.text(cx+0.625, cy+0.3, desc, ha='center', fontsize=6, color='#616161')

    # ==== SECTION 5: Fitur Assembly Lainnya ====
    ax5 = fig.add_axes([0.02, 0.44, 0.47, 0.16])
    ax5.set_xlim(0, 10); ax5.set_ylim(0, 6)
    ax5.axis('off')
    ax5.set_title('5. FITUR ASSEMBLY LAINNYA', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    features = [
        ('Exploded View', 'Tampilkan assembly\nterpisah per komponen\nInsert → Exploded View', C_BLUE, 0.2, 3.5),
        ('Section View', 'Potong assembly\nuntuk lihat dalam\nView → Section View', C_GREEN, 3.5, 3.5),
        ('Interference', 'Deteksi tabrakan\nantar komponen\nEvaluate → Interference', C_RED, 6.8, 3.5),
        ('Mass Properties', 'Massa, volume,\ncenter of mass\nEvaluate → Mass', C_PURPLE, 0.2, 0.8),
        ('BOM', 'Bill of Materials\nDaftar komponen\nDi Drawing env.', C_ORANGE, 3.5, 0.8),
        ('Component\nPattern', 'Linear / Circular\npattern komponen\ndalam assembly', C_TEAL, 6.8, 0.8),
    ]
    for title, desc, col, cx, cy in features:
        ax5.add_patch(FancyBboxPatch((cx, cy-0.3), 2.8, 2.3, boxstyle="round,pad=0.06",
                                      facecolor='white', edgecolor=col, linewidth=1.5))
        ax5.text(cx+1.4, cy+1.4, title, ha='center', fontsize=9, fontweight='bold', color=col)
        ax5.text(cx+1.4, cy+0.3, desc, ha='center', fontsize=7, color='#616161')

    # ==== SECTION 6: Visualisasi Assembly ====
    ax6 = fig.add_axes([0.52, 0.44, 0.47, 0.16])
    ax6.set_xlim(-2, 12); ax6.set_ylim(-1, 7)
    ax6.axis('off')
    ax6.set_title('6. ASSEMBLY WORKFLOW', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    # Workflow boxes
    wf_items = [
        ('1. Insert\nBase Part\n(Fixed)', C_BLUE, 0),
        ('2. Insert\nKomponen\nLain', C_GREEN, 2.8),
        ('3. Tambah\nMates\n(Posisi)', C_PURPLE, 5.6),
        ('4. Verify\n& Motion\nStudy', C_ORANGE, 8.4),
    ]
    for title, col, cx in wf_items:
        ax6.add_patch(FancyBboxPatch((cx, 3.5), 2.3, 2.5, boxstyle="round,pad=0.08",
                                      facecolor='white', edgecolor=col, linewidth=2))
        ax6.text(cx+1.15, 4.75, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color=col)
    # Arrows
    for sx in [2.3, 5.1, 7.9]:
        ax6.annotate('', xy=(sx+0.5, 4.75), xytext=(sx, 4.75),
                     arrowprops=dict(arrowstyle='->', lw=2, color='#9E9E9E'))

    # Mate alignment info
    ax6.add_patch(FancyBboxPatch((0, 0.2), 10.5, 2.5, boxstyle="round,pad=0.08",
                                  facecolor=C_LB, edgecolor=C_BLUE, linewidth=1.2))
    ax6.text(5.25, 2.2, 'Mate Alignment', ha='center', fontsize=10, fontweight='bold', color=C_BLUE)
    ax6.text(2.5, 1.2, '✅ Aligned: Face → arah sama', fontsize=9, color='#424242')
    ax6.text(7.5, 1.2, '✅ Anti-Aligned: Face → berlawanan', fontsize=9, color='#424242')

    # ==== SECTION 7: Percobaan ====
    ax7 = fig.add_axes([0.02, 0.22, 0.47, 0.20])
    ax7.set_xlim(0, 10); ax7.set_ylim(0, 8)
    ax7.axis('off')
    ax7.set_title('7. PERCOBAAN 1-10', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    percobaan = [
        ("1.  Bolt-Nut-Washer", "Coincident + Concentric", C_BLUE),
        ("2.  Engsel / Hinge", "Hinge Mate + Angle limit", C_BLUE),
        ("3.  Slider-Crank", "Distance + Concentric + Slot", C_GREEN),
        ("4.  Gear Pair", "Gear Mate (ratio 20:30)", C_GREEN),
        ("5.  Pulley-Belt", "Path Mate + Tangent", C_PURPLE),
        ("6.  Clamp Assembly", "Coincident + Tangent + Angle", C_PURPLE),
        ("7.  Motor + Reducer", "Standard + Gear Mate (1:3)", C_ORANGE),
        ("8.  Linear Guide", "Width Mate + Coincident", C_ORANGE),
        ("9.  Cam-Follower", "Cam Mate + Concentric", C_TEAL),
        ("10. Complete Mechanism", "Semua mate gabungan", C_TEAL),
    ]
    for i, (name, mates, col) in enumerate(percobaan):
        cy = 7.2 - i * 0.7
        ax7.text(0.2, cy, name, fontsize=8.5, fontweight='bold', color=col)
        ax7.text(5.5, cy, mates, fontsize=8, color='#616161')

    # ==== SECTION 8: Motion Study + Tips ====
    ax8 = fig.add_axes([0.52, 0.22, 0.47, 0.20])
    ax8.set_xlim(0, 10); ax8.set_ylim(0, 8)
    ax8.axis('off')
    ax8.set_title('8. MOTION STUDY & TIPS', fontweight='bold', fontsize=13, color=C_ACCENT, loc='left', pad=8)

    # Motion Study
    ax8.add_patch(FancyBboxPatch((0.2, 4.5), 9.3, 3.0, boxstyle="round,pad=0.08",
                                  facecolor=C_LB, edgecolor=C_BLUE, linewidth=1.5))
    ax8.text(4.85, 7.0, '🎬 BASIC MOTION STUDY', ha='center', fontsize=11, fontweight='bold', color=C_BLUE)
    motion_steps = [
        "1. Klik tab Motion Study 1 (bawah Graphics Area)",
        "2. Pilih Basic Motion dari dropdown",
        "3. Atur Motor pada shaft: Rotary, 30 RPM",
        "4. Klik Play → amati gerakan mekanisme",
        "5. Record → buat video animasi",
    ]
    for i, s in enumerate(motion_steps):
        ax8.text(0.5, 6.3 - i*0.38, s, fontsize=8, color='#424242')

    # Tips
    ax8.add_patch(FancyBboxPatch((0.2, 0.3), 4.3, 3.8, boxstyle="round,pad=0.06",
                                  facecolor='#E8F5E9', edgecolor=C_GREEN, linewidth=1.5))
    ax8.text(2.35, 3.7, "💡 TIPS", ha='center', fontsize=10, fontweight='bold', color=C_GREEN)
    tips = [
        "✅ Part pertama = Fixed",
        "✅ Beri mate bertahap",
        "✅ Cek DOF tiap step",
        "✅ Gunakan Suppress untuk\n    mate bermasalah",
        "✅ Exploded View terakhir",
    ]
    for i, t in enumerate(tips):
        ax8.text(0.5, 3.0 - i*0.55, t, fontsize=7.5, color='#2E7D32')

    # Caution
    ax8.add_patch(FancyBboxPatch((5.0, 0.3), 4.5, 3.8, boxstyle="round,pad=0.06",
                                  facecolor='#FFEBEE', edgecolor=C_RED, linewidth=1.5))
    ax8.text(7.25, 3.7, "⚠️ HINDARI", ha='center', fontsize=10, fontweight='bold', color=C_RED)
    cautions = [
        "❌ Over-constrained assembly",
        "❌ Circular mate references",
        "❌ Fix semua komponen",
        "❌ Mate tanpa face/edge\n    yang tepat",
        "❌ Skip interference check",
    ]
    for i, c in enumerate(cautions):
        ax8.text(5.3, 3.0 - i*0.55, c, fontsize=7.5, color=C_RED)

    # ---- FOOTER ----
    fig.text(0.5, 0.19, 'Modul Praktikum CAD/CAM — Modul 6: CAD Assembly — Standard, Advanced & Mechanical Mates',
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
    fig.text(0.5, 0.975, 'PROJECT MODUL 6: ASSEMBLY MEKANIK + FRAME ALUMINIUM', ha='center', va='top',
             fontsize=22, fontweight='bold', color=C_TITLE,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3E0', edgecolor=C_ORANGE, linewidth=2))
    fig.text(0.5, 0.953, 'Press Tool Sederhana + Assembly Frame Aluminium Workstation',
             ha='center', va='top', fontsize=13, color='#546E7A', style='italic')

    # ==== PROJECT A: Press Tool ====
    ax_a = fig.add_axes([0.02, 0.52, 0.96, 0.42])
    ax_a.set_xlim(0, 20); ax_a.set_ylim(0, 15)
    ax_a.axis('off')
    ax_a.set_title('PROJECT A: MEKANISME PRESS TOOL SEDERHANA', fontweight='bold',
                    fontsize=16, color=C_RED, loc='left', pad=10)

    # Ilustrasi Press Tool (isometric-like)
    # Base Frame
    ax_a.add_patch(FancyBboxPatch((1, 1.5), 8, 1.5, boxstyle="round,pad=0.05",
                                   facecolor='#90A4AE', edgecolor='#37474F', linewidth=2))
    ax_a.text(5, 2.25, 'BASE FRAME', ha='center', fontsize=9, fontweight='bold', color='white')

    # Guide Pillars (2x)
    for px in [2.5, 7.5]:
        ax_a.add_patch(patches.Rectangle((px-0.15, 3.0), 0.3, 5.5,
                                          facecolor='#78909C', edgecolor='#37474F', linewidth=1.5))
    ax_a.text(2.5, 8.8, 'Guide\nPillar', ha='center', fontsize=7, color='#37474F')

    # Die (di base)
    ax_a.add_patch(FancyBboxPatch((3.5, 3.0), 3, 0.8, boxstyle="round,pad=0.03",
                                   facecolor='#FFA726', edgecolor='#E65100', linewidth=2))
    ax_a.text(5, 3.4, 'DIE', ha='center', fontsize=9, fontweight='bold', color='white')

    # Upper Plate
    ax_a.add_patch(FancyBboxPatch((1.5, 6.5), 7, 1.0, boxstyle="round,pad=0.05",
                                   facecolor='#64B5F6', edgecolor='#1565C0', linewidth=2))
    ax_a.text(5, 7.0, 'UPPER PLATE (↕ naik-turun)', ha='center', fontsize=9, fontweight='bold', color='white')

    # Punch
    ax_a.add_patch(patches.Rectangle((4.2, 4.5), 1.6, 2.0,
                                      facecolor='#EF5350', edgecolor='#B71C1C', linewidth=2))
    ax_a.text(5, 5.5, 'PUNCH', ha='center', fontsize=8, fontweight='bold', color='white')

    # Guide Bushings
    for px in [2.5, 7.5]:
        ax_a.add_patch(Circle((px, 6.8), 0.25, facecolor='#FFD54F', edgecolor='#F57F17', linewidth=1.5))
    ax_a.text(7.5, 8.8, 'Guide\nBushing', ha='center', fontsize=7, color='#F57F17')

    # Stripper
    ax_a.add_patch(FancyBboxPatch((3.2, 4.0), 3.6, 0.4, boxstyle="round,pad=0.02",
                                   facecolor='#A5D6A7', edgecolor='#2E7D32', linewidth=1.5))
    ax_a.text(5, 4.2, 'STRIPPER', ha='center', fontsize=7, fontweight='bold', color='#1B5E20')

    # Springs
    for px in [3.5, 6.5]:
        for sy in np.linspace(4.8, 6.3, 6):
            ax_a.plot([px-0.1, px+0.1], [sy, sy+0.15], 'g-', linewidth=1.5)
            ax_a.plot([px+0.1, px-0.1], [sy+0.15, sy+0.3], 'g-', linewidth=1.5)
    ax_a.text(3.5, 4.5, 'Spring', ha='center', fontsize=6, color=C_GREEN)

    # Handle
    ax_a.plot([8.5, 10], [7.0, 8.5], color='#5D4037', linewidth=4, solid_capstyle='round')
    ax_a.text(9.5, 9, 'HANDLE', ha='center', fontsize=8, fontweight='bold', color='#5D4037')

    # Motion arrows
    ax_a.annotate('', xy=(5, 9.5), xytext=(5, 8.5),
                  arrowprops=dict(arrowstyle='->', lw=2.5, color=C_RED))
    ax_a.annotate('', xy=(5, 8.5), xytext=(5, 9.5),
                  arrowprops=dict(arrowstyle='->', lw=2.5, color=C_RED))

    # Komponen list
    ax_a.add_patch(FancyBboxPatch((11.5, 1.0), 8.0, 8.5, boxstyle="round,pad=0.15",
                                   facecolor='#FFF8E1', edgecolor=C_ORANGE, linewidth=1.5))
    ax_a.text(15.5, 9.0, 'KOMPONEN (9 Parts)', ha='center', fontsize=11, fontweight='bold', color=C_ORANGE)

    parts = [
        ("1. Base Frame", "Plat tebal alas"),
        ("2. Guide Pillars (2x)", "Silinder guide"),
        ("3. Guide Bushings (2x)", "Bushing di upper plate"),
        ("4. Upper Plate", "Plat bergerak ↕"),
        ("5. Punch", "Profil potong"),
        ("6. Die", "Cetakan di base"),
        ("7. Stripper", "Plat penekan material"),
        ("8. Spring (4x)", "Pegas penekan"),
        ("9. Handle", "Tuas penggerak"),
    ]
    for i, (name, desc) in enumerate(parts):
        ax_a.text(12.0, 8.2 - i*0.75, f"{name}", fontsize=9, fontweight='bold', color='#424242')
        ax_a.text(16.5, 8.2 - i*0.75, desc, fontsize=8, color='#757575')

    # Deliverables
    ax_a.text(15.5, 1.5, 'Deliverables: 9 .sldprt + Assembly + Exploded + Motion + BOM',
              ha='center', fontsize=8, fontweight='bold', color=C_RED,
              bbox=dict(boxstyle='round,pad=0.2', facecolor=C_LR, edgecolor=C_RED, linewidth=1))

    # ==== PROJECT B: Frame Aluminium ====
    ax_b = fig.add_axes([0.02, 0.06, 0.96, 0.44])
    ax_b.set_xlim(0, 20); ax_b.set_ylim(0, 15)
    ax_b.axis('off')
    ax_b.set_title('PROJECT B: ASSEMBLY FRAME ALUMINIUM WORKSTATION', fontweight='bold',
                    fontsize=16, color=C_TEAL, loc='left', pad=10)

    # Frame illustration (isometric)
    # Vertical posts (4x)
    posts = [(2, 4), (7, 4), (3.5, 6), (8.5, 6)]
    for px, py in posts:
        ax_b.add_patch(patches.Rectangle((px-0.15, py), 0.3, 4.5,
                                          facecolor='#B0BEC5', edgecolor='#455A64', linewidth=1.5))

    # Horizontal bars top
    ax_b.plot([2, 7], [8.5, 8.5], color='#455A64', linewidth=3)
    ax_b.plot([3.5, 8.5], [10.5, 10.5], color='#455A64', linewidth=3)
    ax_b.plot([2, 3.5], [8.5, 10.5], color='#455A64', linewidth=2)
    ax_b.plot([7, 8.5], [8.5, 10.5], color='#455A64', linewidth=2)

    # Horizontal bars bottom
    ax_b.plot([2, 7], [4, 4], color='#455A64', linewidth=3)
    ax_b.plot([3.5, 8.5], [6, 6], color='#455A64', linewidth=3)
    ax_b.plot([2, 3.5], [4, 6], color='#455A64', linewidth=2)
    ax_b.plot([7, 8.5], [4, 6], color='#455A64', linewidth=2)

    # Corner brackets
    for bx, by in [(2, 8.5), (7, 8.5), (2, 4), (7, 4)]:
        ax_b.add_patch(FancyBboxPatch((bx-0.2, by-0.2), 0.4, 0.4, boxstyle="round,pad=0.02",
                                       facecolor='#FFB74D', edgecolor=C_ORANGE, linewidth=1.2))

    # Adjustable feet
    for fx, fy in [(2, 3.5), (7, 3.5), (3.5, 5.5), (8.5, 5.5)]:
        ax_b.add_patch(Circle((fx, fy), 0.2, facecolor='#78909C', edgecolor='#37474F', linewidth=1.5))

    # Labels
    ax_b.text(5, 12, 'FRAME WORKSTATION', ha='center', fontsize=12, fontweight='bold', color=C_TEAL,
              bbox=dict(boxstyle='round,pad=0.3', facecolor=C_LG, edgecolor=C_TEAL, linewidth=1.5))

    ax_b.annotate('Profil 4040\n1200mm (4x)', xy=(4.5, 8.5), xytext=(0.5, 11),
                  fontsize=8, color='#455A64', fontweight='bold',
                  arrowprops=dict(arrowstyle='->', color='#455A64'))
    ax_b.annotate('Profil 4040\n800mm (4x)', xy=(2, 6), xytext=(0.5, 7.5),
                  fontsize=8, color='#455A64', fontweight='bold',
                  arrowprops=dict(arrowstyle='->', color='#455A64'))
    ax_b.annotate('Profil 4040\n710mm (4x)', xy=(7, 6), xytext=(9.5, 7),
                  fontsize=8, color='#455A64', fontweight='bold',
                  arrowprops=dict(arrowstyle='->', color='#455A64'))
    ax_b.annotate('Corner Bracket\n(16x)', xy=(7, 8.3), xytext=(9, 9.5),
                  fontsize=8, color=C_ORANGE, fontweight='bold',
                  arrowprops=dict(arrowstyle='->', color=C_ORANGE))
    ax_b.annotate('Adjustable\nFoot (4x)', xy=(7, 3.5), xytext=(9, 2.5),
                  fontsize=8, color='#37474F', fontweight='bold',
                  arrowprops=dict(arrowstyle='->', color='#37474F'))

    # Komponen list
    ax_b.add_patch(FancyBboxPatch((11.5, 5.0), 8.0, 9.5, boxstyle="round,pad=0.15",
                                   facecolor='#E0F2F1', edgecolor=C_TEAL, linewidth=1.5))
    ax_b.text(15.5, 14.0, 'KOMPONEN ASSEMBLY', ha='center', fontsize=11, fontweight='bold', color=C_TEAL)

    comp = [
        ("Frame Structure:", ""),
        ("  4× Profil 4040", "@ 1200mm (H panjang)"),
        ("  4× Profil 4040", "@ 800mm (H pendek)"),
        ("  4× Profil 4040", "@ 710mm (vertikal)"),
        ("Connectors:", ""),
        ("  16× Corner Bracket", "4040"),
        ("  16× T-Nut M8", "(2 per bracket)"),
        ("  16× Hex Bolt M8×16", "(untuk bracket)"),
        ("Accessories:", ""),
        ("  4× Adjustable Foot", "M10"),
        ("  4× End Cap 4040", "(ujung atas)"),
        ("Optional:", ""),
        ("  2× Gusset Plate", "(penguat diagonal)"),
    ]
    for i, (name, desc) in enumerate(comp):
        is_header = name.endswith(':')
        ax_b.text(12.0, 13.2 - i*0.62, name, fontsize=8.5,
                  fontweight='bold' if is_header else 'normal',
                  color=C_TEAL if is_header else '#424242')
        if desc:
            ax_b.text(17, 13.2 - i*0.62, desc, fontsize=8, color='#757575')

    # Teknik Assembly
    ax_b.add_patch(FancyBboxPatch((0.3, 0.3), 10.5, 4.5, boxstyle="round,pad=0.12",
                                   facecolor=C_LB, edgecolor=C_BLUE, linewidth=1.5))
    ax_b.text(5.55, 4.3, 'TEKNIK ASSEMBLY', ha='center', fontsize=11, fontweight='bold', color=C_BLUE)
    teknik = [
        "1. Insert profil pertama (Fixed)",
        "2. Mate Coincident + Parallel",
        "3. Pattern untuk profil repetitif",
        "4. Insert corner bracket → Coincident ke T-slot",
        "5. Insert bolt & T-nut (Smart Fastener)",
        "6. Limit Mate untuk adjustable foot (0-20mm)",
        "7. Exploded View dengan step configuration",
    ]
    for i, t in enumerate(teknik):
        ax_b.text(0.6, 3.7 - i*0.47, t, fontsize=8.5, color='#424242')

    # Penilaian
    ax_b.add_patch(FancyBboxPatch((11.5, 0.3), 8.0, 4.2, boxstyle="round,pad=0.12",
                                   facecolor='#FFF3E0', edgecolor=C_ORANGE, linewidth=1.5))
    ax_b.text(15.5, 4.0, 'KRITERIA PENILAIAN', ha='center', fontsize=11, fontweight='bold', color=C_ORANGE)
    penilaian = [
        ("A: Kelengkapan + Mate benar", "35%"),
        ("A: Motion Study berjalan", "10%"),
        ("B: Frame + connector ter-assembly", "30%"),
        ("B: Mate tanpa error (fully def)", "10%"),
        ("Exploded View + BOM + Drawing", "15%"),
    ]
    for i, (crit, bobot) in enumerate(penilaian):
        ax_b.text(12.0, 3.3 - i*0.55, f"• {crit}", fontsize=8.5, color='#424242')
        ax_b.text(18.8, 3.3 - i*0.55, bobot, fontsize=9, fontweight='bold', color=C_ORANGE, ha='center')

    # FOOTER
    fig.text(0.5, 0.035, 'Project Praktikum CAD/CAM — Modul 6: Assembly Mekanik + Frame Aluminium Workstation',
             ha='center', fontsize=10, color='#9E9E9E', style='italic')

    plt.savefig(os.path.join(IMG_DIR, 'p01_deskripsi.png'), dpi=150, bbox_inches='tight', facecolor=BG)
    print("✓ image/p01_deskripsi.png")
    plt.close()


# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("GENERATING IMAGES FOR MODUL 6 - CAD ASSEMBLY")
    print("="*60)

    generate_materi_image()
    generate_project_image()

    print("\n✓ Semua gambar Modul 6 berhasil dibuat!")
    print(f"  Lokasi: {IMG_DIR}/")
    print("="*60 + "\n")
