"""
ILUSTRASI DETAIL CONSTRAINTS & DIMENSIONING - MODUL 2
Panduan praktis untuk menyelesaikan sketch dengan benar
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Arc, Rectangle
import warnings
warnings.filterwarnings('ignore')

def constraint_symbols_guide():
    """Panduan lengkap simbol-simbol constraint"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    fig.suptitle('CONSTRAINT SYMBOLS GUIDE - MODUL 2\n(Simbol & Penggunaan Praktis)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Constraint symbols with examples
    constraints = [
        ('Horizontal', 'H', 'blue', 'Lines horizontal'),
        ('Vertical', 'V', 'blue', 'Lines vertical'),
        ('Parallel', '||', 'green', 'Lines parallel'),
        ('Perpendicular', '⊥', 'green', 'Lines 90°'),
        ('Tangent', 'T', 'orange', 'Line tangent to circle'),
        ('Concentric', '⊙', 'purple', 'Same center point'),
        ('Coincident', '•', 'red', 'Points together'),
        ('Equal', '=', 'cyan', 'Same length/radius'),
        ('Symmetric', 'S', 'magenta', 'Mirror about line'),
        ('Collinear', '—', 'brown', 'Points on same line'),
    ]
    
    y_start = 11
    for i, (name, symbol, color, desc) in enumerate(constraints):
        y = y_start - i * 1.1
        
        # Symbol box
        symbol_box = FancyBboxPatch((0.5, y-0.4), 1.5, 0.8, boxstyle="round,pad=0.1",
                                   edgecolor=color, facecolor='white', linewidth=2)
        ax.add_patch(symbol_box)
        ax.text(1.25, y, symbol, ha='center', va='center', fontsize=14, 
               fontweight='bold', color=color)
        
        # Name
        ax.text(2.5, y, name, va='center', fontsize=11, fontweight='bold')
        
        # Description
        ax.text(5, y, desc, va='center', fontsize=10, style='italic')
        
        # Example diagram
        x_ex = 8
        if 'Horizontal' in name:
            ax.plot([x_ex, x_ex+2], [y, y], color=color, linewidth=3)
            ax.text(x_ex+1, y-0.3, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold', 
                   bbox=dict(boxstyle='circle', facecolor='lightblue'))
        
        elif 'Vertical' in name:
            ax.plot([x_ex+1, x_ex+1], [y-0.3, y+0.3], color=color, linewidth=3)
            ax.text(x_ex+0.5, y, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='lightblue'))
        
        elif 'Parallel' in name:
            ax.plot([x_ex, x_ex+2], [y+0.2, y+0.2], color=color, linewidth=2)
            ax.plot([x_ex, x_ex+2], [y-0.2, y-0.2], color=color, linewidth=2)
            ax.text(x_ex+1, y, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='lightgreen'))
        
        elif 'Perpendicular' in name:
            ax.plot([x_ex, x_ex+1.5], [y, y], color=color, linewidth=2)
            ax.plot([x_ex+1.5, x_ex+1.5], [y, y+1], color=color, linewidth=2)
            ax.text(x_ex+1.2, y+0.3, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='lightgreen'))
        
        elif 'Tangent' in name:
            circle = Circle((x_ex+1, y), 0.3, facecolor='none', edgecolor=color, linewidth=2)
            ax.add_patch(circle)
            ax.plot([x_ex+0.4, x_ex+1.6], [y+0.5, y+0.5], color=color, linewidth=2)
            ax.text(x_ex+1.3, y+0.3, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='orange', alpha=0.7))
        
        elif 'Concentric' in name:
            circle1 = Circle((x_ex+1, y), 0.4, facecolor='none', edgecolor=color, linewidth=2)
            circle2 = Circle((x_ex+1, y), 0.2, facecolor='none', edgecolor=color, linewidth=2)
            ax.add_patch(circle1)
            ax.add_patch(circle2)
            ax.text(x_ex+1, y, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold', color='white')
        
        elif 'Coincident' in name:
            ax.plot(x_ex+0.5, y, 'o', color=color, markersize=8)
            ax.plot(x_ex+1.5, y, 'o', color=color, markersize=8)
            ax.plot([x_ex+0.5, x_ex+1.5], [y, y], 'k--', linewidth=1)
            ax.text(x_ex+1, y+0.3, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='lightcoral'))
        
        elif 'Equal' in name:
            circle1 = Circle((x_ex+0.5, y), 0.2, facecolor='none', edgecolor=color, linewidth=2)
            circle2 = Circle((x_ex+1.5, y), 0.2, facecolor='none', edgecolor=color, linewidth=2)
            ax.add_patch(circle1)
            ax.add_patch(circle2)
            ax.text(x_ex+1, y+0.4, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='lightcyan'))
        
        elif 'Symmetric' in name:
            ax.plot([x_ex, x_ex], [y-0.4, y+0.4], 'k--', linewidth=1)
            ax.plot([x_ex-0.3, x_ex-0.1], [y+0.2, y+0.2], color=color, linewidth=2)
            ax.plot([x_ex+0.1, x_ex+0.3], [y-0.2, y-0.2], color=color, linewidth=2)
            ax.text(x_ex+0.5, y, symbol, ha='center', va='center', 
                   fontsize=8, fontweight='bold',
                   bbox=dict(boxstyle='circle', facecolor='lightpink'))
        
        elif 'Collinear' in name:
            ax.plot([x_ex, x_ex+0.5], [y, y], color=color, linewidth=2)
            ax.plot([x_ex+1, x_ex+1.5], [y, y], color=color, linewidth=2)
            ax.plot(x_ex+0.25, y, 'o', color=color, markersize=4)
            ax.plot(x_ex+1.25, y, 'o', color=color, markersize=4)
    
    # Usage tips
    ax.text(12, 10, 'USAGE TIPS:', fontsize=12, fontweight='bold', color='darkblue')
    tips = [
        '• Start with Horizontal/Vertical',
        '• Use Equal for same sizes',
        '• Symmetric for centerlines', 
        '• Coincident for connections',
        '• Check status: Black = Good!'
    ]
    
    for i, tip in enumerate(tips):
        ax.text(12, 9.2 - i*0.6, tip, fontsize=10, color='darkblue')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/10_constraint_symbols_guide.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 10_constraint_symbols_guide.png")
    plt.close()

