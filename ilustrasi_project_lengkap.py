"""
ILUSTRASI PROJECT LENGKAP - MODUL 2 & 3
Membantu praktikan menyelesaikan project dan memahami konsep
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Polygon, Arc, Rectangle
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# MODUL 2 ADDITIONAL ILLUSTRATIONS
# ============================================================================

def panel_kontrol_layout():
    """Project Panel Kontrol dengan dimensi lengkap"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    fig.suptitle('PROJECT PANEL KONTROL - MODUL 2\n(Dimensi & Layout Lengkap)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    ax.set_xlim(-20, 220)
    ax.set_ylim(-20, 170)
    ax.set_aspect('equal')
    ax.set_title('200 x 150mm Panel dengan Semua Komponen', fontweight='bold', fontsize=12)
    
    # Main panel with rounded corners
    panel = FancyBboxPatch((0, 0), 200, 150, boxstyle="round,pad=10",
                          edgecolor='black', facecolor='lightgray', linewidth=2, alpha=0.3)
    ax.add_patch(panel)
    
    # 1. Mounting holes (4 sudut)
    mount_positions = [(10, 10), (190, 10), (10, 140), (190, 140)]
    for i, (x, y) in enumerate(mount_positions):
        mount = Circle((x, y), 3, facecolor='white', edgecolor='blue', linewidth=2)
        ax.add_patch(mount)
        ax.text(x, y, f'M{i+1}', ha='center', va='center', fontsize=8, fontweight='bold')
    
    # 2. Display cutout (kanan atas)
    display = FancyBboxPatch((120, 105), 60, 30, boxstyle="round,pad=3",
                            edgecolor='green', facecolor='lightgreen', linewidth=2, alpha=0.6)
    ax.add_patch(display)
    ax.text(150, 120, 'DISPLAY\n60×30mm\nR3', ha='center', va='center', fontsize=9, fontweight='bold')
    
    # 3. Tombol (3 buah, tengah bawah)
    button_positions = [(50, 30), (85, 30), (120, 30)]
    for i, (x, y) in enumerate(button_positions):
        button = Circle((x, y), 11, facecolor='yellow', edgecolor='orange', linewidth=2, alpha=0.7)
        ax.add_patch(button)
        ax.text(x, y, f'B{i+1}', ha='center', va='center', fontsize=9, fontweight='bold')
        
        # Label slot
        slot = Rectangle((x-7.5, y-20), 15, 3, facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(slot)
    
    # 4. Selector switch (kiri atas)
    selector = Circle((30, 120), 11, facecolor='lightblue', edgecolor='blue', linewidth=2, alpha=0.7)
    ax.add_patch(selector)
    # D-cut (flat)
    flat = Rectangle((19, 115), 22, 10, facecolor='lightblue', edgecolor='blue', linewidth=2, alpha=0.7)
    ax.add_patch(flat)
    ax.text(30, 120, 'SEL', ha='center', va='center', fontsize=8, fontweight='bold')
    
    # 5. Emergency stop (kanan bawah)
    emergency_mark = Circle((165, 35), 27.5, facecolor='none', edgecolor='red', 
                           linewidth=1, linestyle='--', alpha=0.5)
    ax.add_patch(emergency_mark)
    emergency = Circle((165, 35), 20, facecolor='red', edgecolor='darkred', linewidth=3, alpha=0.8)
    ax.add_patch(emergency)
    ax.text(165, 35, 'E-STOP\nØ40mm', ha='center', va='center', fontsize=8, 
           fontweight='bold', color='white')
    
    # 6. Ventilasi slots (kiri bawah)
    for i in range(5):
        y_pos = 35 + i*6
        slot = FancyBboxPatch((15, y_pos), 25, 3, boxstyle="round,pad=1.5",
                             edgecolor='gray', facecolor='white', linewidth=1)
        ax.add_patch(slot)
    ax.text(27.5, 70, 'VENT\nSLOTS', ha='center', va='center', fontsize=8, fontweight='bold')
    
    # 7. Label engraving area (tengah atas)
    label_area = Rectangle((75, 132), 50, 8, facecolor='lightyellow', 
                          edgecolor='purple', linewidth=1, alpha=0.6)
    ax.add_patch(label_area)
    ax.text(100, 136, 'LABEL AREA', ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Dimensi annotations
    ax.annotate('', xy=(200, -10), xytext=(0, -10),
               arrowprops=dict(arrowstyle='<->', lw=1.5, color='red'))
    ax.text(100, -15, '200mm', ha='center', fontsize=10, fontweight='bold', color='red')
    
    ax.annotate('', xy=(210, 150), xytext=(210, 0),
               arrowprops=dict(arrowstyle='<->', lw=1.5, color='red'))
    ax.text(215, 75, '150mm', ha='center', va='center', rotation=90, 
           fontsize=10, fontweight='bold', color='red')
    
    # Constraint indicators
    ax.text(-15, 75, 'SYMMETRIC\n(Mounting)', ha='center', va='center', rotation=90,
           fontsize=8, fontweight='bold', color='blue')
    
    ax.text(100, -5, 'CONSTRAINTS: Symmetric, Equal, Concentric, Pattern, Mirror', 
           ha='center', fontsize=9, fontweight='bold', color='blue')
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/07_project_panel_kontrol.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 07_project_panel_kontrol.png")
    plt.close()

def profil_aluminium_sketches():
    """Sketch profil aluminium dari katalog"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('PROJECT PROFIL ALUMINIUM SKETCHES - MODUL 2\n(Berdasarkan Katalog Connect Automation)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    # 1. Profil 2020
    ax = axes[0, 0]
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 2020 (20×20mm)\n4 Slot, Center Ø5mm', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Main square
    square = Rectangle((-10, -10), 20, 20, facecolor='lightblue', edgecolor='blue', 
                      linewidth=2, alpha=0.6)
    ax.add_patch(square)
    
    # T-slots (4 sisi)
    for i in range(4):
        angle = i * 90
        # Outer slot
        slot_outer = Rectangle((-3, -10), 6, 2, facecolor='white', edgecolor='blue', linewidth=1)
        t = plt.matplotlib.transforms.Affine2D().rotate_deg(angle) + ax.transData
        slot_outer.set_transform(t)
        ax.add_patch(slot_outer)
        
        # Inner slot
        slot_inner = Rectangle((-1.5, -8), 3, 2, facecolor='white', edgecolor='blue', linewidth=1)
        slot_inner.set_transform(t)
        ax.add_patch(slot_inner)
    
    # Center bore
    center = Circle((0, 0), 2.5, facecolor='white', edgecolor='red', linewidth=2)
    ax.add_patch(center)
    ax.text(0, 0, 'Ø5', ha='center', va='center', fontsize=8, fontweight='bold')
    
    ax.text(0, -14, 'Ix = Iy = 7023.91 mm⁴', ha='center', fontsize=8, fontweight='bold')
    
    # 2. Profil 3030
    ax = axes[0, 1]
    ax.set_xlim(-18, 18)
    ax.set_ylim(-18, 18)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 3030 (30×30mm)\n4 Slot, Center Ø12mm', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Main square
    square = Rectangle((-15, -15), 30, 30, facecolor='lightgreen', edgecolor='green', 
                      linewidth=2, alpha=0.6)
    ax.add_patch(square)
    
    # T-slots (4 sisi, larger)
    for i in range(4):
        angle = i * 90
        # Outer slot
        slot_outer = Rectangle((-4, -15), 8, 3, facecolor='white', edgecolor='green', linewidth=1)
        t = plt.matplotlib.transforms.Affine2D().rotate_deg(angle) + ax.transData
        slot_outer.set_transform(t)
        ax.add_patch(slot_outer)
        
        # Inner slot
        slot_inner = Rectangle((-2, -12), 4, 3, facecolor='white', edgecolor='green', linewidth=1)
        slot_inner.set_transform(t)
        ax.add_patch(slot_inner)
    
    # Center bore (larger)
    center = Circle((0, 0), 6, facecolor='white', edgecolor='red', linewidth=2)
    ax.add_patch(center)
    ax.text(0, 0, 'Ø12', ha='center', va='center', fontsize=8, fontweight='bold')
    
    ax.text(0, -20, 'Thickness: ~2mm walls', ha='center', fontsize=8, fontweight='bold')
    
    # 3. Profil 4040
    ax = axes[1, 0]
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 4040 (40×40mm)\n4 Slot, Large Center Bore', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Main square
    square = Rectangle((-20, -20), 40, 40, facecolor='lightyellow', edgecolor='orange', 
                      linewidth=2, alpha=0.6)
    ax.add_patch(square)
    
    # T-slots (4 sisi, industrial size)
    for i in range(4):
        angle = i * 90
        # Outer slot
        slot_outer = Rectangle((-4, -20), 8, 4, facecolor='white', edgecolor='orange', linewidth=1)
        t = plt.matplotlib.transforms.Affine2D().rotate_deg(angle) + ax.transData
        slot_outer.set_transform(t)
        ax.add_patch(slot_outer)
        
        # Inner slot (deeper)
        slot_inner = Rectangle((-3, -16), 6, 4, facecolor='white', edgecolor='orange', linewidth=1)
        slot_inner.set_transform(t)
        ax.add_patch(slot_inner)
    
    # Center structure (cross-shaped)
    center_v = Rectangle((-2, -15), 4, 30, facecolor='lightyellow', edgecolor='orange', linewidth=1)
    center_h = Rectangle((-15, -2), 30, 4, facecolor='lightyellow', edgecolor='orange', linewidth=1)
    ax.add_patch(center_v)
    ax.add_patch(center_h)
    
    ax.text(0, -27, '~10mm depth slots', ha='center', fontsize=8, fontweight='bold')
    
    # 4. Profil 2040
    ax = axes[1, 1]
    ax.set_xlim(-25, 25)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 2040 (20×40mm)\n6 Slot, 2 Center Bores', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Main rectangle
    rect = Rectangle((-20, -10), 40, 20, facecolor='lightcoral', edgecolor='red', 
                    linewidth=2, alpha=0.6)
    ax.add_patch(rect)
    
    # T-slots on short sides (20mm)
    for side in [-1, 1]:
        x_pos = side * 20
        slot = Rectangle((x_pos - side*2, -3), side*4, 6, facecolor='white', edgecolor='red', linewidth=1)
        ax.add_patch(slot)
    
    # T-slots on long sides (40mm) - 2 each side
    for side in [-1, 1]:
        y_pos = side * 10
        for slot_x in [-10, 10]:
            slot = Rectangle((slot_x - 3, y_pos - side*2), 6, side*4, 
                           facecolor='white', edgecolor='red', linewidth=1)
            ax.add_patch(slot)
    
    # 2 Center bores
    center1 = Circle((-10, 0), 2.5, facecolor='white', edgecolor='darkred', linewidth=2)
    center2 = Circle((10, 0), 2.5, facecolor='white', edgecolor='darkred', linewidth=2)
    ax.add_patch(center1)
    ax.add_patch(center2)
    ax.text(-10, 0, 'Ø5', ha='center', va='center', fontsize=7, fontweight='bold')
    ax.text(10, 0, 'Ø5', ha='center', va='center', fontsize=7, fontweight='bold')
    
    ax.text(0, -17, '6 slots total (2+2+2)', ha='center', fontsize=8, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/08_profil_aluminium_sketches.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 08_profil_aluminium_sketches.png")
    plt.close()

def sketching_tutorial_steps():
    """Tutorial step-by-step sketching workflow"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('TUTORIAL SKETCHING WORKFLOW - MODUL 2\n(Step-by-Step Process)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    steps = [
        ('STEP 1: ENTITAS\n(Draw Geometry)', 'blue', 'lightblue'),
        ('STEP 2: CONSTRAINTS\n(Add Relations)', 'green', 'lightgreen'),
        ('STEP 3: DIMENSIONS\n(Size Control)', 'orange', 'lightyellow'),
        ('STEP 4: CHECK STATUS\n(Fully Defined?)', 'purple', 'plum'),
        ('STEP 5: TOOLS\n(Trim, Offset, etc.)', 'cyan', 'lightcyan'),
        ('STEP 6: FINAL CHECK\n(Ready for 3D)', 'red', 'lightpink'),
    ]
    
    for ax, (title, edge_color, face_color) in zip(axes.flat, steps):
        ax.set_xlim(-5, 15)
        ax.set_ylim(-3, 12)
        ax.set_aspect('equal')
        ax.set_title(title, fontweight='bold', fontsize=11, color=edge_color)
        ax.axis('off')
        
        step_num = steps.index((title, edge_color, face_color))
        
        if step_num == 0:  # ENTITAS
            # Draw basic shapes
            ax.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], color=edge_color, linewidth=3)
            circle = Circle((5, 5), 1.5, facecolor='none', edgecolor=edge_color, linewidth=3)
            ax.add_patch(circle)
            ax.text(5, 0, 'Lines, Circles, Arcs', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 1:  # CONSTRAINTS
            # Draw with constraint symbols
            ax.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], color=edge_color, linewidth=3)
            # Add constraint symbols
            ax.text(1, 5, 'V', ha='center', va='center', fontsize=12, fontweight='bold', 
                   bbox=dict(boxstyle='circle', facecolor=face_color))
            ax.text(5, 1, 'H', ha='center', va='center', fontsize=12, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor=face_color))
            ax.text(5, 0, 'Horizontal, Vertical', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 2:  # DIMENSIONS
            # Draw with dimensions
            ax.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], color='black', linewidth=2)
            # Dimension lines
            ax.annotate('', xy=(8, 9.5), xytext=(2, 9.5),
                       arrowprops=dict(arrowstyle='<->', lw=1.5, color=edge_color))
            ax.text(5, 10, '60', ha='center', fontsize=10, fontweight='bold', color=edge_color)
            ax.text(5, 0, 'Size & Position', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 3:  # CHECK STATUS
            # Show status colors
            ax.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], color='black', linewidth=3)  # Fully defined
            ax.text(1, 6, 'BLACK\n(Good)', ha='center', va='center', fontsize=8, fontweight='bold',
                   color='black')
            ax.text(9, 4, 'BLUE\n(Under)', ha='center', va='center', fontsize=8, fontweight='bold',
                   color='blue')
            ax.text(5, 0, 'Color = Status', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 4:  # TOOLS
            # Show trimmed/modified shape
            ax.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], color=edge_color, linewidth=2)
            # Add fillet
            arc = patches.Arc((7.5, 7.5), 1, 1, angle=0, theta1=180, theta2=270, 
                             color=edge_color, linewidth=3)
            ax.add_patch(arc)
            ax.text(5, 0, 'Fillet, Trim, Offset', ha='center', fontsize=9, fontweight='bold')
        
        elif step_num == 5:  # FINAL
            # Show complete sketch
            ax.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], color='black', linewidth=3)
            ax.text(5, 5, '✓', ha='center', va='center', fontsize=24, fontweight='bold', color='green')
            ax.text(5, 0, 'Ready for Extrude!', ha='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/09_sketching_tutorial.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 09_sketching_tutorial.png")
    plt.close()

# ============================================================================
# MODUL 3 ADDITIONAL ILLUSTRATIONS  
# ============================================================================

def clamp_assembly_parts():
    """Project Clamp Assembly Parts visualization"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('PROJECT CLAMP ASSEMBLY PARTS - MODUL 3\n(5 Parts dengan Feature Berbeda)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    # Helper function for isometric
    def to_isometric(x, y, z):
        iso_x = x - z
        iso_y = y + 0.5 * z
        return iso_x, iso_y
    
    def draw_iso_box(ax, w, h, d, x=0, y=0, color='cyan', alpha=0.5):
        corners_3d = [
            [x, y, 0], [x+w, y, 0], [x+w, y+h, 0], [x, y+h, 0],  # bottom
            [x, y, d], [x+w, y, d], [x+w, y+h, d], [x, y+h, d],  # top
        ]
        iso_corners = [to_isometric(*c) for c in corners_3d]
        
        # Draw faces
        top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                     facecolor=color, alpha=alpha, edgecolor='black')
        front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                       facecolor=color, alpha=alpha*0.8, edgecolor='black')
        right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                       facecolor=color, alpha=alpha*0.6, edgecolor='black')
        ax.add_patch(top)
        ax.add_patch(front)
        ax.add_patch(right)
        return iso_corners
    
    # 1. Base Clamp
    ax = axes[0, 0]
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 8)
    ax.set_aspect('equal')
    ax.set_title('1. BASE CLAMP\n(Extrude + Shell + Pattern)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Base plate
    draw_iso_box(ax, 10, 6, 1, color='lightblue')
    # Raised boss
    draw_iso_box(ax, 3, 3, 1.5, x=3.5, y=1.5, color='blue', alpha=0.7)
    
    # Mounting holes (simplified circles)
    hole_pos = [(1, 1), (9, 1), (1, 5), (9, 5)]
    for x, y in hole_pos:
        iso_x, iso_y = to_isometric(x, y, 1)
        hole = Circle((iso_x, iso_y), 0.3, facecolor='white', edgecolor='red', linewidth=1.5)
        ax.add_patch(hole)
    
    ax.text(5, -1, '100×60×10mm\n4×Ø8 holes', ha='center', fontsize=8, fontweight='bold')
    
    # 2. Clamp Arm
    ax = axes[0, 1]
    ax.set_xlim(-2, 14)
    ax.set_ylim(-2, 6)
    ax.set_aspect('equal')
    ax.set_title('2. CLAMP ARM\n(Extrude + Fillet + Chamfer)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Main arm
    draw_iso_box(ax, 12, 2, 1, color='lightgreen')
    
    # Pivot hole
    iso_x, iso_y = to_isometric(1, 1, 1)
    pivot = Circle((iso_x, iso_y), 0.5, facecolor='white', edgecolor='blue', linewidth=2)
    ax.add_patch(pivot)
    
    # Adjustment slot
    slot = patches.Rectangle((to_isometric(9, 0.5, 1)), 2, 0.5, 
                           facecolor='white', edgecolor='orange', linewidth=2)
    ax.add_patch(slot)
    
    ax.text(6, -1, '120×20×10mm\nØ12 pivot, 30×8 slot', ha='center', fontsize=8, fontweight='bold')
    
    # 3. Pressure Pad
    ax = axes[0, 2]
    ax.set_xlim(-3, 7)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')
    ax.set_title('3. PRESSURE PAD\n(Revolve)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Cylinder (isometric)
    draw_iso_box(ax, 4, 4, 2, x=1, y=1, color='yellow', alpha=0.6)
    
    # Make it look cylindrical with ellipse
    cylinder_top = patches.Ellipse(to_isometric(3, 3, 2), 4, 2, 
                                 facecolor='yellow', edgecolor='black', alpha=0.8)
    ax.add_patch(cylinder_top)
    
    # M6 hole
    hole_pos = to_isometric(3, 3, 2)
    hole = Circle(hole_pos, 0.2, facecolor='white', edgecolor='red', linewidth=2)
    ax.add_patch(hole)
    
    ax.text(3, -0.5, 'Ø20×10mm\nM6 threaded', ha='center', fontsize=8, fontweight='bold')
    
    # 4. Pivot Pin
    ax = axes[1, 0]
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.set_title('4. PIVOT PIN\n(Revolve + Chamfer)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Pin as cylinder
    draw_iso_box(ax, 6, 1.2, 1.2, x=1, y=1, color='lightcoral')
    
    # Chamfer indication
    ax.plot([1, 1.5], [1, 1.5], 'purple', linewidth=3)
    ax.plot([7, 6.5], [1, 1.5], 'purple', linewidth=3)
    
    # Groove
    groove = patches.Rectangle((to_isometric(5.5, 0.9, 0.6)), 0.3, 1.4, 
                             facecolor='white', edgecolor='gray', linewidth=1)
    ax.add_patch(groove)
    
    ax.text(4, -0.5, 'Ø12×25mm\nChamfer + Groove', ha='center', fontsize=8, fontweight='bold')
    
    # 5. Knob
    ax = axes[1, 1]
    ax.set_xlim(-2, 8)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.set_title('5. KNOB\n(Revolve + Pattern)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Knob cylinder
    draw_iso_box(ax, 5, 5, 2, x=1, y=0, color='orange', alpha=0.7)
    
    # Knurling pattern (simplified lines)
    for i in range(8):
        angle = i * 45
        x = 3.5 + 2 * np.cos(np.radians(angle))
        y = 2.5 + 1 * np.sin(np.radians(angle))
        ax.plot([x-0.3, x+0.3], [y-0.2, y+0.2], 'black', linewidth=1)
    
    ax.text(3.5, -0.5, 'Ø25mm knob\nKnurling pattern', ha='center', fontsize=8, fontweight='bold')
    
    # 6. Assembly view
    ax = axes[1, 2]
    ax.set_xlim(-2, 14)
    ax.set_ylim(-2, 8)
    ax.set_aspect('equal')
    ax.set_title('ASSEMBLY VIEW\n(All Parts Together)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Simplified assembly
    # Base
    draw_iso_box(ax, 8, 4, 1, x=2, y=2, color='lightblue', alpha=0.5)
    # Arm
    draw_iso_box(ax, 10, 1.5, 1, x=1, y=4, color='lightgreen', alpha=0.5)
    # Pad
    draw_iso_box(ax, 2, 2, 1.5, x=9, y=3, color='yellow', alpha=0.6)
    
    ax.text(6, 0, 'Complete Clamp\n(5 parts)', ha='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/07_clamp_assembly_parts.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 07_clamp_assembly_parts.png")
    plt.close()

def profil_aluminium_3d():
    """Profil Aluminium 3D dari 2D sketch"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('PROFIL ALUMINIUM 3D - MODUL 3\n(Extrude dari Sketch 2D Modul 2)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    def to_isometric(x, y, z):
        iso_x = x - z
        iso_y = y + 0.5 * z
        return iso_x, iso_y
    
    # 1. Profil 2020 - 200mm
    ax = axes[0, 0]
    ax.set_xlim(-5, 25)
    ax.set_ylim(-3, 15)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 2020 → 200mm\n(Small Industrial)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw 3D extrusion
    # Main body
    corners = [
        [0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0],  # front face
        [0, 0, 20], [4, 0, 20], [4, 4, 20], [0, 4, 20],  # back face
    ]
    iso_corners = [to_isometric(*c) for c in corners]
    
    # Draw faces
    top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                 facecolor='lightblue', alpha=0.6, edgecolor='blue')
    front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                   facecolor='lightblue', alpha=0.5, edgecolor='blue')
    right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                   facecolor='lightblue', alpha=0.4, edgecolor='blue')
    ax.add_patch(top)
    ax.add_patch(front)
    ax.add_patch(right)
    
    # T-slots visible on top
    for i in range(2):
        slot_y = 0.5 + i * 3
        slot = patches.Rectangle((to_isometric(1, slot_y, 20)), 2, 0.5, 
                               facecolor='white', edgecolor='blue', linewidth=1)
        ax.add_patch(slot)
    
    ax.text(12, 1, '20×20×200mm\nMaterial: Al 6063-T5', ha='center', fontsize=9, fontweight='bold')
    
    # 2. Profil 3030 - 300mm
    ax = axes[0, 1]
    ax.set_xlim(-5, 30)
    ax.set_ylim(-3, 18)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 3030 → 300mm\n(Medium Duty)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw larger profile
    corners = [
        [0, 0, 0], [6, 0, 0], [6, 6, 0], [0, 6, 0],  # front
        [0, 0, 24], [6, 0, 24], [6, 6, 24], [0, 6, 24],  # back
    ]
    iso_corners = [to_isometric(*c) for c in corners]
    
    top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                 facecolor='lightgreen', alpha=0.6, edgecolor='green')
    front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                   facecolor='lightgreen', alpha=0.5, edgecolor='green')
    right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                   facecolor='lightgreen', alpha=0.4, edgecolor='green')
    ax.add_patch(top)
    ax.add_patch(front)
    ax.add_patch(right)
    
    # Center bore
    center_pos = to_isometric(3, 3, 24)
    center = Circle(center_pos, 0.6, facecolor='white', edgecolor='red', linewidth=2)
    ax.add_patch(center)
    
    ax.text(15, 1, '30×30×300mm\nCenter Ø12mm', ha='center', fontsize=9, fontweight='bold')
    
    # 3. Profil 4040 - 400mm
    ax = axes[1, 0]
    ax.set_xlim(-5, 35)
    ax.set_ylim(-3, 20)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 4040 → 400mm\n(Heavy Duty)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw industrial profile
    corners = [
        [0, 0, 0], [8, 0, 0], [8, 8, 0], [0, 8, 0],  # front
        [0, 0, 28], [8, 0, 28], [8, 8, 28], [0, 8, 28],  # back
    ]
    iso_corners = [to_isometric(*c) for c in corners]
    
    top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                 facecolor='lightyellow', alpha=0.6, edgecolor='orange')
    front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                   facecolor='lightyellow', alpha=0.5, edgecolor='orange')
    right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                   facecolor='lightyellow', alpha=0.4, edgecolor='orange')
    ax.add_patch(top)
    ax.add_patch(front)
    ax.add_patch(right)
    
    # Cross structure visible
    cross_v = patches.Rectangle((to_isometric(3.5, 0, 28)), 1, 8, 
                              facecolor='lightyellow', edgecolor='orange', linewidth=1, alpha=0.8)
    cross_h = patches.Rectangle((to_isometric(0, 3.5, 28)), 8, 1, 
                              facecolor='lightyellow', edgecolor='orange', linewidth=1, alpha=0.8)
    ax.add_patch(cross_v)
    ax.add_patch(cross_h)
    
    ax.text(18, 1, '40×40×400mm\nIndustrial Grade', ha='center', fontsize=9, fontweight='bold')
    
    # 4. Profil 4080 - 500mm
    ax = axes[1, 1]
    ax.set_xlim(-5, 40)
    ax.set_ylim(-3, 22)
    ax.set_aspect('equal')
    ax.set_title('PROFIL 4080 → 500mm\n(Extra Heavy)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Draw rectangular profile
    corners = [
        [0, 0, 0], [12, 0, 0], [12, 6, 0], [0, 6, 0],  # front
        [0, 0, 32], [12, 0, 32], [12, 6, 32], [0, 6, 32],  # back
    ]
    iso_corners = [to_isometric(*c) for c in corners]
    
    top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                 facecolor='lightcoral', alpha=0.6, edgecolor='red')
    front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                   facecolor='lightcoral', alpha=0.5, edgecolor='red')
    right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                   facecolor='lightcoral', alpha=0.4, edgecolor='red')
    ax.add_patch(top)
    ax.add_patch(front)
    ax.add_patch(right)
    
    # 2 center bores
    center1_pos = to_isometric(3, 3, 32)
    center2_pos = to_isometric(9, 3, 32)
    center1 = Circle(center1_pos, 0.4, facecolor='white', edgecolor='darkred', linewidth=2)
    center2 = Circle(center2_pos, 0.4, facecolor='white', edgecolor='darkred', linewidth=2)
    ax.add_patch(center1)
    ax.add_patch(center2)
    
    ax.text(20, 1, '40×80×500mm\n2×Ø5 bores', ha='center', fontsize=9, fontweight='bold')
    
    # Add workflow notes
    fig.text(0.5, 0.02, 'WORKFLOW: Import 2D Sketch → Extrude Boss/Base → Set Length → Add Chamfer → Assign Material', 
            ha='center', fontsize=10, fontweight='bold', style='italic')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/08_profil_aluminium_3d.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 08_profil_aluminium_3d.png")
    plt.close()

