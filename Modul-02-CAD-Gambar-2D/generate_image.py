#!/usr/bin/env python3
"""
Generate Image — Modul 02: CAD Gambar 2D
==========================================
Script untuk membuat semua ilustrasi materi dan project Modul 2.
Gambar disimpan di subfolder image/ dengan format:
  - m##_deskripsi.png  → ilustrasi materi
  - p##_deskripsi.png  → ilustrasi project
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Arc, Wedge, Polygon
import matplotlib.patheffects as pe

# ── Konfigurasi ──────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image')
os.makedirs(OUTPUT_DIR, exist_ok=True)
DPI = 150

# Warna tema
C = {
    'bg':       '#FFFFFF',
    'grid':     '#E8E8E8',
    'line':     '#1A1A2E',
    'dim':      '#0066CC',
    'dim_line': '#4A90D9',
    'fully':    '#000000',
    'under':    '#0066FF',
    'over':     '#FF3300',
    'constr':   '#FF8C00',
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
}


def save(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'  ✅ {filename}')


def make_header(ax, text, y=0.97):
    ax.text(0.5, y, text, transform=ax.transAxes, fontsize=14, fontweight='bold',
            ha='center', va='top', color=C['header'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=C['header'], lw=1.5))


def dim_line(ax, p1, p2, text, offset=0, color=None, fontsize=8):
    if color is None:
        color = C['dim']
    mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
    ax.annotate('', xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle='<->', color=color, lw=1))
    ax.text(mx, my+offset, text, fontsize=fontsize, ha='center', va='bottom',
            color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='none', alpha=0.8))


# ══════════════════════════════════════════════════════════════
#  MATERI ILLUSTRATIONS
# ══════════════════════════════════════════════════════════════

def m01_sketch_entities_overview():
    """Ringkasan entitas sketch: Line, Rect, Circle, Arc, dsb."""
    fig, axes = plt.subplots(3, 4, figsize=(14, 10), facecolor=C['bg'])
    fig.suptitle('MODUL 2 — Entitas Sketch (Sketch Entities)', fontsize=16,
                 fontweight='bold', color=C['header'], y=0.98)

    entities = [
        ('Line', 'accent1'), ('Rectangle', 'accent2'), ('Circle', 'accent3'), ('Arc', 'accent4'),
        ('Polygon', 'accent1'), ('Ellipse', 'accent2'), ('Slot', 'accent3'), ('Spline', 'accent4'),
        ('Point', 'accent1'), ('Centerline', 'accent5'), ('Text', 'accent2'), ('Construction', 'constr'),
    ]

    for ax, (name, col) in zip(axes.flat, entities):
        ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
        ax.set_aspect('equal'); ax.axis('off')
        cc = C[col]

        if name == 'Line':
            ax.plot([-0.8, 0.8], [-0.6, 0.6], color=cc, lw=2.5)
            ax.plot([-0.8, 0.3], [0.2, -0.8], color=cc, lw=2.5)
            ax.plot([0.3, 0.8], [-0.8, 0.2], color=cc, lw=2.5)
        elif name == 'Rectangle':
            ax.add_patch(patches.Rectangle((-0.7, -0.5), 1.4, 1.0, lw=2.5,
                         edgecolor=cc, facecolor=C['fill1'], alpha=0.4))
        elif name == 'Circle':
            ax.add_patch(plt.Circle((0, 0), 0.7, lw=2.5, edgecolor=cc,
                         facecolor=C['fill3'], alpha=0.3))
            ax.plot(0, 0, '+', color=cc, markersize=10, mew=1.5)
        elif name == 'Arc':
            ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=30, theta2=150, color=cc, lw=2.5))
            ax.plot(0, 0, '+', color=cc, markersize=8, mew=1)
        elif name == 'Polygon':
            angles = np.linspace(0, 2*np.pi, 6, endpoint=False) + np.pi/6
            xs, ys = 0.7*np.cos(angles), 0.7*np.sin(angles)
            ax.add_patch(Polygon(np.column_stack([xs, ys]), closed=True, lw=2.5,
                         edgecolor=cc, facecolor=C['fill2'], alpha=0.3))
        elif name == 'Ellipse':
            ax.add_patch(patches.Ellipse((0, 0), 1.4, 0.8, lw=2.5,
                         edgecolor=cc, facecolor=C['fill4'], alpha=0.3))
        elif name == 'Slot':
            ax.add_patch(FancyBboxPatch((-0.7, -0.25), 1.4, 0.5,
                         boxstyle='round,pad=0.25', lw=2.5, edgecolor=cc,
                         facecolor=C['fill1'], alpha=0.3))
        elif name == 'Spline':
            t = np.linspace(-0.8, 0.8, 100)
            y = 0.5*np.sin(2*np.pi*t/1.6) + 0.2*np.sin(4*np.pi*t/1.6)
            ax.plot(t, y, color=cc, lw=2.5)
        elif name == 'Point':
            ax.plot([-0.5, 0, 0.5, 0, -0.3, 0.3],
                    [0.5, 0.7, 0.3, -0.2, -0.6, -0.5], 'o', color=cc, ms=8)
        elif name == 'Centerline':
            ax.plot([-0.9, 0.9], [0, 0], color=cc, lw=1.5, ls='dashdot')
            ax.plot([0, 0], [-0.9, 0.9], color=cc, lw=1.5, ls='dashdot')
        elif name == 'Text':
            ax.text(0, 0, 'CAD', fontsize=28, ha='center', va='center',
                    fontweight='bold', color=cc)
        elif name == 'Construction':
            ax.plot([-0.8, 0.8], [-0.5, 0.5], color=cc, lw=1.5, ls='--')
            ax.add_patch(plt.Circle((0, 0), 0.6, lw=1.5, edgecolor=cc,
                         facecolor='none', linestyle='--'))

        ax.set_title(name, fontsize=10, fontweight='bold', color=C['line'], pad=2)

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm01_sketch_entities_overview.png')


def m02_rectangle_types():
    """5 tipe Rectangle."""
    fig, axes = plt.subplots(1, 5, figsize=(15, 3.5), facecolor=C['bg'])
    fig.suptitle('Tipe-tipe Rectangle', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.02)

    types = ['Corner\nRectangle', 'Center\nRectangle', '3-Point\nCorner',
             '3-Point\nCenter', 'Parallelogram']
    colors = [C['accent1'], C['accent2'], C['accent3'], C['accent4'], C['accent1']]

    for ax, name, clr in zip(axes, types, colors):
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.2, 1.2)
        ax.set_aspect('equal'); ax.axis('off')

        if 'Corner' == name.split('\n')[0]:
            ax.add_patch(patches.Rectangle((-1, -0.7), 2, 1.4, lw=2, ec=clr,
                         fc=C['fill1'], alpha=0.3))
            ax.plot(-1, -0.7, 'o', color=C['accent5'], ms=8, zorder=5)
            ax.plot(1, 0.7, 's', color=C['accent2'], ms=8, zorder=5)
            ax.text(-1.2, -1, 'P1', fontsize=8, color=C['accent5'], fontweight='bold')
            ax.text(1.1, 0.8, 'P2', fontsize=8, color=C['accent2'], fontweight='bold')
        elif 'Center' == name.split('\n')[0] and '3' not in name:
            ax.add_patch(patches.Rectangle((-1, -0.7), 2, 1.4, lw=2, ec=clr,
                         fc=C['fill2'], alpha=0.3))
            ax.plot(0, 0, '+', color=C['accent5'], ms=12, mew=2, zorder=5)
        elif '3-Point' in name and 'Corner' in name:
            pts = [(-1, -0.5), (0.8, -0.7), (1.1, 0.6), (-0.7, 0.8)]
            ax.add_patch(Polygon(pts, closed=True, lw=2, ec=clr, fc=C['fill3'], alpha=0.3))
            for i, p in enumerate(pts[:3]):
                ax.plot(*p, 'o', color=C['accent5'], ms=7, zorder=5)
        elif '3-Point' in name and 'Center' in name:
            pts = [(-0.9, -0.5), (0.9, -0.5), (0.9, 0.5), (-0.9, 0.5)]
            ax.add_patch(Polygon(pts, closed=True, lw=2, ec=clr, fc=C['fill4'], alpha=0.3))
            ax.plot(0, 0, '+', color=C['accent5'], ms=12, mew=2, zorder=5)
        else:
            pts = [(-0.6, -0.6), (1.0, -0.6), (0.6, 0.6), (-1.0, 0.6)]
            ax.add_patch(Polygon(pts, closed=True, lw=2, ec=clr, fc=C['fill1'], alpha=0.3))

        ax.set_title(name, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'm02_rectangle_types.png')


def m03_circle_arc_types():
    """Tipe Circle dan Arc."""
    fig, axes = plt.subplots(1, 5, figsize=(15, 3.5), facecolor=C['bg'])
    fig.suptitle('Tipe Circle dan Arc', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.02)

    titles = ['Center Circle', '3-Point Circle', 'Centerpoint Arc',
              'Tangent Arc', '3-Point Arc']
    for ax, title in zip(axes, titles):
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal'); ax.axis('off')

        if title == 'Center Circle':
            ax.add_patch(plt.Circle((0, 0), 0.9, lw=2.5, ec=C['accent1'],
                         fc=C['fill1'], alpha=0.3))
            ax.plot(0, 0, '+', color=C['accent5'], ms=10, mew=2)
            ax.plot([0, 0.9], [0, 0], '--', color=C['dim'], lw=1)
            ax.text(0.45, 0.12, 'R', fontsize=9, color=C['dim'], fontweight='bold')
        elif title == '3-Point Circle':
            ax.add_patch(plt.Circle((0, 0), 0.9, lw=2.5, ec=C['accent2'],
                         fc=C['fill2'], alpha=0.3))
            for ang in [0, 120, 240]:
                ax.plot(0.9*np.cos(np.radians(ang)), 0.9*np.sin(np.radians(ang)),
                        'o', color=C['accent5'], ms=8, zorder=5)
        elif title == 'Centerpoint Arc':
            ax.add_patch(Arc((0, 0), 1.8, 1.8, theta1=20, theta2=160,
                         color=C['accent3'], lw=2.5))
            ax.plot(0, 0, '+', color=C['accent5'], ms=10, mew=2)
        elif title == 'Tangent Arc':
            ax.plot([-1.2, 0], [0, 0], color=C['steel'], lw=2)
            ax.add_patch(Arc((0, 0.7), 1.4, 1.4, theta1=220, theta2=360,
                         color=C['accent4'], lw=2.5))
            ax.text(-0.3, -0.4, 'Tangent', fontsize=7, color=C['accent4'],
                    fontstyle='italic')
        else:
            ax.add_patch(Arc((0, 0.2), 1.6, 1.6, theta1=200, theta2=340,
                         color=C['accent1'], lw=2.5))
            for ang in [200, 270, 340]:
                ax.plot(0.8*np.cos(np.radians(ang)),
                        0.2 + 0.8*np.sin(np.radians(ang)),
                        'o', color=C['accent5'], ms=8, zorder=5)

        ax.set_title(title, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'm03_circle_arc_types.png')


def m04_sketch_status():
    """Status sketch: Fully Defined, Under Defined, Over Defined."""
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5), facecolor=C['bg'])
    fig.suptitle('Status Sketch', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.0)

    statuses = [
        ('Fully Defined', C['fully'], C['fill2'],
         '✅ Semua garis HITAM\nPosisi & ukuran terkunci'),
        ('Under Defined', C['under'], C['fill1'],
         '⚠️ Garis BIRU\nMasih bisa digeser'),
        ('Over Defined', C['over'], '#FFCDD2',
         '❌ Garis MERAH\nTerlalu banyak constraint'),
    ]

    for ax, (title, color, bgc, desc) in zip(axes, statuses):
        ax.set_xlim(-2, 2); ax.set_ylim(-2, 2.5)
        ax.set_aspect('equal'); ax.axis('off')
        ax.set_facecolor(bgc)

        ax.add_patch(patches.Rectangle((-1.2, -0.8), 2.4, 1.6, lw=3,
                     ec=color, fc='none'))
        ax.add_patch(plt.Circle((0, 0), 0.5, lw=3, ec=color, fc='none'))

        if title == 'Fully Defined':
            dim_line(ax, (-1.2, -1.3), (1.2, -1.3), '60mm', 0.05, color)
            dim_line(ax, (1.6, -0.8), (1.6, 0.8), '40mm', 0.05, color)
        elif title == 'Under Defined':
            dim_line(ax, (-1.2, -1.3), (1.2, -1.3), '60mm', 0.05, color)
            ax.text(1.5, 0, '?', fontsize=18, color=color, fontweight='bold', ha='center')
        else:
            dim_line(ax, (-1.2, -1.3), (1.2, -1.3), '60mm', 0.05, color)
            dim_line(ax, (1.6, -0.8), (1.6, 0.8), '40mm', 0.05, color)
            dim_line(ax, (-1.2, 1.1), (1.2, 1.1), '60mm', 0.05, color)
            ax.text(0, 1.7, 'KONFLIK!', fontsize=9, color=color,
                    fontweight='bold', ha='center')

        ax.set_title(title, fontsize=12, fontweight='bold', color=color, pad=8)
        ax.text(0, -1.8, desc, fontsize=8, ha='center', va='top', color=color,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=color, alpha=0.9))

    fig.tight_layout()
    save(fig, 'm04_sketch_status.png')


def m05_sketch_tools():
    """Sketch Tools: Trim, Extend, Offset, Mirror, Pattern, Fillet, dsb."""
    fig, axes = plt.subplots(2, 4, figsize=(14, 7), facecolor=C['bg'])
    fig.suptitle('Sketch Tools', fontsize=14, fontweight='bold',
                 color=C['header'], y=0.99)

    tools = ['Trim', 'Extend', 'Offset', 'Convert Entities',
             'Mirror', 'Move/Copy', 'Linear Pattern', 'Sketch Fillet']

    for ax, tool in zip(axes.flat, tools):
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal'); ax.axis('off')

        if tool == 'Trim':
            ax.plot([-1, 1], [0, 0], color=C['accent1'], lw=2)
            ax.plot([0, 0], [-1, 1], color=C['accent1'], lw=2)
            ax.plot([0, 0], [0, 1], color=C['accent5'], lw=3, ls='--', alpha=0.5)
            ax.text(0.2, 0.5, '✂', fontsize=16)
        elif tool == 'Extend':
            ax.plot([-1, 0], [0, 0], color=C['accent1'], lw=2)
            ax.plot([0, 1], [0, 0], color=C['accent2'], lw=2, ls='--')
            ax.plot([1, 1], [-0.8, 0.8], color=C['steel'], lw=2)
            ax.text(0.5, 0.15, '→', fontsize=14, color=C['accent2'])
        elif tool == 'Offset':
            ax.add_patch(patches.Rectangle((-0.8, -0.5), 1.6, 1.0, lw=2,
                         ec=C['accent1'], fc='none'))
            ax.add_patch(patches.Rectangle((-1.1, -0.8), 2.2, 1.6, lw=2,
                         ec=C['accent3'], fc='none', ls='--'))
            ax.text(-1.3, 0.65, 'd', fontsize=9, color=C['accent3'], fontweight='bold')
        elif tool == 'Convert Entities':
            ax.plot([-0.8, 0.8], [-0.3, -0.3], color=C['steel'], lw=2.5)
            ax.plot([-0.8, 0.8], [0.3, 0.3], color=C['accent2'], lw=2.5, ls='--')
            ax.annotate('', (0, 0.3), (0, -0.3),
                       arrowprops=dict(arrowstyle='->', color=C['accent4'], lw=1.5))
        elif tool == 'Mirror':
            ax.plot([0, 0], [-1, 1], color=C['accent5'], lw=1.5, ls='dashdot')
            ax.add_patch(Polygon([(-1, -0.5), (-0.3, -0.5), (-0.3, 0.5), (-1, 0.5)],
                         closed=True, lw=2, ec=C['accent1'], fc=C['fill1'], alpha=0.3))
            ax.add_patch(Polygon([(1, -0.5), (0.3, -0.5), (0.3, 0.5), (1, 0.5)],
                         closed=True, lw=2, ec=C['accent2'], fc=C['fill2'], alpha=0.3))
            ax.text(0, -1.1, 'Centerline', fontsize=7, ha='center', color=C['accent5'])
        elif tool == 'Move/Copy':
            ax.add_patch(patches.Rectangle((-1.2, -0.3), 0.8, 0.6, lw=2,
                         ec=C['steel'], fc=C['fill1'], alpha=0.3))
            ax.add_patch(patches.Rectangle((0.2, 0.1), 0.8, 0.6, lw=2,
                         ec=C['accent2'], fc=C['fill2'], alpha=0.4))
            ax.annotate('', (0.6, 0.4), (-0.8, 0),
                       arrowprops=dict(arrowstyle='->', color=C['accent3'], lw=1.5, ls='--'))
        elif tool == 'Linear Pattern':
            for i in range(4):
                ax.add_patch(plt.Circle((-0.9+i*0.6, 0), 0.2, lw=2,
                             ec=C['accent1'] if i == 0 else C['accent2'],
                             fc=C['fill1'] if i == 0 else C['fill2'], alpha=0.4))
            ax.annotate('', (0.9, -0.5), (-0.9, -0.5),
                       arrowprops=dict(arrowstyle='<->', color=C['dim'], lw=1))
            ax.text(0, -0.7, 'Spacing', fontsize=7, ha='center', color=C['dim'])
        elif tool == 'Sketch Fillet':
            ax.plot([-1, 0], [0, 0], color=C['accent1'], lw=2)
            ax.plot([0, 0], [0, 1], color=C['accent1'], lw=2)
            ax.add_patch(Arc((0.4, 0.4), 0.8, 0.8, theta1=90, theta2=180,
                         color=C['accent3'], lw=2.5))
            ax.text(0.25, 0.55, 'R', fontsize=10, color=C['accent3'], fontweight='bold')

        ax.set_title(tool, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm05_sketch_tools.png')


def m06_dimension_types():
    """Tipe Dimensi: Smart, Horizontal, Vertical, Ordinate, Baseline, Path."""
    fig, axes = plt.subplots(2, 3, figsize=(13, 8), facecolor=C['bg'])
    fig.suptitle('Tipe-tipe Dimensi', fontsize=14, fontweight='bold',
                 color=C['header'], y=0.99)

    dim_types = ['Smart Dimension', 'Horizontal', 'Vertical',
                 'Ordinate', 'Baseline', 'Path Dimension']
    for ax, dt in zip(axes.flat, dim_types):
        ax.set_xlim(-2, 2); ax.set_ylim(-1.5, 1.8)
        ax.set_aspect('equal'); ax.axis('off')

        if dt == 'Smart Dimension':
            ax.plot([-1.2, 1.2], [-0.5, -0.5], color=C['accent1'], lw=2)
            ax.plot([-1.2, -1.2], [-0.5, 0.7], color=C['accent1'], lw=2)
            dim_line(ax, (-1.2, -0.9), (1.2, -0.9), '60')
            dim_line(ax, (-1.6, -0.5), (-1.6, 0.7), '30')
            ax.add_patch(plt.Circle((0.3, 0.2), 0.4, lw=2, ec=C['accent1'], fc='none'))
            ax.text(0.3, 0.8, 'Ø20', fontsize=9, color=C['dim'], ha='center',
                    fontweight='bold')
        elif dt == 'Horizontal':
            ax.plot([-1.2, 1], [-0.3, 0.5], color=C['accent1'], lw=2)
            dim_line(ax, (-1.2, -0.8), (1, -0.8), '55 (H)')
        elif dt == 'Vertical':
            ax.plot([-0.5, 0.7], [-0.8, 0.8], color=C['accent1'], lw=2)
            dim_line(ax, (1.3, -0.8), (1.3, 0.8), '40 (V)')
        elif dt == 'Ordinate':
            ax.plot(0, -0.8, 'o', color=C['accent5'], ms=8)
            ax.text(0, -1.1, 'Origin', fontsize=7, ha='center', color=C['accent5'])
            for i, (x, label) in enumerate([(0, '0'), (0.5, '12.5'),
                                             (1.0, '25'), (1.5, '37.5')]):
                ax.plot(x, 0, 'o', color=C['accent1'], ms=5)
                ax.plot([x, x], [0, 0.8+i*0.15], color=C['dim_line'], lw=0.7)
                ax.text(x, 0.9+i*0.15, label, fontsize=8, ha='center',
                        color=C['dim'], fontweight='bold')
        elif dt == 'Baseline':
            for i, (x, label) in enumerate([(0, '30'), (0.7, '55'), (1.3, '70')]):
                y = -0.7 - i*0.35
                dim_line(ax, (-1.5, y), (x, y), label)
        elif dt == 'Path Dimension':
            t = np.linspace(0, 2*np.pi*0.7, 50)
            ax.plot(t - 1.2, 0.5*np.sin(t), color=C['accent1'], lw=2)
            ax.text(0, -0.8, 'Panjang path = 85.3', fontsize=9, ha='center',
                    color=C['dim'], fontweight='bold',
                    bbox=dict(boxstyle='round', fc=C['fill1'], ec=C['dim']))

        ax.set_title(dt, fontsize=10, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm06_dimension_types.png')


def m07_constraints():
    """15 jenis constraint/relation dalam sketch."""
    fig, axes = plt.subplots(3, 5, figsize=(15, 9), facecolor=C['bg'])
    fig.suptitle('Sketch Constraints / Relations', fontsize=15,
                 fontweight='bold', color=C['header'], y=0.99)

    constraints = [
        ('Horizontal', '—'), ('Vertical', '|'), ('Coincident', '●'),
        ('Concentric', '◎'), ('Tangent', '⟨'),
        ('Perpendicular', '⊥'), ('Parallel', '∥'), ('Equal', '='),
        ('Midpoint', 'M'), ('Symmetric', '↔'),
        ('Collinear', '——'), ('Coradial', '◎'), ('Fix', '📌'),
        ('Pierce', '✕'), ('Merge', '●'),
    ]

    for ax, (name, sym) in zip(axes.flat, constraints):
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal'); ax.axis('off')
        cc = C['accent2']

        if name == 'Horizontal':
            ax.plot([-1, 1], [0, 0], color=cc, lw=2.5)
        elif name == 'Vertical':
            ax.plot([0, 0], [-0.8, 0.8], color=cc, lw=2.5)
        elif name == 'Coincident':
            ax.plot([-1, 0], [-0.5, 0], color=C['accent1'], lw=2)
            ax.plot([0, 1], [0, 0.5], color=C['accent3'], lw=2)
            ax.plot(0, 0, 'o', color=C['accent5'], ms=10, zorder=5)
        elif name == 'Concentric':
            ax.add_patch(plt.Circle((0, 0), 0.8, lw=2, ec=C['accent1'], fc='none'))
            ax.add_patch(plt.Circle((0, 0), 0.4, lw=2, ec=C['accent3'], fc='none'))
            ax.plot(0, 0, '+', color=C['accent5'], ms=10, mew=2)
        elif name == 'Tangent':
            ax.add_patch(plt.Circle((0, 0.3), 0.6, lw=2, ec=C['accent1'], fc='none'))
            ax.plot([-1.2, 1.2], [-0.3, -0.3], color=C['accent3'], lw=2)
        elif name == 'Perpendicular':
            ax.plot([-1, 1], [0, 0], color=C['accent1'], lw=2)
            ax.plot([0, 0], [-0.8, 0.8], color=C['accent3'], lw=2)
            ax.add_patch(patches.Rectangle((0, 0), 0.2, 0.2, lw=1,
                         ec=C['accent5'], fc='none'))
        elif name == 'Parallel':
            ax.plot([-1, 1], [-0.3, -0.3], color=C['accent1'], lw=2)
            ax.plot([-1, 1], [0.3, 0.3], color=C['accent3'], lw=2)
        elif name == 'Equal':
            ax.plot([-1, 0], [0.3, 0.3], color=C['accent1'], lw=2.5)
            ax.plot([0.1, 1.1], [-0.3, -0.3], color=C['accent3'], lw=2.5)
            ax.text(0.05, 0, '=', fontsize=16, ha='center', color=C['accent5'],
                    fontweight='bold')
        elif name == 'Midpoint':
            ax.plot([-1, 1], [0, 0], color=C['accent1'], lw=2)
            ax.plot(0, 0, 'D', color=C['accent5'], ms=10, zorder=5)
        elif name == 'Symmetric':
            ax.plot([0, 0], [-1, 1], color=C['accent5'], lw=1.5, ls='dashdot')
            ax.plot(-0.7, 0.3, 's', color=C['accent1'], ms=10)
            ax.plot(0.7, 0.3, 's', color=C['accent3'], ms=10)
            ax.annotate('', (-0.7, 0.3), (0.7, 0.3),
                       arrowprops=dict(arrowstyle='<->', color=C['dim'], lw=1))
        elif name == 'Collinear':
            ax.plot([-1, -0.1], [0.2, 0.2], color=C['accent1'], lw=2)
            ax.plot([0.2, 1], [0.2, 0.2], color=C['accent3'], lw=2)
            ax.plot([-1, 1], [0.2, 0.2], color=C['dim_line'], lw=0.7, ls='--')
        elif name == 'Coradial':
            ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=30, theta2=90,
                         color=C['accent1'], lw=2.5))
            ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=200, theta2=300,
                         color=C['accent3'], lw=2.5))
            ax.plot(0, 0, '+', color=C['accent5'], ms=8, mew=1.5)
        elif name == 'Fix':
            ax.plot([-0.5, 0.5], [-0.3, 0.3], color=C['accent1'], lw=2)
            ax.text(0, 0.7, '📌', fontsize=18, ha='center')
        elif name == 'Pierce':
            ax.add_patch(plt.Circle((0, 0), 0.6, lw=2, ec=C['accent1'], fc='none'))
            ax.plot(0, 0, 'x', color=C['accent5'], ms=14, mew=3, zorder=5)
        elif name == 'Merge':
            ax.plot(-0.5, 0, 'o', color=C['accent1'], ms=10)
            ax.plot(0.5, 0, 'o', color=C['accent3'], ms=10)
            ax.annotate('', (0.1, 0), (0.5, 0),
                       arrowprops=dict(arrowstyle='<-', color=C['accent5'], lw=1.5))
            ax.annotate('', (-0.1, 0), (-0.5, 0),
                       arrowprops=dict(arrowstyle='<-', color=C['accent5'], lw=1.5))

        ax.set_title(f'{name} ({sym})', fontsize=8, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm07_constraints.png')


def m08_design_intent():
    """Design Intent: cara benar vs salah mendefinisikan sketch."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor=C['bg'])
    fig.suptitle('Design Intent — Lubang di Tengah Plat', fontsize=14,
                 fontweight='bold', color=C['header'], y=1.0)

    # SALAH
    ax = axes[0]
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 4)
    ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(patches.Rectangle((0, 0), 4, 3, lw=2, ec=C['accent5'],
                 fc='#FFEBEE', alpha=0.3))
    ax.add_patch(plt.Circle((2, 1.5), 0.5, lw=2, ec=C['accent5'], fc='none'))
    dim_line(ax, (0, -0.4), (2, -0.4), '50', color=C['accent5'])
    dim_line(ax, (2, -0.8), (4, -0.8), '50', color=C['accent5'])
    ax.set_title('❌ SALAH — Dimensi dari kedua sisi', fontsize=11,
                 fontweight='bold', color=C['accent5'])

    # BENAR
    ax = axes[1]
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 4)
    ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(patches.Rectangle((0, 0), 4, 3, lw=2, ec=C['accent2'],
                 fc='#E8F5E9', alpha=0.3))
    ax.add_patch(plt.Circle((2, 1.5), 0.5, lw=2, ec=C['accent2'], fc='none'))
    ax.plot([2, 2], [0, 3], color=C['accent5'], lw=1, ls='dashdot')
    ax.text(2.15, 2.7, 'CL', fontsize=8, color=C['accent5'])
    ax.set_title('✅ BENAR — Symmetric + Centerline', fontsize=11,
                 fontweight='bold', color=C['accent2'])

    fig.tight_layout()
    save(fig, 'm08_design_intent.png')


