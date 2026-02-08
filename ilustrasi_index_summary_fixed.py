"""
INDEX SUMMARY SEMUA ILUSTRASI - MODUL 2 & 3
Complete reference untuk praktikan
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import warnings
warnings.filterwarnings('ignore')

def create_index_summary():
    """Create comprehensive index of all illustrations"""
    fig, axes = plt.subplots(1, 2, figsize=(20, 14))
    fig.suptitle('INDEX LENGKAP ILUSTRASI CAD/CAM - MODUL 2 & 3\n(24 Gambar untuk Membantu Praktikan)', 
                fontsize=16, fontweight='bold', y=0.95)
    
    # MODUL 2 Index
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.set_title('📐 MODUL 2: CAD GAMBAR 2D\n(12 Ilustrasi Sketching)', fontweight='bold', fontsize=14, color='blue')
    ax.axis('off')
    
    # Simple text-based index for Modul 2
    y_start = 15
    ax.text(5, y_start, 'KONSEP DASAR', ha='center', fontsize=12, fontweight='bold', color='darkblue',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    files_2 = [
        '01_entitas_sketch.png',
        '02_sketch_constraints.png', 
        '03_sketch_status.png',
        '04_dimensioning.png',
        '05_sketch_tools.png'
    ]
    
    y_pos = 14
    for f in files_2:
        ax.text(0.5, y_pos, f, fontsize=9, family='monospace', color='darkblue', fontweight='bold')
        y_pos -= 0.7
    
    ax.text(5, 10.5, 'PROJECT & TUTORIAL', ha='center', fontsize=12, fontweight='bold', color='darkgreen',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    files_2_project = [
        '07_project_panel_kontrol.png',
        '08_profil_aluminium_sketches.png',
        '09_sketching_tutorial.png'
    ]
    
    y_pos = 9.8
    for f in files_2_project:
        ax.text(0.5, y_pos, f, fontsize=9, family='monospace', color='darkgreen', fontweight='bold')
        y_pos -= 0.7
    
    ax.text(5, 7.5, 'PANDUAN PRAKTIS', ha='center', fontsize=12, fontweight='bold', color='darkorange',
           bbox=dict(boxstyle='round', facecolor='orange', alpha=0.7))
    
    files_2_guide = [
        '10_constraint_symbols_guide.png',
        '11_dimensioning_practices.png',
        '12_sketch_troubleshooting.png'
    ]
    
    y_pos = 6.8
    for f in files_2_guide:
        ax.text(0.5, y_pos, f, fontsize=9, family='monospace', color='darkorange', fontweight='bold')
        y_pos -= 0.7
    
    # MODUL 3 Index  
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.set_title('🔧 MODUL 3: CAD GAMBAR 3D\n(12 Ilustrasi Features)', fontweight='bold', fontsize=14, color='red')
    ax.axis('off')
    
    # Simple text-based index for Modul 3
    y_start = 15
    ax.text(5, y_start, 'FEATURE DASAR', ha='center', fontsize=12, fontweight='bold', color='darkred',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    files_3 = [
        '01_extrude_feature.png',
        '02_revolve_feature.png',
        '03_fillet_chamfer.png',
        '04_shell_draft.png',
        '05_pattern_features.png',
        '06_feature_workflow.png'
    ]
    
    y_pos = 14
    for f in files_3:
        ax.text(0.5, y_pos, f, fontsize=9, family='monospace', color='darkred', fontweight='bold')
        y_pos -= 0.7
    
    ax.text(5, 10.5, 'PROJECT & TUTORIAL', ha='center', fontsize=12, fontweight='bold', color='darkgreen',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    files_3_project = [
        '07_clamp_assembly_parts.png',
        '08_profil_aluminium_3d.png',
        '09_feature_tutorial_complete.png'
    ]
    
    y_pos = 9.8
    for f in files_3_project:
        ax.text(0.5, y_pos, f, fontsize=9, family='monospace', color='darkgreen', fontweight='bold')
        y_pos -= 0.7
    
    ax.text(5, 7.5, 'MANAGEMENT & PREP', ha='center', fontsize=12, fontweight='bold', color='darkorange',
           bbox=dict(boxstyle='round', facecolor='orange', alpha=0.7))
    
    files_3_mgmt = [
        '10_feature_tree_management.png',
        '11_assembly_preparation.png',
        '12_advanced_features_preview.png'
    ]
    
    y_pos = 6.8
    for f in files_3_mgmt:
        ax.text(0.5, y_pos, f, fontsize=9, family='monospace', color='darkorange', fontweight='bold')
        y_pos -= 0.7
    
    # Usage instructions at bottom
    fig.text(0.5, 0.03, 
            '📋 CARA PENGGUNAAN: Buka gambar sesuai topik yang dipelajari | 🎯 GOAL: Praktikan dapat menyelesaikan semua project dengan bantuan visual ini', 
            ha='center', fontsize=11, fontweight='bold', style='italic', color='darkgreen',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8, pad=1))
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/INDEX_ILUSTRASI_LENGKAP.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: INDEX_ILUSTRASI_LENGKAP.png")
    plt.close()

def create_quick_reference():
    """Create quick reference card for common tasks"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    fig.suptitle('QUICK REFERENCE CARD - MODUL 2 & 3\n(Cheat Sheet untuk Praktikan)', 
                fontsize=14, fontweight='bold', y=0.95)
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.set_title('Essential Shortcuts & Tips', fontweight='bold', fontsize=12)
    ax.axis('off')
    
    # Sections
    sections = [
        ('SKETCHING (Modul 2)', 0.5, 9, 'blue', [
            'L = Line | C = Circle | R = Rectangle',
            'D = Smart Dimension | Ctrl+Q = Rebuild', 
            'Goal: BLACK sketch (Fully Defined)',
            'Constraints: H(orizontal), V(ertical), E(qual)',
        ]),
        ('CONSTRAINTS PRIORITY', 6.5, 9, 'green', [
            '1. Horizontal/Vertical first',
            '2. Coincident for connections',
            '3. Equal for same sizes',
            '4. Symmetric for centerlines',
        ]),
        ('3D FEATURES (Modul 3)', 0.5, 5.5, 'red', [
            'Extrude: Sketch → Boss/Base',
            'Cut: Sketch → Extruded Cut',
            'Fillet: Select edges → R value',
            'Pattern: Select feature → Direction',
        ]),
        ('FEATURE ORDER', 6.5, 5.5, 'orange', [
            '1. Base Feature (Extrude)',
            '2. Additional features (Cut)',
            '3. Fillets/Chamfers',
            '4. Patterns (last)',
        ]),
        ('TROUBLESHOOTING', 0.5, 2, 'purple', [
            'Blue sketch → Add constraints',
            'Red sketch → Remove dimensions',
            'Feature fails → Check sketch',
            'Save often! (Ctrl+S)',
        ]),
        ('FILE NAMING', 6.5, 2, 'brown', [
            'Format: M0X_Name_Size.sldprt',
            'Example: M03_Base_100x60.sldprt', 
            'Use descriptive names always',
            'Avoid: Part1, untitled, etc.',
        ]),
    ]
    
    for title, x, y, color, items in sections:
        # Section header
        header_box = FancyBboxPatch((x, y-0.3), 5.5, 0.6, 
                                   boxstyle="round,pad=0.1",
                                   edgecolor=color, facecolor='white', 
                                   linewidth=2)
        ax.add_patch(header_box)
        ax.text(x+2.75, y, title, ha='center', va='center', fontsize=11, fontweight='bold', color=color)
        
        # Items
        for i, item in enumerate(items):
            item_y = y - 0.8 - i*0.4
            item_box = Rectangle((x+0.1, item_y-0.15), 5.3, 0.3, 
                               facecolor=color, alpha=0.1, edgecolor=color, linewidth=0.5)
            ax.add_patch(item_box)
            ax.text(x+0.2, item_y, f'• {item}', va='center', fontsize=9, color='black')
    
    plt.tight_layout()
    plt.savefig('/home/sirobo/Documents/Praktikum-CADCAM/QUICK_REFERENCE_CARD.png', 
               dpi=150, bbox_inches='tight')
    print("✓ Gambar: QUICK_REFERENCE_CARD.png")
    plt.close()

