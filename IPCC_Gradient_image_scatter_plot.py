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

def adjust_spines(ax, visible_spines):
    for loc, spine in ax.spines.items():
        if loc in visible_spines:
            spine.set_position(('outward', 20))  # outward by 10 points
        else:
            spine.set_visible(False)
            
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

xmin, xmax = xlim = 0, 5
ymin, ymax = ylim = 0, 10
ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)
gradient_image(ax, direction=1, extent=(xmin, xmax, ymin, ymax), 
                cmap=plt.cm.autumn_r, cmap_range=(0, 1), alpha=1,
                vmin = 0,vmax = 1)
ax.set_aspect('auto')

plt.scatter(np.random.uniform(low = 0.8,high = 1.2,size = 100), 
            np.random.uniform(low = 5,high = 8,size = 100), c = "w", edgecolors='k', linewidths = 2)

plt.scatter(np.random.uniform(low = 1.8,high = 2.2,size = 100), 
            np.random.uniform(low = 3,high = 6,size = 100), c = "w", edgecolors='k', linewidths = 2)

plt.scatter(np.random.uniform(low = 2.8,high = 3.2,size = 100), 
            np.random.uniform(low = 1,high = 6,size = 100), c = "w", edgecolors='k', linewidths = 2)


plt.scatter(np.random.uniform(low = 3.8,high = 4.2,size = 100), 
            np.random.uniform(low = 1,high = 8,size = 100), c = "w", edgecolors='k', linewidths = 2)

data1 = np.random.uniform(low=5, high=8, size=100)
data2 = np.random.uniform(low=3, high=6, size=100)
data3 = np.random.uniform(low=1, high=6, size=100)
data4 = np.random.uniform(low=1, high=8, size=100)

# 绘制透明色箱线图
boxplot_data = [data1, data2, data3, data4]
positions = [1, 2, 3, 4]
xticks_labels = ['$>1$', '$>1.5$', '$>2$', '$>3$']

box = plt.boxplot(boxplot_data, positions=positions, widths=0.3, patch_artist=True,
                  showfliers=False,
                  showcaps=False,
                  whis = 0
                  )
grey_color = 'gray'
alpha_value = 0.7
for element in ['boxes', 'whiskers', 'caps', 'medians']:
    plt.setp(box[element], color=grey_color, alpha=alpha_value)
    
for median in box['medians']:
    median.set_color('black')
    median.set_linewidth(3)

for box in box['boxes']:
    box.set_edgecolor('black')
    box.set_linewidth(2)
    

plt.xticks(positions, xticks_labels, weight = 'bold', fontsize = 15)

adjust_spines(ax, ['left', 'bottom'])

plt.xlabel('Global Warming(°C)', fontdict=fontdicts,
           labelpad = 20)
plt.ylabel('% biodiversity change', fontdict=fontdicts)

plt.show()