def m09_drawing_line_types():
    """Jenis garis dalam gambar teknik."""
    fig, ax = plt.subplots(figsize=(12, 6), facecolor=C['bg'])
    make_header(ax, 'Garis dalam Gambar Teknik (Drawing Standards)')
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis('off')

    lines_info = [
        ('Garis Tebal (Visible)', '-',  2.5, C['line'],    'Garis yang terlihat'),
        ('Garis Tipis (Hidden)',   '--', 2.0, C['steel'],   'Garis tersembunyi'),
        ('Garis Pusat (Center)',   '-.', 1.5, C['accent5'], 'Sumbu simetri'),
        ('Garis Dimensi',         '-',  1.0, C['dim'],     'Garis ukuran'),
        ('Garis Phantom', (0,(5,2,1,2,1,2)), 1.5, C['accent4'], 'Posisi alternatif'),
        ('Garis Section',         '-',  2.5, C['accent3'], 'Garis potong'),
    ]

    for i, (name, ls, lw, color, desc) in enumerate(lines_info):
        y = 5.8 - i * 0.9
        ax.plot([1.5, 4.5], [y, y], color=color, lw=lw, linestyle=ls)
        ax.text(0.2, y, name, fontsize=10, va='center', fontweight='bold', color=color)
        ax.text(5.0, y, desc, fontsize=9, va='center', color=C['line'])

    fig.tight_layout()
    save(fig, 'm09_drawing_line_types.png')


