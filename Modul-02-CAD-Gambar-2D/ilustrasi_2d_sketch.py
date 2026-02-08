"""
VISUALISASI KONSEP 2D SKETCHING - MODUL 2
Mengilustrasikan:
1. Entitas Sketch (Line, Rectangle, Circle, Arc)
2. Constraints (Horizontal, Vertical, Tangent, Concentric)
3. Dimensions (Fully Defined vs Under Defined)
4. Sketch Tools (Offset, Pattern, Fillet)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Arc, FancyBboxPatch, Circle, Wedge
import matplotlib.lines as mlines

# ============================================================================
# 1. ENTITAS SKETCH DASAR
# ============================================================================
def sketch_entities():
    """Visualisasi entitas-entitas sketch dasar"""
    fig, axes = plt.subplots(2, 3, figsize=(14, 10))
    fig.suptitle('ENTITAS SKETCH DASAR - MODUL 2', fontsize=14, fontweight='bold')
    
    # 1.1 LINE (GARIS)
    ax = axes[0, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('1. LINE (GARIS)', fontweight='bold')
    
    # Garis normal
    ax.plot([1, 8], [2, 7], 'b-', linewidth=2.5, label='Garis Normal')
    ax.plot([1, 8], [2, 7], 'bo', markersize=6)
    
    # Garis konstruksi
    ax.plot([2, 7], [8, 3], 'g--', linewidth=2, label='Konstruksi')
    ax.legend(loc='lower left', fontsize=9)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # 1.2 RECTANGLE (PERSEGI PANJANG)
    ax = axes[0, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('2. RECTANGLE', fontweight='bold')
    
    rect = patches.Rectangle((2, 2), 6, 4, linewidth=2.5, edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax.add_patch(rect)
    # Corner points
    ax.plot([2, 8, 8, 2, 2], [2, 2, 6, 6, 2], 'bo', markersize=6)
    ax.text(5, 4, 'Rectangle\n6 x 4 mm', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # 1.3 CIRCLE (LINGKARAN)
    ax = axes[0, 2]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('3. CIRCLE', fontweight='bold')
    
    circle = Circle((5, 5), 3, edgecolor='blue', facecolor='lightblue', alpha=0.3, linewidth=2.5)
    ax.add_patch(circle)
    ax.plot(5, 5, 'bo', markersize=6, label='Center')
    ax.plot([5, 8], [5, 5], 'r-', linewidth=2)
    ax.text(6.5, 5.5, 'R=3', fontsize=9, color='red')
    ax.legend(fontsize=9)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # 1.4 ARC (BUSUR)
    ax = axes[1, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('4. ARC (BUSUR)', fontweight='bold')
    
    # Arc dari center point
    theta = np.linspace(0, np.pi/2, 100)
    x_arc = 5 + 3*np.cos(theta)
    y_arc = 5 + 3*np.sin(theta)
    ax.plot(x_arc, y_arc, 'b-', linewidth=2.5, label='Arc')
    ax.plot(5, 5, 'bo', markersize=6)
    ax.plot([8, 5], [5, 8], 'ro', markersize=5)
    ax.text(5, 3, 'Center Arc\nR=3, angle=90°', ha='center', fontsize=9)
    ax.legend(fontsize=9)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # 1.5 ELLIPSE (ELIPS)
    ax = axes[1, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('5. ELLIPSE', fontweight='bold')
    
    ellipse = patches.Ellipse((5, 5), 6, 3, angle=0, edgecolor='blue', facecolor='lightblue', alpha=0.3, linewidth=2.5)
    ax.add_patch(ellipse)
    ax.plot(5, 5, 'bo', markersize=6, label='Center')
    ax.plot([5, 8], [5, 5], 'r-', linewidth=1.5, label='Major axis')
    ax.plot([5, 5], [5, 6.5], 'g-', linewidth=1.5, label='Minor axis')
    ax.legend(fontsize=8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # 1.6 SLOT
    ax = axes[1, 2]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('6. SLOT (STRAIGHT)', fontweight='bold')
    
    # Slot adalah persegi panjang dengan semi-circle di ujungnya
    slot_rect = patches.Rectangle((2, 4), 6, 2, linewidth=0, edgecolor='none', facecolor='lightblue', alpha=0.3)
    ax.add_patch(slot_rect)
    slot_left = patches.Wedge((2, 5), 1, 90, 270, linewidth=0, facecolor='lightblue', alpha=0.3)
    ax.add_patch(slot_left)
    slot_right = patches.Wedge((8, 5), 1, 270, 90, linewidth=0, facecolor='lightblue', alpha=0.3)
    ax.add_patch(slot_right)
    
    ax.plot([2, 8, 8, 2, 2], [4, 4, 6, 6, 4], 'b-', linewidth=2.5)
    ax.plot([2, 8], [3, 3], 'r--', linewidth=1, label='Centerline')
    ax.legend(fontsize=9)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/01_entitas_sketch.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: 01_entitas_sketch.png")
    plt.close()

# ============================================================================
# 2. SKETCH CONSTRAINTS (RELASI)
# ============================================================================
def sketch_constraints():
    """Visualisasi berbagai jenis constraints pada sketch"""
    fig, axes = plt.subplots(2, 3, figsize=(14, 10))
    fig.suptitle('SKETCH CONSTRAINTS (RELASI) - MODUL 2', fontsize=14, fontweight='bold')
    
    # 2.1 HORIZONTAL & VERTICAL
    ax = axes[0, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('1. HORIZONTAL & VERTICAL', fontweight='bold')
    
    # Horizontal line
    ax.plot([1, 7], [7, 7], 'b-', linewidth=2.5)
    ax.text(4, 7.5, 'Horizontal', ha='center', fontsize=9, color='blue', fontweight='bold')
    
    # Vertical line
    ax.plot([8, 8], [2, 8], 'r-', linewidth=2.5)
    ax.text(8.7, 5, 'Vertical', ha='left', fontsize=9, color='red', fontweight='bold', rotation=90)
    
    # Constraint symbols
    ax.text(4, 5, '—', fontsize=20, ha='center', color='blue', alpha=0.5)
    ax.text(9, 5, '|', fontsize=20, ha='center', color='red', alpha=0.5)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10)
    
    # 2.2 PARALLEL & PERPENDICULAR
    ax = axes[0, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('2. PARALLEL & PERPENDICULAR', fontweight='bold')
    
    # Parallel lines
    ax.plot([1, 6], [7, 7], 'b-', linewidth=2.5, label='Line 1')
    ax.plot([1.5, 6.5], [4, 4], 'b-', linewidth=2.5, label='Line 2 (Parallel)')
    ax.text(3.5, 5.5, 'Parallel\n||', ha='center', fontsize=10, fontweight='bold', color='blue')
    
    # Perpendicular
    ax.plot([8, 8], [2, 8], 'r-', linewidth=2.5)
    ax.plot([6, 10], [5, 5], 'r-', linewidth=2.5)
    ax.plot(8, 5, 'r+', markersize=12, markeredgewidth=2)
    ax.text(7, 3, '⊥ Perpendicular', ha='center', fontsize=9, color='red', fontweight='bold')
    
    ax.legend(fontsize=9, loc='upper left')
    ax.set_xlim(0, 11)
    
    # 2.3 TANGENT
    ax = axes[0, 2]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('3. TANGENT', fontweight='bold')
    
    # Circle
    circle = Circle((3, 5), 2, edgecolor='blue', facecolor='none', linewidth=2.5)
    ax.add_patch(circle)
    
    # Tangent line to circle
    ax.plot([1, 7], [7, 3], 'r-', linewidth=2.5, label='Tangent Line')
    
    # Tangent point
    ax.plot(3.8, 6.7, 'go', markersize=8, label='Tangent Point')
    
    ax.text(4.5, 8, 'Line Tangent\nto Circle', ha='center', fontsize=9, fontweight='bold')
    ax.legend(fontsize=9)
    ax.set_xlim(0, 8)
    
    # 2.4 CONCENTRIC
    ax = axes[1, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('4. CONCENTRIC', fontweight='bold')
    
    circle1 = Circle((5, 5), 3, edgecolor='blue', facecolor='none', linewidth=2.5)
    ax.add_patch(circle1)
    circle2 = Circle((5, 5), 1.5, edgecolor='red', facecolor='none', linewidth=2.5)
    ax.add_patch(circle2)
    ax.plot(5, 5, 'go', markersize=8)
    ax.text(5, 0.5, 'Concentric\nSame Center', ha='center', fontsize=9, fontweight='bold')
    
    # 2.5 COINCIDENT
    ax = axes[1, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('5. COINCIDENT', fontweight='bold')
    
    ax.plot([1, 8], [2, 7], 'b-', linewidth=2.5, label='Line 1')
    ax.plot([2, 7], [1, 8], 'r-', linewidth=2.5, label='Line 2')
    ax.plot(4.5, 4.5, 'go', markersize=10, label='Coincident Point')
    ax.text(5, 8.5, 'Lines share\ncommon point', ha='center', fontsize=9, fontweight='bold')
    ax.legend(fontsize=8)
    
    # 2.6 EQUAL
    ax = axes[1, 2]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('6. EQUAL (LENGTH)', fontweight='bold')
    
    ax.plot([1, 5], [7, 7], 'b-', linewidth=2.5, label='Line 1: L1')
    ax.plot([6, 10], [7, 7], 'b-', linewidth=2.5, label='Line 2: L2')
    ax.text(3, 5.5, 'L1', fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor='lightblue'))
    ax.text(8, 5.5, 'L2', fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    circle1 = Circle((2.5, 3), 2, edgecolor='r', facecolor='none', linewidth=2.5, label='Circle 1: R1')
    ax.add_patch(circle1)
    circle2 = Circle((7.5, 3), 2, edgecolor='r', facecolor='none', linewidth=2.5, label='Circle 2: R2')
    ax.add_patch(circle2)
    
    ax.text(5, 0.5, 'L1 = L2 = R1 = R2\nEQUAL Constraint', ha='center', fontsize=9, fontweight='bold')
    ax.legend(fontsize=8)
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/02_sketch_constraints.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: 02_sketch_constraints.png")
    plt.close()

# ============================================================================
# 3. SKETCH STATUS (FULLY DEFINED vs UNDER DEFINED vs OVER DEFINED)
# ============================================================================
def sketch_status():
    """Visualisasi status sketch dan degree of freedom"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('SKETCH STATUS - MODUL 2', fontsize=14, fontweight='bold')
    
    # UNDER DEFINED (Biru)
    ax = axes[0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('UNDER DEFINED (Biru)', fontweight='bold', color='blue')
    
    rect = patches.Rectangle((2, 3), 6, 4, linewidth=3, edgecolor='blue', facecolor='lightblue', alpha=0.2)
    ax.add_patch(rect)
    
    ax.text(5, 5, 'Rectangle\nNo Dimensions!\nNo Constraints!', ha='center', va='center', fontsize=10, fontweight='bold', color='blue')
    ax.text(5, 1, 'DOF > 0\n(Degrees of Freedom)', ha='center', fontsize=9, style='italic', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    # FULLY DEFINED (Hitam)
    ax = axes[1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('FULLY DEFINED (Hitam)', fontweight='bold', color='black')
    
    rect = patches.Rectangle((2, 2.5), 6, 5, linewidth=3, edgecolor='black', facecolor='lightgray', alpha=0.3)
    ax.add_patch(rect)
    
    # Dimension lines
    ax.annotate('', xy=(2, 1.5), xytext=(8, 1.5), arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(5, 0.8, 'W = 6mm', ha='center', fontsize=10, fontweight='bold')
    
    ax.annotate('', xy=(1.5, 2.5), xytext=(1.5, 7.5), arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(0.5, 5, 'H = 5mm', ha='center', fontsize=10, fontweight='bold', rotation=90)
    
    ax.text(5, 5, '✓ All constraints\n✓ All dimensions', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(5, 8.5, 'READY untuk Feature!', ha='center', fontsize=9, style='italic', 
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7, edgecolor='green', linewidth=2))
    
    # OVER DEFINED (Merah)
    ax = axes[2]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('OVER DEFINED (Merah)', fontweight='bold', color='red')
    
    rect = patches.Rectangle((2, 3), 6, 4, linewidth=3, edgecolor='red', facecolor='lightcoral', alpha=0.2)
    ax.add_patch(rect)
    
    # Conflicting dimensions
    ax.text(5, 5, 'W = 6mm\nW = 7mm\n(CONFLICT!)', ha='center', va='center', fontsize=10, fontweight='bold', color='red')
    
    ax.text(5, 1, '❌ Conflicting\nConstraints\nor Dimensions', ha='center', fontsize=9, fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7, edgecolor='red', linewidth=2))
    
    for ax_obj in axes:
        ax_obj.set_xlim(-1, 10)
        ax_obj.set_ylim(-1, 10)
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/03_sketch_status.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: 03_sketch_status.png")
    plt.close()

# ============================================================================
# 4. DIMENSIONING (PEMBERIAN UKURAN)
# ============================================================================
def dimensioning():
    """Visualisasi berbagai jenis dimensioning"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('DIMENSIONING (PEMBERIAN UKURAN) - MODUL 2', fontsize=14, fontweight='bold')
    
    # 4.1 LINEAR DIMENSION
    ax = axes[0, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('1. LINEAR DIMENSION', fontweight='bold')
    
    rect = patches.Rectangle((2, 3), 6, 4, linewidth=2, edgecolor='black', facecolor='lightgray', alpha=0.3)
    ax.add_patch(rect)
    
    # Width dimension
    ax.annotate('', xy=(2, 1.5), xytext=(8, 1.5), arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
    ax.text(5, 0.7, '80mm', ha='center', fontsize=10, fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    # Height dimension
    ax.annotate('', xy=(1.2, 3), xytext=(1.2, 7), arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
    ax.text(0.3, 5, '50mm', ha='center', fontsize=10, fontweight='bold', rotation=90, 
            bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    # 4.2 ANGULAR DIMENSION
    ax = axes[0, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('2. ANGULAR DIMENSION', fontweight='bold')
    
    # Two lines at angle
    ax.plot([2, 8], [5, 5], 'k-', linewidth=2)
    ax.plot([5, 8], [5, 8], 'k-', linewidth=2)
    
    # Arc for angle
    theta = np.linspace(0, np.pi/4, 50)
    arc_x = 5 + 1.5*np.cos(theta)
    arc_y = 5 + 1.5*np.sin(theta)
    ax.plot(arc_x, arc_y, 'b-', linewidth=2)
    ax.text(6.5, 5.8, '45°', fontsize=11, fontweight='bold', color='blue',
            bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    ax.plot([2, 5, 8], [5, 5, 8], 'ko', markersize=5)
    
    # 4.3 RADIAL DIMENSION
    ax = axes[1, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('3. RADIAL & DIAMETER DIMENSION', fontweight='bold')
    
    circle = Circle((5, 5), 2.5, edgecolor='black', facecolor='lightgray', alpha=0.3, linewidth=2)
    ax.add_patch(circle)
    ax.plot(5, 5, 'ko', markersize=5)
    
    # Radius dimension
    ax.plot([5, 7.5], [5, 5], 'b-', linewidth=2)
    ax.text(6.3, 5.5, 'R = 25mm', fontsize=10, fontweight='bold', color='blue',
            bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    # Diameter dimension (atas)
    ax.plot([2.5, 7.5], [8, 8], 'r--', linewidth=1)
    ax.annotate('', xy=(2.5, 8.5), xytext=(7.5, 8.5), arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(5, 8.8, 'Ø50mm', ha='center', fontsize=10, fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='lightyellow'))
    
    # 4.4 DRIVEN vs REFERENCE DIMENSION
    ax = axes[1, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('4. DRIVEN vs REFERENCE DIMENSION', fontweight='bold')
    
    rect1 = patches.Rectangle((1, 6.5), 3, 2, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax.add_patch(rect1)
    ax.text(2.5, 7.5, 'DRIVING\n(Can edit)', ha='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='green', linewidth=2))
    ax.annotate('', xy=(1, 6), xytext=(4, 6), arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text(2.5, 5.5, '30mm', ha='center', fontsize=9, fontweight='bold', color='green')
    
    rect2 = patches.Rectangle((5.5, 6.5), 3, 2, linewidth=2, edgecolor='gray', facecolor='lightgray', alpha=0.3)
    ax.add_patch(rect2)
    ax.text(7, 7.5, 'REFERENCE\n(Informasi)', ha='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='orange', linewidth=2))
    ax.annotate('', xy=(5.5, 6), xytext=(8.5, 6), arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
    ax.text(7, 5.5, '[15mm]', ha='center', fontsize=9, fontweight='bold', color='orange')
    
    ax.text(5, 2, 'Driving Dimension: Mengontrol shape\nReference Dimension: Info saja (dari constraints)', 
            ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/04_dimensioning.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: 04_dimensioning.png")
    plt.close()

# ============================================================================
# 5. SKETCH TOOLS (OFFSET, PATTERN, FILLET)
# ============================================================================
def sketch_tools():
    """Visualisasi sketch tools"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('SKETCH TOOLS - MODUL 2', fontsize=14, fontweight='bold')
    
    # 5.1 OFFSET
    ax = axes[0, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('1. OFFSET ENTITIES', fontweight='bold')
    
    # Original rectangle
    rect1 = patches.Rectangle((2, 2), 6, 4, linewidth=2.5, edgecolor='blue', facecolor='none', linestyle='-')
    ax.add_patch(rect1)
    ax.text(5, 2.5, 'Original', ha='center', fontsize=9, color='blue', fontweight='bold')
    
    # Offset rectangle (inward)
    rect2 = patches.Rectangle((2.8, 2.8), 4.4, 2.4, linewidth=2, edgecolor='red', facecolor='none', linestyle='--')
    ax.add_patch(rect2)
    ax.text(5, 3.2, 'Offset -0.8', ha='center', fontsize=9, color='red', fontweight='bold')
    
    # Offset arrows
    ax.annotate('', xy=(6.5, 2.5), xytext=(6, 2.8), arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.text(7, 2.3, 'Inward', fontsize=8, color='purple')
    
    # 5.2 TRIM
    ax = axes[0, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('2. TRIM ENTITIES', fontweight='bold')
    
    # Lines before trim
    ax.text(2, 8, 'BEFORE TRIM:', fontsize=9, fontweight='bold')
    ax.plot([1, 8], [7, 7], 'b-', linewidth=2)
    ax.plot([4, 4], [3, 8], 'b-', linewidth=2)
    ax.plot(4, 7, 'bo', markersize=8, label='Intersection')
    
    # Lines after trim
    ax.text(2, 1.5, 'AFTER TRIM:', fontsize=9, fontweight='bold')
    ax.plot([1, 4], [6, 6], 'r-', linewidth=2, label='Trimmed')
    ax.plot([4, 4], [3, 6], 'r-', linewidth=2, label='Trimmed')
    ax.plot([4, 8], [6, 6], 'gray', linewidth=1, linestyle='--', label='Removed')
    ax.plot([4, 4], [6, 8], 'gray', linewidth=1, linestyle='--', label='Removed')
    
    ax.legend(fontsize=8, loc='lower right')
    
    # 5.3 MIRROR
    ax = axes[1, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('3. MIRROR ENTITIES', fontweight='bold')
    
    # Mirror line (centerline)
    ax.axvline(x=5, color='green', linewidth=2, linestyle='--', label='Mirror Line')
    
    # Original shape (kiri)
    circle1 = Circle((3, 5), 1, edgecolor='blue', facecolor='lightblue', alpha=0.5, linewidth=2)
    ax.add_patch(circle1)
    ax.plot([3, 4], [5, 6], 'b-', linewidth=2)
    ax.text(2.5, 5, 'Original', fontsize=9, color='blue', fontweight='bold')
    
    # Mirrored shape (kanan)
    circle2 = Circle((7, 5), 1, edgecolor='red', facecolor='lightcoral', alpha=0.5, linewidth=2)
    ax.add_patch(circle2)
    ax.plot([6, 7], [5, 6], 'r-', linewidth=2)
    ax.text(7.5, 5, 'Mirrored', fontsize=9, color='red', fontweight='bold')
    
    ax.legend(fontsize=9)
    
    # 5.4 PATTERN
    ax = axes[1, 1]
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('4. LINEAR & CIRCULAR PATTERN', fontweight='bold')
    
    # Linear Pattern
    ax.text(2, 9, 'Linear Pattern (Seeding):', fontsize=9, fontweight='bold')
    for i in range(4):
        circle = Circle((1.5 + i*1.2, 7), 0.4, edgecolor='blue', facecolor='lightblue', alpha=0.6, linewidth=1.5)
        ax.add_patch(circle)
    ax.text(3.5, 6.3, 'Linear\nSpacing: 1.2mm', fontsize=8, color='blue', fontweight='bold')
    
    # Circular Pattern
    ax.text(8, 9, 'Circular Pattern:', fontsize=9, fontweight='bold')
    center_x, center_y = 8, 6.5
    n_pattern = 6
    for i in range(n_pattern):
        angle = 2 * np.pi * i / n_pattern
        x = center_x + 1.5 * np.cos(angle)
        y = center_y + 1.5 * np.sin(angle)
        circle = Circle((x, y), 0.4, edgecolor='red', facecolor='lightcoral', alpha=0.6, linewidth=1.5)
        ax.add_patch(circle)
    ax.plot(center_x, center_y, 'r+', markersize=12, markeredgewidth=2)
    ax.text(8, 4.3, f'Circular\n{n_pattern} instances', fontsize=8, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/05_sketch_tools.png', dpi=150, bbox_inches='tight')
    print("✓ Gambar: 05_sketch_tools.png")
    plt.close()

# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("GENERATING VISUALIZATIONS FOR MODUL 2 - 2D SKETCHING")
    print("="*60)
    
    sketch_entities()
    sketch_constraints()
    sketch_status()
    dimensioning()
    sketch_tools()
    
    print("\n✓ Semua gambar 2D Sketching berhasil dibuat!")
    print("  Lokasi: /home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/")
    print("="*60 + "\n")
