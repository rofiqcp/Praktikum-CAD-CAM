#!/usr/bin/env python3
"""
Generate Image — Modul 03: CAD Gambar 3D Part 1 (Feature Dasar)
================================================================
Script untuk membuat semua ilustrasi materi dan project Modul 3.
Gambar disimpan di subfolder image/ dengan format:
  - m##_deskripsi.png  → ilustrasi materi
  - p##_deskripsi.png  → ilustrasi project
  
Menggunakan isometric projection 2D (BUKAN mplot3d) untuk semua
visualisasi 3D guna menghindari konflik library matplotlib.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Arc, Polygon
from matplotlib.collections import PatchCollection

# ── Konfigurasi ──────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image')
os.makedirs(OUTPUT_DIR, exist_ok=True)
DPI = 150

C = {
    'bg':       '#FFFFFF',
    'line':     '#1A1A2E',
    'dim':      '#0066CC',
    'dim_line': '#4A90D9',
    'accent1':  '#2196F3',
    'accent2':  '#4CAF50',
    'accent3':  '#FF9800',
    'accent4':  '#9C27B0',
    'accent5':  '#F44336',
    'fill1':    '#BBDEFB',
    'fill2':    '#C8E6C9',
    'fill3':    '#FFE0B2',
    'fill4':    '#E1BEE7',
    'header':   '#1565C0',
    'panel':    '#F5F5F5',
    'steel':    '#B0BEC5',
    'alu':      '#CFD8DC',
    'face_top': '#90CAF9',
    'face_front': '#64B5F6',
    'face_right': '#42A5F5',
    'cut':      '#EF5350',
    'cut_fill': '#FFCDD2',
}


def save(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'  ✅ {filename}')


def make_header(ax, text, y=0.97):
    ax.text(0.5, y, text, transform=ax.transAxes, fontsize=14, fontweight='bold',
            ha='center', va='top', color=C['header'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD',
                      edgecolor=C['header'], lw=1.5))


def dim_line(ax, p1, p2, text, offset=0, color=None, fontsize=8):
    if color is None:
        color = C['dim']
    mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
    ax.annotate('', xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle='<->', color=color, lw=1))
    ax.text(mx, my+offset, text, fontsize=fontsize, ha='center', va='bottom',
            color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='none', alpha=0.8))


# ── Isometric Helpers ────────────────────────────────────────
def iso(x, y, z):
    """Convert 3D (x,y,z) to isometric 2D (ix,iy)."""
    ix = (x - z) * np.cos(np.pi/6)
    iy = y + (x + z) * np.sin(np.pi/6)
    return ix, iy


def draw_iso_box(ax, ox, oy, oz, sx, sy, sz,
                 fc_top=None, fc_front=None, fc_right=None,
                 ec=None, lw=1.5, alpha=0.8):
    """Draw an isometric box at origin (ox,oy,oz) with size (sx,sy,sz)."""
    if fc_top is None: fc_top = C['face_top']
    if fc_front is None: fc_front = C['face_front']
    if fc_right is None: fc_right = C['face_right']
    if ec is None: ec = C['line']

    # 8 corners
    corners = {}
    for i, (dx, dy, dz) in enumerate([
        (0,0,0), (sx,0,0), (sx,sy,0), (0,sy,0),
        (0,0,sz), (sx,0,sz), (sx,sy,sz), (0,sy,sz)
    ]):
        corners[i] = iso(ox+dx, oy+dy, oz+dz)

    # Top face (4,5,6,7)
    top = Polygon([corners[4], corners[5], corners[6], corners[7]],
                  closed=True, fc=fc_top, ec=ec, lw=lw, alpha=alpha, zorder=3)
    ax.add_patch(top)

    # Front face (0,1,5,4)
    front = Polygon([corners[0], corners[1], corners[5], corners[4]],
                    closed=True, fc=fc_front, ec=ec, lw=lw, alpha=alpha, zorder=2)
    ax.add_patch(front)

    # Right face (1,2,6,5)
    right = Polygon([corners[1], corners[2], corners[6], corners[5]],
                    closed=True, fc=fc_right, ec=ec, lw=lw, alpha=alpha, zorder=2)
    ax.add_patch(right)


def draw_iso_cylinder_top(ax, cx, cy, cz, r, h, color=None, ec=None, alpha=0.7, n=60):
    """Draw isometric cylinder (simplified: top ellipse + sides)."""
    if color is None: color = C['face_top']
    if ec is None: ec = C['line']

    # Top ellipse
    theta = np.linspace(0, 2*np.pi, n)
    top_pts = [iso(cx + r*np.cos(t), cy + h, cz + r*np.sin(t)) for t in theta]
    top_x = [p[0] for p in top_pts]
    top_y = [p[1] for p in top_pts]
    ax.fill(top_x, top_y, color=color, ec=ec, lw=1, alpha=alpha, zorder=4)

    # Bottom ellipse (partial — front half only)
    bot_pts = [iso(cx + r*np.cos(t), cy, cz + r*np.sin(t)) for t in theta]
    bot_x = [p[0] for p in bot_pts]
    bot_y = [p[1] for p in bot_pts]

    # Side surface
    side_x = top_x + bot_x[::-1]
    side_y = top_y + bot_y[::-1]
    ax.fill(side_x, side_y, color=color, ec='none', alpha=alpha*0.7, zorder=3)
    ax.plot(top_x, top_y, color=ec, lw=1, zorder=5)

    # Visible bottom edges
    half = n // 2
    ax.plot(bot_x[:half], bot_y[:half], color=ec, lw=1, zorder=3)
    # Left and right vertical lines
    ax.plot([top_x[0], bot_x[0]], [top_y[0], bot_y[0]], color=ec, lw=1, zorder=3)
    ax.plot([top_x[half], bot_x[half]], [top_y[half], bot_y[half]], color=ec, lw=1, zorder=3)


# ══════════════════════════════════════════════════════════════
#  MATERI ILLUSTRATIONS
# ══════════════════════════════════════════════════════════════

def m01_feature_based_workflow():
    """Workflow Feature-Based Modeling: Base → Boss → Cut → Fillet → Pattern."""
    fig, ax = plt.subplots(figsize=(14, 5), facecolor=C['bg'])
    make_header(ax, 'Feature-Based Parametric Modeling — Workflow')
    ax.set_xlim(0, 14); ax.set_ylim(0, 5); ax.axis('off')

    steps = [
        ('1. Base\nFeature', C['accent1'], 'Extrude/\nRevolve'),
        ('2. Boss\n(Tambah)', C['accent2'], 'Penambahan\nMaterial'),
        ('3. Cut\n(Potong)', C['accent5'], 'Pengurangan\nMaterial'),
        ('4. Fillet/\nChamfer', C['accent3'], 'Detail\nEdge'),
        ('5. Pattern', C['accent4'], 'Pengulangan\nFeature'),
        ('6. Detail\nFeatures', C['dim'], 'Shell, Draft\nHole Wizard'),
    ]

    for i, (label, color, desc) in enumerate(steps):
        x = 1.1 + i * 2.1
        ax.add_patch(FancyBboxPatch((x-0.85, 1.2), 1.7, 2.5,
                     boxstyle='round,pad=0.15', facecolor='white',
                     edgecolor=color, lw=2))
        ax.text(x, 3.2, label, fontsize=9, ha='center', va='center',
                color=color, fontweight='bold')
        ax.text(x, 1.7, desc, fontsize=7, ha='center', va='center',
                color=C['steel'])
        if i < len(steps) - 1:
            ax.annotate('', (x+1.15, 2.45), (x+0.9, 2.45),
                       arrowprops=dict(arrowstyle='->', color=C['steel'], lw=1.5))

    ax.text(7, 0.6, 'Base Feature → Boss sebelum Cut → Fillet/Chamfer terakhir → Beri nama deskriptif',
            fontsize=9, ha='center', color=C['accent2'], fontstyle='italic',
            bbox=dict(boxstyle='round', fc=C['fill2'], ec=C['accent2']))

    fig.tight_layout()
    save(fig, 'm01_feature_workflow.png')


def m02_extrude_boss_cut():
    """Extruded Boss/Base dan Extruded Cut."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 6), facecolor=C['bg'])
    fig.suptitle('Extruded Boss/Base  vs  Extruded Cut', fontsize=14,
                 fontweight='bold', color=C['header'], y=1.0)

    # Boss
    ax = axes[0]
    ax.set_xlim(-5, 6); ax.set_ylim(-2, 6)
    ax.set_aspect('equal'); ax.axis('off')
    draw_iso_box(ax, 0, 0, 0, 4, 2, 3)
    # Sketch outline (bottom)
    s_pts = [iso(0, 0, 0), iso(4, 0, 0), iso(4, 0, 3), iso(0, 0, 3)]
    sx = [p[0] for p in s_pts]; sy = [p[1] for p in s_pts]
    ax.plot(sx + [sx[0]], sy + [sy[0]], '--', color=C['accent1'], lw=1.5)
    # Arrow showing direction
    p1 = iso(2, 0, 1.5); p2 = iso(2, 2, 1.5)
    ax.annotate('', p2, p1,
               arrowprops=dict(arrowstyle='->', color=C['accent2'], lw=2))
    ax.text(p2[0]+0.3, p2[1], 'Depth', fontsize=9, color=C['accent2'], fontweight='bold')

    # Parameter table
    params = ['Blind (jarak)', 'Through All', 'Up To Surface',
              'Mid Plane', 'Draft angle']
    for i, p in enumerate(params):
        ax.text(-4.5, 5 - i*0.6, f'• {p}', fontsize=8, color=C['line'])

    ax.set_title('Extruded Boss/Base\n(Menambah material)', fontsize=11,
                 fontweight='bold', color=C['accent2'])

    # Cut
    ax = axes[1]
    ax.set_xlim(-5, 6); ax.set_ylim(-2, 6)
    ax.set_aspect('equal'); ax.axis('off')
    draw_iso_box(ax, 0, 0, 0, 4, 2, 3)
    # Cut hole (circle on top)
    theta = np.linspace(0, 2*np.pi, 40)
    r = 0.6
    top_pts = [iso(2 + r*np.cos(t), 2, 1.5 + r*np.sin(t)) for t in theta]
    tx = [p[0] for p in top_pts]; ty = [p[1] for p in top_pts]
    ax.fill(tx, ty, color=C['cut_fill'], ec=C['cut'], lw=2, zorder=5)
    # Arrow downward
    p1 = iso(2, 2.5, 1.5); p2 = iso(2, 0.5, 1.5)
    ax.annotate('', p2, p1,
               arrowprops=dict(arrowstyle='->', color=C['accent5'], lw=2))
    ax.text(p1[0]+0.3, p1[1]+0.3, 'Cut', fontsize=9, color=C['accent5'], fontweight='bold')

    params = ['Blind', 'Through All', 'Flip side', 'Normal cut']
    for i, p in enumerate(params):
        ax.text(-4.5, 5 - i*0.6, f'• {p}', fontsize=8, color=C['line'])

    ax.set_title('Extruded Cut\n(Mengurangi material)', fontsize=11,
                 fontweight='bold', color=C['accent5'])

    fig.tight_layout()
    save(fig, 'm02_extrude_boss_cut.png')


