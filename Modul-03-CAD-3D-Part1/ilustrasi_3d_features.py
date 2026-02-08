"""
VISUALISASI KONSEP 3D FEATURES - MODUL 3
Versi stabil dengan isometric drawing 2D yang mudah dipahami
Mengilustrasikan:
1. Extrude (Boss & Cut)
2. Revolve (Boss & Cut)
3. Fillet & Chamfer
4. Shell & Draft
5. Pattern (Linear & Circular)
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Polygon, Arc
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# HELPER FUNCTION: ISOMETRIC PROJECTION
# ============================================================================
def to_isometric(x, y, z):
    """Convert 3D coordinates to isometric 2D projection"""
    iso_x = x - z
    iso_y = y + 0.5 * z
    return iso_x, iso_y

def draw_isometric_box(ax, width, height, depth, x_start=0, y_start=0, 
                       face_color='cyan', edge_color='black', alpha=0.4, linewidth=2):
    """Draw 3D box dalam isometric view"""
    
    # Corner points dalam 3D
    corners_3d = [
        [x_start, y_start, 0],  # 0: bottom-left-front
        [x_start+width, y_start, 0],  # 1: bottom-right-front
        [x_start+width, y_start+height, 0],  # 2: bottom-right-back
        [x_start, y_start+height, 0],  # 3: bottom-left-back
        [x_start, y_start, depth],  # 4: top-left-front
        [x_start+width, y_start, depth],  # 5: top-right-front
        [x_start+width, y_start+height, depth],  # 6: top-right-back
        [x_start, y_start+height, depth],  # 7: top-left-back
    ]
    
    # Konversi ke isometric 2D
    iso_corners = [to_isometric(*c) for c in corners_3d]
    
    # Draw top face (paling terlihat)
    top_face = [iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]]
    top_poly = Polygon(top_face, facecolor=face_color, edgecolor=edge_color, 
                       linewidth=linewidth, alpha=alpha)
    ax.add_patch(top_poly)
    
    # Draw front face
    front_face = [iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]]
    front_poly = Polygon(front_face, facecolor='lightblue', edgecolor=edge_color, 
                         linewidth=linewidth, alpha=alpha*0.8)
    ax.add_patch(front_poly)
    
    # Draw right face
    right_face = [iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]]
    right_poly = Polygon(right_face, facecolor='lightcyan', edgecolor=edge_color, 
                         linewidth=linewidth, alpha=alpha*0.6)
    ax.add_patch(right_poly)
    
    return iso_corners

# ============================================================================
# 1. EXTRUDE FEATURE
# ============================================================================
def extrude_feature():
    """Visualisasi Extrude Boss dan Cut"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle('EXTRUDE FEATURE - MODUL 3', fontsize=14, fontweight='bold', y=0.98)
    
    # 1.1 EXTRUDE BOSS
    ax = axes[0]
    ax.set_xlim(-3, 8)
    ax.set_ylim(-3, 8)
    ax.set_aspect('equal')
    ax.set_title('1. EXTRUDE BOSS\n(2D → 3D Solid)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw 2D sketch
    sketch_corners = [[0, 0], [4, 0], [4, 3], [0, 3]]
    sketch_poly = Polygon(sketch_corners, facecolor='lightblue', edgecolor='blue', 
                         linewidth=2.5, alpha=0.7)
    ax.add_patch(sketch_poly)
    ax.text(2, 1.5, 'Sketch 2D', ha='center', va='center', fontsize=10, 
           fontweight='bold', color='blue')
    
    # Arrow
    ax.annotate('', xy=(6, 1.5), xytext=(4.5, 1.5),
               arrowprops=dict(arrowstyle='->', lw=2.5, color='red'))
    ax.text(5.2, 2.3, 'Extrude\n3mm', ha='center', fontsize=9, color='red', fontweight='bold')
    
    # Draw 3D box (isometric)
    iso_corners = draw_isometric_box(ax, 4, 3, 3, x_start=5.5, y_start=0, 
                                     face_color='cyan', alpha=0.5)
    ax.text(7.2, 2, '3D Solid', ha='center', fontsize=10, fontweight='bold', color='darkblue')
    
    # 1.2 EXTRUDE CUT
    ax = axes[1]
    ax.set_xlim(-2, 10)
    ax.set_ylim(-2, 8)
    ax.set_aspect('equal')
    ax.set_title('2. EXTRUDE CUT\n(Potong Lubang)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw base solid
    iso_corners = draw_isometric_box(ax, 6, 4, 2, x_start=0, y_start=0, 
                                     face_color='cyan', alpha=0.4)
    
    # Draw hole (circle on top face)
    hole_pos = to_isometric(3, 2, 2)
    hole = Circle(hole_pos, 0.6, facecolor='white', edgecolor='red', 
                 linewidth=2.5, linestyle='--')
    ax.add_patch(hole)
    ax.text(hole_pos[0], hole_pos[1]-1, 'Ø1.6\nThrough All', ha='center', 
           fontsize=9, color='red', fontweight='bold')
    
    # 1.3 EXTRUDE OPTIONS
    ax = axes[2]
    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-0.5, 10)
    ax.set_title('3. END CONDITIONS', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    options = [
        'Blind (jarak tertentu)',
        'Through All (tembus)',
        'Up To Surface',
        'Up To Vertex',
        'Mid Plane (simetris)',
    ]
    
    colors = ['cyan', 'lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
    
    for i, (opt, color) in enumerate(zip(options, colors)):
        y = 8 - i*1.7
        box = FancyBboxPatch((0.5, y-0.5), 9, 1, boxstyle="round,pad=0.1",
                            edgecolor='black', facecolor=color, linewidth=1.5, alpha=0.7)
        ax.add_patch(box)
        ax.text(1, y, f'• {opt}', fontsize=10, fontweight='bold', va='center')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/01_extrude_feature.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 01_extrude_feature.png")
    plt.close()

# ============================================================================
# 2. REVOLVE FEATURE
# ============================================================================
def revolve_feature():
    """Visualisasi Revolve Boss"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle('REVOLVE FEATURE - MODUL 3', fontsize=14, fontweight='bold', y=0.98)
    
    # 2.1 SKETCH PROFILE
    ax = axes[0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('1. SKETCH PROFILE\n(Trapezoid)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Sketch
    profile = [[0, 0], [1, 0], [1.5, 3], [0.5, 3]]
    profile_poly = Polygon(profile, facecolor='lightblue', edgecolor='blue', 
                          linewidth=2.5, alpha=0.7)
    ax.add_patch(profile_poly)
    
    # Centerline (revolve axis)
    ax.plot([0, 0], [0, 3.5], 'r--', linewidth=2.5, label='Centerline')
    ax.plot([0]*2, [0, 3.5], 'ro', markersize=6)
    ax.text(-0.5, 1.5, 'Axis', fontsize=9, color='red', fontweight='bold')
    
    ax.text(1.5, 1.5, 'Profil\nRevolution', ha='left', fontsize=9, fontweight='bold')
    ax.legend(fontsize=9, loc='upper right')
    ax.set_xlim(-1.5, 4)
    
    # 2.2 REVOLVE VISUALIZATION
    ax = axes[1]
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_title('2. REVOLVE 360°\n(Rotate & Sweep)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw revolved shape (cone-like)
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Top circle (small)
    r_top = 0.5
    x_top = r_top * np.cos(theta)
    y_top = r_top * np.sin(theta)
    ax.plot(x_top, y_top + 2.5, 'cyan', linewidth=2)
    ax.fill(x_top, y_top + 2.5, 'cyan', alpha=0.3)
    
    # Middle circles
    for h in [1, 1.5, 2]:
        r = 0.5 + (3-h) * 0.5/3
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot(x, y + 2.5 - h, 'cyan', linewidth=1, alpha=0.6)
    
    # Bottom circle (large)
    r_bottom = 1
    x_bottom = r_bottom * np.cos(theta)
    y_bottom = r_bottom * np.sin(theta)
    ax.plot(x_bottom, y_bottom - 0.5, 'cyan', linewidth=2)
    ax.fill(x_bottom, y_bottom - 0.5, 'cyan', alpha=0.3)
    
    # Profile outline
    ax.plot([0, 1], [-0.5, 0], 'b--', linewidth=1.5, alpha=0.5)
    ax.plot([1, 1.5], [0, 2.5], 'b--', linewidth=1.5, alpha=0.5)
    ax.plot([1.5, 0], [2.5, 3.5], 'b--', linewidth=1.5, alpha=0.5)
    
    # Center axis
    ax.plot([0, 0], [-1, 4], 'r--', linewidth=1.5, alpha=0.7)
    ax.text(-0.8, 1.5, 'Axis', fontsize=8, color='red')
    
    ax.text(0, -3, 'Shape dari Revolution', ha='center', fontsize=9, fontweight='bold')
    
    # 2.3 SYARAT REVOLVE
    ax = axes[2]
    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-0.5, 10)
    ax.set_title('3. SYARAT REVOLVE', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # CORRECT
    ax.text(1, 8.5, 'CORRECT:', fontsize=10, fontweight='bold', color='green')
    profile_x = [1, 2, 2, 1]
    profile_y = [6, 6, 7.5, 7.5]
    ax.plot(profile_x + [profile_x[0]], profile_y + [profile_y[0]], 'g-', linewidth=2.5)
    ax.plot([0, 0], [5.5, 8], 'r--', linewidth=2)
    ax.text(0.2, 6.5, 'Axis', fontsize=8, color='red', fontweight='bold')
    ax.text(2.5, 6.8, 'Profile\nsatu sisi', fontsize=8, color='green', fontweight='bold')
    
    # WRONG
    ax.text(1, 4.5, 'WRONG:', fontsize=10, fontweight='bold', color='red')
    bad_x = [1.5, 2.5, 2.5, 1.5]
    bad_y = [2.5, 2.5, 3.5, 3.5]
    ax.plot(bad_x + [bad_x[0]], bad_y + [bad_y[0]], 'r-', linewidth=2.5)
    ax.plot([2, 2], [2.3, 3.8], 'b--', linewidth=2)
    ax.text(2.3, 3, 'Axis', fontsize=8, color='blue', fontweight='bold')
    ax.text(3.2, 3, 'Profile\nmemotong\naxis', fontsize=8, color='red', fontweight='bold')
    
    # Rules
    ax.text(1, 0.5, 'Profil harus di satu sisi centerline', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/02_revolve_feature.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 02_revolve_feature.png")
    plt.close()

# ============================================================================
# 3. FILLET & CHAMFER
# ============================================================================
def fillet_chamfer():
    """Visualisasi Fillet dan Chamfer"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle('FILLET & CHAMFER - MODUL 3', fontsize=14, fontweight='bold', y=0.98)
    
    # 3.1 SHARP EDGE
    ax = axes[0]
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('1. SHARP EDGE\n(Original)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw box
    iso_corners = draw_isometric_box(ax, 4, 3, 2, x_start=0, y_start=0, 
                                     face_color='lightgray', alpha=0.4)
    
    # Highlight sharp edges
    for i in [0, 1, 2]:
        ax.plot([iso_corners[i][0], iso_corners[i+1][0]], 
               [iso_corners[i][1], iso_corners[i+1][1]], 'r-', linewidth=3)
    
    ax.text(2, 6.5, 'Sharp Edges (90°)', fontsize=9, color='red', fontweight='bold')
    
    # 3.2 FILLET
    ax = axes[1]
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('2. FILLET\n(Pembulatan R=2mm)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw box with rounded corners
    iso_corners = draw_isometric_box(ax, 4, 3, 2, x_start=0, y_start=0, 
                                     face_color='lightgreen', alpha=0.5)
    
    # Draw fillet arcs (simplified)
    for i in [0, 1, 2]:
        start = iso_corners[i]
        end = iso_corners[i+1]
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.plot([start[0], mid_x, end[0]], [start[1], mid_y+0.3, end[1]], 
               'g-', linewidth=3)
    
    ax.text(2, 6.5, 'Rounded Edges (Smooth)', fontsize=9, color='green', fontweight='bold')
    
    # 3.3 CHAMFER
    ax = axes[2]
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('3. CHAMFER\n(Potongan 2x2mm)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw box with chamfered corners
    iso_corners = draw_isometric_box(ax, 4, 3, 2, x_start=0, y_start=0, 
                                     face_color='lightcoral', alpha=0.5)
    
    # Draw chamfer lines (beveled)
    for i in [0, 1, 2]:
        start = iso_corners[i]
        end = iso_corners[i+1]
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        offset_x = (end[1] - start[1]) * 0.1
        offset_y = -(end[0] - start[0]) * 0.1
        ax.plot([start[0]+offset_x, mid_x, end[0]-offset_x], 
               [start[1]+offset_y, mid_y, end[1]-offset_y], 
               'purple', linewidth=3)
    
    ax.text(2, 6.5, 'Beveled Edges (Angled)', fontsize=9, color='purple', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/03_fillet_chamfer.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 03_fillet_chamfer.png")
    plt.close()

# ============================================================================
# 4. SHELL & DRAFT
# ============================================================================
def shell_draft():
    """Visualisasi Shell dan Draft"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('SHELL & DRAFT FEATURE - MODUL 3', fontsize=14, fontweight='bold', y=0.98)
    
    # 4.1 SHELL
    ax = axes[0]
    ax.set_xlim(-2, 8)
    ax.set_ylim(-2, 8)
    ax.set_aspect('equal')
    ax.set_title('SHELL (Membuat Hollow)\nThickness = 2mm', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Outer box (solid)
    iso_outer = draw_isometric_box(ax, 4, 3, 2, x_start=0, y_start=0, 
                                   face_color='cyan', alpha=0.5)
    
    # Inner box (hollow) - offset
    iso_inner = draw_isometric_box(ax, 3.5, 2.5, 1.6, x_start=0.25, y_start=0.25, 
                                   face_color='white', alpha=0.8)
    
    ax.text(2, 6, 'BEFORE: Solid', fontsize=10, color='cyan', fontweight='bold')
    ax.text(2, -1, 'AFTER: Hollow (2mm wall)', fontsize=10, color='blue', fontweight='bold')
    
    # 4.2 DRAFT
    ax = axes[1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 9)
    ax.set_title('DRAFT (Sudut Ejection)\nuntuk Molding', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # No draft
    ax.text(1, 8, 'WITHOUT DRAFT:', fontsize=10, fontweight='bold', color='blue')
    ax.plot([0.5, 2], [7, 3.5], 'b-', linewidth=2.5)
    ax.plot([0.5, 0.5], [7, 3.5], 'b-', linewidth=2.5)
    ax.plot([2, 2], [7, 3.5], 'b-', linewidth=2.5)
    ax.text(0.2, 5, '0°', fontsize=9, color='blue', fontweight='bold')
    
    # With draft
    ax.text(5.5, 8, 'WITH DRAFT (2°):', fontsize=10, fontweight='bold', color='red')
    ax.plot([4, 6], [7, 3.5], 'r-', linewidth=2.5)  # Slanted
    ax.plot([4, 4], [7, 3.5], 'r-', linewidth=2.5)
    ax.plot([6, 6], [7, 3.5], 'r-', linewidth=2.5)
    
    # Angle indicator
    ax.plot([4, 5.5], [7, 7], 'r--', linewidth=1, alpha=0.5)
    ax.text(4.7, 7.3, '2°', fontsize=9, color='red', fontweight='bold')
    
    ax.text(2.5, 1.5, 'Draft membuat\neasy ejection', ha='center', fontsize=9, fontweight='bold')
    ax.text(7.5, 1.5, 'Easier to remove\nfrom mold', ha='center', fontsize=9, 
           fontweight='bold', color='red')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/04_shell_draft.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 04_shell_draft.png")
    plt.close()

# ============================================================================
# 5. PATTERN FEATURES
# ============================================================================
def pattern_features():
    """Visualisasi Pattern"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('PATTERN FEATURES - MODUL 3', fontsize=14, fontweight='bold', y=0.98)
    
    # 5.1 LINEAR PATTERN
    ax = axes[0]
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 7)
    ax.set_aspect('equal')
    ax.set_title('LINEAR PATTERN\n(Seeding 1 lubang)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Base plate
    plate = patches.Rectangle((0, 1), 10, 3, edgecolor='black', facecolor='lightgray', 
                             linewidth=2, alpha=0.3)
    ax.add_patch(plate)
    
    # Holes in linear pattern
    for i in range(5):
        x = 1 + i*2
        hole = Circle((x, 2.5), 0.35, edgecolor='red', facecolor='white', linewidth=2)
        ax.add_patch(hole)
        
        if i == 0:
            ax.text(x, 2.5, 'S', ha='center', va='center', fontsize=8, 
                   color='red', fontweight='bold')
        else:
            ax.text(x, 2.5, str(i), ha='center', va='center', fontsize=8, 
                   color='red', fontweight='bold')
    
    # Direction arrow
    ax.annotate('', xy=(8.5, 4.2), xytext=(2.5, 4.2),
               arrowprops=dict(arrowstyle='->', lw=2, color='green'))
    ax.text(5.5, 4.7, 'Direction (X-axis)', ha='center', fontsize=9, 
           color='green', fontweight='bold')
    
    ax.text(5.5, 0.3, 'Spacing: 2mm, Count: 5', ha='center', fontsize=9, fontweight='bold')
    
    # 5.2 CIRCULAR PATTERN
    ax = axes[1]
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.set_title('CIRCULAR PATTERN\n(Around Center)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Base circle
    base_circle = Circle((0, 0), 4.5, edgecolor='black', facecolor='lightgray', 
                        linewidth=2, alpha=0.3)
    ax.add_patch(base_circle)
    
    # Center
    ax.plot(0, 0, 'ko', markersize=8)
    ax.text(0.3, 0.3, 'Center', fontsize=8)
    
    # Holes in circular pattern
    n_pattern = 8
    for i in range(n_pattern):
        angle = 2 * np.pi * i / n_pattern
        x = 3.5 * np.cos(angle)
        y = 3.5 * np.sin(angle)
        
        hole = Circle((x, y), 0.4, edgecolor='red', facecolor='white', linewidth=1.5)
        ax.add_patch(hole)
        
        if i == 0:
            ax.text(x+0.15, y+0.15, 'S', ha='center', va='center', fontsize=8, 
                   color='red', fontweight='bold')
        else:
            ax.text(x+0.15, y+0.15, str(i), ha='center', va='center', fontsize=7, 
                   color='red', fontweight='bold')
    
    ax.text(0, -5.5, f'{n_pattern} instances @ {360/n_pattern:.0f}° spacing', 
           ha='center', fontsize=9, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/05_pattern_features.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 05_pattern_features.png")
    plt.close()

# ============================================================================
# 6. FEATURE WORKFLOW
# ============================================================================
def feature_workflow():
    """Visualisasi workflow lengkap"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('FEATURE-BASED PART MODELING WORKFLOW - MODUL 3', 
                fontsize=14, fontweight='bold', y=0.98)
    
    steps = [
        ('STEP 1: SKETCH\n(2D Profile)', 'blue', 'lightblue'),
        ('STEP 2: EXTRUDE\n(Base Feature)', 'cyan', 'lightcyan'),
        ('STEP 3: FILLET\n(Round Edges)', 'green', 'lightgreen'),
        ('STEP 4: CUT\n(Make Hole)', 'orange', 'lightyellow'),
        ('STEP 5: CHAMFER\n(Bevel)', 'purple', 'plum'),
        ('STEP 6: PATTERN\n(Repeat 6x)', 'magenta', 'lightpink'),
    ]
    
    for ax, (title, edge_color, face_color) in zip(axes.flat, steps):
        ax.set_xlim(-1, 10)
        ax.set_ylim(-1, 10)
        ax.set_aspect('equal')
        ax.set_title(title, fontweight='bold', fontsize=11, color=edge_color)
        ax.axis('off')
        
        step_num = steps.index((title, edge_color, face_color))
        
        if step_num == 0:  # SKETCH
            sketch = Polygon([[2, 2], [8, 2], [8, 6], [2, 6]], 
                           edgecolor=edge_color, facecolor=face_color, 
                           linewidth=2.5, alpha=0.6)
            ax.add_patch(sketch)
            ax.plot([2, 8, 8, 2, 2], [2, 2, 6, 6, 2], 'o', 
                   color=edge_color, markersize=5)
            ax.text(5, 4, '2D Profile\n80 x 50mm', ha='center', va='center', 
                   fontsize=10, fontweight='bold')
        
        elif step_num == 1:  # EXTRUDE
            iso_corners = draw_isometric_box(ax, 6, 4, 2, x_start=1, y_start=1, 
                                            face_color=face_color, edge_color=edge_color, alpha=0.6)
            ax.text(4, -0.5, '3D Solid\nH=30mm', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 2:  # FILLET
            iso_corners = draw_isometric_box(ax, 6, 4, 2, x_start=1, y_start=1, 
                                            face_color=face_color, edge_color=edge_color, alpha=0.6)
            ax.text(4, -0.5, 'Fillet\nR=2mm', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 3:  # CUT
            iso_corners = draw_isometric_box(ax, 6, 4, 2, x_start=1, y_start=1, 
                                            face_color=face_color, edge_color=edge_color, alpha=0.6)
            # Draw hole
            hole_pos = to_isometric(4, 3, 2)
            hole = Circle(hole_pos, 0.6, facecolor='white', edgecolor='red', linewidth=2)
            ax.add_patch(hole)
            ax.text(4, -0.5, 'Cut\nØ20mm', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 4:  # CHAMFER
            iso_corners = draw_isometric_box(ax, 6, 4, 2, x_start=1, y_start=1, 
                                            face_color=face_color, edge_color=edge_color, alpha=0.6)
            ax.text(4, -0.5, 'Chamfer\n2x2mm', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 5:  # PATTERN
            for i in range(3):
                for j in range(2):
                    x = 2 + i*2.5
                    y = 2 + j*2.5
                    mini_box = patches.Rectangle((x-0.6, y-0.6), 1.2, 1.2, 
                                                edgecolor=edge_color, facecolor=face_color, 
                                                linewidth=1.5, alpha=0.6)
                    ax.add_patch(mini_box)
            ax.text(5, 8.5, '6 Instances', ha='center', fontsize=10, fontweight='bold', color=edge_color)
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/06_feature_workflow.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 06_feature_workflow.png")
    plt.close()

# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    print("\n" + "="*70)
    print("GENERATING VISUALIZATIONS FOR MODUL 3 - 3D FEATURES")
    print("="*70)
    
    try:
        extrude_feature()
        revolve_feature()
        fillet_chamfer()
        shell_draft()
        pattern_features()
        feature_workflow()
        
        print("\n" + "="*70)
        print("SEMUA GAMBAR 3D FEATURES BERHASIL DIBUAT!")
        print("="*70)
        print("\nLokasi: /home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/")
        print("\nGambar yang dihasilkan:")
        print("  01_extrude_feature.png      - Extrude Boss & Cut")
        print("  02_revolve_feature.png      - Revolve Concept")
        print("  03_fillet_chamfer.png       - Fillet & Chamfer")
        print("  04_shell_draft.png          - Shell & Draft")
        print("  05_pattern_features.png     - Linear & Circular Pattern")
        print("  06_feature_workflow.png     - Complete Workflow")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
