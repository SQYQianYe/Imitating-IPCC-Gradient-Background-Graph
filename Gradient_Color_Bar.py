import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
config = {
    "font.family": 'DejaVu Sans',
    "font.size": 15,
    'font.style': 'normal',
    'font.weight': 'bold',
    "mathtext.fontset": 'stix',
    "font.serif": ['cmb10'],
    "axes.unicode_minus": False,
}
plt.rcParams.update(config)
np.random.seed(19680801)

def createFigure(figsize=(12, 8), dpi=300, subplotAdj=None, **kwargs):
    figure = plt.figure(figsize=figsize, dpi=dpi, **kwargs)
    if subplotAdj is not None:
        plt.subplots_adjust(**subplotAdj)
    return figure

def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, interpolation='bicubic', clim=(0, 1),
                   aspect='auto', **kwargs)
    return im

def gradient_bar(ax, x, y, yerr=None, width=0.5, bottom=0, cmap=plt.cm.Blues_r):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=cmap, cmap_range=(0, 0.8))
    if yerr is not None:
        ax.errorbar(x + width/2, y, yerr=yerr, fmt='none', ecolor='black', capsize=3, lw=1)

def gradient_legend(ax, cmap, label, loc="upper right", width=0.8, height=0.15, fontsize=10, n_colors=100):
    gradient_rects = []
    for i in range(n_colors):
        x0 = i / n_colors
        x1 = (i + 1) / n_colors
        rect = patches.Rectangle((x0, 0), x1 - x0, 1, facecolor=cmap(i / n_colors))
        gradient_rects.append(rect)

    collection = PatchCollection(gradient_rects, match_original=True, transform=ax.transAxes)
    ax.add_collection(collection)
    ax.annotate(label, xy=(0, 1), xytext=(0, 1.2), xycoords='axes fraction', fontsize=fontsize, fontweight='bold')
    rect = patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='none', lw=1, transform=ax.transAxes)
    # ax.add_patch(rect)

    if loc == "upper right":
        ax.set_position([1 - width, 1 - height, width, height])
    elif loc == "upper left":
        ax.set_position([0, 1 - height, width, height])
    elif loc == "lower left":
        ax.set_position([0, 0, width, height])
    elif loc == "lower right":
        ax.set_position([1 - width, 0, width, height])
        
createFigure(figsize=(12, 8), dpi=300, subplotAdj=dict(left=0.04, right=0.98,
                                                       top=0.9, bottom=0.05, wspace=0.13, hspace=0.1))

ax = plt.subplot(111)
ax.set(xlim=(0, 10), ylim=(0, 1.2))

N = 10
x = np.arange(N) * 1.5
y = np.random.rand(N)
yerr = np.random.rand(N) * 0.1

gradient_bar(ax, x, y, yerr=yerr, width=0.3)
gradient_bar(ax, x + 0.3, y, yerr=yerr, width=0.3, cmap=plt.cm.Reds_r)

legend_ax1 = plt.axes([0, 0, 1, 1])
legend_ax1.axis('off')
gradient_legend(legend_ax1, plt.cm.Blues_r, 'Dataset 1', loc='upper left', width=0.25, height=0.05)
legend_ax2 = plt.axes([0, 0, 1, 1])
legend_ax2.axis('off')
gradient_legend(legend_ax2, plt.cm.Reds_r, 'Dataset 2', loc='upper right', width=0.25, height=0.05)

plt.show()