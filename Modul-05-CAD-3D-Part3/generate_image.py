"""
VISUALISASI KONSEP TEKNIK LANJUTAN - MODUL 5
Mengilustrasikan:
1. Configurations & Design Table
2. Equations & Link Values
3. Surface Modeling
4. Mold Tools
5. Weldments
6. Library Features & Import/Export
7. Deskripsi Materi (Overview)
8. Deskripsi Project (Overview)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Polygon, Arc
import os
import warnings
warnings.filterwarnings('ignore')

IMG_DIR = '/home/sirobo/Documents/Praktikum-CADCAM/Modul-05-CAD-3D-Part3/image'
os.makedirs(IMG_DIR, exist_ok=True)


# ============================================================================
# 1. CONFIGURATIONS & DESIGN TABLE
# ============================================================================
def configurations_design_table():
    """Visualisasi Configurations dan Design Table"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('CONFIGURATIONS & DESIGN TABLE — MODUL 5', fontsize=14, fontweight='bold')

    # 1.1 Configurations
    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('1. CONFIGURATIONS', fontweight='bold', fontsize=12)

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 13, boxstyle='round,pad=0.3',
                 facecolor='#e3f2fd', edgecolor='#1565c0', linewidth=2))

    # One file, multiple configs
    ax.text(6, 13, '📂 Bolt_Standard.sldprt', fontsize=11, fontweight='bold', ha='center', color='#1565c0')
    ax.plot([6, 6], [12.5, 10.5], 'k-', linewidth=2)
    ax.plot([6, 2], [10.5, 9], 'k-', linewidth=1.5)
    ax.plot([6, 6], [10.5, 9], 'k-', linewidth=1.5)
    ax.plot([6, 10], [10.5, 9], 'k-', linewidth=1.5)

    configs = [
        (2, 'M6', '#42a5f5', 'Ø6\nL=20', 1.2),
        (6, 'M8', '#66bb6a', 'Ø8\nL=25', 1.6),
        (10, 'M10', '#ffa726', 'Ø10\nL=30', 2.0),
    ]
    for cx, name, color, spec, r in configs:
        ax.add_patch(FancyBboxPatch((cx-1.5, 4), 3, 4.5, boxstyle='round,pad=0.2',
                     facecolor='white', edgecolor=color, linewidth=2))
        ax.text(cx, 8, name, fontsize=13, fontweight='bold', ha='center', color=color)
        # Simple bolt shape
        ax.add_patch(patches.Rectangle((cx-r/2, 5.5), r, 2, facecolor=color, alpha=0.4, edgecolor='#333'))
        ax.add_patch(FancyBboxPatch((cx-r*0.8, 5.5+2), r*1.6, 0.6, boxstyle='round,pad=0.05',
                     facecolor=color, alpha=0.6, edgecolor='#333'))
        ax.text(cx, 4.5, spec, fontsize=8, ha='center', color='#333')

    ax.text(6, 2, '1 file → 3 configurations\nDimensi berbeda per config', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='orange'))

    # 1.2 Design Table
    ax = axes[1]
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('2. DESIGN TABLE (Excel)', fontweight='bold', fontsize=12)

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 13.4, 13, boxstyle='round,pad=0.3',
                 facecolor='#e8f5e9', edgecolor='#2e7d32', linewidth=2))

    # Table
    table_data = [
        ['Parameter', 'M6', 'M8', 'M10'],
        ['D1@Sketch1\n(diameter)', '6', '8', '10'],
        ['D2@Sketch1\n(head dia)', '10', '13', '16'],
        ['D1@Extrude1\n(length)', '20', '25', '30'],
        ['D1@Fillet1\n(fillet R)', '0.5', '0.8', '1.0'],
    ]
    colors_row = ['#c8e6c9', '#fff', '#f5f5f5', '#fff', '#f5f5f5']

    table_x, table_y = 1, 3
    col_w = [3.5, 2.2, 2.2, 2.2]
    row_h = 1.6

    for r, row in enumerate(table_data):
        for c, cell in enumerate(row):
            x = table_x + sum(col_w[:c])
            y = table_y + (len(table_data) - r) * row_h
            fc = '#2e7d32' if r == 0 else colors_row[r]
            tc = 'white' if r == 0 else '#333'
            fw = 'bold' if r == 0 or c == 0 else 'normal'
            ax.add_patch(patches.Rectangle((x, y), col_w[c], row_h,
                         facecolor=fc, edgecolor='#333', linewidth=1))
            ax.text(x + col_w[c]/2, y + row_h/2, cell, fontsize=8, ha='center', va='center',
                    color=tc, fontweight=fw)

    ax.text(7, 12.5, '📊 Excel Embedded di SolidWorks', fontsize=11, fontweight='bold', ha='center', color='#2e7d32')
    ax.text(7, 2, 'Insert → Tables → Design Table\nOtomatis manage semua configurations', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='orange'))

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/01_configurations_design_table.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/01_configurations_design_table.png")
    plt.close()