def feature_tutorial_complete():
    """Complete 3D feature tutorial"""
    fig, axes = plt.subplots(3, 3, figsize=(18, 15))
    fig.suptitle('COMPLETE 3D FEATURE TUTORIAL - MODUL 3\n(From Sketch to Finished Part)', 
                fontsize=14, fontweight='bold', y=0.97)
    
    def to_isometric(x, y, z):
        iso_x = x - z
        iso_y = y + 0.5 * z
        return iso_x, iso_y
    
    def draw_simple_box(ax, w, h, d, color='cyan', alpha=0.5):
        corners = [
            [0, 0, 0], [w, 0, 0], [w, h, 0], [0, h, 0],  # bottom
            [0, 0, d], [w, 0, d], [w, h, d], [0, h, d],  # top
        ]
        iso_corners = [to_isometric(*c) for c in corners]
        
        top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                     facecolor=color, alpha=alpha, edgecolor='black', linewidth=1)
        front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                       facecolor=color, alpha=alpha*0.8, edgecolor='black', linewidth=1)
        right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                       facecolor=color, alpha=alpha*0.6, edgecolor='black', linewidth=1)
        ax.add_patch(top)
        ax.add_patch(front)
        ax.add_patch(right)
        return iso_corners
    
    steps = [
        ('1. PLANE SELECT\n(Front/Top/Right)', 'blue'),
        ('2. SKETCH 2D\n(Rectangle)', 'green'),
        ('3. EXTRUDE BOSS\n(Base Feature)', 'cyan'),
        ('4. NEW SKETCH\n(on Face)', 'orange'),
        ('5. EXTRUDE CUT\n(Remove Material)', 'red'),
        ('6. FILLET EDGES\n(Round Corners)', 'purple'),
        ('7. CHAMFER\n(Bevel Edge)', 'brown'),
        ('8. PATTERN\n(Repeat Feature)', 'magenta'),
        ('9. FINAL PART\n(Complete)', 'darkgreen'),
    ]
    
    for i, (ax, (title, color)) in enumerate(zip(axes.flat, steps)):
        ax.set_xlim(-2, 8)
        ax.set_ylim(-2, 6)
        ax.set_aspect('equal')
        ax.set_title(title, fontweight='bold', fontsize=10, color=color)
        ax.axis('off')
        
        if i == 0:  # Plane select
            # Draw coordinate system
            ax.plot([0, 3], [2, 2], 'r-', linewidth=3, label='X')
            ax.plot([0, 0], [2, 5], 'g-', linewidth=3, label='Y')
            ax.plot([0, -1.5], [2, 3], 'b-', linewidth=3, label='Z')
            ax.text(1.5, 1.5, 'X', fontsize=12, fontweight='bold', color='red')
            ax.text(-0.5, 3.5, 'Y', fontsize=12, fontweight='bold', color='green')
            ax.text(-1.8, 3.5, 'Z', fontsize=12, fontweight='bold', color='blue')
            ax.text(0, 0.5, 'Select Plane', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 1:  # Sketch 2D
            # Draw rectangle sketch
            ax.plot([1, 5, 5, 1, 1], [1, 1, 4, 4, 1], color='blue', linewidth=3)
            ax.plot([1, 5, 5, 1], [1, 1, 4, 4], 'o', color='blue', markersize=4)
            ax.text(3, 0, 'Rectangle\n40×30mm', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 2:  # Extrude
            draw_simple_box(ax, 4, 3, 2, color='cyan', alpha=0.6)
            ax.text(2, 0, 'Extrude 20mm', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 3:  # New sketch
            draw_simple_box(ax, 4, 3, 2, color='lightgray', alpha=0.3)
            # Circle on top
            circle_pos = to_isometric(2, 1.5, 2)
            circle = Circle(circle_pos, 0.5, facecolor='none', edgecolor='blue', linewidth=3)
            ax.add_patch(circle)
            ax.text(2, 0, 'Circle on\nTop Face', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 4:  # Cut
            draw_simple_box(ax, 4, 3, 2, color='lightgray', alpha=0.3)
            # Hole
            hole_pos = to_isometric(2, 1.5, 2)
            hole = Circle(hole_pos, 0.5, facecolor='white', edgecolor='red', linewidth=2)
            ax.add_patch(hole)
            ax.text(2, 0, 'Through All\nHole', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 5:  # Fillet
            draw_simple_box(ax, 4, 3, 2, color='lightgreen', alpha=0.5)
            # Rounded edge indication
            arc = patches.Arc(to_isometric(4, 3, 2), 0.8, 0.4, angle=0, theta1=0, theta2=90, 
                             color='green', linewidth=3)
            ax.add_patch(arc)
            ax.text(2, 0, 'Fillet R2\nSmooth Edge', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 6:  # Chamfer
            draw_simple_box(ax, 4, 3, 2, color='lightyellow', alpha=0.5)
            # Chamfer line
            ax.plot([to_isometric(4, 0, 2)[0]-0.3, to_isometric(4, 0, 2)[0]], 
                   [to_isometric(4, 0, 2)[1]+0.3, to_isometric(4, 0, 2)[1]], 
                   color='brown', linewidth=3)
            ax.text(2, 0, 'Chamfer 1×45°\nBevel Edge', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 7:  # Pattern
            # Multiple boxes
            for j in range(2):
                for k in range(2):
                    corners = [
                        [j*2.5, k*2, 0], [j*2.5+1.5, k*2, 0], [j*2.5+1.5, k*2+1, 0], [j*2.5, k*2+1, 0],
                        [j*2.5, k*2, 1], [j*2.5+1.5, k*2, 1], [j*2.5+1.5, k*2+1, 1], [j*2.5, k*2+1, 1],
                    ]
                    iso_corners = [to_isometric(*c) for c in corners]
                    
                    top = Polygon([iso_corners[4], iso_corners[5], iso_corners[6], iso_corners[7]], 
                                 facecolor='lightpink', alpha=0.4, edgecolor='black', linewidth=1)
                    front = Polygon([iso_corners[0], iso_corners[1], iso_corners[5], iso_corners[4]], 
                                   facecolor='lightpink', alpha=0.3, edgecolor='black', linewidth=1)
                    right = Polygon([iso_corners[1], iso_corners[2], iso_corners[6], iso_corners[5]], 
                                   facecolor='lightpink', alpha=0.2, edgecolor='black', linewidth=1)
                    ax.add_patch(top)
                    ax.add_patch(front)
                    ax.add_patch(right)
            ax.text(2, -0.5, 'Linear Pattern\n2×2 Array', ha='center', fontsize=8, fontweight='bold')
        
        elif i == 8:  # Final
            draw_simple_box(ax, 4, 3, 2, color='lightcoral', alpha=0.6)
            # Complete with all features
            ax.text(2, 4.5, '✓ COMPLETE', ha='center', fontsize=10, fontweight='bold', color='green')
            ax.text(2, 0, 'Ready for\nAssembly!', ha='center', fontsize=8, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/09_feature_tutorial_complete.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 09_feature_tutorial_complete.png")
    plt.close()

# ============================================================================
# MAIN FUNCTION
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*80)
    print("GENERATING ADDITIONAL ILLUSTRATIONS FOR MODUL 2 & 3")
    print("Membantu praktikan menyelesaikan project dan memahami konsep")
    print("="*80)
    
    try:
        # MODUL 2 Additional Illustrations
        print("\n📐 MODUL 2 ADDITIONAL ILLUSTRATIONS:")
        panel_kontrol_layout()
        profil_aluminium_sketches()
        sketching_tutorial_steps()
        
        # MODUL 3 Additional Illustrations  
        print("\n🔧 MODUL 3 ADDITIONAL ILLUSTRATIONS:")
        clamp_assembly_parts()
        profil_aluminium_3d()
        feature_tutorial_complete()
        
        print("\n" + "="*80)
        print("🎉 SEMUA ILUSTRASI TAMBAHAN BERHASIL DIBUAT!")
        print("="*80)
        
        print("\n📂 MODUL 2 - Total 9 gambar:")
        print("  01-05: Konsep dasar sketching")
        print("  06: (reserved)")
        print("  07: Project Panel Kontrol layout")
        print("  08: Profil Aluminium sketches")
        print("  09: Sketching tutorial workflow")
        
        print("\n📂 MODUL 3 - Total 9 gambar:")
        print("  01-06: Feature dasar")
        print("  07: Clamp Assembly parts")
        print("  08: Profil Aluminium 3D")
        print("  09: Complete feature tutorial")
        
        print("\n🎯 Total: 18 ilustrasi lengkap untuk membantu praktikan!")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()