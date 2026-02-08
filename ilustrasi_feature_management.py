"""
ILUSTRASI FEATURE MANAGEMENT & ASSEMBLY PREP - MODUL 3
Advanced concepts untuk 3D modeling workflow
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Rectangle
import warnings
warnings.filterwarnings('ignore')

def feature_tree_management():
    """Feature tree dan order management"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 10))
    fig.suptitle('FEATURE TREE MANAGEMENT - MODUL 3\n(Order & Dependencies)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    # 1. Feature Tree Structure
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_title('FEATURE TREE STRUCTURE\n(SolidWorks Feature Manager)', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    # Tree structure
    features = [
        ('📄 Part1.sldprt', 0, 'darkblue', 'white'),
        ('📐 Front Plane', 0.5, 'gray', 'white'),
        ('📐 Top Plane', 0.5, 'gray', 'white'),
        ('📐 Right Plane', 0.5, 'gray', 'white'),
        ('🟦 Sketch1', 1, 'blue', 'lightblue'),
        ('🔧 Extrude1 (Base)', 1, 'green', 'lightgreen'),
        ('🟦 Sketch2', 1, 'blue', 'lightblue'),
        ('🔧 Extrude-Cut1', 1, 'red', 'lightcoral'),
        ('🔧 Fillet1', 1, 'purple', 'plum'),
        ('🔧 Linear Pattern1', 1, 'orange', 'lightyellow'),
        ('📁 Material <Al 6063>', 0.5, 'brown', 'wheat'),
    ]
    
    y_start = 11
    for i, (name, indent, color, bg_color) in enumerate(features):
        y = y_start - i * 0.8
        x = 0.5 + indent
        
        # Tree line
        if indent > 0:
            ax.plot([0.3, x-0.1], [y, y], 'k-', linewidth=1, alpha=0.5)
        
        # Feature box
        feature_box = FancyBboxPatch((x, y-0.25), 8-indent, 0.5, 
                                    boxstyle="round,pad=0.05",
                                    edgecolor=color, facecolor=bg_color, 
                                    linewidth=1.5, alpha=0.7)
        ax.add_patch(feature_box)
        
        # Feature text
        ax.text(x+0.2, y, name, va='center', fontsize=10, fontweight='bold' if 'Part1' in name else 'normal')
        
        # Order number
        if 'Sketch' in name or 'Extrude' in name or 'Fillet' in name or 'Pattern' in name:
            order = ['Sketch1', 'Extrude1', 'Sketch2', 'Extrude-Cut1', 'Fillet1', 'Linear Pattern1'].index(name.split(' ')[0]) + 1 if name.split(' ')[0] in ['Sketch1', 'Extrude1', 'Sketch2', 'Extrude-Cut1', 'Fillet1', 'Linear'] else 0
            if order > 0:
                order_circle = Circle((x+7.5-indent, y), 0.15, facecolor='red', edgecolor='darkred')
                ax.add_patch(order_circle)
                ax.text(x+7.5-indent, y, str(order), ha='center', va='center', 
                       fontsize=8, fontweight='bold', color='white')
    
    # Dependencies arrow
    ax.annotate('DEPENDS ON', xy=(9, 6), xytext=(9, 8),
               arrowprops=dict(arrowstyle='->', lw=2, color='red'),
               fontsize=10, fontweight='bold', color='red', ha='center')
    
    ax.text(5, 0.5, 'Order matters! Base → Cut → Fillet → Pattern', 
           ha='center', fontsize=11, fontweight='bold', color='darkgreen',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # 2. Feature Editing Rules
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_title('FEATURE EDITING RULES\n(Do\'s and Don\'ts)', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    rules = [
        ('✓ GOOD PRACTICES', 'green', 'lightgreen'),
        ('• Edit sketch before feature', 'darkgreen', 'white'),
        ('• Keep features simple', 'darkgreen', 'white'),
        ('• Use descriptive names', 'darkgreen', 'white'),
        ('• Group related features', 'darkgreen', 'white'),
        ('• Save often', 'darkgreen', 'white'),
        ('✗ BAD PRACTICES', 'red', 'lightcoral'),
        ('• Delete base features', 'darkred', 'white'),
        ('• Complex single features', 'darkred', 'white'),
        ('• Random feature order', 'darkred', 'white'),
        ('• Too many fillets early', 'darkred', 'white'),
        ('• Ignore error warnings', 'darkred', 'white'),
    ]
    
    y_pos = 11
    for rule, color, bg_color in rules:
        if '✓' in rule or '✗' in rule:
            # Header
            header_box = FancyBboxPatch((0.5, y_pos-0.3), 9, 0.6, 
                                       boxstyle="round,pad=0.1",
                                       edgecolor=color, facecolor=bg_color, 
                                       linewidth=2, alpha=0.8)
            ax.add_patch(header_box)
            ax.text(5, y_pos, rule, ha='center', va='center', fontsize=12, fontweight='bold', color=color)
            y_pos -= 1
        else:
            # Rule item
            ax.text(1, y_pos, rule, va='center', fontsize=10, color=color)
            y_pos -= 0.7
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/10_feature_tree_management.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 10_feature_tree_management.png")
    plt.close()

def assembly_preparation():
    """Persiapan part untuk assembly"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('ASSEMBLY PREPARATION - MODUL 3\n(Persiapan Part untuk Assembly)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    def to_isometric(x, y, z):
        iso_x = x - z
        iso_y = y + 0.5 * z
        return iso_x, iso_y
    
    def draw_part(ax, w, h, d, x=0, y=0, color='cyan', alpha=0.5, holes=None):
        corners = [
            [x, y, 0], [x+w, y, 0], [x+w, y+h, 0], [x, y+h, 0],
            [x, y, d], [x+w, y, d], [x+w, y+h, d], [x, y+h, d],
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
        
        # Add holes if specified
        if holes:
            for hx, hy in holes:
                hole_pos = to_isometric(x+hx, y+hy, d)
                hole = Circle(hole_pos, 0.3, facecolor='white', edgecolor='red', linewidth=1.5)
                ax.add_patch(hole)
        
        return iso_corners
    
    # 1. Proper Dimensions
    ax = axes[0, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('1. PROPER DIMENSIONS\n(Standard Sizes)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Standard part
    draw_part(ax, 6, 4, 2, color='lightblue', alpha=0.6)
    
    # Dimension callouts
    ax.text(3, -0.5, '40 x 60 x 20mm\n(Standard sizes)', ha='center', fontsize=9, 
           fontweight='bold', color='blue')
    ax.text(8, 4, 'Use standard\nmaterials &\nsizes when\npossible', ha='left', 
           fontsize=9, fontweight='bold', color='darkgreen',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # 2. Mounting Features
    ax = axes[0, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('2. MOUNTING FEATURES\n(Holes & Fasteners)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Part with mounting holes
    holes = [(1, 1), (5, 1), (1, 3), (5, 3)]
    draw_part(ax, 6, 4, 2, color='lightgreen', alpha=0.6, holes=holes)
    
    # Hole annotations
    for i, (hx, hy) in enumerate(holes):
        hole_pos = to_isometric(hx+1, hy+1, 2)
        if i == 0:  # Only annotate first hole
            ax.text(hole_pos[0]+1, hole_pos[1], 'M6 holes\nfor bolts', ha='left', fontsize=9,
                   fontweight='bold', color='red',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    ax.text(3, -0.5, 'Standard hole pattern\n(Compatible with T-slots)', ha='center', 
           fontsize=9, fontweight='bold', color='green')
    
    # 3. Material Assignment
    ax = axes[1, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.set_title('3. MATERIAL ASSIGNMENT\n(Properties & Appearance)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # Different materials
    materials = [
        (1, 1, 'Steel', 'lightgray', 'gray'),
        (4, 1, 'Aluminum', 'lightblue', 'blue'),
        (1, 4, 'Plastic', 'lightyellow', 'orange'),
        (4, 4, 'Brass', 'lightcoral', 'brown'),
    ]
    
    for x, y, mat, color, edge_color in materials:
        draw_part(ax, 1.5, 1.5, 1, x=x, y=y, color=color, alpha=0.7)
        ax.text(x+0.75, y-0.3, mat, ha='center', fontsize=8, fontweight='bold', color=edge_color)
    
    ax.text(3, 0, 'Assign materials for:\n• Mass properties\n• Appearance\n• Analysis', 
           ha='center', fontsize=9, fontweight='bold', color='darkblue')
    
    # 4. File Naming Convention
    ax = axes[1, 1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title('4. FILE NAMING\n(Convention & Organization)', fontweight='bold', fontsize=11)
    ax.axis('off')
    
    # File naming examples
    file_names = [
        ('✓ GOOD:', 'green'),
        ('M03_Base_Clamp.sldprt', 'darkgreen'),
        ('M03_Arm_120x20.sldprt', 'darkgreen'),  
        ('M03_Pin_M6x25.sldprt', 'darkgreen'),
        ('M03_Profil2020_200mm.sldprt', 'darkgreen'),
        ('✗ BAD:', 'red'),
        ('Part1.sldprt', 'darkred'),
        ('untitled.sldprt', 'darkred'),
        ('asdf.sldprt', 'darkred'),
        ('NewPart123.sldprt', 'darkred'),
    ]
    
    y_pos = 7.5
    for name, color in file_names:
        if '✓' in name or '✗' in name:
            ax.text(1, y_pos, name, fontsize=12, fontweight='bold', color=color)
            y_pos -= 0.5
        else:
            ax.text(1.5, y_pos, name, fontsize=10, color=color, family='monospace')
            y_pos -= 0.4
    
    # Naming rules
    rules_box = FancyBboxPatch((0.5, 0.5), 9, 2, boxstyle="round,pad=0.2",
                              edgecolor='blue', facecolor='lightblue', alpha=0.7)
    ax.add_patch(rules_box)
    ax.text(5, 1.5, 'NAMING RULES:\n• Module prefix (M03_)\n• Descriptive name\n• Key dimensions\n• Standard extension', 
           ha='center', va='center', fontsize=10, fontweight='bold', color='darkblue')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/11_assembly_preparation.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 11_assembly_preparation.png")
    plt.close()

def advanced_features_preview():
    """Preview advanced features untuk modul selanjutnya"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('ADVANCED FEATURES PREVIEW - MODUL 3\n(Persiapan untuk Modul 4-7)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    def to_isometric(x, y, z):
        iso_x = x - z
        iso_y = y + 0.5 * z
        return iso_x, iso_y
    
    features = [
        ('LOFT', 'lightblue', 'Complex transitions'),
        ('SWEEP', 'lightgreen', 'Path-based features'),
        ('BOUNDARY', 'lightyellow', 'Multi-direction'),
        ('WRAP', 'lightcoral', 'Text on surfaces'), 
        ('VARIABLE FILLET', 'lightpink', 'Changing radius'),
        ('REFERENCE GEOMETRY', 'lightgray', 'Planes & axes'),
    ]
    
    for i, (ax, (feature, color, desc)) in enumerate(zip(axes.flat, features)):
        ax.set_xlim(-2, 8)
        ax.set_ylim(-2, 6)
        ax.set_aspect('equal')
        ax.set_title(f'{feature}\n({desc})', fontweight='bold', fontsize=11)
        ax.axis('off')
        
        if i == 0:  # Loft
            # Draw loft-like shape
            bottom = patches.Ellipse((3, 1), 4, 2, facecolor=color, alpha=0.6, edgecolor='blue')
            top = patches.Ellipse(to_isometric(3, 3, 2), 2, 1, facecolor=color, alpha=0.8, edgecolor='blue')
            ax.add_patch(bottom)
            ax.add_patch(top)
            # Connect with lines
            ax.plot([1, to_isometric(2, 3, 2)[0]], [1, to_isometric(2, 3, 2)[1]], 'b-', alpha=0.5)
            ax.plot([5, to_isometric(4, 3, 2)[0]], [1, to_isometric(4, 3, 2)[1]], 'b-', alpha=0.5)
        
        elif i == 1:  # Sweep
            # Draw sweep path and profile
            t = np.linspace(0, 2*np.pi, 100)
            x_path = 3 + 2*np.cos(t)
            y_path = 3 + np.sin(t)
            ax.plot(x_path, y_path, 'g-', linewidth=3, alpha=0.7)
            # Profile at start
            profile = Circle((5, 3), 0.3, facecolor=color, edgecolor='green', alpha=0.8)
            ax.add_patch(profile)
        
        elif i == 2:  # Boundary
            # Draw boundary surface
            # Control curves
            curve1 = np.array([[1, 1], [3, 2], [5, 1]])
            curve2 = np.array([[1, 4], [3, 5], [5, 4]])
            ax.plot(curve1[:, 0], curve1[:, 1], 'orange', linewidth=2)
            ax.plot(curve2[:, 0], curve2[:, 1], 'orange', linewidth=2)
            # Surface representation
            surface = Polygon([(1, 1), (5, 1), (5, 4), (1, 4)], 
                            facecolor=color, alpha=0.5, edgecolor='orange')
            ax.add_patch(surface)
        
        elif i == 3:  # Wrap
            # Cylinder with wrapped text
            cylinder = patches.Ellipse((3, 3), 3, 1.5, facecolor=color, alpha=0.6, edgecolor='red')
            ax.add_patch(cylinder)
            # Curved text path
            t = np.linspace(-0.5, 0.5, 20)
            x_text = 3 + 1.2*np.cos(t)
            y_text = 3 + 0.3*np.sin(t)
            ax.plot(x_text, y_text, 'red', linewidth=2)
            ax.text(3, 3, 'TEXT', ha='center', va='center', fontsize=10, fontweight='bold')
        
        elif i == 4:  # Variable fillet
            # Rectangle with variable fillet
            rect_points = [(1, 2), (5, 2), (5, 4), (1, 4)]
            rect = Polygon(rect_points, facecolor=color, alpha=0.6, edgecolor='purple')
            ax.add_patch(rect)
            # Different radius fillets
            fillet1 = patches.Arc((5, 4), 0.5, 0.5, angle=0, theta1=180, theta2=270, 
                                 color='purple', linewidth=3)
            fillet2 = patches.Arc((1, 4), 1, 1, angle=0, theta1=270, theta2=360,
                                 color='purple', linewidth=3)
            ax.add_patch(fillet1)
            ax.add_patch(fillet2)
            ax.text(2, 1.5, 'R varies', fontsize=8, fontweight='bold', color='purple')
        
        elif i == 5:  # Reference geometry
            # Coordinate system and reference planes
            ax.plot([1, 5], [3, 3], 'k--', linewidth=2, alpha=0.5, label='Ref Plane')
            ax.plot([3, 3], [1, 5], 'k--', linewidth=2, alpha=0.5)
            ax.plot([2, 4], [2, 4], 'k--', linewidth=2, alpha=0.5)
            # Axis
            ax.plot([3, 4], [3, 3], 'r-', linewidth=3, label='Axis')
            ax.text(4.2, 3, 'Axis1', fontsize=8, fontweight='bold', color='red')
            ax.text(3.2, 5, 'Plane1', fontsize=8, fontweight='bold', color='gray')
    
    # Add note at bottom
    fig.text(0.5, 0.02, 'These advanced features will be covered in Modul 4-7. Master the basics first!', 
            ha='center', fontsize=12, fontweight='bold', style='italic', color='darkblue')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/12_advanced_features_preview.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 12_advanced_features_preview.png")
    plt.close()

if __name__ == '__main__':
    print("\n" + "="*75)
    print("GENERATING FEATURE MANAGEMENT & ASSEMBLY GUIDES - MODUL 3")
    print("="*75)
    
    try:
        feature_tree_management()
        assembly_preparation()
        advanced_features_preview()
        
        print("\n" + "="*75)
        print("✓ SEMUA PANDUAN FEATURE MANAGEMENT BERHASIL DIBUAT!")
        print("="*75)
        print("\nGambar tambahan untuk Modul 3:")
        print("  10: Feature tree management")
        print("  11: Assembly preparation") 
        print("  12: Advanced features preview")
        print("\n🎯 GRAND TOTAL: 24 ilustrasi lengkap! (12 per modul)")
        print("="*75 + "\n")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()