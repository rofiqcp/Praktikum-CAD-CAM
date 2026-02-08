"""
VISUALISASI KONSEP 3D FEATURES LANJUTAN - MODUL 4
Mengilustrasikan:
1. Loft (transisi antar profil)
2. Sweep (profil sepanjang path)
3. Boundary Boss, Wrap, Flex, Dome
4. Split, Combine (Multibody)
5. Reference Geometry
6. Deskripsi Materi (Overview)
7. Deskripsi Project (Overview)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Polygon, Arc
import os
import warnings
warnings.filterwarnings('ignore')

IMG_DIR = '/home/sirobo/Documents/Praktikum-CADCAM/Modul-04-CAD-3D-Part2/image'
os.makedirs(IMG_DIR, exist_ok=True)

# ============================================================================
# HELPER: ISOMETRIC PROJECTION
# ============================================================================
def to_iso(x, y, z):
    """Convert 3D coordinates to 2D isometric projection"""
    iso_x = x - z * 0.5
    iso_y = y + z * 0.35
    return iso_x, iso_y


# ============================================================================
# 1. LOFT FEATURE
# ============================================================================
def loft_feature():
    """Visualisasi Loft: transisi antar beberapa profil"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('LOFT FEATURE — MODUL 4', fontsize=14, fontweight='bold')

    # 1.1 Basic Loft (Circle → Square)
    ax = axes[0]
    ax.set_xlim(-5, 15)
    ax.set_ylim(-3, 15)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('1. Basic Loft\n(Circle → Square)', fontweight='bold')

    # Bottom circle (profile 1)
    theta = np.linspace(0, 2*np.pi, 100)
    cx, cy = 5, 2
    r = 3
    x_circ = cx + r * np.cos(theta)
    y_circ = cy + r * np.sin(theta)
    ax.plot(x_circ, y_circ, 'b-', linewidth=2.5, label='Profile 1 (Circle)')
    ax.text(cx, cy, 'Ø60mm\nz=0', ha='center', fontsize=8, color='blue')

    # Top square (profile 2) — shifted up
    sq_cx, sq_cy = 5, 12
    sq_s = 2.5
    sq_x = [sq_cx-sq_s, sq_cx+sq_s, sq_cx+sq_s, sq_cx-sq_s, sq_cx-sq_s]
    sq_y = [sq_cy-sq_s, sq_cy-sq_s, sq_cy+sq_s, sq_cy+sq_s, sq_cy-sq_s]
    ax.plot(sq_x, sq_y, 'r-', linewidth=2.5, label='Profile 2 (Square)')
    ax.text(sq_cx, sq_cy, '40×40mm\nz=80', ha='center', fontsize=8, color='red')

    # Transition lines
    for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
        px = cx + r * np.cos(angle)
        py_b = cy + r * np.sin(angle)
        if angle == 0: tx, ty = sq_cx+sq_s, sq_cy-sq_s
        elif angle == np.pi/2: tx, ty = sq_cx+sq_s, sq_cy+sq_s
        elif angle == np.pi: tx, ty = sq_cx-sq_s, sq_cy+sq_s
        else: tx, ty = sq_cx-sq_s, sq_cy-sq_s
        ax.plot([px, tx], [py_b, ty], 'g--', linewidth=1, alpha=0.5)

    ax.fill_between(x_circ, y_circ, alpha=0.1, color='blue')
    ax.legend(fontsize=8, loc='lower left')

    # 1.2 Multi-Profile Loft (Vase)
    ax = axes[1]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 18)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('2. Multi-Profile Loft\n(Vase — 4 profil)', fontweight='bold')

    profiles = [
        (5, 1, 3, 'Ø60 (z=0)', 'blue'),
        (5, 5, 2, 'Ø40 (z=30)', 'green'),
        (5, 10, 2.5, 'Ø50 (z=60)', 'orange'),
        (5, 15, 3.5, 'Ø70 (z=90)', 'red'),
    ]
    for cx, cy, r, label, color in profiles:
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(cx + r*np.cos(theta), cy + r*np.sin(theta), color=color, linewidth=2)
        ax.text(cx, cy, label, ha='center', fontsize=7, color=color, fontweight='bold')

    # Connect profiles with smooth curves
    for side in [-1, 1]:
        xs = [5 + side*p[2] for p in profiles]
        ys = [p[1] for p in profiles]
        ax.plot(xs, ys, 'k--', linewidth=1, alpha=0.4)

    ax.text(5, -1.5, 'Loft melalui 4 profil\n+ Shell 2mm', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='orange'))

    # 1.3 Loft with Guide Curves
    ax = axes[2]
    ax.set_xlim(-3, 13)
    ax.set_ylim(-2, 16)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('3. Loft + Guide Curves', fontweight='bold')

    # Two profiles
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(5 + 3*np.cos(theta), 1 + 3*np.sin(theta), 'b-', linewidth=2.5, label='Profile 1')
    ax.plot(5 + 2*np.cos(theta), 13 + 2*np.sin(theta), 'r-', linewidth=2.5, label='Profile 2')

    # Guide curves (curved)
    t = np.linspace(0, 1, 50)
    for side in [-1, 1]:
        gx = 5 + side * (3 - t * 1 + 0.8*np.sin(t*np.pi))
        gy = 1 + t * 12
        ax.plot(gx, gy, 'g-', linewidth=2, label='Guide Curve' if side == -1 else None)

    ax.text(5, 7, 'Guide Curve\nmengontrol\nbentuk transisi', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='#e8f5e9', edgecolor='green'))
    ax.legend(fontsize=8, loc='lower left')

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/01_loft_feature.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/01_loft_feature.png")
    plt.close()