def m10_gdt_symbols():
    """Simbol GD&T dasar."""
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=C['bg'])
    make_header(ax, 'Simbol GD&T (Geometric Dimensioning & Tolerancing)')
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis('off')

    gdts = [
        ('⊕', 'Position',        'Posisi lubang/fitur', C['accent1']),
        ('○', 'Circularity',      'Kebulatan',          C['accent2']),
        ('⊘', 'Cylindricity',     'Kesilindrian',       C['accent3']),
        ('═', 'Flatness',         'Kerataan',           C['accent4']),
        ('∠', 'Angularity',       'Kesudutan',          C['accent1']),
        ('⫽', 'Parallelism',      'Kesejajaran',        C['accent2']),
        ('⊥', 'Perpendicularity', 'Ketegaklurusan',     C['accent3']),
        ('↗', 'Runout',           'Penyimpangan putar', C['accent4']),
    ]

    for i, (sym, name, desc, color) in enumerate(gdts):
        y = 7.8 - i * 0.95
        box = FancyBboxPatch((0.5, y-0.3), 0.8, 0.6, boxstyle='round,pad=0.05',
                            facecolor='#E3F2FD', edgecolor=color, lw=1.5)
        ax.add_patch(box)
        ax.text(0.9, y, sym, fontsize=16, ha='center', va='center',
                color=color, fontweight='bold')
        ax.text(1.8, y+0.05, name, fontsize=11, va='center',
                fontweight='bold', color=C['line'])
        ax.text(4.5, y+0.05, f'— {desc}', fontsize=10, va='center', color=C['steel'])

        # Frame kontrol
        fx = 7.0
        ax.add_patch(patches.Rectangle((fx, y-0.2), 2.5, 0.4, lw=1,
                     ec=color, fc='white'))
        ax.plot([fx+0.6, fx+0.6], [y-0.2, y+0.2], color=color, lw=1)
        ax.plot([fx+1.5, fx+1.5], [y-0.2, y+0.2], color=color, lw=1)
        ax.text(fx+0.3, y, sym, fontsize=10, ha='center', va='center', color=color)
        ax.text(fx+1.05, y, '0.05', fontsize=8, ha='center', va='center', color=C['line'])
        ax.text(fx+2.0, y, 'A', fontsize=9, ha='center', va='center',
                color=C['accent5'], fontweight='bold')

    fig.tight_layout()
    save(fig, 'm10_gdt_symbols.png')