def m03_revolve():
    """Revolved Boss/Base dan Revolved Cut."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 6), facecolor=C['bg'])
    fig.suptitle('Revolved Boss/Base  &  Revolved Cut', fontsize=14,
                 fontweight='bold', color=C['header'], y=1.0)

    # Revolve Boss
    ax = axes[0]
    ax.set_xlim(-4, 4); ax.set_ylim(-3, 5)
    ax.set_aspect('equal'); ax.axis('off')

    # Profile (half section of stepped shaft)
    # Draw stepped profile
    profile_x = [0, 2, 2, 1.5, 1.5, 1, 1, 0]
    profile_y = [0, 0, 1, 1, 2.5, 2.5, 4, 4]
    ax.fill(profile_x, profile_y, color=C['fill1'], ec=C['accent1'], lw=2, alpha=0.5)
    # Mirror side
    mirror_x = [0, -2, -2, -1.5, -1.5, -1, -1, 0]
    ax.fill(mirror_x, profile_y, color=C['fill1'], ec=C['accent1'], lw=2, alpha=0.3)
    # Centerline
    ax.plot([0, 0], [-0.5, 4.5], color=C['accent5'], lw=1.5, ls='dashdot')
    ax.text(0.15, 4.5, 'Axis', fontsize=8, color=C['accent5'])
    # Rotation arrow
    arc_angle = np.linspace(0, 1.5*np.pi, 40)
    ax.plot(3*np.cos(arc_angle)-0.5, 2+0.8*np.sin(arc_angle),
            color=C['accent3'], lw=2)
    ax.text(2.5, 2.8, '360°', fontsize=9, color=C['accent3'], fontweight='bold')

    # Requirements
    reqs = ['✅ Centerline = sumbu putar', '✅ Profil tertutup',
            '✅ Profil di satu sisi CL', '❌ Profil TIDAK memotong CL']
    for i, r in enumerate(reqs):
        ax.text(-3.8, -0.5 - i*0.55, r, fontsize=8, color=C['line'])

    ax.set_title('Revolved Boss\n(Profil → Putar)', fontsize=11,
                 fontweight='bold', color=C['accent2'])

    # Revolve Cut
    ax = axes[1]
    ax.set_xlim(-4, 4); ax.set_ylim(-3, 5)
    ax.set_aspect('equal'); ax.axis('off')

    # Full cylinder outline
    ax.fill([-2, 2, 2, -2], [0, 0, 4, 4], color=C['fill1'], ec=C['accent1'],
            lw=2, alpha=0.3)
    # Groove cut
    ax.fill([-2.2, -1.8, -1.8, -2.2], [1.5, 1.5, 2.5, 2.5],
            color=C['cut_fill'], ec=C['cut'], lw=1.5)
    ax.fill([1.8, 2.2, 2.2, 1.8], [1.5, 1.5, 2.5, 2.5],
            color=C['cut_fill'], ec=C['cut'], lw=1.5)
    ax.plot([0, 0], [-0.5, 4.5], color=C['accent5'], lw=1.5, ls='dashdot')
    ax.text(0.15, 4.5, 'Axis', fontsize=8, color=C['accent5'])
    ax.text(2.5, 2, 'Groove\nCut', fontsize=8, color=C['cut'], fontweight='bold')

    ax.set_title('Revolved Cut\n(Potong melingkar)', fontsize=11,
                 fontweight='bold', color=C['accent5'])

    fig.tight_layout()
    save(fig, 'm03_revolve.png')


def m04_fillet_chamfer():
    """Fillet dan Chamfer 3D (tipe-tipe)."""
    fig, axes = plt.subplots(2, 4, figsize=(14, 7), facecolor=C['bg'])
    fig.suptitle('Fillet & Chamfer 3D', fontsize=14, fontweight='bold',
                 color=C['header'], y=0.99)

    items = [
        ('Constant Fillet', 'fillet'), ('Variable Fillet', 'fillet'),
        ('Face Fillet', 'fillet'), ('Full Round', 'fillet'),
        ('Equal Distance', 'chamfer'), ('Angle Distance', 'chamfer'),
        ('Distance-Distance', 'chamfer'), ('Vertex Chamfer', 'chamfer'),
    ]

    for ax, (name, kind) in zip(axes.flat, items):
        ax.set_xlim(-2, 2); ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal'); ax.axis('off')

        if kind == 'fillet':
            clr = C['accent2']
            # Draw L-shape corner
            ax.plot([-1.5, 0, 0], [0, 0, 1.2], color=C['line'], lw=2)
            if 'Constant' in name:
                arc = Arc((0, 0), 0.8, 0.8, theta1=90, theta2=180,
                         color=clr, lw=3)
                ax.add_patch(arc)
                ax.text(0.5, 0.5, 'R = const', fontsize=7, color=clr,
                        fontweight='bold')
            elif 'Variable' in name:
                # Variable radius arc
                t = np.linspace(np.pi/2, np.pi, 30)
                r_arr = np.linspace(0.3, 0.6, 30)
                ax.plot(r_arr*np.cos(t), r_arr*np.sin(t), color=clr, lw=3)
                ax.text(0.3, 0.5, 'R varies', fontsize=7, color=clr, fontweight='bold')
            elif 'Face' in name:
                ax.add_patch(patches.Rectangle((-1.2, -0.8), 1.0, 1.6, lw=1.5,
                             ec=C['accent1'], fc=C['fill1'], alpha=0.3))
                ax.add_patch(patches.Rectangle((0.2, -0.8), 1.0, 1.6, lw=1.5,
                             ec=C['accent3'], fc=C['fill3'], alpha=0.3))
                arc = Arc((0, 0), 0.8, 0.8, theta1=60, theta2=120,
                         color=clr, lw=3)
                ax.add_patch(arc)
                ax.text(0, -1.2, 'Between\n2 faces', fontsize=7, ha='center',
                        color=clr, fontweight='bold')
            else:  # Full Round
                ax.add_patch(patches.Rectangle((-1.2, -0.5), 2.4, 1.0, lw=1.5,
                             ec=C['line'], fc=C['fill2'], alpha=0.3))
                arc = Arc((0, 0.5), 2.0, 1.0, theta1=0, theta2=180,
                         color=clr, lw=3)
                ax.add_patch(arc)
                ax.text(0, -1.0, '3 faces', fontsize=7, ha='center',
                        color=clr, fontweight='bold')
        else:  # chamfer
            clr = C['accent3']
            ax.plot([-1.5, 0, 0], [0, 0, 1.2], color=C['line'], lw=2)
            if 'Equal' in name:
                ax.plot([-0.5, 0, 0, -0.5], [0, 0, 0.5, 0], color=clr, lw=3)
                ax.text(0.3, 0.5, 'D × D', fontsize=7, color=clr, fontweight='bold')
            elif 'Angle' in name:
                ax.plot([-0.5, 0, 0, -0.5], [0, 0, 0.7, 0], color=clr, lw=3)
                ax.text(0.3, 0.5, 'D × θ', fontsize=7, color=clr, fontweight='bold')
            elif 'Distance-D' in name:
                ax.plot([-0.3, 0, 0, -0.3], [0, 0, 0.7, 0], color=clr, lw=3)
                ax.text(0.3, 0.5, 'D1 × D2', fontsize=7, color=clr, fontweight='bold')
            else:  # Vertex
                ax.plot([-1, 0], [0, 0], color=C['line'], lw=2)
                ax.plot([0, 0], [0, 1], color=C['line'], lw=2)
                ax.plot([0, 0.7], [0, 0], color=C['line'], lw=2)
                # Triangle cut
                ax.fill([-0.3, 0, 0, -0.3], [0, 0, 0.3, 0], color=clr, alpha=0.4)
                ax.text(0.3, 0.5, 'Vertex\n3 edges', fontsize=7, color=clr,
                        fontweight='bold')

        ax.set_title(name, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm04_fillet_chamfer.png')


def m05_shell_draft():
    """Shell dan Draft features."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 6), facecolor=C['bg'])
    fig.suptitle('Shell & Draft Features', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.0)

    # Shell
    ax = axes[0]
    ax.set_xlim(-5, 6); ax.set_ylim(-2, 6)
    ax.set_aspect('equal'); ax.axis('off')

    # Outer box
    draw_iso_box(ax, 0, 0, 0, 4, 3, 3, alpha=0.4)
    # Inner cavity (smaller box showing wall thickness)
    draw_iso_box(ax, 0.3, 0.3, 0.3, 3.4, 2.7, 2.4,
                fc_top='white', fc_front='#E3F2FD', fc_right='#BBDEFB',
                ec=C['accent1'], lw=1, alpha=0.6)

    # Labels
    p1 = iso(0.15, 1.5, 0); p2 = iso(0.3, 1.5, 0.3)
    ax.annotate('', p2, p1,
               arrowprops=dict(arrowstyle='<->', color=C['dim'], lw=1.5))
    ax.text(p1[0]-0.5, p1[1], 't', fontsize=10, color=C['dim'], fontweight='bold')

    ax.text(0, -1.5, 'Face atas dihilangkan\nKetebalan dinding = t', fontsize=9,
            ha='center', color=C['accent1'],
            bbox=dict(boxstyle='round', fc=C['fill1'], ec=C['accent1']))
    ax.set_title('Shell\n(Benda berongga)', fontsize=11, fontweight='bold',
                 color=C['accent1'])

    # Draft
    ax = axes[1]
    ax.set_xlim(-5, 6); ax.set_ylim(-2, 6)
    ax.set_aspect('equal'); ax.axis('off')

    # Base (normal box)
    draw_iso_box(ax, 0, 0, 0, 4, 0.5, 3, alpha=0.3)

    # Drafted walls (trapezoid sides)
    # Front face with draft
    pts_front = [iso(0.3, 0.5, 0), iso(3.7, 0.5, 0),
                 iso(4, 3, 0), iso(0, 3, 0)]
    ax.add_patch(Polygon(pts_front, closed=True, fc=C['fill3'], ec=C['accent3'],
                 lw=2, alpha=0.5))

    # Draft angle indicator
    ax.plot([iso(0, 0.5, 0)[0], iso(0, 3, 0)[0]],
            [iso(0, 0.5, 0)[1], iso(0, 3, 0)[1]],
            color=C['steel'], lw=1, ls='--')
    ax.text(-2, 3, 'Draft\nAngle α', fontsize=9, color=C['accent3'], fontweight='bold')

    ax.text(0, -1.5, 'Kemiringan dinding\nuntuk proses molding', fontsize=9,
            ha='center', color=C['accent3'],
            bbox=dict(boxstyle='round', fc=C['fill3'], ec=C['accent3']))
    ax.set_title('Draft\n(Sudut kemiringan)', fontsize=11, fontweight='bold',
                 color=C['accent3'])

    fig.tight_layout()
    save(fig, 'm05_shell_draft.png')