# ============================================================================
# 2. SWEEP FEATURE
# ============================================================================
def sweep_feature():
    """Visualisasi Sweep: profil sepanjang path"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('SWEEP FEATURE — MODUL 4', fontsize=14, fontweight='bold')

    # 2.1 Basic Sweep (Pipe)
    ax = axes[0]
    ax.set_xlim(-2, 14)
    ax.set_ylim(-2, 14)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('1. Basic Sweep\n(Pipe Bend)', fontweight='bold')

    # Path (L-shape with fillet)
    ax.plot([0, 8], [2, 2], 'r-', linewidth=3, label='Path')
    theta_bend = np.linspace(0, np.pi/2, 50)
    bend_r = 3
    bx = 8 + bend_r * np.cos(np.pi - theta_bend)
    by = 2 + bend_r + bend_r * np.sin(-theta_bend + np.pi/2)
    ax.plot(bx, by, 'r-', linewidth=3)
    ax.plot([8 + bend_r, 8 + bend_r], [2 + bend_r, 12], 'r-', linewidth=3)

    # Profile circle at start
    theta = np.linspace(0, 2*np.pi, 50)
    ax.plot(0 + 0.8*np.cos(theta), 2 + 0.8*np.sin(theta), 'b-', linewidth=2.5, label='Profile Ø20mm')
    ax.text(0, 0.5, 'Profile\n(Circle)', ha='center', fontsize=8, color='blue')
    ax.text(6, 3.5, 'Path\n(L-shape)', ha='center', fontsize=8, color='red')

    ax.legend(fontsize=8)

    # 2.2 Helix Sweep (Spring)
    ax = axes[1]
    ax.set_xlim(-5, 10)
    ax.set_ylim(-2, 16)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('2. Helix Sweep\n(Spring)', fontweight='bold')

    # Helix path (side view)
    t = np.linspace(0, 8*2*np.pi, 500)
    pitch = 1.2
    r_helix = 2.5
    hx = r_helix * np.cos(t)
    hy = t / (2*np.pi) * pitch + 1
    ax.plot(hx, hy, 'r-', linewidth=2, label='Helix Path')

    # Wire profile indicator
    ax.plot(r_helix + 0.3*np.cos(theta), 1 + 0.3*np.sin(theta), 'b-', linewidth=2.5)
    ax.text(r_helix + 1, 1, 'Wire Ø3mm', fontsize=8, color='blue')

    ax.text(0, 11.5, f'Pitch: 10mm\nØ25mm\n8 turns', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='orange'))
    ax.legend(fontsize=8)

    # 2.3 Sweep with Twist
    ax = axes[2]
    ax.set_xlim(-4, 10)
    ax.set_ylim(-2, 14)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('3. Sweep with Twist\n(Along Path)', fontweight='bold')

    # Straight path
    ax.plot([3, 3], [0, 12], 'r-', linewidth=3, label='Path (straight)')

    # Profile at bottom (square)
    sq = 1.5
    ax.plot([3-sq, 3+sq, 3+sq, 3-sq, 3-sq], [0-sq, 0-sq, 0+sq, 0+sq, 0-sq], 'b-', linewidth=2.5, label='Profile (square)')

    # Twisted profile at top (rotated square)
    angle = np.radians(45)
    corners = [(-sq, -sq), (sq, -sq), (sq, sq), (-sq, sq), (-sq, -sq)]
    rotated = [(c[0]*np.cos(angle)-c[1]*np.sin(angle)+3,
                c[0]*np.sin(angle)+c[1]*np.cos(angle)+12) for c in corners]
    ax.plot([r[0] for r in rotated], [r[1] for r in rotated], 'g-', linewidth=2.5, label='Twisted 45°')

    # Intermediate profiles
    for z, ang in [(3, 11.25), (6, 22.5), (9, 33.75)]:
        a = np.radians(ang)
        rot = [(c[0]*np.cos(a)-c[1]*np.sin(a)+3, c[0]*np.sin(a)+c[1]*np.cos(a)+z) for c in corners]
        ax.plot([r[0] for r in rot], [r[1] for r in rot], 'gray', linewidth=1, alpha=0.5)

    ax.text(7, 6, 'Twist: 45°\nalong path', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='#e8f5e9', edgecolor='green'))
    ax.legend(fontsize=8, loc='lower left')

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/02_sweep_feature.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/02_sweep_feature.png")
    plt.close()


# ============================================================================
# 3. ADVANCED FEATURES (Wrap, Dome, Flex, Split, Combine)
# ============================================================================
def advanced_features():
    """Visualisasi feature lanjutan"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('ADVANCED FEATURES — MODUL 4', fontsize=14, fontweight='bold')

    # 3.1 Wrap (Emboss/Deboss)
    ax = axes[0, 0]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('1. WRAP (Emboss/Deboss)', fontweight='bold')

    # Cylinder side view
    ax.add_patch(patches.Rectangle((1, 1), 8, 8, linewidth=2, edgecolor='#333',
                 facecolor='#cfd8dc', alpha=0.5))
    # Text on surface
    ax.text(5, 5, 'CAD\nCAM', ha='center', va='center', fontsize=18, fontweight='bold',
            color='#1565c0', alpha=0.7)
    ax.text(5, 0, 'Emboss text\npada silinder', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # 3.2 Dome
    ax = axes[0, 1]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('2. DOME', fontweight='bold')

    # Base
    ax.add_patch(patches.Rectangle((1, 1), 8, 3, linewidth=2, edgecolor='#333',
                 facecolor='#cfd8dc', alpha=0.5))
    # Dome curve
    t = np.linspace(0, np.pi, 100)
    dome_x = 5 + 4 * np.cos(t)
    dome_y = 4 + 2.5 * np.sin(t)
    ax.fill_between(dome_x, dome_y, 4, color='#90caf9', alpha=0.5)
    ax.plot(dome_x, dome_y, 'b-', linewidth=2.5)
    ax.annotate('', xy=(5, 6.5), xytext=(5, 4), arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(6, 5.5, 'Height', fontsize=9, color='red', fontweight='bold')
    ax.text(5, 0, 'Dome pada\nface datar', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # 3.3 Flex (Bending)
    ax = axes[0, 2]
    ax.set_xlim(-3, 13)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('3. FLEX (Bending)', fontweight='bold')

    # Original (straight)
    ax.add_patch(patches.Rectangle((0, 4), 5, 1.5, linewidth=2, edgecolor='blue',
                 facecolor='lightblue', alpha=0.4, linestyle='--'))
    ax.text(2.5, 3, 'Original\n(straight)', ha='center', fontsize=8, color='blue')

    # Bent
    theta_b = np.linspace(0, np.pi/3, 100)
    r_b = 6
    cx_b, cy_b = 5, 3
    outer_x = cx_b + (r_b + 0.75) * np.cos(theta_b + np.pi/2)
    outer_y = cy_b + (r_b + 0.75) * np.sin(theta_b + np.pi/2)
    inner_x = cx_b + (r_b - 0.75) * np.cos(theta_b + np.pi/2)
    inner_y = cy_b + (r_b - 0.75) * np.sin(theta_b + np.pi/2)
    ax.plot(outer_x, outer_y, 'r-', linewidth=2.5)
    ax.plot(inner_x, inner_y, 'r-', linewidth=2.5)
    ax.text(8, 7, 'Bent\n(Flex)', ha='center', fontsize=8, color='red', fontweight='bold')

    # 3.4 Split Line / Split
    ax = axes[1, 0]
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('4. SPLIT LINE / SPLIT', fontweight='bold')

    ax.add_patch(patches.Rectangle((1, 1), 8, 8, linewidth=2, edgecolor='#333',
                 facecolor='#cfd8dc', alpha=0.4))
    # Split line
    ax.plot([1, 9], [5, 5], 'r-', linewidth=3, label='Split Line')
    ax.add_patch(patches.Rectangle((1, 5), 8, 4, linewidth=0, facecolor='#bbdefb', alpha=0.4))
    ax.add_patch(patches.Rectangle((1, 1), 8, 4, linewidth=0, facecolor='#c8e6c9', alpha=0.4))
    ax.text(5, 7, 'Region A', ha='center', fontsize=10, fontweight='bold', color='#1565c0')
    ax.text(5, 3, 'Region B', ha='center', fontsize=10, fontweight='bold', color='#2e7d32')
    ax.legend(fontsize=9)

    # 3.5 Combine (Multibody)
    ax = axes[1, 1]
    ax.set_xlim(-2, 14)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('5. COMBINE (Multibody)', fontweight='bold')

    # Body 1 (box)
    ax.add_patch(patches.Rectangle((0.5, 2), 5, 5, linewidth=2, edgecolor='blue',
                 facecolor='lightblue', alpha=0.4))
    ax.text(3, 4.5, 'Body 1\n(Box)', ha='center', fontsize=9, color='blue')

    # Body 2 (circle)
    c = Circle((8, 4.5), 2.5, edgecolor='red', facecolor='lightcoral', alpha=0.4, linewidth=2)
    ax.add_patch(c)
    ax.text(8, 4.5, 'Body 2\n(Cylinder)', ha='center', fontsize=9, color='red')

    # Operations
    ops = ['Add (+)', 'Subtract (−)', 'Common (∩)']
    colors = ['#2e7d32', '#c62828', '#e65100']
    for i, (op, col) in enumerate(zip(ops, colors)):
        ax.text(3 + i * 4, 0, op, ha='center', fontsize=9, fontweight='bold', color=col,
                bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor=col))

    # 3.6 Boundary Boss
    ax = axes[1, 2]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('6. BOUNDARY BOSS/BASE', fontweight='bold')

    # Two directions
    ax.annotate('', xy=(9, 5), xytext=(5, 5), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(7, 5.8, 'Dir 1', fontsize=10, fontweight='bold', color='blue')
    ax.annotate('', xy=(5, 9), xytext=(5, 5), arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(5.5, 7.5, 'Dir 2', fontsize=10, fontweight='bold', color='red')

    # Boundary curves
    t = np.linspace(0, 1, 50)
    for i in range(3):
        bx = 1 + t * 8
        by = 2 + i*3 + 0.8*np.sin(t*np.pi)
        ax.plot(bx, by, 'g-', linewidth=2, alpha=0.6)
    for i in range(3):
        bx_v = 1 + i * 4
        by_v = np.linspace(2, 8, 50) + 0.5*np.sin(np.linspace(0, np.pi, 50))
        ax.plot([bx_v]*50 if isinstance(bx_v, (int, float)) else bx_v,
                by_v, 'm-', linewidth=2, alpha=0.6)

    ax.text(5, 0.5, 'Kurva batas di 2 arah\n(lebih presisi dari Loft)', ha='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='#f3e5f5', edgecolor='purple'))

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/03_advanced_features.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/03_advanced_features.png")
    plt.close()


# ============================================================================
# 4. REFERENCE GEOMETRY
# ============================================================================
def reference_geometry():
    """Visualisasi Reference Geometry: Plane, Axis, Coordinate System"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('REFERENCE GEOMETRY — MODUL 4', fontsize=14, fontweight='bold')

    # 4.1 Reference Planes
    ax = axes[0]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('1. REFERENCE PLANES', fontweight='bold')

    # Default planes
    planes = [
        ('Front Plane', '#42a5f5', [(1, 1), (9, 1), (9, 5), (1, 5)]),
        ('Top Plane', '#66bb6a', [(2, 6), (10, 6), (10, 8), (2, 8)]),
        ('Right Plane', '#ffa726', [(3, 3), (7, 3), (7, 10), (3, 10)]),
    ]
    for name, color, corners in planes:
        poly = Polygon(corners, facecolor=color, alpha=0.2, edgecolor=color, linewidth=2)
        ax.add_patch(poly)

    # Offset plane
    ax.plot([0, 8], [9.5, 9.5], 'r--', linewidth=2, label='Offset Plane')
    ax.annotate('', xy=(5, 9.5), xytext=(5, 8), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(6, 8.7, 'Offset\n30mm', fontsize=8, color='red')

    ax.text(5, 0, 'Front (XY), Top (XZ), Right (YZ)\n+ Offset / Angle / Normal', ha='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='lightyellow'))
    ax.legend(fontsize=8)

    # 4.2 Reference Axis
    ax = axes[1]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('2. REFERENCE AXIS', fontweight='bold')

    # Cylinder
    c = Circle((5, 5), 3, edgecolor='#333', facecolor='#cfd8dc', alpha=0.3, linewidth=2)
    ax.add_patch(c)
    c2 = Circle((5, 5), 1, edgecolor='#333', facecolor='white', linewidth=1.5)
    ax.add_patch(c2)

    # Axis
    ax.plot([5, 5], [0, 10], 'r-', linewidth=3, label='Axis (from cylinder)')
    ax.plot(5, 5, 'r+', markersize=15, markeredgewidth=3)
    ax.text(6, 1, 'Axis dari\ncylindrical face', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow'))
    ax.legend(fontsize=8)

    # 4.3 Coordinate System
    ax = axes[2]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_title('3. COORDINATE SYSTEM', fontweight='bold')

    origin = (5, 5)
    ax.annotate('', xy=(10, 5), xytext=origin, arrowprops=dict(arrowstyle='->', color='red', lw=3))
    ax.text(10.3, 5, 'X', fontsize=14, fontweight='bold', color='red')
    ax.annotate('', xy=(5, 10), xytext=origin, arrowprops=dict(arrowstyle='->', color='green', lw=3))
    ax.text(5, 10.5, 'Y', fontsize=14, fontweight='bold', color='green')
    ax.annotate('', xy=(2, 3), xytext=origin, arrowprops=dict(arrowstyle='->', color='blue', lw=3))
    ax.text(1.5, 2.5, 'Z', fontsize=14, fontweight='bold', color='blue')
    ax.plot(*origin, 'ko', markersize=8)
    ax.text(5, 0, 'Custom Coordinate System\nuntuk analisis & export', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow'))

    plt.tight_layout()
    plt.savefig(f'{IMG_DIR}/04_reference_geometry.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: image/04_reference_geometry.png")
    plt.close()


# ============================================================================
# 5. DESKRIPSI MATERI (m01_deskripsi.png)
# ============================================================================
def materi_deskripsi():
    """Overview lengkap materi Modul 4: Feature Lanjutan"""
    fig = plt.figure(figsize=(18, 22))
    fig.patch.set_facecolor('#f0f4f8')

    # HEADER
    fig.text(0.5, 0.97, 'MODUL 4: CAD GAMBAR 3D — PART 2', fontsize=22, fontweight='bold',
             ha='center', va='top', color='#1a237e',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#bbdefb', edgecolor='#1565c0', linewidth=3))
    fig.text(0.5, 0.945, 'FEATURE LANJUTAN (Loft, Sweep, Wrap, Combine)', fontsize=14, fontweight='bold',
             ha='center', va='top', color='#0d47a1')

    # --- Section 1: Loft ---
    ax1 = fig.add_axes([0.03, 0.78, 0.45, 0.15])
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.add_patch(FancyBboxPatch((0.2, 0.5), 9.5, 9, boxstyle='round,pad=0.3',
                  facecolor='#e3f2fd', edgecolor='#1565c0', linewidth=2))
    ax1.text(5, 9, '🔀 LOFT', fontsize=14, fontweight='bold', ha='center', color='#1565c0')
    loft_items = [
        'Membuat bentuk 3D dari beberapa profil pada plane berbeda',
        'Minimum 2 profil sketch pada plane terpisah',
        'Opsi: Guide Curves untuk kontrol bentuk transisi',
        'Start/End Constraints: Normal to Profile, Tangency',
        'Contoh: Vase, Botol, Transisi penampang',
    ]
    for i, item in enumerate(loft_items):
        ax1.text(0.5, 7.5 - i * 1.5, f'• {item}', fontsize=9, ha='left')

    # --- Section 2: Sweep ---
    ax2 = fig.add_axes([0.52, 0.78, 0.45, 0.15])
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.add_patch(FancyBboxPatch((0.2, 0.5), 9.5, 9, boxstyle='round,pad=0.3',
                  facecolor='#e8f5e9', edgecolor='#2e7d32', linewidth=2))
    ax2.text(5, 9, '➰ SWEEP', fontsize=14, fontweight='bold', ha='center', color='#2e7d32')
    sweep_items = [
        'Menarik profil sketch sepanjang jalur (path)',
        'Profile = penampang, Path = jalur yang diikuti',
        'Opsi: Follow Path, Keep Normal Constant, Twist',
        'Helix Path: Untuk spring, thread, coil',
        'Contoh: Pipa, Spring, Handle, Thread',
    ]
    for i, item in enumerate(sweep_items):
        ax2.text(0.5, 7.5 - i * 1.5, f'• {item}', fontsize=9, ha='left')

    # --- Section 3: Boundary, Wrap, Flex ---
    ax3 = fig.add_axes([0.03, 0.57, 0.45, 0.19])
    ax3.set_xlim(0, 10); ax3.set_ylim(0, 12)
    ax3.axis('off')
    ax3.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 11.3, boxstyle='round,pad=0.3',
                  facecolor='#fff3e0', edgecolor='#e65100', linewidth=2))
    ax3.text(5, 11, '🧩 FEATURE TAMBAHAN', fontsize=13, fontweight='bold', ha='center', color='#e65100')

    features = [
        ('Boundary Boss', 'Seperti Loft tapi 2 arah (Dir1 + Dir2)'),
        ('Wrap', 'Emboss/Deboss/Scribe pada permukaan lengkung'),
        ('Flex', 'Bending, Twisting, Tapering, Stretching'),
        ('Dome', 'Permukaan cembung/cekung pada face datar'),
        ('Indent', 'Cekungan berdasarkan bentuk body lain'),
        ('Deform', 'Deformasi dgn point/curve/surface'),
    ]
    for i, (name, desc) in enumerate(features):
        ax3.text(0.8, 9.5 - i * 1.7, f'• {name}', fontsize=9.5, ha='left', fontweight='bold')
        ax3.text(0.8, 8.7 - i * 1.7, f'   {desc}', fontsize=8.5, ha='left', color='#555')

    # --- Section 4: Split & Combine ---
    ax4 = fig.add_axes([0.52, 0.57, 0.45, 0.19])
    ax4.set_xlim(0, 10); ax4.set_ylim(0, 12)
    ax4.axis('off')
    ax4.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 11.3, boxstyle='round,pad=0.3',
                  facecolor='#f3e5f5', edgecolor='#6a1b9a', linewidth=2))
    ax4.text(5, 11, '✂️ SPLIT & COMBINE', fontsize=13, fontweight='bold', ha='center', color='#6a1b9a')

    split_items = [
        ('Split Line', 'Membagi face menjadi beberapa region'),
        ('Split', 'Memotong body menjadi beberapa body terpisah'),
        ('Combine: Add', 'Menggabungkan beberapa solid body'),
        ('Combine: Subtract', 'Mengurangi body satu dengan lainnya'),
        ('Combine: Common', 'Irisan (intersection) 2 body'),
        ('Multibody Part', 'Beberapa solid body dalam 1 file'),
    ]
    for i, (name, desc) in enumerate(split_items):
        ax4.text(0.8, 9.5 - i * 1.7, f'• {name}', fontsize=9.5, ha='left', fontweight='bold')
        ax4.text(0.8, 8.7 - i * 1.7, f'   {desc}', fontsize=8.5, ha='left', color='#555')

    # --- Section 5: Reference Geometry ---
    ax5 = fig.add_axes([0.03, 0.38, 0.45, 0.17])
    ax5.set_xlim(0, 10); ax5.set_ylim(0, 10)
    ax5.axis('off')
    ax5.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 9.3, boxstyle='round,pad=0.3',
                  facecolor='#e0f7fa', edgecolor='#00695c', linewidth=2))
    ax5.text(5, 9, '📐 REFERENCE GEOMETRY', fontsize=13, fontweight='bold', ha='center', color='#00695c')

    ref_items = [
        ('Plane', 'Offset, Through Line/Point, Angle, Normal to Curve'),
        ('Axis', 'Dari 2 plane, cylindrical face, atau 2 point'),
        ('Coordinate System', 'Kustom untuk analisis dan export'),
        ('Mate Reference', 'Untuk auto-mate di assembly'),
    ]
    for i, (name, desc) in enumerate(ref_items):
        ax5.text(0.8, 7.5 - i * 1.7, f'• {name}', fontsize=9.5, ha='left', fontweight='bold')
        ax5.text(0.8, 6.7 - i * 1.7, f'   {desc}', fontsize=8.5, ha='left', color='#555')

    # --- Section 6: Percobaan ---
    ax6 = fig.add_axes([0.52, 0.38, 0.45, 0.17])
    ax6.set_xlim(0, 10); ax6.set_ylim(0, 10)
    ax6.axis('off')
    ax6.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 9.3, boxstyle='round,pad=0.3',
                  facecolor='#fce4ec', edgecolor='#880e4f', linewidth=2))
    ax6.text(5, 9, '🔬 PERCOBAAN 1-10', fontsize=13, fontweight='bold', ha='center', color='#880e4f')

    percobaan = [
        'P1: Vase (Loft 4 profil + Shell)',
        'P2: Pipe Bend (Sweep L-shape)',
        'P3: Spring (Sweep Helix, 8 turns)',
        'P4: Bottle (Loft + Revolve + Thread)',
        'P5: Propeller (Loft airfoil + Circular Pattern)',
        'P6: Handle/Grip (Sweep + Loft + Wrap)',
        'P7: Cam 3D (Loft + Sweep)',
        'P8: Enclosure Ergonomis (Loft + Shell + Dome)',
        'P9: Text Emboss pada Silinder (Wrap)',
        'P10: Multi-Body Part (Combine)',
    ]
    for i, p in enumerate(percobaan):
        ax6.text(0.8, 7.5 - i * 0.75, f'• {p}', fontsize=8, ha='left')

    # --- Bottom summary ---
    ax7 = fig.add_axes([0.03, 0.12, 0.94, 0.23])
    ax7.set_xlim(0, 20); ax7.set_ylim(0, 10)
    ax7.axis('off')
    ax7.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 9.5, boxstyle='round,pad=0.3',
                  facecolor='#fffde7', edgecolor='#f57f17', linewidth=2))
    ax7.text(10, 9.2, '📋 RINGKASAN FEATURE LANJUTAN', fontsize=14, fontweight='bold', ha='center', color='#e65100')

    features_summary = [
        ('LOFT', 'Transisi\nantar profil', '#42a5f5'),
        ('SWEEP', 'Profil\nsepanjang path', '#66bb6a'),
        ('BOUNDARY', 'Loft\n2 arah', '#ffa726'),
        ('WRAP', 'Emboss/\nDeboss', '#ef5350'),
        ('FLEX', 'Bend/\nTwist', '#ab47bc'),
        ('DOME', 'Permukaan\ncembung', '#26a69a'),
        ('SPLIT', 'Bagi\nface/body', '#78909c'),
        ('COMBINE', 'Add/Sub/\nCommon', '#8d6e63'),
    ]
    for i, (name, desc, color) in enumerate(features_summary):
        x = 1.2 + i * 2.4
        ax7.add_patch(FancyBboxPatch((x - 0.8, 2), 2.1, 6, boxstyle='round,pad=0.2',
                      facecolor=color, edgecolor='#444', linewidth=1.5, alpha=0.3))
        ax7.text(x + 0.2, 7, name, fontsize=9, fontweight='bold', ha='center', color='#333')
        ax7.text(x + 0.2, 4.5, desc, fontsize=7.5, ha='center', va='center', color='#333')

    # Footer
    fig.text(0.5, 0.06, 'Feature lanjutan memungkinkan bentuk kompleks: organik, transisi, multi-body',
             fontsize=11, ha='center', color='#1565c0', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd', edgecolor='#1565c0', linewidth=2))
    fig.text(0.5, 0.025, 'Praktikum CAD/CAM — Modul 4: CAD Gambar 3D Part 2', fontsize=10, ha='center', color='#888')

    plt.savefig(f'{IMG_DIR}/m01_deskripsi.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    print("✓ Gambar: image/m01_deskripsi.png")
    plt.close()


# ============================================================================
# 6. DESKRIPSI PROJECT (p01_deskripsi.png)
# ============================================================================
def project_deskripsi():
    """Overview lengkap Project Modul 4: Joystick Controller + Aksesoris Aluminium"""
    fig = plt.figure(figsize=(18, 20))
    fig.patch.set_facecolor('#f5f5f5')

    # HEADER
    fig.text(0.5, 0.97, 'PROJECT MODUL 4: JOYSTICK CONTROLLER + AKSESORIS', fontsize=20, fontweight='bold',
             ha='center', va='top', color='#b71c1c',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffcdd2', edgecolor='#c62828', linewidth=3))
    fig.text(0.5, 0.945, 'Feature Lanjutan: Loft, Sweep, Dome, Wrap, Combine', fontsize=14, fontweight='bold',
             ha='center', va='top', color='#c62828')

    # ========== PROJECT A: JOYSTICK CONTROLLER ==========
    ax_pa = fig.add_axes([0.03, 0.55, 0.94, 0.38])
    ax_pa.set_xlim(0, 20); ax_pa.set_ylim(0, 15)
    ax_pa.axis('off')
    ax_pa.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 14.5, boxstyle='round,pad=0.3',
                    facecolor='#e8eaf6', edgecolor='#283593', linewidth=2))
    ax_pa.text(10, 14, '🎮 PROJECT A: JOYSTICK CONTROLLER', fontsize=15, fontweight='bold', ha='center', color='#283593')

    # Joystick illustration
    # Base plate
    ax_pa.add_patch(FancyBboxPatch((2, 2), 7, 2, boxstyle='round,pad=0.2',
                    facecolor='#78909c', edgecolor='#333', linewidth=2))
    ax_pa.text(5.5, 3, 'Base Plate\n(Extrude + Pattern)', ha='center', fontsize=8, color='white')

    # Body housing (loft shape)
    body_x = [2.5, 8.5, 8, 3]
    body_y = [4, 4, 9, 9]
    body = Polygon(list(zip(body_x, body_y)), facecolor='#455a64', edgecolor='#333', linewidth=2, alpha=0.7)
    ax_pa.add_patch(body)
    ax_pa.text(5.5, 6.5, 'Body Housing\n(Loft 3 profil +\nShell + Dome)', ha='center', fontsize=8, color='white')

    # Joystick stick
    ax_pa.plot([5.5, 5.5], [9, 12], 'k-', linewidth=4)
    ax_pa.text(6.5, 10.5, 'Stick\n(Sweep)', fontsize=8, color='#333')

    # Joystick knob
    c = Circle((5.5, 12.5), 0.7, facecolor='#e53935', edgecolor='#333', linewidth=2)
    ax_pa.add_patch(c)
    ax_pa.text(7, 12.5, 'Knob (Loft)', fontsize=8, color='#333')

    # Buttons
    for i in range(4):
        bc = Circle((3 + i * 0.9, 8), 0.3, facecolor='#ffa000', edgecolor='#333', linewidth=1.5)
        ax_pa.add_patch(bc)
    ax_pa.text(4.3, 7, 'Button Caps (Dome)', fontsize=8, color='#333')

    # Label
    ax_pa.add_patch(FancyBboxPatch((3, 5), 5, 0.6, boxstyle='round,pad=0.1',
                    facecolor='#90a4ae', edgecolor='#333', linewidth=1))
    ax_pa.text(5.5, 5.3, 'Label (Wrap)', ha='center', fontsize=7, color='#333')

    # Parts list
    parts_x = 12
    ax_pa.text(parts_x, 12.5, 'PART LIST:', fontsize=12, fontweight='bold', color='#283593')
    parts = [
        '1. Body Housing — Loft + Shell + Dome',
        '2. Joystick Stick — Sweep (taper profile)',
        '3. Joystick Knob — Loft (sphere-like)',
        '4. Button Caps (4x) — Dome pada silinder',
        '5. Base Plate — Extrude + Circular Pattern',
        '6. Label Plate — Wrap text pada body',
    ]
    for i, p in enumerate(parts):
        ax_pa.text(parts_x, 11.3 - i * 1.5, p, fontsize=9, ha='left')

    ax_pa.text(parts_x, 2, 'Feature: Loft, Sweep, Shell, Dome,\nWrap, Circular Pattern, Fillet',
               fontsize=9, fontweight='bold', color='#c62828',
               bbox=dict(boxstyle='round', facecolor='#ffcdd2', edgecolor='#c62828'))

    # ========== PROJECT B: AKSESORIS ALUMINIUM ==========
    ax_pb = fig.add_axes([0.03, 0.12, 0.94, 0.4])
    ax_pb.set_xlim(0, 20); ax_pb.set_ylim(0, 15)
    ax_pb.axis('off')
    ax_pb.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 14.5, boxstyle='round,pad=0.3',
                    facecolor='#e8f5e9', edgecolor='#2e7d32', linewidth=2))
    ax_pb.text(10, 14, '🔩 PROJECT B: AKSESORIS PROFIL ALUMINIUM', fontsize=15, fontweight='bold', ha='center', color='#2e7d32')

    accessories = [
        ('Corner\nBracket 90°', '28×28×26mm\n2x M6 holes\nDiecast style', '#42a5f5'),
        ('T-Nut M6\nSlot 8mm', '13.5×8mm\nSpring-loaded\nDrop-in', '#66bb6a'),
        ('End Cap\n4040', '40×40mm\nClip-on plastic\nTebal 5mm', '#ffa726'),
        ('Handle\nPlastic', '~130mm\n2 mounting holes\nErgonomis', '#ef5350'),
        ('Gusset\nPlate', '40×40mm t=4mm\n2 slot T-nut\nR5 fillet', '#ab47bc'),
    ]

    for i, (name, specs, color) in enumerate(accessories):
        x = 1 + i * 3.8
        ax_pb.add_patch(FancyBboxPatch((x - 0.3, 4), 3.4, 8.5, boxstyle='round,pad=0.3',
                        facecolor='white', edgecolor=color, linewidth=2))

        # Simple shape representation
        ax_pb.add_patch(FancyBboxPatch((x + 0.3, 8.5), 2.4, 3, boxstyle='round,pad=0.2',
                        facecolor=color, edgecolor='#444', linewidth=1.5, alpha=0.3))

        ax_pb.text(x + 1.4, 12, name, fontsize=9, fontweight='bold', ha='center', color=color)
        ax_pb.text(x + 1.4, 6, specs, fontsize=7.5, ha='center', va='top', color='#333')

    # Penilaian
    ax_pb.text(10, 2.5, 'Feature: Extrude + Fillet + Chamfer + Revolve + Loft + Sweep', fontsize=10,
               ha='center', fontweight='bold', color='#2e7d32',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='#c8e6c9', edgecolor='#2e7d32'))
    ax_pb.text(10, 1, 'Referensi: Aluminium Catalog (halaman 18-26, 55, 96)',
               fontsize=10, ha='center', color='#555')

    # Footer
    fig.text(0.5, 0.06, 'Deliverables: 6 part Joystick (.sldprt) + 5 part Aksesoris (.sldprt) = 11 file',
             fontsize=11, ha='center', color='#c62828', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffcdd2', edgecolor='#c62828'))
    fig.text(0.5, 0.025, 'Praktikum CAD/CAM — Modul 4: Project Feature Lanjutan', fontsize=10, ha='center', color='#888')

    plt.savefig(f'{IMG_DIR}/p01_deskripsi.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    print("✓ Gambar: image/p01_deskripsi.png")
    plt.close()


# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("GENERATING VISUALIZATIONS FOR MODUL 4 - 3D PART 2")
    print("="*60)

    loft_feature()
    sweep_feature()
    advanced_features()
    reference_geometry()
    materi_deskripsi()
    project_deskripsi()

    print("\n✓ Semua gambar Modul 4 berhasil dibuat!")
    print(f"  Lokasi: {IMG_DIR}/")
    print("="*60 + "\n")