def m11_advanced_sketch():
    """Fitur Lanjutan: Equations, Driven Dim, Global Var, Blocks, 3D Sketch."""
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), facecolor=C['bg'])
    fig.suptitle('Fitur Sketching Lanjutan', fontsize=14, fontweight='bold',
                 color=C['header'], y=0.99)

    features = ['Equations', 'Driven Dimension', 'Global Variables',
                'Sketch Blocks', '3D Sketch', 'Contour Selection']

    for ax, feat in zip(axes.flat, features):
        ax.set_xlim(-2, 2); ax.set_ylim(-1.5, 1.8)
        ax.set_aspect('equal'); ax.axis('off')

        if feat == 'Equations':
            for i, line in enumerate(['"Width" = 100',
                                       '"Height" = "Width" / 2',
                                       '"Fillet" = "Width" * 0.1']):
                ax.text(0, 0.8-i*0.6, line, fontsize=9, ha='center', family='monospace',
                        color=C['accent1'], fontweight='bold',
                        bbox=dict(boxstyle='round', fc=C['fill1'], ec=C['accent1'], alpha=0.7))
            ax.text(0, -1.1, '→ Dimensi otomatis berubah', fontsize=8,
                    ha='center', color=C['accent2'])
        elif feat == 'Driven Dimension':
            ax.add_patch(patches.Rectangle((-1.2, -0.5), 2.4, 1.0, lw=2,
                         ec=C['accent1'], fc=C['fill1'], alpha=0.2))
            ax.text(0, -0.9, '(60)', fontsize=12, ha='center',
                    color=C['steel'], fontweight='bold')
            ax.text(0, 1.1, 'Driven = referensi saja\nDalam kurung (  )', fontsize=8,
                    ha='center', color=C['accent4'],
                    bbox=dict(boxstyle='round', fc=C['fill4'], ec=C['accent4']))
        elif feat == 'Global Variables':
            for i, line in enumerate(['Thickness = 5', 'Bolt_Dia = 8', 'Clearance = 0.5']):
                ax.text(0, 0.7-i*0.5, line, fontsize=9, ha='center',
                        color=C['accent2'], fontweight='bold')
            ax.text(0, -1.0, 'Digunakan di seluruh Part', fontsize=8,
                    ha='center', color=C['accent4'],
                    bbox=dict(boxstyle='round', fc=C['fill3'], ec=C['accent4']))
        elif feat == 'Sketch Blocks':
            for dx in [-0.8, 0.8]:
                ax.add_patch(FancyBboxPatch((dx-0.35, -0.3), 0.7, 0.6,
                             boxstyle='round,pad=0.05', lw=1.5,
                             ec=C['accent3'], fc=C['fill3'], alpha=0.4))
                ax.text(dx, 0, 'T', fontsize=14, ha='center', va='center',
                        color=C['accent3'], fontweight='bold')
            ax.annotate('', (0.45, 0), (-0.45, 0),
                       arrowprops=dict(arrowstyle='->', color=C['accent5'], lw=1.5, ls='--'))
            ax.text(0, 0.8, 'Reusable Block', fontsize=9, ha='center',
                    color=C['accent3'],
                    bbox=dict(boxstyle='round', fc='white', ec=C['accent3']))
        elif feat == '3D Sketch':
            ax.annotate('', (1.2, 0), (0, 0),
                       arrowprops=dict(arrowstyle='->', color=C['accent5'], lw=2))
            ax.annotate('', (0, 1.2), (0, 0),
                       arrowprops=dict(arrowstyle='->', color=C['accent2'], lw=2))
            ax.annotate('', (-0.8, -0.5), (0, 0),
                       arrowprops=dict(arrowstyle='->', color=C['accent1'], lw=2))
            ax.text(1.3, 0, 'X', fontsize=10, color=C['accent5'], fontweight='bold')
            ax.text(0, 1.4, 'Y', fontsize=10, color=C['accent2'], fontweight='bold')
            ax.text(-0.95, -0.6, 'Z', fontsize=10, color=C['accent1'], fontweight='bold')
            ax.plot([0, 0.8, 0.8], [0, 0, 0.7], color=C['accent3'], lw=2.5)
        elif feat == 'Contour Selection':
            ax.add_patch(plt.Circle((-0.3, 0), 0.7, lw=2, ec=C['accent1'], fc='none'))
            ax.add_patch(plt.Circle((0.3, 0), 0.7, lw=2, ec=C['accent3'], fc='none'))
            theta = np.linspace(-np.pi/3, np.pi/3, 50)
            ax.fill(-0.3 + 0.7*np.cos(theta), 0.7*np.sin(theta),
                    color=C['accent4'], alpha=0.3)
            ax.text(0, -1.1, 'Pilih kontur tertentu', fontsize=8,
                    ha='center', color=C['accent4'])

        ax.set_title(feat, fontsize=10, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm11_advanced_sketch.png')


def m12_reference_geometry():
    """Reference Geometry: Plane, Axis, Coordinate System."""
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5), facecolor=C['bg'])
    fig.suptitle('Reference Geometry untuk Sketching', fontsize=14,
                 fontweight='bold', color=C['header'], y=1.02)

    # Plane
    ax = axes[0]
    ax.set_xlim(-2, 2); ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Polygon([(-1.5, -0.3), (1.5, -0.3), (1.2, 0.4), (-1.8, 0.4)],
                 closed=True, lw=1.5, ec=C['accent1'], fc=C['fill1'], alpha=0.3))
    ax.text(0, 0, 'Base Plane', fontsize=8, ha='center', color=C['accent1'])
    ax.add_patch(Polygon([(-1.5, 0.5), (1.5, 0.5), (1.2, 1.2), (-1.8, 1.2)],
                 closed=True, lw=1.5, ec=C['accent3'], fc=C['fill3'], alpha=0.3, ls='--'))
    ax.text(0, 0.8, 'Offset Plane', fontsize=8, ha='center', color=C['accent3'])
    ax.annotate('', (-1.65, 1.2), (-1.65, 0.4),
               arrowprops=dict(arrowstyle='<->', color=C['dim'], lw=1))
    ax.text(-1.9, 0.8, 'd', fontsize=10, color=C['dim'], fontweight='bold')
    ax.set_title('Reference Plane', fontsize=11, fontweight='bold', color=C['line'])

    # Axis
    ax = axes[1]
    ax.set_xlim(-2, 2); ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(plt.Circle((0, 0), 0.8, lw=2, ec=C['accent1'],
                 fc=C['fill1'], alpha=0.2))
    ax.plot([0, 0], [-1.5, 1.5], color=C['accent5'], lw=2, ls='dashdot')
    ax.text(0.2, 1.4, 'Axis', fontsize=10, color=C['accent5'], fontweight='bold')
    ax.set_title('Reference Axis', fontsize=11, fontweight='bold', color=C['line'])

    # Coordinate System
    ax = axes[2]
    ax.set_xlim(-2, 2); ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal'); ax.axis('off')
    ax.annotate('', (1.5, 0), (0, 0),
               arrowprops=dict(arrowstyle='->', color=C['accent5'], lw=2.5))
    ax.annotate('', (0, 1.5), (0, 0),
               arrowprops=dict(arrowstyle='->', color=C['accent2'], lw=2.5))
    ax.annotate('', (-1, -0.7), (0, 0),
               arrowprops=dict(arrowstyle='->', color=C['accent1'], lw=2.5))
    ax.text(1.6, 0.1, 'X', fontsize=12, color=C['accent5'], fontweight='bold')
    ax.text(0.1, 1.6, 'Y', fontsize=12, color=C['accent2'], fontweight='bold')
    ax.text(-1.2, -0.85, 'Z', fontsize=12, color=C['accent1'], fontweight='bold')
    ax.plot(0, 0, 'o', color=C['line'], ms=6, zorder=5)
    ax.set_title('Coordinate System', fontsize=11, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'm12_reference_geometry.png')


