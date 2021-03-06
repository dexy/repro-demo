### "imports"
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

### "graphing-defaults"
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

### "generate-data"
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = 10.0 * (Z2 - Z1)
X
Y

### "excel"
import xlwt
book = xlwt.Workbook()

sheet = book.add_sheet('X')

for i in xrange(len(X)):
    x = X[i]
    for j in xrange(len(x)):
        sheet.write(i, j, x[j])

sheet = book.add_sheet('Y')

for i in xrange(len(Y)):
    y = Y[i]
    for j in xrange(len(y)):
        sheet.write(i, j, y[j])

sheet = book.add_sheet('Z')

for i in xrange(len(Z)):
    z = Z[i]
    for j in xrange(len(z)):
        sheet.write(i, j, z[j])

book.save('contour_demo_data.xls')

### "simple-contour-plot"
plt.figure()
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')
with open("simple-contour-plot.png", "wb") as f:
    plt.savefig(f)

### "contour-labels"
plt.figure()
CS = plt.contour(X, Y, Z)
manual_locations = [(-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
plt.clabel(CS, inline=1, fontsize=10, manual=manual_locations)
plt.title('labels at selected locations')
with open("contour-plot-manual-labels.png", "wb") as f:
    plt.savefig(f)

### "negative-contours"
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
plt.figure()
CS = plt.contour(X, Y, Z, 6,
                 colors='k', # negative contours will be dashed by default
                 )
plt.clabel(CS, fontsize=9, inline=1)
plt.title('Single color - negative contours solid')
with open("negative-contours-solid.png", "wb") as f:
    plt.savefig(f)

### "colormap"
plt.figure()
im = plt.imshow(Z, interpolation='bilinear', origin='lower',
                cmap=cm.gray, extent=(-3,3,-2,2))
levels = np.arange(-1.2, 1.6, 0.2)
CS = plt.contour(Z, levels,
                 origin='lower',
                 linewidths=2,
                 extent=(-3,3,-2,2))
with open("colormap.png", "wb") as f:
    plt.savefig(f)


### "params"
import json
variables = {
        'delta' : delta
        }
with open("vars.json", "wb") as f:
    json.dump(variables, f)