if __name__ == '__main__':
    print("\n" + "="*80)
    print("GENERATING INDEX & QUICK REFERENCE - FINAL SUMMARY")
    print("="*80)
    
    try:
        create_index_summary()
        create_quick_reference()
        
        print("\n" + "="*80)
        print("🎉 SEMUA ILUSTRASI & DOKUMENTASI LENGKAP SELESAI!")
        print("="*80)
        
        print("\n📊 FINAL SUMMARY:")
        print("  📂 Modul 2: 12 ilustrasi (01-12)")
        print("  📂 Modul 3: 12 ilustrasi (01-12)")
        print("  📋 Index lengkap: 1 gambar")
        print("  🔧 Quick reference: 1 gambar")
        print("  ────────────────────────────")
        print("  🎯 GRAND TOTAL: 26 gambar lengkap!")
        
        print("\n📍 LOKASI FILE:")
        print("  /home/sirobo/Documents/Praktikum-CADCAM/Modul-02-CAD-Gambar-2D/")
        print("  /home/sirobo/Documents/Praktikum-CADCAM/Modul-03-CAD-3D-Part1/")
        print("  /home/sirobo/Documents/Praktikum-CADCAM/INDEX_ILUSTRASI_LENGKAP.png")
        print("  /home/sirobo/Documents/Praktikum-CADCAM/QUICK_REFERENCE_CARD.png")
        
        print("\n🎓 PRAKTIKAN SEKARANG MEMILIKI:")
        print("  ✓ Visual guide untuk setiap konsep")
        print("  ✓ Step-by-step tutorial workflows")
        print("  ✓ Project examples dengan dimensi lengkap")
        print("  ✓ Troubleshooting guide untuk masalah umum")
        print("  ✓ Best practices untuk profesional workflow")
        print("  ✓ Quick reference untuk shortcuts & tips")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()