def m13_drawing_views():
    """Jenis View dalam Drawing."""
    fig, ax = plt.subplots(figsize=(13, 7), facecolor=C['bg'])
    make_header(ax, 'Jenis View dalam Engineering Drawing')
    ax.set_xlim(0, 13); ax.set_ylim(0, 7); ax.axis('off')

    # Front
    ax.add_patch(patches.Rectangle((0.5, 3.5), 3, 2.5, lw=2, ec=C['accent1'],
                 fc=C['fill1'], alpha=0.3))
    ax.add_patch(plt.Circle((2, 4.75), 0.4, lw=1.5, ec=C['accent1'], fc='none'))
    ax.text(2, 6.3, 'FRONT VIEW', fontsize=9, ha='center',
            fontweight='bold', color=C['accent1'])

    # Top
    ax.add_patch(patches.Rectangle((0.5, 0.5), 3, 1.8, lw=2, ec=C['accent2'],
                 fc=C['fill2'], alpha=0.3))
    ax.text(2, 2.6, 'TOP VIEW', fontsize=9, ha='center',
            fontweight='bold', color=C['accent2'])

    # Right
    ax.add_patch(patches.Rectangle((4.5, 3.5), 1.8, 2.5, lw=2, ec=C['accent3'],
                 fc=C['fill3'], alpha=0.3))
    ax.text(5.4, 6.3, 'RIGHT VIEW', fontsize=9, ha='center',
            fontweight='bold', color=C['accent3'])

    # Section
    ax.add_patch(patches.Rectangle((7, 3.5), 3, 2.5, lw=2, ec=C['accent4'],
                 fc=C['fill4'], alpha=0.3))
    for i in range(8):
        xs = 7 + i * 0.4
        ax.plot([xs, xs+0.3], [3.5, 3.8], color=C['accent4'], lw=0.5, alpha=0.5)
        ax.plot([xs, xs+0.3], [5.7, 6.0], color=C['accent4'], lw=0.5, alpha=0.5)
    ax.text(8.5, 6.3, 'SECTION A-A', fontsize=9, ha='center',
            fontweight='bold', color=C['accent4'])

    # Detail
    ax.add_patch(plt.Circle((10.5, 1.5), 1, lw=2, ec=C['accent5'], fc='white'))
    ax.add_patch(patches.Rectangle((10, 1.1), 1, 0.8, lw=1.5, ec=C['accent5'],
                 fc=C['fill1'], alpha=0.3))
    ax.text(10.5, 2.8, 'DETAIL B (2:1)', fontsize=9, ha='center',
            fontweight='bold', color=C['accent5'])

    for i, v in enumerate(['Standard Views', 'Projected View', 'Section View',
                            'Detail View', 'Auxiliary View']):
        ax.text(7, 0.5+i*0.4, f'• {v}', fontsize=8, color=C['line'])

    fig.tight_layout()
    save(fig, 'm13_drawing_views.png')