# ============================================================================
# 2. EQUATIONS & PARAMETRIC
# ============================================================================
def equations_parametric():
    """Visualisasi Equations dan Parametric Design"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle('EQUATIONS & PARAMETRIC DESIGN — MODUL 5', fontsize=14, fontweight='bold')

    # 2.1 Equations
    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('1. EQUATIONS (Rumus Parametrik)', fontweight='bold')

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 11.4, boxstyle='round,pad=0.3',
                 facecolor='#fff3e0', edgecolor='#e65100', linewidth=2))

    # Equations examples
    ax.text(6, 11, '⚙️ Tools → Equations', fontsize=12, fontweight='bold', ha='center', color='#e65100')

    equations = [
        ('"Width@Sketch1" = 100', 'Dimensi langsung'),
        ('"Height@Sketch1" = "Width" * 0.6', 'Proporsional'),
        ('"Fillet@Fillet1" = "Width" * 0.1', 'Fillet otomatis'),
        ('"Wall" = IF("Width">150, 3, 2)', 'Kondisional'),
        ('sqrt("W"^2 + "H"^2)', 'Fungsi matematika'),
    ]
    for i, (eq, desc) in enumerate(equations):
        y = 9.5 - i * 1.8
        ax.add_patch(FancyBboxPatch((0.8, y - 0.5), 10.4, 1.5, boxstyle='round,pad=0.1',
                     facecolor='white', edgecolor='#e65100', linewidth=1))
        ax.text(1.2, y + 0.3, eq, fontsize=9, fontweight='bold', family='monospace', color='#333')
        ax.text(1.2, y - 0.2, f'→ {desc}', fontsize=8, color='#777')

    ax.text(6, 0.8, 'Ubah 1 variabel → semua dimensi update!', ha='center', fontsize=9,
            fontweight='bold', color='#c62828')

    # 2.2 External Link (Excel)
    ax = axes[1]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('2. LINK TO EXTERNAL FILE (Excel)', fontweight='bold')

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 11.4, boxstyle='round,pad=0.3',
                 facecolor='#f3e5f5', edgecolor='#6a1b9a', linewidth=2))

    # Excel file
    ax.add_patch(FancyBboxPatch((1, 7), 4.5, 4, boxstyle='round,pad=0.2',
                 facecolor='#c8e6c9', edgecolor='#2e7d32', linewidth=2))
    ax.text(3.25, 10.5, '📊 Excel File', fontsize=11, fontweight='bold', ha='center', color='#2e7d32')
    excel_data = [('Length', '100'), ('Width', '50'), ('Thickness', '5')]
    for i, (param, val) in enumerate(excel_data):
        ax.text(1.5, 9.8 - i * 0.9, f'{param}: {val}', fontsize=9, family='monospace')

    # Arrow
    ax.annotate('', xy=(8, 9), xytext=(6, 9), arrowprops=dict(arrowstyle='->', color='#6a1b9a', lw=3))
    ax.text(7, 9.5, 'Link', fontsize=10, fontweight='bold', ha='center', color='#6a1b9a')

    # SolidWorks part
    ax.add_patch(FancyBboxPatch((7, 7), 4.5, 4, boxstyle='round,pad=0.2',
                 facecolor='#bbdefb', edgecolor='#1565c0', linewidth=2))
    ax.text(9.25, 10.5, '📐 SolidWorks', fontsize=11, fontweight='bold', ha='center', color='#1565c0')
    ax.text(9.25, 9, 'Part auto-update\nketika Excel\nberubah', ha='center', fontsize=9, color='#333')

    # Global Variables
    ax.add_patch(FancyBboxPatch((1, 1.5), 10, 4.5, boxstyle='round,pad=0.2',
                 facecolor='white', edgecolor='#6a1b9a', linewidth=1.5))
    ax.text(6, 5.5, '🔗 Global Variables', fontsize=11, fontweight='bold', ha='center', color='#6a1b9a')
    gv = ['• "Thickness" = 5  →  dipakai di seluruh part',
          '• "Slot_Width" = 8  →  dipakai di banyak feature',
          '• Ubah 1x → update semua feature terkait']
    for i, g in enumerate(gv):
        ax.text(1.5, 4.5 - i * 1.1, g, fontsize=9, ha='left')

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/02_equations_parametric.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/02_equations_parametric.png")
    plt.close()


# ============================================================================
# 3. SURFACE MODELING
# ============================================================================
def surface_modeling():
    """Visualisasi Surface Modeling"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('SURFACE MODELING — MODUL 5', fontsize=14, fontweight='bold')

    surface_types = [
        ('Extruded\nSurface', 'Surface dari sketch\ndi-extrude (tanpa tebal)', '#42a5f5'),
        ('Revolved\nSurface', 'Surface dari sketch\ndiputar terhadap axis', '#66bb6a'),
        ('Lofted\nSurface', 'Surface dari\nbeberapa profil', '#ffa726'),
        ('Swept\nSurface', 'Surface sepanjang\npath', '#ef5350'),
        ('Planar\nSurface', 'Surface datar\nuntuk menutup lubang', '#ab47bc'),
        ('Knit\nSurface', 'Menggabungkan\nbeberapa surface', '#26a69a'),
    ]

    for idx, (name, desc, color) in enumerate(surface_types):
        row, col = idx // 3, idx % 3
        ax = axes[row, col]
        ax.set_xlim(-1, 11)
        ax.set_ylim(-1, 11)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.2)
        ax.set_title(f'{idx+1}. {name.replace(chr(10), " ")}', fontweight='bold')

        if idx == 0:  # Extruded Surface
            t = np.linspace(0, np.pi, 50)
            ax.plot(1 + t*2.5, 5 + 2*np.sin(t), color, linewidth=3)
            ax.plot(3 + t*2.5, 3 + 2*np.sin(t), color, linewidth=2, alpha=0.5)
            for tt in [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:
                ax.plot([1+tt*2.5, 3+tt*2.5], [5+2*np.sin(tt), 3+2*np.sin(tt)], color, linewidth=1, alpha=0.3)
        elif idx == 1:  # Revolved Surface
            theta = np.linspace(0, 2*np.pi, 100)
            for r in [2, 2.5, 3]:
                ax.plot(5 + r*np.cos(theta), 5 + r*0.3*np.sin(theta), color, linewidth=1.5, alpha=0.4 + r*0.1)
            ax.plot([5, 5], [1, 9], 'k--', linewidth=1.5, label='Axis')
            ax.legend(fontsize=8)
        elif idx == 2:  # Lofted Surface
            for i, (cy, r) in enumerate([(2, 2), (5, 3), (8, 1.5)]):
                t = np.linspace(0, np.pi, 50)
                ax.plot(5 + r*np.cos(t), cy + r*0.2*np.sin(t), color, linewidth=2)
            ax.plot([3, 2, 3.5], [2, 5, 8], color=color, linestyle='--', linewidth=1, alpha=0.5)
            ax.plot([7, 8, 6.5], [2, 5, 8], color=color, linestyle='--', linewidth=1, alpha=0.5)
        elif idx == 3:  # Swept Surface
            t = np.linspace(0, 3*np.pi, 200)
            sx = 2 + t * 0.8
            sy = 5 + 2*np.sin(t)
            ax.plot(sx, sy, color, linewidth=2.5)
            ax.plot(sx, sy + 0.5, color, linewidth=1, alpha=0.4)
            ax.plot(sx, sy - 0.5, color, linewidth=1, alpha=0.4)
        elif idx == 4:  # Planar Surface
            theta = np.linspace(0, 2*np.pi, 100)
            ax.plot(5 + 3*np.cos(theta), 5 + 3*np.sin(theta), color, linewidth=2.5)
            ax.fill(5 + 3*np.cos(theta), 5 + 3*np.sin(theta), color=color, alpha=0.2)
            ax.text(5, 5, 'Planar\n(flat)', ha='center', fontsize=9, color=color, fontweight='bold')
        elif idx == 5:  # Knit Surface
            for i, (cx, cy, r) in enumerate([(3, 5, 2.5), (7, 5, 2.5)]):
                theta = np.linspace(0, 2*np.pi, 100)
                ax.plot(cx + r*np.cos(theta), cy + r*np.sin(theta), color, linewidth=2, alpha=0.6)
            ax.annotate('', xy=(5.5, 5), xytext=(4.5, 5), arrowprops=dict(arrowstyle='<->', color='red', lw=2))
            ax.text(5, 3.5, 'Knit = Join', ha='center', fontsize=9, color='red', fontweight='bold')

        ax.text(5, 0, desc, ha='center', fontsize=8, bbox=dict(boxstyle='round', facecolor='lightyellow'))

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/03_surface_modeling.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/03_surface_modeling.png")
    plt.close()


# ============================================================================
# 4. WELDMENTS & MOLD TOOLS
# ============================================================================
def weldments_mold():
    """Visualisasi Weldments dan Mold Tools"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('WELDMENTS & MOLD TOOLS — MODUL 5', fontsize=14, fontweight='bold')

    # 4.1 Weldments
    ax = axes[0]
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 13)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('1. WELDMENTS (Frame Structure)', fontweight='bold')

    # Frame (table top view → isometric simplified)
    # Top frame
    ax.plot([1, 13], [11, 11], 'b-', linewidth=6, solid_capstyle='round')
    ax.plot([1, 13], [7, 7], 'b-', linewidth=6, solid_capstyle='round')
    ax.plot([1, 1], [7, 11], 'b-', linewidth=6, solid_capstyle='round')
    ax.plot([13, 13], [7, 11], 'b-', linewidth=6, solid_capstyle='round')

    # Legs
    ax.plot([1, 1], [7, 1], 'r-', linewidth=6, solid_capstyle='round')
    ax.plot([13, 13], [7, 1], 'r-', linewidth=6, solid_capstyle='round')
    ax.plot([7, 7], [7, 1], 'r-', linewidth=5, solid_capstyle='round', alpha=0.4)

    # Cross brace
    ax.plot([1, 13], [4, 4], 'g-', linewidth=4, solid_capstyle='round', label='Cross Support 3030')

    # Labels
    ax.text(7, 11.8, 'Frame Atas: 4040', fontsize=9, ha='center', color='blue', fontweight='bold')
    ax.text(0, 4, 'Kaki: 4040', fontsize=9, ha='left', color='red', fontweight='bold')
    ax.text(7, 4.8, 'Cross: 3030', fontsize=9, ha='center', color='green', fontweight='bold')

    ax.text(7, -0.5, 'Workflow: 3D Sketch → Structural Member\n→ Trim Corners → Cut List (BOM)', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='orange'))

    # 4.2 Mold Tools
    ax = axes[1]
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 13)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('2. MOLD TOOLS (Injection Mold)', fontweight='bold')

    # Cavity (top)
    ax.add_patch(patches.Rectangle((1, 7), 12, 4.5, facecolor='#bbdefb', edgecolor='#1565c0', linewidth=2))
    ax.text(7, 10, 'CAVITY (Rongga Atas)', fontsize=11, ha='center', fontweight='bold', color='#1565c0')
    # Cavity shape
    t = np.linspace(0, np.pi, 100)
    ax.fill_between(4 + t*2, 7, 7 + 1.5*np.sin(t), color='#e3f2fd', edgecolor='#333')

    # Parting line
    ax.plot([1, 13], [7, 7], 'r-', linewidth=3)
    ax.text(14, 7, 'Parting\nLine', fontsize=9, color='red', fontweight='bold')

    # Core (bottom)
    ax.add_patch(patches.Rectangle((1, 2.5), 12, 4.5, facecolor='#c8e6c9', edgecolor='#2e7d32', linewidth=2))
    ax.text(7, 4, 'CORE (Inti Bawah)', fontsize=11, ha='center', fontweight='bold', color='#2e7d32')
    # Core protrusion
    t = np.linspace(0, np.pi, 100)
    ax.fill_between(4 + t*2, 7, 7 - 1*np.sin(t), color='#e8f5e9', edgecolor='#333')

    # Workflow
    steps = ['Draft\nAnalysis', 'Scale\n(Shrinkage)', 'Parting\nLine', 'Parting\nSurface', 'Tooling\nSplit']
    for i, step in enumerate(steps):
        x = 2 + i * 2.5
        ax.add_patch(FancyBboxPatch((x-0.8, 0.2), 2, 1.8, boxstyle='round,pad=0.1',
                     facecolor='#fff3e0', edgecolor='#e65100', linewidth=1.5))
        ax.text(x + 0.2, 1.1, step, fontsize=7.5, ha='center', va='center', fontweight='bold', color='#e65100')
        if i < 4:
            ax.annotate('', xy=(x+1.5, 1.1), xytext=(x+1.1, 1.1),
                       arrowprops=dict(arrowstyle='->', color='#e65100', lw=1.5))

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/04_weldments_mold.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/04_weldments_mold.png")
    plt.close()


# ============================================================================
# 5. LIBRARY FEATURES & IMPORT/EXPORT
# ============================================================================
def library_import_export():
    """Visualisasi Library Features dan Import/Export"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle('LIBRARY FEATURES & IMPORT/EXPORT — MODUL 5', fontsize=14, fontweight='bold')

    # 5.1 Library Features
    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('1. DESIGN LIBRARY & LIBRARY FEATURES', fontweight='bold')

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 11.4, boxstyle='round,pad=0.3',
                 facecolor='#e0f7fa', edgecolor='#00695c', linewidth=2))

    # Library tree
    ax.text(2, 11, '📚 Design Library', fontsize=12, fontweight='bold', color='#00695c')
    tree_items = [
        ('  📁 Toolbox', 'Bolt, Nut, Washer, Bearing'),
        ('  📁 Custom Features', 'T-Slot, Pocket, Pattern'),
        ('  📁 Parts', 'Reusable components'),
        ('  📁 Assemblies', 'Sub-assemblies'),
    ]
    for i, (name, desc) in enumerate(tree_items):
        ax.text(1, 9.5 - i * 1.5, name, fontsize=10, fontweight='bold', ha='left')
        ax.text(1, 8.8 - i * 1.5, f'       → {desc}', fontsize=8.5, ha='left', color='#555')

    # Library Feature workflow
    ax.add_patch(FancyBboxPatch((0.8, 0.8), 10.4, 3, boxstyle='round,pad=0.2',
                 facecolor='white', edgecolor='#00695c', linewidth=1.5))
    ax.text(6, 3.3, '📦 Library Feature (.sldlfp)', fontsize=10, fontweight='bold', ha='center', color='#00695c')
    ax.text(6, 2.2, 'Buat Feature → Save As .sldlfp → Drag & Drop ke part lain', ha='center', fontsize=9)
    ax.text(6, 1.3, 'Contoh: T-Slot profile, Custom pocket, Mounting pattern', ha='center', fontsize=8, color='#777')

    # 5.2 Import/Export
    ax = axes[1]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('2. IMPORT & EXPORT FORMATS', fontweight='bold')

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 11.4, boxstyle='round,pad=0.3',
                 facecolor='#fce4ec', edgecolor='#880e4f', linewidth=2))

    ax.text(6, 11, '📥 IMPORT', fontsize=12, fontweight='bold', ha='center', color='#2e7d32')
    imports = [
        ('STEP (.stp)', '✅ Paling direkomendasikan'),
        ('IGES (.igs)', '⚠️ Geometry saja'),
        ('Parasolid (.x_t)', '✅ Siemens native'),
        ('STL (.stl)', '⚠️ Mesh, bukan solid'),
        ('DXF/DWG', '📐 2D AutoCAD'),
    ]
    for i, (fmt, note) in enumerate(imports):
        ax.text(1, 9.8 - i * 1, f'• {fmt}  {note}', fontsize=8.5, ha='left')

    ax.plot([1, 11], [4.5, 4.5], 'k-', linewidth=1, alpha=0.3)

    ax.text(6, 4, '📤 EXPORT', fontsize=12, fontweight='bold', ha='center', color='#c62828')
    exports = [
        ('STEP', 'Universal CAD exchange'),
        ('STL', '3D Printing (mesh)'),
        ('DXF', '2D CNC / Laser cutting'),
        ('eDrawings', 'Viewer untuk review'),
    ]
    for i, (fmt, use) in enumerate(exports):
        ax.text(1, 3 - i * 0.9, f'• {fmt} → {use}', fontsize=8.5, ha='left')

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/05_library_import_export.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/05_library_import_export.png")
    plt.close()