def dimensioning_best_practices():
    """Best practices untuk dimensioning"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('DIMENSIONING BEST PRACTICES - MODUL 2\n(Cara Benar Memberi Dimensi)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    # 1. Linear Dimensions
    ax = axes[0, 0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title('LINEAR DIMENSIONS\n(Horizontal & Vertical)', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    # Draw rectangle with proper dimensions
    rect = Rectangle((2, 2), 6, 3, facecolor='lightblue', edgecolor='blue', linewidth=2, alpha=0.6)
    ax.add_patch(rect)
    
    # Horizontal dimension
    ax.annotate('', xy=(8, 6), xytext=(2, 6),
               arrowprops=dict(arrowstyle='<->', lw=2, color='red'))
    ax.text(5, 6.5, '60mm', ha='center', fontsize=11, fontweight='bold', color='red')
    
    # Vertical dimension
    ax.annotate('', xy=(1, 5), xytext=(1, 2),
               arrowprops=dict(arrowstyle='<->', lw=2, color='red'))
    ax.text(0.5, 3.5, '30mm', ha='center', va='center', rotation=90, 
           fontsize=11, fontweight='bold', color='red')
    
    ax.text(5, 0.5, 'GOOD: Outside sketch boundary', ha='center', fontsize=10, 
           fontweight='bold', color='green')
    
    # 2. Angular Dimensions
    ax = axes[0, 1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title('ANGULAR DIMENSIONS\n(Between Lines)', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    # Draw angle
    ax.plot([3, 7], [3, 3], 'blue', linewidth=3)  # horizontal line
    ax.plot([3, 6], [3, 6], 'blue', linewidth=3)  # angled line
    
    # Angle arc
    angle_arc = patches.Arc((3, 3), 2, 2, angle=0, theta1=0, theta2=45, 
                           color='red', linewidth=2)
    ax.add_patch(angle_arc)
    ax.text(4.2, 3.8, '45°', fontsize=11, fontweight='bold', color='red')
    
    # Angle symbol
    ax.text(3.5, 2.5, '∠', fontsize=16, fontweight='bold', color='red')
    
    ax.text(5, 0.5, 'GOOD: Angular symbol clear', ha='center', fontsize=10, 
           fontweight='bold', color='green')
    
    # 3. Radial Dimensions
    ax = axes[1, 0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title('RADIAL DIMENSIONS\n(Radius & Diameter)', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    # Circle with radius
    circle = Circle((4, 4), 2, facecolor='lightgreen', edgecolor='green', linewidth=2, alpha=0.6)
    ax.add_patch(circle)
    
    # Radius line
    ax.plot([4, 6], [4, 4], 'red', linewidth=2)
    ax.text(6.5, 4, 'R20', fontsize=11, fontweight='bold', color='red')
    
    # Center mark
    ax.plot([3.8, 4.2], [4, 4], 'k-', linewidth=2)
    ax.plot([4, 4], [3.8, 4.2], 'k-', linewidth=2)
    
    # Diameter annotation
    ax.annotate('', xy=(6, 4), xytext=(2, 4),
               arrowprops=dict(arrowstyle='<->', lw=1.5, color='purple'))
    ax.text(4, 1.5, 'Ø40', ha='center', fontsize=11, fontweight='bold', color='purple')
    
    ax.text(5, 0.5, 'R for Radius, Ø for Diameter', ha='center', fontsize=10, 
           fontweight='bold', color='green')
    
    # 4. Driven vs Reference
    ax = axes[1, 1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title('DRIVEN vs REFERENCE\n(Gray = Reference only)', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    # Two rectangles
    rect1 = Rectangle((1, 3), 3, 2, facecolor='lightcoral', edgecolor='red', linewidth=2, alpha=0.6)
    rect2 = Rectangle((6, 3), 2, 2, facecolor='lightyellow', edgecolor='orange', linewidth=2, alpha=0.6)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    
    # Driven dimension (black)
    ax.annotate('', xy=(4, 6), xytext=(1, 6),
               arrowprops=dict(arrowstyle='<->', lw=2, color='black'))
    ax.text(2.5, 6.5, '30', ha='center', fontsize=11, fontweight='bold', color='black')
    ax.text(2.5, 2, 'DRIVEN\n(Controls size)', ha='center', fontsize=9, fontweight='bold', color='red')
    
    # Reference dimension (gray)
    ax.annotate('', xy=(8, 6), xytext=(6, 6),
               arrowprops=dict(arrowstyle='<->', lw=2, color='gray'))
    ax.text(7, 6.5, '(20)', ha='center', fontsize=11, fontweight='bold', color='gray')
    ax.text(7, 2, 'REFERENCE\n(Display only)', ha='center', fontsize=9, fontweight='bold', color='gray')
    
    ax.text(5, 0.5, 'Driven (black) controls, Reference (gray) shows', ha='center', fontsize=10, 
           fontweight='bold', color='blue')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/11_dimensioning_practices.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 11_dimensioning_practices.png")
    plt.close()

def sketch_troubleshooting():
    """Common sketch problems and solutions"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('SKETCH TROUBLESHOOTING - MODUL 2\n(Masalah Umum & Solusi)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    problems = [
        ('UNDER DEFINED\n(Blue sketch)', 'blue', 'ADD MORE\nCONSTRAINTS'),
        ('OVER DEFINED\n(Red sketch)', 'red', 'DELETE EXTRA\nDIMENSIONS'),
        ('OPEN CONTOUR\n(Gap in sketch)', 'orange', 'CLOSE THE\nGAP'),
        ('SELF INTERSECT\n(Lines cross)', 'purple', 'TRIM OR\nREDRAW'),
        ('NO CONSTRAINTS\n(Floating)', 'gray', 'ADD RELATIONS\n& DIMENSIONS'),
        ('WRONG ORIGIN\n(Bad position)', 'brown', 'MOVE TO\nORIGIN')
    ]
    
    solutions = [
        'Add Horizontal/Vertical\nconstraints',
        'Remove conflicting\ndimensions',
        'Use Coincident to\nconnect endpoints', 
        'Use Trim tool or\nredraw clean lines',
        'Start with basic\nrelations first',
        'Use Coincident with\norigin point'
    ]
    
    for i, (ax, (problem, color, solution)) in enumerate(zip(axes.flat, problems)):
        ax.set_xlim(-1, 8)
        ax.set_ylim(-1, 7)
        ax.set_aspect('equal')
        ax.set_title(problem, fontweight='bold', fontsize=11, color=color)
        ax.axis('off')
        
        if i == 0:  # Under defined
            # Floating rectangle
            ax.plot([2, 5, 5, 2, 2], [2, 2, 4, 4, 2], color='blue', linewidth=3, alpha=0.7)
            ax.text(3.5, 3, '?', ha='center', va='center', fontsize=20, fontweight='bold', color='blue')
            ax.text(3.5, 1, 'Needs constraints!', ha='center', fontsize=9, fontweight='bold', color='blue')
            
        elif i == 1:  # Over defined
            # Rectangle with too many dimensions
            ax.plot([2, 5, 5, 2, 2], [2, 2, 4, 4, 2], color='red', linewidth=3, alpha=0.7)
            # Multiple conflicting dimensions
            ax.annotate('', xy=(5, 5), xytext=(2, 5), arrowprops=dict(arrowstyle='<->', color='red'))
            ax.annotate('', xy=(5, 5.3), xytext=(2, 5.3), arrowprops=dict(arrowstyle='<->', color='red'))
            ax.text(3.5, 3, '!', ha='center', va='center', fontsize=20, fontweight='bold', color='red')
            ax.text(3.5, 1, 'Too many dimensions!', ha='center', fontsize=9, fontweight='bold', color='red')
            
        elif i == 2:  # Open contour
            # Rectangle with gap
            ax.plot([2, 5], [2, 2], color='orange', linewidth=3)
            ax.plot([5, 5], [2, 4], color='orange', linewidth=3)
            ax.plot([5, 2], [4, 4], color='orange', linewidth=3)
            ax.plot([2, 2], [4, 2.2], color='orange', linewidth=3)  # Gap here
            ax.plot([2, 2], [1.8, 2], 'ro', markersize=8)  # Show gap
            ax.text(1.5, 1.9, 'GAP!', fontsize=8, fontweight='bold', color='red')
            
        elif i == 3:  # Self intersect
            # Lines crossing
            ax.plot([1, 6], [2, 4], color='purple', linewidth=3)
            ax.plot([1, 6], [4, 2], color='purple', linewidth=3)
            ax.plot(3.5, 3, 'ro', markersize=10)  # Intersection point
            ax.text(3.5, 1, 'Lines cross!', ha='center', fontsize=9, fontweight='bold', color='purple')
            
        elif i == 4:  # No constraints
            # Sketch with no relations
            ax.plot([2, 5, 4, 2, 2], [2, 2, 4, 3.5, 2], color='gray', linewidth=3, alpha=0.7)
            ax.text(3.5, 3, '⚠', ha='center', va='center', fontsize=16, fontweight='bold', color='gray')
            ax.text(3.5, 1, 'No relations!', ha='center', fontsize=9, fontweight='bold', color='gray')
            
        elif i == 5:  # Wrong origin
            # Sketch far from origin
            ax.plot([5, 7, 7, 5, 5], [4, 4, 6, 6, 4], color='brown', linewidth=3, alpha=0.7)
            ax.plot(0, 0, 'ko', markersize=8)  # Origin
            ax.plot([0, 6], [0, 5], 'k--', alpha=0.5)  # Distance to origin
            ax.text(0, -0.5, 'Origin', ha='center', fontsize=8, fontweight='bold')
            ax.text(6, 1, 'Too far!', ha='center', fontsize=9, fontweight='bold', color='brown')
        
        # Solution text
        ax.text(3.5, -0.5, solutions[i], ha='center', va='top', fontsize=8, 
               fontweight='bold', color='green',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/12_sketch_troubleshooting.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: 12_sketch_troubleshooting.png")
    plt.close()

if __name__ == '__main__':
    print("\n" + "="*70)
    print("GENERATING DETAILED CONSTRAINT & DIMENSIONING GUIDES - MODUL 2")
    print("="*70)
    
    try:
        constraint_symbols_guide()
        dimensioning_best_practices() 
        sketch_troubleshooting()
        
        print("\n" + "="*70)
        print("✓ SEMUA PANDUAN DETAIL BERHASIL DIBUAT!")
        print("="*70)
        print("\nGambar tambahan untuk Modul 2:")
        print("  10: Constraint symbols guide")
        print("  11: Dimensioning best practices") 
        print("  12: Sketch troubleshooting")
        print("\n🎯 Total sekarang: 21 ilustrasi lengkap!")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()