def m14_tips_best_practices():
    """Tips Do's and Don'ts."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 7), facecolor=C['bg'])
    fig.suptitle("Tips & Best Practices Sketching", fontsize=14,
                 fontweight='bold', color=C['header'], y=0.99)

    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.set_facecolor('#E8F5E9')
    ax.set_title("✅ Do's", fontsize=13, fontweight='bold', color=C['accent2'], pad=10)
    for i, d in enumerate(['Mulai sketch dari Origin',
                            'Constraints sebelum dimensi',
                            'Buat sketch Fully Defined',
                            'Gunakan Construction Lines',
                            'Manfaatkan Mirror & Pattern',
                            'Beri nama deskriptif',
                            'Gunakan Equations utk design family',
                            'Simpan profil standar sbg Blocks']):
        ax.text(0.5, 8.8 - i*1.05, f'✅  {d}', fontsize=10, va='center',
                color=C['accent2'], fontweight='bold')

    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.set_facecolor('#FFEBEE')
    ax.set_title("❌ Don'ts", fontsize=13, fontweight='bold', color=C['accent5'], pad=10)
    for i, d in enumerate(['Sketch Over Defined',
                            'Fix constraint berlebihan',
                            'Abaikan Design Intent',
                            'Sketch terlalu kompleks',
                            'Lupa menyimpan file']):
        ax.text(0.5, 8.8 - i*1.5, f'❌  {d}', fontsize=10, va='center',
                color=C['accent5'], fontweight='bold')

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm14_tips_best_practices.png')


def m15_slot_polygon_types():
    """Tipe-tipe Slot dan Polygon."""
    fig, axes = plt.subplots(2, 4, figsize=(14, 7), facecolor=C['bg'])
    fig.suptitle('Tipe Slot & Polygon', fontsize=14, fontweight='bold',
                 color=C['header'], y=0.99)

    items = [
        ('Straight Slot', 'slot'), ('Centerpoint Slot', 'slot'),
        ('3-Pt Arc Slot', 'slot'), ('Center Arc Slot', 'slot'),
        ('Triangle (3)', 'poly'), ('Square (4)', 'poly'),
        ('Pentagon (5)', 'poly'), ('Hexagon (6)', 'poly'),
    ]

    for ax, (name, kind) in zip(axes.flat, items):
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.2, 1.2)
        ax.set_aspect('equal'); ax.axis('off')

        if kind == 'slot':
            if 'Straight' in name:
                ax.add_patch(FancyBboxPatch((-1, -0.25), 2, 0.5,
                             boxstyle='round,pad=0.25', lw=2, ec=C['accent1'],
                             fc=C['fill1'], alpha=0.3))
            elif 'Centerpoint S' in name:
                ax.add_patch(FancyBboxPatch((-0.8, -0.3), 1.6, 0.6,
                             boxstyle='round,pad=0.3', lw=2, ec=C['accent2'],
                             fc=C['fill2'], alpha=0.3))
                ax.plot(0, 0, '+', color=C['accent5'], ms=10, mew=2)
            elif '3-Pt' in name:
                ax.add_patch(Arc((0, 0), 2, 2, theta1=30, theta2=150,
                             color=C['accent3'], lw=2))
                ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=30, theta2=150,
                             color=C['accent3'], lw=2))
            else:
                ax.add_patch(Arc((0, 0), 2, 2, theta1=-30, theta2=120,
                             color=C['accent4'], lw=2))
                ax.add_patch(Arc((0, 0), 1.3, 1.3, theta1=-30, theta2=120,
                             color=C['accent4'], lw=2))
                ax.plot(0, 0, '+', color=C['accent5'], ms=10, mew=2)
        else:
            n = int(name.split('(')[1].split(')')[0])
            angles = np.linspace(0, 2*np.pi, n, endpoint=False) + np.pi/2
            xs, ys = 0.8*np.cos(angles), 0.8*np.sin(angles)
            ci = n - 3
            cols = [C['accent1'], C['accent2'], C['accent3'], C['accent4']]
            fills = [C['fill1'], C['fill2'], C['fill3'], C['fill4']]
            ax.add_patch(Polygon(np.column_stack([xs, ys]), closed=True, lw=2.5,
                         ec=cols[ci], fc=fills[ci], alpha=0.3))
            r_in = 0.8 * np.cos(np.pi/n)
            ax.add_patch(plt.Circle((0, 0), r_in, lw=1, ec=C['dim_line'],
                         fc='none', ls='--'))

        ax.set_title(name, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    save(fig, 'm15_slot_polygon_types.png')


def m16_workflow_sketching():
    """Workflow umum sketching."""
    fig, ax = plt.subplots(figsize=(14, 5), facecolor=C['bg'])
    make_header(ax, 'Workflow Sketching di SolidWorks')
    ax.set_xlim(0, 14); ax.set_ylim(0, 5); ax.axis('off')

    steps = [
        ('1. Pilih\nPlane', C['accent1']),
        ('2. Mulai\nSketch', C['accent2']),
        ('3. Gambar\nEntitas', C['accent3']),
        ('4. Tambah\nConstraints', C['accent4']),
        ('5. Beri\nDimensi', C['dim']),
        ('6. Fully\nDefined?', C['accent2']),
        ('7. Exit\nSketch', C['accent5']),
    ]

    for i, (label, color) in enumerate(steps):
        x = 1 + i * 1.8
        ax.add_patch(FancyBboxPatch((x-0.7, 1.5), 1.4, 2.0,
                     boxstyle='round,pad=0.15', facecolor='white',
                     edgecolor=color, lw=2))
        ax.text(x, 2.5, label, fontsize=8, ha='center', va='center',
                color=color, fontweight='bold')
        if i < len(steps) - 1:
            ax.annotate('', (x+1.0, 2.5), (x+0.75, 2.5),
                       arrowprops=dict(arrowstyle='->', color=C['steel'], lw=1.5))

    fig.tight_layout()
    save(fig, 'm16_workflow_sketching.png')


# ══════════════════════════════════════════════════════════════
#  PROJECT ILLUSTRATIONS
# ══════════════════════════════════════════════════════════════

def p01_panel_kontrol_layout():
    """Project A: Layout panel kontrol 200×150mm."""
    fig, ax = plt.subplots(figsize=(12, 9), facecolor=C['bg'])
    make_header(ax, 'Project A — Panel Kontrol (200 × 150 mm)')
    ax.set_xlim(-20, 230); ax.set_ylim(-30, 180)
    ax.set_aspect('equal'); ax.axis('off')

    # Panel outline
    ax.add_patch(FancyBboxPatch((0, 0), 200, 150, boxstyle='round,pad=10',
                 lw=2.5, edgecolor=C['line'], facecolor=C['panel']))

    # Mounting holes
    for x, y in [(10, 10), (10, 140), (190, 10), (190, 140)]:
        ax.add_patch(plt.Circle((x, y), 3, lw=1.5, ec=C['accent1'], fc='white'))
        ax.text(x, y, '+', fontsize=6, ha='center', va='center', color=C['accent1'])

    # Display cutout
    ax.add_patch(FancyBboxPatch((120, 105), 60, 30, boxstyle='round,pad=3',
                 lw=2, edgecolor=C['accent2'], facecolor='#E3F2FD'))
    ax.text(150, 120, 'DISPLAY', fontsize=8, ha='center', va='center',
            color=C['accent2'], fontweight='bold')
    dim_line(ax, (120, 100), (180, 100), '60')
    dim_line(ax, (185, 105), (185, 135), '30')

    # 3 Push buttons
    for i in range(3):
        bx = 65 + i * 35
        ax.add_patch(plt.Circle((bx, 30), 11, lw=2, ec=C['accent3'],
                     fc=C['fill3'], alpha=0.4))
        ax.text(bx, 30, f'B{i+1}', fontsize=7, ha='center', va='center',
                color=C['accent3'], fontweight='bold')
        ax.add_patch(patches.Rectangle((bx-7.5, 20), 15, 3, lw=1,
                     ec=C['steel'], fc='white'))
    ax.text(100, 12, 'Ø22mm × 3 (jarak 35mm)', fontsize=7, ha='center', color=C['dim'])

    # Selector Switch
    ax.add_patch(plt.Circle((30, 120), 11, lw=2, ec=C['accent4'],
                 fc=C['fill4'], alpha=0.4))
    ax.plot([21, 21], [112, 128], color=C['accent4'], lw=2)
    ax.text(30, 120, 'SEL', fontsize=7, ha='center', va='center',
            color=C['accent4'], fontweight='bold')
    ax.text(30, 105, 'Ø22 D-cut', fontsize=7, ha='center', color=C['dim'])

    # E-Stop
    ax.add_patch(plt.Circle((165, 35), 27.5, lw=1.5, ec=C['accent5'],
                 fc='none', ls='--'))
    ax.add_patch(plt.Circle((165, 35), 20, lw=2.5, ec=C['accent5'],
                 fc='#FFCDD2', alpha=0.5))
    ax.text(165, 35, 'E-STOP', fontsize=7, ha='center', va='center',
            color=C['accent5'], fontweight='bold')
    ax.text(165, 8, 'Ø40mm', fontsize=7, ha='center', color=C['dim'])

    # Ventilasi slots
    for i in range(5):
        ax.add_patch(FancyBboxPatch((15, 20+i*6), 25, 3,
                     boxstyle='round,pad=1.5', lw=1, edgecolor=C['accent1'],
                     facecolor='white'))
    ax.text(27, 55, 'Ventilasi\n25×3mm ×5', fontsize=6, ha='center', color=C['dim'])

    # Label area
    ax.add_patch(patches.Rectangle((75, 138), 50, 8, lw=1.5, ec=C['steel'], fc='white'))
    ax.text(100, 142, 'LABEL', fontsize=7, ha='center', va='center', color=C['steel'])

    # Overall dims
    dim_line(ax, (0, -15), (200, -15), '200 mm')
    dim_line(ax, (-15, 0), (-15, 150), '150 mm')

    fig.tight_layout()
    save(fig, 'p01_panel_kontrol_layout.png')


def p02_panel_kontrol_constraints():
    """Project A: Constraints yang digunakan."""
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=C['bg'])
    make_header(ax, 'Project A — Constraints yang Wajib Digunakan')
    ax.set_xlim(0, 12); ax.set_ylim(0, 7); ax.axis('off')

    items = [
        ('Symmetric', 'Mounting holes simetris\nterhadap sumbu vertikal', C['accent1'], '↔'),
        ('Equal', 'Semua slot ventilasi\nsama panjang', C['accent2'], '='),
        ('Concentric', 'Marking zone & E-Stop\nsepusat', C['accent3'], '◎'),
        ('Pattern', 'Slot ventilasi →\nLinear Pattern', C['accent4'], '⊞'),
        ('Mirror', 'Mounting holes →\nMirror', C['accent5'], '⟷'),
        ('Perpendicular', 'Sudut panel 90°\n+ horizontal/vertical', C['dim'], '⊥'),
    ]

    for i, (name, desc, color, sym) in enumerate(items):
        col = i % 3; row = i // 3
        x = 1 + col * 3.8; y = 5.2 - row * 2.8
        ax.add_patch(FancyBboxPatch((x-0.5, y-0.8), 3.3, 2.0,
                     boxstyle='round,pad=0.2', facecolor='white',
                     edgecolor=color, lw=2))
        ax.text(x+1.1, y+0.8, f'{sym}  {name}', fontsize=11,
                fontweight='bold', color=color)
        ax.text(x+1.1, y-0.2, desc, fontsize=8, color=C['line'], va='center')

    fig.tight_layout()
    save(fig, 'p02_panel_kontrol_constraints.png')


def p03_profil_aluminium_2020():
    """Project B: Profil Aluminium 2020 (20×20mm)."""
    fig, ax = plt.subplots(figsize=(8, 8), facecolor=C['bg'])
    make_header(ax, 'Project B — Profil Aluminium 2020 (20×20mm)')
    ax.set_xlim(-15, 15); ax.set_ylim(-15, 15)
    ax.set_aspect('equal'); ax.axis('off')

    # Outer
    ax.add_patch(patches.Rectangle((-10, -10), 20, 20, lw=2.5,
                 ec=C['line'], fc=C['alu'], alpha=0.3))

    # T-slots
    sw, sd = 3, 4
    for orient in ['top', 'bottom', 'left', 'right']:
        if orient == 'top':
            pts = [(-sw, 10), (-sw, 10-sd+1), (-sw-1, 10-sd+1),
                   (-sw-1, 10-sd), (sw+1, 10-sd), (sw+1, 10-sd+1),
                   (sw, 10-sd+1), (sw, 10)]
        elif orient == 'bottom':
            pts = [(-sw, -10), (-sw, -10+sd-1), (-sw-1, -10+sd-1),
                   (-sw-1, -10+sd), (sw+1, -10+sd), (sw+1, -10+sd-1),
                   (sw, -10+sd-1), (sw, -10)]
        elif orient == 'left':
            pts = [(-10, -sw), (-10+sd-1, -sw), (-10+sd-1, -sw-1),
                   (-10+sd, -sw-1), (-10+sd, sw+1), (-10+sd-1, sw+1),
                   (-10+sd-1, sw), (-10, sw)]
        else:
            pts = [(10, -sw), (10-sd+1, -sw), (10-sd+1, -sw-1),
                   (10-sd, -sw-1), (10-sd, sw+1), (10-sd+1, sw+1),
                   (10-sd+1, sw), (10, sw)]
        ax.add_patch(Polygon(pts, closed=False, lw=1.5,
                     ec=C['accent1'], fc='white'))

    # Center bore
    ax.add_patch(plt.Circle((0, 0), 2.5, lw=1.5, ec=C['accent5'], fc='white'))

    # Centerlines
    ax.plot([-12, 12], [0, 0], color=C['accent5'], lw=0.8, ls='dashdot', alpha=0.5)
    ax.plot([0, 0], [-12, 12], color=C['accent5'], lw=0.8, ls='dashdot', alpha=0.5)

    dim_line(ax, (-10, -13), (10, -13), '20 mm')
    dim_line(ax, (13, -10), (13, 10), '20 mm')
    ax.text(0, 4, 'Ø5', fontsize=8, ha='center', color=C['dim'], fontweight='bold')
    ax.text(0, 12, 'T-Slot: 6mm', fontsize=8, ha='center', color=C['accent1'],
            bbox=dict(boxstyle='round', fc='white', ec=C['accent1']))
    ax.text(0, -14.5, 'TIPS: Gambar 1/4 → Mirror 2× (simetri 4 arah)',
            fontsize=8, ha='center', color=C['accent2'], fontstyle='italic',
            bbox=dict(boxstyle='round', fc=C['fill2'], ec=C['accent2']))

    fig.tight_layout()
    save(fig, 'p03_profil_aluminium_2020.png')


def p04_profil_aluminium_family():
    """Project B: Keluarga profil aluminium."""
    fig, axes = plt.subplots(1, 4, figsize=(16, 5), facecolor=C['bg'])
    fig.suptitle('Keluarga Profil Aluminium', fontsize=14, fontweight='bold',
                 color=C['header'], y=1.02)

    profiles = [
        ('2020', 10, 10, 1, 2.5, '6mm slot'),
        ('2040', 10, 20, 2, 2.5, '6mm slot'),
        ('3030', 15, 15, 1, 6, '8mm slot'),
        ('4040', 20, 20, 1, 6, '8mm slot'),
    ]

    for ax, (name, hw, hh, n_bore, bore_r, slot_info) in zip(axes, profiles):
        ax.set_xlim(-hw-8, hw+8); ax.set_ylim(-hh-8, hh+8)
        ax.set_aspect('equal'); ax.axis('off')

        ax.add_patch(patches.Rectangle((-hw, -hh), 2*hw, 2*hh, lw=2.5,
                     ec=C['line'], fc=C['alu'], alpha=0.3))

        sw = hw * 0.3
        for side in ['top', 'bottom', 'left', 'right']:
            if side == 'top':
                ax.plot([-sw, -sw, sw, sw], [hh, hh-hw*0.35, hh-hw*0.35, hh],
                        color=C['accent1'], lw=1.5)
            elif side == 'bottom':
                ax.plot([-sw, -sw, sw, sw], [-hh, -hh+hw*0.35, -hh+hw*0.35, -hh],
                        color=C['accent1'], lw=1.5)
            elif side == 'left':
                ax.plot([-hw, -hw+hh*0.35, -hw+hh*0.35, -hw], [-sw, -sw, sw, sw],
                        color=C['accent1'], lw=1.5)
            elif side == 'right':
                ax.plot([hw, hw-hh*0.35, hw-hh*0.35, hw], [-sw, -sw, sw, sw],
                        color=C['accent1'], lw=1.5)

        if name == '2040':
            for dy in [-hh//2, hh//2]:
                ax.plot([-hw, -hw+hh*0.35, -hw+hh*0.35, -hw],
                        [dy-sw, dy-sw, dy+sw, dy+sw], color=C['accent1'], lw=1)
                ax.plot([hw, hw-hh*0.35, hw-hh*0.35, hw],
                        [dy-sw, dy-sw, dy+sw, dy+sw], color=C['accent1'], lw=1)

        if n_bore == 1:
            ax.add_patch(plt.Circle((0, 0), bore_r, lw=1.5, ec=C['accent5'], fc='white'))
        else:
            for dy in [-hh//2, hh//2]:
                ax.add_patch(plt.Circle((0, dy), bore_r, lw=1.5,
                             ec=C['accent5'], fc='white'))

        ax.plot([-hw-2, hw+2], [0, 0], color=C['steel'], lw=0.5, ls='dashdot', alpha=0.4)
        ax.plot([0, 0], [-hh-2, hh+2], color=C['steel'], lw=0.5, ls='dashdot', alpha=0.4)
        dim_line(ax, (-hw, -hh-4), (hw, -hh-4), f'{2*hw}', fontsize=8)

        ax.set_title(f'Profil {name}\n{2*hw}×{2*hh}mm — {slot_info}',
                     fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'p04_profil_aluminium_family.png')


def p05_sketch_technique():
    """Teknik sketching profil: 1/4 → Mirror → Full."""
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5), facecolor=C['bg'])
    fig.suptitle('Teknik Sketching Profil — Quarter → Mirror → Full',
                 fontsize=14, fontweight='bold', color=C['header'], y=1.02)

    titles = ['① Gambar 1/4\n(Kuadran I)', '② Mirror Horizontal\n(Kuadran I+II)',
              '③ Mirror Vertikal\n(Full Profile)', '④ Tambah\nCenter Bore']

    for ax, title in zip(axes, titles):
        ax.set_xlim(-12, 12); ax.set_ylim(-12, 12)
        ax.set_aspect('equal'); ax.axis('off')
        ax.plot([-11, 11], [0, 0], color=C['accent5'], lw=0.8, ls='dashdot', alpha=0.4)
        ax.plot([0, 0], [-11, 11], color=C['accent5'], lw=0.8, ls='dashdot', alpha=0.4)

        if '1/4' in title:
            ax.add_patch(patches.Rectangle((0, 0), 10, 10, lw=2.5,
                         ec=C['accent1'], fc=C['fill1'], alpha=0.3))
        elif 'Horizontal' in title:
            for sx in [1, -1]:
                ax.add_patch(patches.Rectangle((0 if sx==1 else -10, 0), 10, 10, lw=2,
                             ec=C['accent1'] if sx==1 else C['accent2'],
                             fc=C['fill1'] if sx==1 else C['fill2'], alpha=0.3))
        elif 'Vertikal' in title:
            for sx, sy in [(1,1), (-1,1), (1,-1), (-1,-1)]:
                ax.add_patch(patches.Rectangle((0 if sx==1 else -10,
                             0 if sy==1 else -10), 10, 10, lw=2,
                             ec=C['accent2'], fc=C['fill2'], alpha=0.2))
        else:
            ax.add_patch(patches.Rectangle((-10, -10), 20, 20, lw=2,
                         ec=C['accent2'], fc=C['fill2'], alpha=0.2))
            ax.add_patch(plt.Circle((0, 0), 2.5, lw=2, ec=C['accent5'], fc='white'))

        ax.set_title(title, fontsize=9, fontweight='bold', color=C['line'])

    fig.tight_layout()
    save(fig, 'p05_sketch_technique.png')


# ══════════════════════════════════════════════════════════════
#  MATERI DESKRIPSI  (m01_deskripsi.png)
# ══════════════════════════════════════════════════════════════
def materi_deskripsi():
    """Infografis overview seluruh materi Modul 2."""
    fig = plt.figure(figsize=(18, 22))
    fig.patch.set_facecolor('#f0f4f8')

    # ── HEADER ──
    fig.text(0.5, 0.97, 'MODUL 2: CAD GAMBAR 2D', fontsize=22, fontweight='bold',
             ha='center', va='top', color='#1a237e',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#bbdefb',
                       edgecolor='#1565c0', linewidth=3))
    fig.text(0.5, 0.945, 'SKETCHING · DIMENSIONING · CONSTRAINTS',
             fontsize=14, fontweight='bold', ha='center', va='top', color='#0d47a1')

    # ── 1. Konsep Dasar Sketching ──
    ax = fig.add_axes([0.03, 0.78, 0.45, 0.15])
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.2, 0.5), 9.5, 9,
                 boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#1565c0', lw=2))
    ax.text(5, 9, '📐 KONSEP DASAR SKETCHING', fontsize=13, fontweight='bold',
            ha='center', color='#1565c0')
    for i, t in enumerate([
        '• Sketch = Gambar 2D pada Plane / Face',
        '• Entitas: Line, Circle, Arc, Spline, Slot, Polygon',
        '• Status: Fully Defined (hitam) / Under (biru) / Over (merah)',
        '• Selalu usahakan Fully Defined sebelum Feature 3D',
        '• Shortcut: L (Line), R (Rect), C (Circle), D (Dim)',
    ]):
        c = '#c62828' if i == 3 else '#333'
        fw = 'bold' if i == 3 else 'normal'
        ax.text(0.5, 7.5 - i * 1.5, t, fontsize=9, ha='left', color=c, fontweight=fw)

    # ── 2. Entitas Sketch ──
    ax = fig.add_axes([0.52, 0.78, 0.45, 0.15])
    ax.set_xlim(0, 12); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.2, 0.5), 11.5, 9,
                 boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=2))
    ax.text(6, 9, '🔷 ENTITAS SKETCH (12 Jenis)', fontsize=13, fontweight='bold',
            ha='center', color='#2e7d32')
    entities = ['Line (L)', 'Rectangle (R)', 'Circle (C)', 'Arc', 'Polygon', 'Ellipse',
                'Slot', 'Spline', 'Point', 'Centerline', 'Text', 'Construction']
    for i, e in enumerate(entities):
        ax.text(1 + (i % 3) * 4, 7 - (i // 3) * 1.8, f'• {e}', fontsize=9, ha='left')

    # ── 3. Constraints ──
    ax = fig.add_axes([0.03, 0.57, 0.45, 0.19])
    ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 11.3,
                 boxstyle='round,pad=0.3', facecolor='#fff3e0', edgecolor='#e65100', lw=2))
    ax.text(5, 11, '🔗 SKETCH CONSTRAINTS (15 Jenis)', fontsize=13, fontweight='bold',
            ha='center', color='#e65100')
    cons = [('Horizontal —', 'Garis horizontal'), ('Vertical |', 'Garis vertikal'),
            ('Coincident ●', 'Titik bertemu'),     ('Concentric ◎', 'Sepusat'),
            ('Tangent ⟨', 'Bersinggungan'),        ('Perpendicular ⊥', 'Tegak lurus'),
            ('Parallel ∥', 'Sejajar'),             ('Equal =', 'Sama ukuran'),
            ('Symmetric ↔', 'Simetris'),           ('Midpoint M', 'Titik tengah')]
    for i, (n, d) in enumerate(cons):
        col, row = i % 2, i // 2
        ax.text(0.8 + col * 5, 9.5 - row * 1.7, n, fontsize=9, ha='left', fontweight='bold')
        ax.text(0.8 + col * 5, 8.7 - row * 1.7, f'  {d}', fontsize=8, ha='left', color='#555')

    # ── 4. Dimensioning ──
    ax = fig.add_axes([0.52, 0.57, 0.45, 0.19])
    ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 11.3,
                 boxstyle='round,pad=0.3', facecolor='#f3e5f5', edgecolor='#6a1b9a', lw=2))
    ax.text(5, 11, '📏 DIMENSIONING (Smart Dimension: D)', fontsize=13, fontweight='bold',
            ha='center', color='#6a1b9a')
    for i, d in enumerate([
        'Smart Dimension → Auto-detect tipe',
        'Linear: Panjang garis / jarak 2 titik',
        'Angular: Sudut antar 2 garis',
        'Radial: Radius lingkaran/arc (R)',
        'Diameter: Diameter lingkaran (Ø)',
        'Ordinate: Dimensi berantai dari datum',
        'Driving vs Reference (Read-only)',
        'Equations: Dimensi parametrik',
    ]):
        ax.text(1, 9.5 - i * 1.1, f'• {d}', fontsize=9, ha='left')

    # ── 5. Sketch Tools ──
    ax = fig.add_axes([0.03, 0.38, 0.45, 0.17])
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 9.3,
                 boxstyle='round,pad=0.3', facecolor='#e0f7fa', edgecolor='#00695c', lw=2))
    ax.text(5, 9, '🛠️ SKETCH TOOLS', fontsize=13, fontweight='bold',
            ha='center', color='#00695c')
    tools = [('Trim (T)', 'Potong entitas'),       ('Extend', 'Perpanjang entitas'),
             ('Offset', 'Copy dgn jarak'),          ('Mirror', 'Cerminkan centerline'),
             ('Linear Pattern', 'Ulang linear'),     ('Circular Pattern', 'Ulang melingkar'),
             ('Fillet', 'Pembulatan sudut'),          ('Chamfer', 'Potongan sudut')]
    for i, (n, d) in enumerate(tools):
        col, row = i % 2, i // 2
        ax.text(0.8 + col * 5, 7.5 - row * 1.7, n, fontsize=9, ha='left', fontweight='bold')
        ax.text(0.8 + col * 5, 6.7 - row * 1.7, f'  {d}', fontsize=8, ha='left', color='#555')

    # ── 6. Teknik Lanjutan ──
    ax = fig.add_axes([0.52, 0.38, 0.45, 0.17])
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.2, 0.3), 9.5, 9.3,
                 boxstyle='round,pad=0.3', facecolor='#fce4ec', edgecolor='#880e4f', lw=2))
    ax.text(5, 9, '🚀 TEKNIK LANJUTAN', fontsize=13, fontweight='bold',
            ha='center', color='#880e4f')
    for i, a in enumerate([
        'Design Intent — Sketch sesuai niat desain',
        'Fully Define Sketch — Auto-constraint tool',
        'Equations — Dimensi parametrik dgn rumus',
        'Global Variables — Variabel reusable',
        'Sketch Blocks — Profil reusable (.sldblk)',
        '3D Sketch — Sketching di ruang XYZ',
        'Contour Selection — Pilih kontur overlap',
        'Sketch Picture — Tracing dari gambar ref',
    ]):
        ax.text(1, 7.5 - i * 0.95, f'• {a}', fontsize=8.5, ha='left')

    # ── 7. Percobaan 1-15 ──
    ax = fig.add_axes([0.03, 0.12, 0.94, 0.24])
    ax.set_xlim(0, 20); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 9.5,
                 boxstyle='round,pad=0.3', facecolor='#fffde7', edgecolor='#f57f17', lw=2))
    ax.text(10, 9.2, '📋 PERCOBAAN 1–15 (LATIHAN PRAKTIKUM)',
            fontsize=14, fontweight='bold', ha='center', color='#e65100')
    perc = [('P1','Geometri Dasar\nLine & Rect'), ('P2','Lingkaran\n& Arc'),
            ('P3','Polygon\n& Slot'),              ('P4','Trim, Extend\n& Offset'),
            ('P5','Mirror\n& Pattern'),            ('P6','Profil Cam\n(Constraints)'),
            ('P7','Spline\n(Airfoil)'),            ('P8','Gasket\nIndustri'),
            ('P9','Bracket\nEngsel'),              ('P10','Flange\n(Lingkaran)')]
    for i, (num, desc) in enumerate(perc):
        x = 1 + i * 1.9
        ax.add_patch(FancyBboxPatch((x - 0.7, 3.5), 1.6, 4.5,
                     boxstyle='round,pad=0.2', facecolor=plt.cm.Set3(i / 10),
                     edgecolor='#666', lw=1.5, alpha=0.8))
        ax.text(x + 0.1, 7.2, num, fontsize=10, fontweight='bold', ha='center', color='#333')
        ax.text(x + 0.1, 5.3, desc, fontsize=7.5, ha='center', va='center', color='#333')
    ax.text(10, 1.5, 'P11–P15: Equations, Blocks, 3D Sketch, Drawing Views, GD&T',
            fontsize=10, ha='center', color='#555', fontweight='bold')

    # ── Footer ──
    fig.text(0.5, 0.06,
             'Tips: Selalu mulai dari Origin | Constraints dulu, lalu Dimensi | Pastikan Fully Defined',
             fontsize=11, ha='center', color='#1565c0', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd',
                       edgecolor='#1565c0', lw=2))
    fig.text(0.5, 0.025, 'Praktikum CAD/CAM — Modul 2: CAD Gambar 2D',
             fontsize=10, ha='center', color='#888')

    save(fig, 'm01_deskripsi.png')


# ══════════════════════════════════════════════════════════════
#  PROJECT DESKRIPSI  (p01_deskripsi.png)
# ══════════════════════════════════════════════════════════════
def project_deskripsi():
    """Infografis overview seluruh project Modul 2."""
    fig = plt.figure(figsize=(18, 20))
    fig.patch.set_facecolor('#f5f5f5')

    # ── HEADER ──
    fig.text(0.5, 0.97, 'PROJECT MODUL 2: GAMBAR TEKNIK 2D', fontsize=20, fontweight='bold',
             ha='center', va='top', color='#b71c1c',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffcdd2',
                       edgecolor='#c62828', linewidth=3))
    fig.text(0.5, 0.945, 'PANEL KONTROL MESIN + PROFIL ALUMINIUM',
             fontsize=14, fontweight='bold', ha='center', va='top', color='#c62828')

    # ══════ PROJECT A: PANEL KONTROL ══════
    ax = fig.add_axes([0.03, 0.55, 0.94, 0.38])
    ax.set_xlim(0, 20); ax.set_ylim(0, 15); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 14.5,
                 boxstyle='round,pad=0.3', facecolor='#e8eaf6', edgecolor='#283593', lw=2))
    ax.text(10, 14, '🎛️ PROJECT A: PANEL KONTROL MESIN',
            fontsize=15, fontweight='bold', ha='center', color='#283593')

    # Panel outline
    px, py, pw, ph = 1, 1.5, 8, 10
    ax.add_patch(FancyBboxPatch((px, py), pw, ph,
                 boxstyle='round,pad=0.3', facecolor='#cfd8dc', edgecolor='#37474f', lw=2.5))
    ax.text(px + pw/2, py + ph + 0.5, '200 × 150 mm', fontsize=9, ha='center', fontweight='bold')

    # Mounting holes
    for dx, dy in [(0.5, 0.5), (0.5, ph - 0.5), (pw - 0.5, 0.5), (pw - 0.5, ph - 0.5)]:
        ax.add_patch(plt.Circle((px + dx, py + dy), 0.2, fc='white', ec='#333', lw=1.5))

    # Display cutout
    ax.add_patch(FancyBboxPatch((px + 4.5, py + 7.5), 3, 1.5,
                 boxstyle='round,pad=0.1', facecolor='#263238', edgecolor='#333', lw=1.5))
    ax.text(px + 6, py + 8.25, 'LCD\nDisplay', fontsize=7, ha='center', color='white')

    # Push buttons
    for i in range(3):
        ax.add_patch(plt.Circle((px + 2.5 + i * 1.5, py + 2.5), 0.5,
                     fc='#e53935', ec='#333', lw=1.5))
    ax.text(px + 4, py + 1.5, 'Ø22 Push Buttons', fontsize=7, ha='center', color='#555')

    # Selector
    ax.add_patch(plt.Circle((px + 1.5, py + 8.5), 0.5, fc='#ffa000', ec='#333', lw=1.5))
    ax.text(px + 1.5, py + 7.5, 'Selector', fontsize=7, ha='center', color='#555')

    # E-Stop
    ax.add_patch(plt.Circle((px + 6.5, py + 3), 0.8, fc='#d32f2f', ec='#b71c1c', lw=2))
    ax.text(px + 6.5, py + 3, 'E-STOP', fontsize=6, ha='center', color='white', fontweight='bold')

    # Ventilation slots
    for i in range(5):
        ax.add_patch(FancyBboxPatch((px + 1, py + 4.5 + i * 0.5), 2, 0.15,
                     boxstyle='round,pad=0.05', facecolor='#455a64', edgecolor='#333', lw=1))
    ax.text(px + 2, py + 4, 'Ventilasi', fontsize=7, ha='center', color='#555')

    # Specs
    sx = 11
    ax.text(sx, 12.5, 'SPESIFIKASI:', fontsize=12, fontweight='bold', color='#283593')
    for i, s in enumerate([
        '• Ukuran: 200 × 150 mm, Fillet R10',
        '• 4 mounting Ø6mm (10mm dari tepi)',
        '• Display cutout: 60 × 30 mm, R3',
        '• 3 tombol Ø22mm (spacing 35mm)',
        '• Selector switch Ø22mm + D-cut',
        '• E-stop Ø40mm + marking Ø55mm',
        '• 5 slot ventilasi: 25 × 3mm (R1.5)',
        '• Label area: 50 × 8mm',
    ]):
        ax.text(sx, 11.3 - i * 1.2, s, fontsize=9, ha='left')

    ax.text(sx, 2, 'CONSTRAINTS WAJIB:', fontsize=10, fontweight='bold', color='#c62828')
    for i, c in enumerate(['Symmetric, Equal, Concentric',
                           'Perpendicular, Horizontal, Vertical',
                           'Pattern (slot), Mirror (mounting)']):
        ax.text(sx, 1.2 - i * 0.8, f'• {c}', fontsize=9, ha='left')

    # ══════ PROJECT B: PROFIL ALUMINIUM ══════
    ax = fig.add_axes([0.03, 0.12, 0.94, 0.4])
    ax.set_xlim(0, 20); ax.set_ylim(0, 15); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.1, 0.2), 19.7, 14.5,
                 boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2e7d32', lw=2))
    ax.text(10, 14, '🔩 PROJECT B: SKETCH PROFIL ALUMINIUM',
            fontsize=15, fontweight='bold', ha='center', color='#2e7d32')

    profiles = [('2020', '20×20mm\n4 Slot\nØ5mm bore\nT-slot 6mm', '#42a5f5'),
                ('2040', '20×40mm\n6 Slot\n2× Ø5mm bore\nT-slot 6mm', '#66bb6a'),
                ('3030', '30×30mm\n4 Slot\nØ12mm bore\nT-slot 8mm', '#ffa726'),
                ('4040', '40×40mm\n4 Slot\nØ12mm bore\nT-slot 8mm', '#ef5350')]

    for i, (name, specs, clr) in enumerate(profiles):
        x = 1.5 + i * 4.8
        ax.add_patch(FancyBboxPatch((x - 0.5, 5.5), 4, 7,
                     boxstyle='round,pad=0.3', facecolor='white', edgecolor=clr, lw=2))
        sz = 1.5 + i * 0.3
        ax.add_patch(patches.Rectangle((x + 0.5, 8.5), sz, sz,
                     facecolor=clr, edgecolor='#333', lw=2, alpha=0.4))
        ax.plot([x + 0.5 + sz/2]*2, [8.5, 8.5 + sz], 'k--', lw=0.8, alpha=0.5)
        ax.plot([x + 0.5, x + 0.5 + sz], [8.5 + sz/2]*2, 'k--', lw=0.8, alpha=0.5)
        ax.add_patch(plt.Circle((x + 0.5 + sz/2, 8.5 + sz/2), sz * 0.12,
                     fc='white', ec='#333', lw=1.5))
        ax.text(x + 1.5, 12, f'Profil {name}', fontsize=11, fontweight='bold', ha='center', color=clr)
        ax.text(x + 1.5, 7, specs, fontsize=8.5, ha='center', va='top', color='#333')

    ax.text(10, 2.5, 'TEKNIK: Gambar ¼ profil → Mirror 2× (simetri 4 arah)',
            fontsize=11, ha='center', fontweight='bold', color='#2e7d32',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#c8e6c9', edgecolor='#2e7d32'))
    ax.text(10, 1, 'Constraints: Symmetric + Equal + Perpendicular + Concentric',
            fontsize=10, ha='center', color='#555')

    # ── Footer ──
    fig.text(0.5, 0.06,
             'Deliverables: M02_ProjectA_PanelKontrol.sldprt + 4 file Profil Aluminium (.sldprt)',
             fontsize=11, ha='center', color='#c62828', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffcdd2', edgecolor='#c62828'))
    fig.text(0.5, 0.025, 'Praktikum CAD/CAM — Modul 2: Project Gambar 2D',
            fontsize=10, ha='center', color='#888')

    save(fig, 'p01_deskripsi.png')


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('='*60)
    print(' MODUL 02 — Generating Images')
    print('='*60)

    print('\n📚 Materi:')
    materi_deskripsi()
    m01_sketch_entities_overview()
    m02_rectangle_types()
    m03_circle_arc_types()
    m04_sketch_status()
    m05_sketch_tools()
    m06_dimension_types()
    m07_constraints()
    m08_design_intent()
    m09_drawing_line_types()
    m10_gdt_symbols()
    m11_advanced_sketch()
    m12_reference_geometry()
    m13_drawing_views()
    m14_tips_best_practices()
    m15_slot_polygon_types()
    m16_workflow_sketching()

    print('\n📐 Project:')
    project_deskripsi()
    p01_panel_kontrol_layout()
    p02_panel_kontrol_constraints()
    p03_profil_aluminium_2020()
    p04_profil_aluminium_family()
    p05_sketch_technique()

    print('\n' + '='*60)
    print(f' ✅ Total: 23 gambar berhasil dibuat di image/')
    print('='*60)