def m06_hole_wizard():
    """Hole Wizard — jenis-jenis lubang standar."""
    fig, axes = plt.subplots(2, 3, figsize=(13, 8), facecolor=C['bg'])
    fig.suptitle('Hole Wizard — Jenis Lubang Standar', fontsize=14,
                 fontweight='bold', color=C['header'], y=0.99)

    holes = [
        ('Hole (Simple)', C['accent1']),
        ('Counterbore', C['accent2']),
        ('Countersink', C['accent3']),
        ('Straight Tap', C['accent4']),
        ('Tapered Tap', C['accent5']),
        ('Legacy', C['dim']),
    ]

    for ax, (name, clr) in zip(axes.flat, holes):
        ax.set_xlim(-2, 2); ax.set_ylim(-2.5, 1.5)
        ax.set_aspect('equal'); ax.axis('off')

        # Block cross-section
        ax.add_patch(patches.Rectangle((-1.8, -2), 3.6, 2.5, lw=1.5,
                     ec=C['steel'], fc=C['alu'], alpha=0.2))

        if name == 'Hole (Simple)':
            ax.fill([-0.3, 0.3, 0.3, -0.3], [0.5, 0.5, -2, -2],
                    color='white', ec=clr, lw=2)
            dim_line(ax, (-0.3, 0.7), (0.3, 0.7), 'Ø', fontsize=8, color=clr)
        elif name == 'Counterbore':
            ax.fill([-0.3, 0.3, 0.3, 0.6, 0.6, -0.6, -0.6, -0.3],
                    [0.5, 0.5, -0.3, -0.3, -2, -2, -0.3, -0.3],
                    color='white', ec=clr, lw=2)
            ax.text(0.8, -0.8, 'Cbore', fontsize=7, color=clr, fontweight='bold')
        elif name == 'Countersink':
            ax.fill([-0.3, 0.3, 0.3, 0.7, -0.7, -0.3],
                    [0.2, 0.2, -2, 0.5, 0.5, 0.2],
                    color='white', ec=clr, lw=2)
            ax.text(0.8, 0, 'Csink', fontsize=7, color=clr, fontweight='bold')
        elif name == 'Straight Tap':
            ax.fill([-0.3, 0.3, 0.3, -0.3], [0.5, 0.5, -1.5, -1.5],
                    color='white', ec=clr, lw=2)
            # Thread lines
            for y in np.arange(-1.3, 0.4, 0.25):
                ax.plot([-0.3, 0.3], [y, y+0.1], color=clr, lw=0.7)
            ax.text(0.5, -0.5, 'Thread', fontsize=7, color=clr, fontweight='bold')
        elif name == 'Tapered Tap':
            ax.fill([-0.3, 0.3, 0.25, -0.25], [0.5, 0.5, -1.5, -1.5],
                    color='white', ec=clr, lw=2)
            for y in np.arange(-1.3, 0.4, 0.25):
                ax.plot([-0.28, 0.28], [y, y+0.1], color=clr, lw=0.7)
            ax.text(0.5, -0.5, 'Taper', fontsize=7, color=clr, fontweight='bold')
        else:
            ax.fill([-0.3, 0.3, 0.3, -0.3], [0.5, 0.5, -1.8, -1.8],
                    color='white', ec=clr, lw=2)
            ax.text(0.5, -0.5, 'Legacy', fontsize=7, color=clr, fontweight='bold')

        ax.set_title(name, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm06_hole_wizard.png')


def m07_pattern_mirror():
    """Linear Pattern, Circular Pattern, Mirror Feature."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), facecolor=C['bg'])
    fig.suptitle('Pattern & Mirror Features', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.02)

    # Linear Pattern
    ax = axes[0]
    ax.set_xlim(-1, 7); ax.set_ylim(-1, 5)
    ax.set_aspect('equal'); ax.axis('off')

    for r in range(3):
        for c in range(5):
            clr = C['accent1'] if (r == 0 and c == 0) else C['accent2']
            fc = C['fill1'] if (r == 0 and c == 0) else C['fill2']
            ax.add_patch(plt.Circle((0.5 + c*1.2, 0.5 + r*1.5), 0.35,
                         lw=1.5, ec=clr, fc=fc, alpha=0.5))
    ax.annotate('', (6, -0.3), (0.5, -0.3),
               arrowprops=dict(arrowstyle='<->', color=C['dim'], lw=1))
    ax.text(3.25, -0.6, 'Dir 1: spacing × count', fontsize=7,
            ha='center', color=C['dim'])
    ax.annotate('', (-0.3, 3.5), (-0.3, 0.5),
               arrowprops=dict(arrowstyle='<->', color=C['dim'], lw=1))
    ax.text(-0.7, 2, 'Dir 2', fontsize=7, ha='center', color=C['dim'],
            rotation=90)
    ax.set_title('Linear Pattern\n5 × 3', fontsize=10, fontweight='bold',
                 color=C['line'])

    # Circular Pattern
    ax = axes[1]
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_aspect('equal'); ax.axis('off')

    ax.add_patch(plt.Circle((0, 0), 2.2, lw=1, ec=C['dim_line'],
                 fc='none', ls='--'))
    for i in range(8):
        ang = i * 45
        x = 2.2 * np.cos(np.radians(ang))
        y = 2.2 * np.sin(np.radians(ang))
        clr = C['accent1'] if i == 0 else C['accent3']
        fc = C['fill1'] if i == 0 else C['fill3']
        ax.add_patch(plt.Circle((x, y), 0.3, lw=1.5, ec=clr, fc=fc, alpha=0.5))
    ax.plot(0, 0, '+', color=C['accent5'], ms=12, mew=2)
    ax.text(0, -2.8, '8 × 45° = 360°', fontsize=8, ha='center',
            color=C['dim'], fontweight='bold')
    ax.set_title('Circular Pattern\n8 instances', fontsize=10,
                 fontweight='bold', color=C['line'])

    # Mirror
    ax = axes[2]
    ax.set_xlim(-4, 4); ax.set_ylim(-3, 3)
    ax.set_aspect('equal'); ax.axis('off')

    ax.plot([0, 0], [-2.5, 2.5], color=C['accent5'], lw=2, ls='dashdot')
    ax.text(0.15, 2.5, 'Mirror\nPlane', fontsize=7, color=C['accent5'])

    # Original side
    pts_o = [(-3, -1.5), (-1, -1.5), (-1, -0.5), (-2, -0.5),
             (-2, 0.5), (-1, 0.5), (-1, 1.5), (-3, 1.5)]
    ax.add_patch(Polygon(pts_o, closed=True, lw=2, ec=C['accent1'],
                 fc=C['fill1'], alpha=0.4))
    # Mirrored side
    pts_m = [(3, -1.5), (1, -1.5), (1, -0.5), (2, -0.5),
             (2, 0.5), (1, 0.5), (1, 1.5), (3, 1.5)]
    ax.add_patch(Polygon(pts_m, closed=True, lw=2, ec=C['accent2'],
                 fc=C['fill2'], alpha=0.4))
    ax.set_title('Mirror Feature', fontsize=10, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'm07_pattern_mirror.png')


def m08_end_conditions():
    """End Conditions: Blind, Through All, Up To Surface, Mid Plane."""
    fig, axes = plt.subplots(1, 4, figsize=(15, 4.5), facecolor=C['bg'])
    fig.suptitle('Extrude End Conditions', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.02)

    conditions = [
        ('Blind', 'Jarak tertentu (D)'),
        ('Through All', 'Tembus seluruhnya'),
        ('Up To Surface', 'Sampai permukaan'),
        ('Mid Plane', 'Simetris D/2 + D/2'),
    ]

    for ax, (name, desc) in zip(axes, conditions):
        ax.set_xlim(-2, 2); ax.set_ylim(-2, 2.5)
        ax.set_aspect('equal'); ax.axis('off')

        # Base rectangle
        ax.add_patch(patches.Rectangle((-1.5, -1.5), 3, 2.5, lw=2,
                     ec=C['steel'], fc=C['alu'], alpha=0.15))

        if name == 'Blind':
            ax.add_patch(patches.Rectangle((-0.5, -1.5), 1, 1.5, lw=2,
                         ec=C['accent1'], fc=C['fill1'], alpha=0.5))
            dim_line(ax, (0.7, -1.5), (0.7, 0), 'D', color=C['accent1'])
        elif name == 'Through All':
            ax.add_patch(patches.Rectangle((-0.5, -1.5), 1, 2.5, lw=2,
                         ec=C['accent2'], fc=C['fill2'], alpha=0.5))
            ax.text(0, 0.3, '↕', fontsize=20, ha='center', color=C['accent2'])
        elif name == 'Up To Surface':
            ax.plot([-1.5, 1.5], [0.3, 0.3], color=C['accent3'], lw=2, ls='--')
            ax.add_patch(patches.Rectangle((-0.5, -1.5), 1, 1.8, lw=2,
                         ec=C['accent3'], fc=C['fill3'], alpha=0.5))
            ax.text(1.6, 0.3, 'Surface', fontsize=7, color=C['accent3'])
        elif name == 'Mid Plane':
            ax.plot([-1.5, 1.5], [-0.25, -0.25], color=C['accent4'], lw=1.5, ls='dashdot')
            ax.add_patch(patches.Rectangle((-0.5, -1.5), 1, 2.5, lw=2,
                         ec=C['accent4'], fc=C['fill4'], alpha=0.5))
            dim_line(ax, (0.7, -0.25), (0.7, 1), 'D/2', color=C['accent4'])
            dim_line(ax, (0.7, -1.5), (0.7, -0.25), 'D/2', color=C['accent4'])

        ax.set_title(f'{name}', fontsize=10, fontweight='bold', color=C['line'])
        ax.text(0, -1.9, desc, fontsize=7, ha='center', color=C['steel'])

    fig.tight_layout()
    save(fig, 'm08_end_conditions.png')


def m09_feature_tree():
    """Feature Manager Design Tree — urutan dan organisasi."""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor=C['bg'])
    make_header(ax, 'Feature Manager Design Tree')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')

    tree_items = [
        ('📦 Part1', 0, C['line'], True),
        ('  📐 Front Plane', 1, C['steel'], False),
        ('  📐 Top Plane', 1, C['steel'], False),
        ('  📐 Right Plane', 1, C['steel'], False),
        ('  ⊕ Origin', 1, C['steel'], False),
        ('  🟦 Boss-Extrude1 (Base)', 1, C['accent1'], True),
        ('  🟦 Boss-Extrude2 (Raised)', 1, C['accent2'], True),
        ('  🔴 Cut-Extrude1 (Hole)', 1, C['accent5'], True),
        ('  🟡 Fillet1 (R5)', 1, C['accent3'], True),
        ('  🟡 Chamfer1 (2mm)', 1, C['accent3'], True),
        ('  🔵 CirPattern1 (4x)', 1, C['accent4'], True),
        ('  🔴 Cut-Extrude2 (Slot)', 1, C['accent5'], True),
        ('  ⚙️ Material: Al 6061', 1, C['steel'], False),
    ]

    for i, (text, indent, color, is_feature) in enumerate(tree_items):
        y = 8.8 - i * 0.6
        x = 1 + indent * 0.3

        if is_feature:
            ax.add_patch(FancyBboxPatch((x-0.1, y-0.2), 5.5, 0.4,
                         boxstyle='round,pad=0.05', fc='#F5F5F5' if i % 2 == 0 else 'white',
                         ec=color, lw=1, alpha=0.5))

        ax.text(x, y, text, fontsize=9, va='center', color=color,
                fontweight='bold' if is_feature else 'normal')

    # Tips
    tips = [
        '💡 Beri nama deskriptif pada setiap feature',
        '💡 Boss dulu, baru Cut',
        '💡 Fillet/Chamfer terakhir',
        '💡 Feature urut = history-based',
    ]
    for i, tip in enumerate(tips):
        ax.text(7, 7 - i*0.6, tip, fontsize=8, color=C['accent2'])

    fig.tight_layout()
    save(fig, 'm09_feature_tree.png')


def m10_tips_3d():
    """Tips pembuatan Feature 3D."""
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=C['bg'])
    make_header(ax, 'Tips Pembuatan Feature 3D')
    ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis('off')

    tips = [
        ('1', 'Base Feature', 'Selalu mulai dengan feature utama\nyang mendefinisikan bentuk dasar',
         C['accent1']),
        ('2', 'Boss → Cut', 'Buat semua Boss (tambah material)\nsebelum Cut (kurangi material)',
         C['accent2']),
        ('3', 'Fillet/Chamfer', 'Tambahkan fillet dan chamfer\nsetelah semua feature utama selesai',
         C['accent3']),
        ('4', 'Feature Tree', 'Beri nama deskriptif\npada setiap feature',
         C['accent4']),
        ('5', 'Reference Geometry', 'Gunakan plane tambahan\njika diperlukan',
         C['dim']),
        ('6', 'End Condition', 'Pilih end condition sesuai\ndesign intent (Through All vs Blind)',
         C['accent5']),
    ]

    for i, (num, title, desc, color) in enumerate(tips):
        col = i % 2; row = i // 2
        x = 1 + col * 5.5; y = 6.5 - row * 2.2

        ax.add_patch(FancyBboxPatch((x-0.3, y-0.7), 5, 1.8,
                     boxstyle='round,pad=0.15', facecolor='white',
                     edgecolor=color, lw=2))

        ax.add_patch(plt.Circle((x+0.2, y+0.5), 0.35, fc=color, ec='white', lw=2))
        ax.text(x+0.2, y+0.5, num, fontsize=12, ha='center', va='center',
                color='white', fontweight='bold')
        ax.text(x+0.9, y+0.5, title, fontsize=10, fontweight='bold', color=color)
        ax.text(x+0.9, y-0.2, desc, fontsize=8, color=C['line'])

    fig.tight_layout()
    save(fig, 'm10_tips_3d.png')


def m11_isometric_demo():
    """Demo: box isometric menunjukkan extrude dari sketch ke 3D."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), facecolor=C['bg'])
    fig.suptitle('Dari Sketch 2D → Feature 3D', fontsize=14,
                 fontweight='bold', color=C['header'], y=1.02)

    # Step 1: Sketch
    ax = axes[0]
    ax.set_xlim(-4, 5); ax.set_ylim(-2, 5)
    ax.set_aspect('equal'); ax.axis('off')
    # Draw sketch on front plane
    sk_pts = [iso(0, 0, 0), iso(4, 0, 0), iso(4, 0, 3), iso(0, 0, 3)]
    sx = [p[0] for p in sk_pts]; sy = [p[1] for p in sk_pts]
    ax.fill(sx, sy, color=C['fill1'], ec=C['accent1'], lw=2.5, alpha=0.4)
    ax.text(0, -1.5, 'Sketch 2D\n(di Plane)', fontsize=9, ha='center',
            color=C['accent1'], fontweight='bold')
    ax.set_title('① Sketch', fontsize=11, fontweight='bold', color=C['line'])

    # Step 2: Extrude
    ax = axes[1]
    ax.set_xlim(-4, 5); ax.set_ylim(-2, 5)
    ax.set_aspect('equal'); ax.axis('off')
    # Ghost sketch
    ax.fill(sx, sy, color=C['fill1'], ec=C['accent1'], lw=1, alpha=0.2)
    # Arrow
    p1 = iso(2, 0, 1.5); p2 = iso(2, 2, 1.5)
    ax.annotate('', p2, p1,
               arrowprops=dict(arrowstyle='->', color=C['accent2'], lw=2.5))
    ax.text(p2[0]+0.5, p2[1], 'Extrude\n30mm', fontsize=9,
            color=C['accent2'], fontweight='bold')
    ax.set_title('② Extrude', fontsize=11, fontweight='bold', color=C['line'])

    # Step 3: Result
    ax = axes[2]
    ax.set_xlim(-4, 5); ax.set_ylim(-2, 5)
    ax.set_aspect('equal'); ax.axis('off')
    draw_iso_box(ax, 0, 0, 0, 4, 2, 3)
    ax.text(0, -1.5, 'Solid 3D\n80 × 50 × 30 mm', fontsize=9, ha='center',
            color=C['accent2'], fontweight='bold')
    ax.set_title('③ Result', fontsize=11, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'm11_isometric_demo.png')


# ══════════════════════════════════════════════════════════════
#  PROJECT ILLUSTRATIONS
# ══════════════════════════════════════════════════════════════

def p01_clamp_assembly_overview():
    """Project A: Overview Clamp Assembly — 5 parts."""
    fig, ax = plt.subplots(figsize=(14, 7), facecolor=C['bg'])
    make_header(ax, 'Project A — Clamp Assembly (5 Parts)')
    ax.set_xlim(0, 14); ax.set_ylim(0, 7); ax.axis('off')

    parts = [
        ('1. Base Clamp', 'Extrude + Shell\n+ Pattern',
         '100×60×10mm\n4× Ø8mm holes\nBoss Ø30×5mm', C['accent1']),
        ('2. Clamp Arm', 'Extrude + Fillet\n+ Chamfer',
         '120×20×10mm\nØ12mm pivot hole\nSlot 30×8mm', C['accent2']),
        ('3. Pressure Pad', 'Revolve',
         'Ø20×10mm\nFillet R3\nM6 thread', C['accent3']),
        ('4. Pivot Pin', 'Revolve + Chamfer',
         'Ø12×25mm\nChamfer 1×45°\nCirclip groove', C['accent4']),
        ('5. Knob', 'Revolve + Pattern',
         'Ø25mm\nKnurling pattern', C['accent5']),
    ]

    for i, (name, features, spec, color) in enumerate(parts):
        x = 1.3 + i * 2.4
        ax.add_patch(FancyBboxPatch((x-1, 1.0), 2.2, 4.5,
                     boxstyle='round,pad=0.15', facecolor='white',
                     edgecolor=color, lw=2))

        # Number circle
        ax.add_patch(plt.Circle((x+0.1, 5.0), 0.3, fc=color, ec='white', lw=2))
        ax.text(x+0.1, 5.0, str(i+1), fontsize=11, ha='center', va='center',
                color='white', fontweight='bold')

        ax.text(x+0.1, 4.3, name.split('. ')[1], fontsize=10,
                ha='center', fontweight='bold', color=color)
        ax.text(x+0.1, 3.5, features, fontsize=7, ha='center',
                color=C['steel'], linespacing=1.4)
        ax.text(x+0.1, 2.0, spec, fontsize=7, ha='center',
                color=C['line'], linespacing=1.4,
                bbox=dict(boxstyle='round,pad=0.1', fc=C['panel'], ec=C['steel'], alpha=0.5))

    fig.tight_layout()
    save(fig, 'p01_clamp_assembly_overview.png')


def p02_clamp_base():
    """Project A Part 1: Base Clamp isometric."""
    fig, ax = plt.subplots(figsize=(10, 7), facecolor=C['bg'])
    make_header(ax, 'Part 1 — Base Clamp')
    ax.set_xlim(-6, 8); ax.set_ylim(-3, 7)
    ax.set_aspect('equal'); ax.axis('off')

    # Base plate
    draw_iso_box(ax, 0, 0, 0, 5, 0.5, 3)

    # Raised boss (cylinder on top)
    draw_iso_cylinder_top(ax, 2.5, 0.5, 1.5, 0.8, 0.3, color=C['fill2'],
                         ec=C['accent2'])

    # 4 mounting holes (circles on top face)
    for hx, hz in [(0.5, 0.5), (4.5, 0.5), (0.5, 2.5), (4.5, 2.5)]:
        cx, cy = iso(hx, 0.5, hz)
        ax.add_patch(plt.Circle((cx, cy), 0.12, fc='white', ec=C['accent5'], lw=1.5, zorder=5))

    # Annotations
    ax.text(-4, 5, 'Base Plate:\n100×60×10mm', fontsize=9, color=C['accent1'],
            bbox=dict(boxstyle='round', fc=C['fill1'], ec=C['accent1']))
    ax.text(-4, 3.5, '4× Ø8mm holes', fontsize=9, color=C['accent5'])
    ax.text(-4, 2.5, 'Boss Ø30×5mm', fontsize=9, color=C['accent2'])
    ax.text(-4, 1.5, 'Features:\nExtrude + Pattern', fontsize=8, color=C['steel'])

    fig.tight_layout()
    save(fig, 'p02_clamp_base.png')


def p03_clamp_arm():
    """Project A Part 2: Clamp Arm."""
    fig, ax = plt.subplots(figsize=(10, 7), facecolor=C['bg'])
    make_header(ax, 'Part 2 — Clamp Arm')
    ax.set_xlim(-6, 8); ax.set_ylim(-3, 7)
    ax.set_aspect('equal'); ax.axis('off')

    # Arm body
    draw_iso_box(ax, 0, 0, 0, 6, 0.5, 1)

    # Pivot hole (left end)
    cx1, cy1 = iso(0.5, 0.5, 0.5)
    ax.add_patch(plt.Circle((cx1, cy1), 0.18, fc='white', ec=C['accent5'], lw=2, zorder=5))

    # Slot (right end) — simplified as elongated hole
    for dx in [4.5, 5.0, 5.5]:
        cx, cy = iso(dx, 0.5, 0.5)
        ax.add_patch(plt.Circle((cx, cy), 0.1, fc='white', ec=C['accent3'], lw=1, zorder=5))

    # Annotations
    ax.text(-4, 5, 'Clamp Arm:\n120×20×10mm', fontsize=9, color=C['accent1'],
            bbox=dict(boxstyle='round', fc=C['fill1'], ec=C['accent1']))
    ax.text(-4, 3.5, 'Ø12mm pivot hole', fontsize=9, color=C['accent5'])
    ax.text(-4, 2.5, 'Slot 30×8mm', fontsize=9, color=C['accent3'])
    ax.text(-4, 1.5, 'Fillet R5 all edges', fontsize=8, color=C['accent2'])

    fig.tight_layout()
    save(fig, 'p03_clamp_arm.png')


def p04_clamp_revolve_parts():
    """Project A Parts 3-5: Pressure Pad, Pivot Pin, Knob (Revolve)."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), facecolor=C['bg'])
    fig.suptitle('Clamp Revolve Parts', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.02)

    # Pressure Pad
    ax = axes[0]
    ax.set_xlim(-3, 3); ax.set_ylim(-2, 4)
    ax.set_aspect('equal'); ax.axis('off')
    # Profile
    pad_x = [-1, 1, 1, 0.7, -0.7, -1]
    pad_y = [0, 0, 1.5, 1.5, 1.5, 1.5]
    ax.fill(pad_x, pad_y, color=C['fill3'], ec=C['accent3'], lw=2, alpha=0.5)
    # Fillet at bottom
    ax.add_patch(Arc((-0.7, 0.3), 0.6, 0.6, theta1=180, theta2=270,
                 color=C['accent2'], lw=2))
    ax.add_patch(Arc((0.7, 0.3), 0.6, 0.6, theta1=270, theta2=360,
                 color=C['accent2'], lw=2))
    ax.plot([0, 0], [-0.5, 2], color=C['accent5'], lw=1, ls='dashdot')
    ax.text(0, 2.5, 'Pressure Pad\nØ20×10mm', fontsize=9, ha='center',
            color=C['accent3'], fontweight='bold')
    ax.set_title('Part 3: Pressure Pad', fontsize=10, fontweight='bold', color=C['line'])

    # Pivot Pin
    ax = axes[1]
    ax.set_xlim(-3, 3); ax.set_ylim(-2, 4)
    ax.set_aspect('equal'); ax.axis('off')
    # Stepped profile
    ax.fill([-0.6, 0.6, 0.6, -0.6], [0, 0, 3, 3],
            color=C['fill4'], ec=C['accent4'], lw=2, alpha=0.5)
    # Chamfers
    ax.fill([0.4, 0.6, 0.6], [3, 2.8, 3], color='white', ec=C['accent4'], lw=1)
    ax.fill([-0.4, -0.6, -0.6], [3, 2.8, 3], color='white', ec=C['accent4'], lw=1)
    ax.fill([0.4, 0.6, 0.6], [0, 0.2, 0], color='white', ec=C['accent4'], lw=1)
    ax.fill([-0.4, -0.6, -0.6], [0, 0.2, 0], color='white', ec=C['accent4'], lw=1)
    # Groove
    ax.add_patch(patches.Rectangle((-0.7, 1.2), 1.4, 0.15, lw=1,
                 ec=C['accent5'], fc=C['cut_fill']))
    ax.plot([0, 0], [-0.5, 3.5], color=C['accent5'], lw=1, ls='dashdot')
    ax.text(0, -1, 'Pivot Pin\nØ12×25mm', fontsize=9, ha='center',
            color=C['accent4'], fontweight='bold')
    ax.set_title('Part 4: Pivot Pin', fontsize=10, fontweight='bold', color=C['line'])

    # Knob
    ax = axes[2]
    ax.set_xlim(-3, 3); ax.set_ylim(-2, 4)
    ax.set_aspect('equal'); ax.axis('off')
    # Knob profile
    theta = np.linspace(0, 2*np.pi, 36, endpoint=False)
    r_knob = 1.2 + 0.15 * np.sin(18 * theta)  # Knurling pattern
    x_knob = r_knob * np.cos(theta)
    y_knob = 1.5 + r_knob * np.sin(theta)
    ax.fill(x_knob, y_knob, color=C['fill1'], ec=C['accent1'], lw=1.5, alpha=0.5)
    ax.add_patch(plt.Circle((0, 1.5), 0.4, fc='white', ec=C['accent5'], lw=1.5))
    ax.text(0, -0.5, 'Knob\nØ25mm', fontsize=9, ha='center',
            color=C['accent1'], fontweight='bold')
    ax.set_title('Part 5: Knob', fontsize=10, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'p04_clamp_revolve_parts.png')


def p05_profil_aluminium_3d():
    """Project B: Profil Aluminium 3D — extrude dari sketch."""
    fig, axes = plt.subplots(1, 4, figsize=(16, 5), facecolor=C['bg'])
    fig.suptitle('Project B — Profil Aluminium 3D (Extrude)', fontsize=14,
                 fontweight='bold', color=C['header'], y=1.02)

    profiles = [
        ('2020', 200, 10),
        ('3030', 300, 15),
        ('4040', 400, 20),
        ('4080', 500, 20),
    ]

    for ax, (name, length, half_w) in zip(axes, profiles):
        ax.set_xlim(-5, 7); ax.set_ylim(-3, 6)
        ax.set_aspect('equal'); ax.axis('off')

        # Simplified isometric profile + extrusion
        s = half_w / 20  # scale factor
        draw_iso_box(ax, 0, 0, 0, 2*s, 4, 2*s if '80' not in name else 4*s,
                    fc_top=C['alu'], fc_front='#B0BEC5', fc_right='#90A4AE')

        # T-slot indicators on front face
        p_mid = iso(s, 2, 0)
        ax.plot([p_mid[0]-0.15, p_mid[0]+0.15], [p_mid[1], p_mid[1]],
                color=C['accent1'], lw=2)

        ax.text(0, -2, f'Profil {name}\n{length}mm', fontsize=9,
                ha='center', color=C['accent2'], fontweight='bold')

        w = half_w * 2
        h = half_w * 2 if '80' not in name else half_w * 4
        ax.text(0, -2.8, f'{w}×{h}mm', fontsize=8, ha='center', color=C['dim'])

        ax.set_title(name, fontsize=10, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'p05_profil_aluminium_3d.png')


def p06_profil_extrude_workflow():
    """Project B: Workflow extrude profil: Sketch → Extrude → Chamfer → Material."""
    fig, ax = plt.subplots(figsize=(14, 5), facecolor=C['bg'])
    make_header(ax, 'Workflow Extrude Profil Aluminium')
    ax.set_xlim(0, 14); ax.set_ylim(0, 5); ax.axis('off')

    steps = [
        ('1. Import/Copy\nSketch M02', C['accent1']),
        ('2. Extrude\nBoss/Base', C['accent2']),
        ('3. Chamfer\nUjung', C['accent3']),
        ('4. Cut Through\nCenter Bore', C['accent5']),
        ('5. Assign\nMaterial', C['accent4']),
        ('6. Mass\nProperties', C['dim']),
    ]

    for i, (label, color) in enumerate(steps):
        x = 1.1 + i * 2.1
        ax.add_patch(FancyBboxPatch((x-0.85, 1.5), 1.7, 2.0,
                     boxstyle='round,pad=0.15', facecolor='white',
                     edgecolor=color, lw=2))
        ax.text(x, 2.5, label, fontsize=8, ha='center', va='center',
                color=color, fontweight='bold')
        if i < len(steps) - 1:
            ax.annotate('', (x+1.15, 2.5), (x+0.9, 2.5),
                       arrowprops=dict(arrowstyle='->', color=C['steel'], lw=1.5))

    ax.text(7, 0.8, 'Material: Aluminum 6063-T5 | Chamfer: 0.5×45° (2020/3030) atau 1×45° (4040/4080)',
            fontsize=8, ha='center', color=C['accent2'], fontstyle='italic',
            bbox=dict(boxstyle='round', fc=C['fill2'], ec=C['accent2']))

    fig.tight_layout()
    save(fig, 'p06_profil_extrude_workflow.png')


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('='*60)
    print(' MODUL 03 — Generating Images')
    print('='*60)

    print('\n📚 Materi:')
    m01_feature_based_workflow()
    m02_extrude_boss_cut()
    m03_revolve()
    m04_fillet_chamfer()
    m05_shell_draft()
    m06_hole_wizard()
    m07_pattern_mirror()
    m08_end_conditions()
    m09_feature_tree()
    m10_tips_3d()
    m11_isometric_demo()

    print('\n📐 Project:')
    p01_clamp_assembly_overview()
    p02_clamp_base()
    p03_clamp_arm()
    p04_clamp_revolve_parts()
    p05_profil_aluminium_3d()
    p06_profil_extrude_workflow()

    print('\n' + '='*60)
    print(f' ✅ Total: 17 gambar berhasil dibuat di image/')
    print('='*60)
