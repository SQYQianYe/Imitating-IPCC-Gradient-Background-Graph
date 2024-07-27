import numpy as np
from matplotlib import pyplot as plt
fontdicts = {'fontsize': 20,
          'fontweight': 'bold',
          'color': 'k',
          'verticalalignment': 'baseline', }
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

def createFigure(figsize=(12, 8), dpi=300, subplotAdj=None, **kwargs):
    figure = plt.figure(figsize=figsize, dpi=dpi, **kwargs)
    if subplotAdj is not None:
        plt.subplots_adjust(**subplotAdj)
    return figure
            
def gradient_image(ax, extent, direction=0.3, cmap_range=(0, 1),
                   vmin=0, vmax=1.5, **kwargs):
    """
    draw gradient image
    :param extent: tuple (xmin, xmax, ymin, ymax)
    :param direction: float
        The direction of the gradient. This is a number in
        range 0 (=vertical) to 1 (=horizontal).
    :param cmap_range: tuple
        The range of the colormap.
    :param vertical: bool
        Whether the gradient is vertical or horizontal.
    :param vmin: float
        Minimum value for normalization.
    :param vmax: float
        Maximum value for normalization.
    :param kwargs: other arguments for imshow.
    
    example:
    # background image
    gradient_image(ax, direction=1, extent=(0, 0.5, 0, 1), transform=ax.transAxes,
                   cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.3)
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    
    if phi == 1:
        X = np.array([[v @ [0, 1], v @ [1, 1]],
                      [v @ [0, 0], v @ [1, 0]]])
    else:
        X = np.array([[v @ [1, 0], v @ [1, 1]],
                      [v @ [0, 0], v @ [0, 1]]])
    
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, extent=extent, interpolation='bicubic',
                   vmin=vmin, vmax=vmax, **kwargs)
    ax.set_aspect('auto')
    return im
createFigure(figsize=(10, 10), dpi=300, subplotAdj=dict(left=0.04, right=0.98,
                                                       top=0.9, bottom=0.05, wspace=0.13, hspace=0.1))
ax = plt.subplot(111)

xmin, xmax = xlim = 1850,2020
ymin, ymax = ylim = -1, 3.5
ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)
gradient_image(ax, direction=0, extent=(1850, 1900, -1, 0.5),
                cmap=plt.cm.gist_gray, cmap_range=(0.2, 0.8), alpha=0.3,
                vmin = 0,vmax = 1)
        
x = np.arange(1850, 2021)
mean = 0.5  
std_dev = 0.3
y = np.clip(np.random.normal(mean, std_dev, len(x)), -0.5, 1.5)

y[149:] += 0.09 * (x[149:] - 1999)

ax.plot(x, y, color='black')

ax.xaxis.set_major_formatter(plt.ScalarFormatter())

plt.show()