# ============================================================================
# 6. DESKRIPSI MATERI (m01_deskripsi.png)
# ============================================================================
def materi_deskripsi():
    """Overview lengkap materi Modul 5: Teknik Lanjutan"""
    fig = plt.figure(figsize=(18, 22))
    fig.patch.set_facecolor('#f0f4f8')

    # HEADER
    fig.text(0.5, 0.97, 'MODUL 5: CAD GAMBAR 3D — PART 3', fontsize=22, fontweight='bold',
             ha='center', va='top', color='#1a237e',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#bbdefb', edgecolor='#1565c0', linewidth=3))
    fig.text(0.5, 0.945, 'TEKNIK LANJUTAN (Configurations, Surfaces, Weldments)', fontsize=14,
             fontweight='bold', ha='center', va='top', color='#0d47a1')

    # --- Section 1: Configurations ---
    ax1 = fig.add_axes([0.03, 0.78, 0.45, 0.15])
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.add_patch(FancyBboxPatch((0.2, 0.5), 9.5, 9, boxstyle='round,pad=0.3',
                  facecolor='#e3f2fd', edgecolor='#1565c0', linewidth=2))
    ax1.text(5, 9, '⚙️ CONFIGURATIONS & DESIGN TABLE', fontsize=12, fontweight='bold', ha='center', color='#1565c0')
    config_items = [
        'Configurations: Variasi model dalam 1 file (S, M, L, XL)',
        'Design Table: Excel embedded untuk manage configs',
        'Parameter otomatis: dimensi, feature suppress, material',
        'Contoh: Bolt M6/M8/M10, Profil aluminium series',
        'Shortcut: Right-click → Add Configuration',
    ]
    for i, item in enumerate(config_items):
        ax1.text(0.5, 7.5 - i * 1.5, f'• {item}', fontsize=9, ha='left')

    # --- Section 2: Equations ---
    ax2 = fig.add_axes([0.52, 0.78, 0.45, 0.15])
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.add_patch(FancyBboxPatch((0.2, 0.5), 9.5, 9, boxstyle='round,pad=0.3',
                  facecolor='#e8f5e9', edgecolor='#2e7d32', linewidth=2))
    ax2.text(5, 9, '📊 EQUATIONS & PARAMETRIC', fontsize=12, fontweight='bold', ha='center', color='#2e7d32')
    eq_items = [
        'Advanced Equations: IF(), sin(), cos(), sqrt()',
        'Linked Dimensions: Dimensi terikat ke dimensi lain',
        'Global Variables: Variabel reusable di seluruh part',
        'External Link: Parameter dari Excel (.xlsx)',
        'Conditional: IF(Width>150, 3, 2) → auto wall thickness',
    ]
    for i, item in enumerate(eq_items):
        ax2.text(0.5, 7.5 - i * 1.5, f'• {item}', fontsize=9, ha='left')

    # --- Section 3: Surface Modeling ---
    ax3 = fig.add_axes([0.03, 0.57, 0.45, 0.19])
    ax3.set_xlim(0, 10); ax3.set_ylim(0, 12)
    ax3.axis('off')
    ax3.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 11.3, boxstyle='round,pad=0.3',
                  facecolor='#fff3e0', edgecolor='#e65100', linewidth=2))
    ax3.text(5, 11, '🌊 SURFACE MODELING', fontsize=13, fontweight='bold', ha='center', color='#e65100')

    surfaces = [
        ('Surface Tools', 'Extruded, Revolved, Lofted, Swept, Boundary'),
        ('Planar Surface', 'Menutup lubang dengan surface datar'),
        ('Knit Surface', 'Menggabungkan beberapa surface'),
        ('Trim/Untrim', 'Memotong/restore surface'),
        ('Extend/Offset', 'Memperpanjang edge / offset surface'),
        ('Thicken', 'Surface → Solid (memberi ketebalan)'),
    ]
    for i, (name, desc) in enumerate(surfaces):
        ax3.text(0.8, 9.5 - i * 1.7, f'• {name}', fontsize=9.5, ha='left', fontweight='bold')
        ax3.text(0.8, 8.7 - i * 1.7, f'   {desc}', fontsize=8.5, ha='left', color='#555')

    # --- Section 4: Mold Tools ---
    ax4 = fig.add_axes([0.52, 0.57, 0.45, 0.19])
    ax4.set_xlim(0, 10); ax4.set_ylim(0, 12)
    ax4.axis('off')
    ax4.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 11.3, boxstyle='round,pad=0.3',
                  facecolor='#f3e5f5', edgecolor='#6a1b9a', linewidth=2))
    ax4.text(5, 11, '🏭 MOLD TOOLS & WELDMENTS', fontsize=13, fontweight='bold', ha='center', color='#6a1b9a')

    mold_weld = [
        ('Mold: Draft Analysis', 'Analisis sudut draft untuk ejection'),
        ('Mold: Scale', 'Kompensasi shrinkage material'),
        ('Mold: Parting Line/Surface', 'Pemisah core dan cavity'),
        ('Mold: Tooling Split', 'Split menjadi Core + Cavity'),
        ('Weldments: Structural Member', 'Profil standar (tube, angle, channel)'),
        ('Weldments: Cut List', 'BOM otomatis untuk fabrikasi'),
    ]
    for i, (name, desc) in enumerate(mold_weld):
        ax4.text(0.8, 9.5 - i * 1.7, f'• {name}', fontsize=9, ha='left', fontweight='bold')
        ax4.text(0.8, 8.7 - i * 1.7, f'   {desc}', fontsize=8, ha='left', color='#555')

    # --- Section 5: Library & Import/Export ---
    ax5 = fig.add_axes([0.03, 0.38, 0.45, 0.17])
    ax5.set_xlim(0, 10); ax5.set_ylim(0, 10)
    ax5.axis('off')
    ax5.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 9.3, boxstyle='round,pad=0.3',
                  facecolor='#e0f7fa', edgecolor='#00695c', linewidth=2))
    ax5.text(5, 9, '📚 LIBRARY & IMPORT/EXPORT', fontsize=13, fontweight='bold', ha='center', color='#00695c')

    lib_items = [
        ('Design Library', 'Toolbox (Bolt/Nut/Washer/Bearing)'),
        ('Library Feature', 'Custom feature reusable (.sldlfp)'),
        ('Import', 'STEP ✅, IGES, Parasolid, STL, DXF'),
        ('Export', 'STEP, STL (3D Print), DXF (CNC), eDrawings'),
        ('Import Diagnostics', 'Repair: Knit gaps, Heal edges, Fill holes'),
    ]
    for i, (name, desc) in enumerate(lib_items):
        ax5.text(0.8, 7.5 - i * 1.4, f'• {name}', fontsize=9.5, ha='left', fontweight='bold')
        ax5.text(0.8, 6.8 - i * 1.4, f'   {desc}', fontsize=8.5, ha='left', color='#555')

    # --- Section 6: In-Context & Best Practices ---
    ax6 = fig.add_axes([0.52, 0.38, 0.45, 0.17])
    ax6.set_xlim(0, 10); ax6.set_ylim(0, 10)
    ax6.axis('off')
    ax6.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 9.3, boxstyle='round,pad=0.3',
                  facecolor='#fce4ec', edgecolor='#880e4f', linewidth=2))
    ax6.text(5, 9, '🔗 IN-CONTEXT & BEST PRACTICES', fontsize=12, fontweight='bold', ha='center', color='#880e4f')

    practices = [
        'In-Context Design: Part referensi ke part lain di assembly',
        'Top-Down Design: Desain dari assembly ke part',
        'External References: Update otomatis (→...)',
        'Sketch Fully Defined: Semua hitam sebelum feature',
        'Name Features: Rename sesuai fungsi',
        'Simplify: Configurations untuk model besar',
        'Avoid circular references dalam equations',
        'Keep Feature Tree organized dan clean',
    ]
    for i, p in enumerate(practices):
        ax6.text(0.8, 7.5 - i * 0.95, f'• {p}', fontsize=8.5, ha='left')

    # --- Section 7: Percobaan ---
    ax7 = fig.add_axes([0.03, 0.12, 0.94, 0.23])
    ax7.set_xlim(0, 20); ax7.set_ylim(0, 10)
    ax7.axis('off')
    ax7.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 9.5, boxstyle='round,pad=0.3',
                  facecolor='#fffde7', edgecolor='#f57f17', linewidth=2))
    ax7.text(10, 9.2, '📋 PERCOBAAN 1-10', fontsize=14, fontweight='bold', ha='center', color='#e65100')

    percobaan = [
        ('P1', 'Bolt Multi-Size\n(Configurations)'),
        ('P2', 'Profil Aluminium\n(Design Table)'),
        ('P3', 'Parametric\nEnclosure'),
        ('P4', 'Mouse Housing\n(Surface)'),
        ('P5', 'Simple Mold\n(Mold Tools)'),
        ('P6', 'Aluminium Frame\n(Weldments)'),
        ('P7', 'Library Feature\n(T-Slot)'),
        ('P8', 'Excel-Driven\nPart'),
        ('P9', 'In-Context\nBracket'),
        ('P10', 'Import &\nRepair'),
    ]
    for i, (num, desc) in enumerate(percobaan):
        x = 1 + i * 1.9
        color = plt.cm.Set3(i / 10)
        ax7.add_patch(FancyBboxPatch((x - 0.7, 3.5), 1.6, 4.5, boxstyle='round,pad=0.2',
                      facecolor=color, edgecolor='#666', linewidth=1.5, alpha=0.8))
        ax7.text(x + 0.1, 7.2, num, fontsize=10, fontweight='bold', ha='center', color='#333')
        ax7.text(x + 0.1, 5.3, desc, fontsize=7, ha='center', va='center', color='#333')

    # Footer
    fig.text(0.5, 0.06, 'Teknik lanjutan: Produktivitas tinggi melalui Configurations, Parametric, dan Reusability',
             fontsize=11, ha='center', color='#1565c0', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd', edgecolor='#1565c0', linewidth=2))
    fig.text(0.5, 0.025, 'Praktikum CAD/CAM — Modul 5: CAD Gambar 3D Part 3', fontsize=10, ha='center', color='#888')

    plt.savefig(f'{IMG_DIR}/m01_deskripsi.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    print("✓ Gambar: image/m01_deskripsi.png")
    plt.close()


# ============================================================================
# 7. DESKRIPSI PROJECT (p01_deskripsi.png)
# ============================================================================
def project_deskripsi():
    """Overview lengkap Project Modul 5: Sistem Profil Aluminium Modular"""
    fig = plt.figure(figsize=(18, 22))
    fig.patch.set_facecolor('#f5f5f5')

    # HEADER
    fig.text(0.5, 0.97, 'PROJECT MODUL 5: SISTEM PROFIL ALUMINIUM MODULAR', fontsize=19, fontweight='bold',
             ha='center', va='top', color='#b71c1c',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffcdd2', edgecolor='#c62828', linewidth=3))
    fig.text(0.5, 0.945, 'Design Table, Weldments, Parametric Bracket', fontsize=14, fontweight='bold',
             ha='center', va='top', color='#c62828')

    # ========== PROJECT A: Library Profil Aluminium ==========
    ax_pa = fig.add_axes([0.03, 0.68, 0.94, 0.25])
    ax_pa.set_xlim(0, 20); ax_pa.set_ylim(0, 10)
    ax_pa.axis('off')
    ax_pa.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 9.5, boxstyle='round,pad=0.3',
                    facecolor='#e8eaf6', edgecolor='#283593', linewidth=2))
    ax_pa.text(10, 9.2, '📐 PROJECT A: LIBRARY PROFIL ALUMINIUM (Design Table)', fontsize=14,
               fontweight='bold', ha='center', color='#283593')

    profiles = ['2020', '2040', '3030', '3060', '4040', '4080', '4545', '5050']
    colors_p = ['#42a5f5', '#66bb6a', '#ffa726', '#ef5350', '#ab47bc', '#26a69a', '#78909c', '#8d6e63']

    for i, (name, color) in enumerate(zip(profiles, colors_p)):
        x = 1.2 + i * 2.3
        ax_pa.add_patch(FancyBboxPatch((x - 0.7, 3), 2, 4.5, boxstyle='round,pad=0.2',
                        facecolor=color, edgecolor='#444', linewidth=1.5, alpha=0.3))
        ax_pa.text(x + 0.3, 6.5, name, fontsize=10, fontweight='bold', ha='center', color='#333')
        # Simple cross
        s = 0.5 + i * 0.05
        ax_pa.add_patch(patches.Rectangle((x + 0.3 - s, 4.5 - s), s*2, s*2,
                        facecolor=color, edgecolor='#333', linewidth=1, alpha=0.5))

    ax_pa.text(10, 1.5, '1 file Master + Design Table → 8 configurations otomatis', fontsize=11,
               ha='center', fontweight='bold', color='#283593',
               bbox=dict(boxstyle='round', facecolor='#c5cae9', edgecolor='#283593'))
    ax_pa.text(10, 0.5, '+ Connector Series: Corner Bracket 2020/3030/4040/4545 + Gusset Plate 20/30/40',
               fontsize=9, ha='center', color='#555')

    # ========== PROJECT B: Workstation Frame ==========
    ax_pb = fig.add_axes([0.03, 0.38, 0.94, 0.28])
    ax_pb.set_xlim(0, 20); ax_pb.set_ylim(0, 12)
    ax_pb.axis('off')
    ax_pb.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 11.5, boxstyle='round,pad=0.3',
                    facecolor='#e8f5e9', edgecolor='#2e7d32', linewidth=2))
    ax_pb.text(10, 11.2, '🏗️ PROJECT B: WORKSTATION FRAME (Weldments)', fontsize=14,
               fontweight='bold', ha='center', color='#2e7d32')

    # Simplified frame drawing
    # Top frame
    ax_pb.plot([2, 9], [9, 9], 'b-', linewidth=5, solid_capstyle='round')
    ax_pb.plot([2, 9], [7, 7], 'b-', linewidth=5, solid_capstyle='round')
    ax_pb.plot([2, 2], [7, 9], 'b-', linewidth=5, solid_capstyle='round')
    ax_pb.plot([9, 9], [7, 9], 'b-', linewidth=5, solid_capstyle='round')
    # Legs
    ax_pb.plot([2, 2], [7, 3], 'b-', linewidth=5, solid_capstyle='round')
    ax_pb.plot([9, 9], [7, 3], 'b-', linewidth=5, solid_capstyle='round')
    # Cross
    ax_pb.plot([2, 9], [5, 5], 'g-', linewidth=3, solid_capstyle='round')
    # Diagonal
    ax_pb.plot([2, 9], [3, 7], 'r--', linewidth=2)

    # Specs
    specs_x = 12
    ax_pb.text(specs_x, 10, 'SPESIFIKASI:', fontsize=11, fontweight='bold', color='#2e7d32')
    specs = [
        '• Panjang: 1200mm',
        '• Lebar: 800mm',
        '• Tinggi: 750mm',
        '• Frame utama: 4040',
        '• Cross support: 3030',
        '• 4 adjustable feet (M10)',
        '• Diagonal brace belakang',
    ]
    for i, s in enumerate(specs):
        ax_pb.text(specs_x, 9 - i * 1.0, s, fontsize=9, ha='left')

    # Cut List
    ax_pb.text(specs_x, 2, 'CUT LIST (BOM):', fontsize=10, fontweight='bold', color='#c62828')
    ax_pb.text(specs_x, 1, '4040 Horiz Long(4), Short(4), Vert(4) + 3030 Cross(2), Diag(2)',
               fontsize=8, ha='left', color='#555')

    # ========== PROJECT C: Parametric Bracket ==========
    ax_pc = fig.add_axes([0.03, 0.12, 0.94, 0.24])
    ax_pc.set_xlim(0, 20); ax_pc.set_ylim(0, 10)
    ax_pc.axis('off')
    ax_pc.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 9.5, boxstyle='round,pad=0.3',
                    facecolor='#fff3e0', edgecolor='#e65100', linewidth=2))
    ax_pc.text(10, 9.2, '📊 PROJECT C: PARAMETRIC MOUNTING BRACKET (Excel-Linked)', fontsize=14,
               fontweight='bold', ha='center', color='#e65100')

    # Excel → SolidWorks flow
    # Excel
    ax_pc.add_patch(FancyBboxPatch((1, 2), 6, 6, boxstyle='round,pad=0.2',
                    facecolor='#c8e6c9', edgecolor='#2e7d32', linewidth=2))
    ax_pc.text(4, 7.5, '📊 BracketParameters.xlsx', fontsize=10, fontweight='bold', ha='center', color='#2e7d32')

    params = [('Profile_Width', '20 / 30 / 40'), ('Slot_Width', '6 / 8 / 8'),
              ('Bracket_Length', '60 / 90 / 120'), ('Hole_Diameter', '5.5 / 6.8 / 9'),
              ('Thickness', '3 / 4 / 5')]
    for i, (name, vals) in enumerate(params):
        ax_pc.text(1.5, 6.5 - i * 1.0, f'{name}: {vals}', fontsize=8, ha='left', family='monospace')

    # Arrow
    ax_pc.annotate('', xy=(10, 5), xytext=(8, 5), arrowprops=dict(arrowstyle='->', color='#e65100', lw=3))
    ax_pc.text(9, 5.8, 'Auto\nUpdate', fontsize=9, ha='center', fontweight='bold', color='#e65100')

    # SolidWorks bracket
    ax_pc.add_patch(FancyBboxPatch((11, 2), 7, 6, boxstyle='round,pad=0.2',
                    facecolor='#bbdefb', edgecolor='#1565c0', linewidth=2))
    ax_pc.text(14.5, 7.5, '📐 ParametricBracket.sldprt', fontsize=10, fontweight='bold', ha='center', color='#1565c0')

    # Simple bracket shapes (3 sizes)
    for i, (sz, col) in enumerate([(1.0, '#42a5f5'), (1.4, '#66bb6a'), (1.8, '#ffa726')]):
        bx = 12 + i * 2
        ax_pc.add_patch(FancyBboxPatch((bx, 3), sz*1.2, sz*2, boxstyle='round,pad=0.1',
                        facecolor=col, edgecolor='#333', linewidth=1.5, alpha=0.5))
        ax_pc.text(bx + sz*0.6, 2.5, f'P{(i+1)*10+10}', fontsize=8, ha='center', fontweight='bold')

    ax_pc.text(14.5, 1, 'Ubah Excel → Bracket auto-update!', fontsize=10, ha='center',
               fontweight='bold', color='#1565c0')

    # Footer
    fig.text(0.5, 0.06, 'Deliverables: 2 part Master (.sldprt) + Frame (.sldprt) + CutList (.xlsx) + Bracket (.sldprt) + Excel',
             fontsize=10, ha='center', color='#c62828', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffcdd2', edgecolor='#c62828'))
    fig.text(0.5, 0.025, 'Praktikum CAD/CAM — Modul 5: Project Sistem Profil Aluminium Modular', fontsize=10,
             ha='center', color='#888')

    plt.savefig(f'{IMG_DIR}/p01_deskripsi.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    print("✓ Gambar: image/p01_deskripsi.png")
    plt.close()


# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("GENERATING VISUALIZATIONS FOR MODUL 5 - 3D PART 3")
    print("="*60)

    configurations_design_table()
    equations_parametric()
    surface_modeling()
    weldments_mold()
    library_import_export()
    materi_deskripsi()
    project_deskripsi()

    print("\n✓ Semua gambar Modul 5 berhasil dibuat!")
    print(f"  Lokasi: {IMG_DIR}/")
    print("="*60 + "\n")
