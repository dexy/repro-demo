## Contour Plots

Illustrate simple contour plotting, contours on an image with
a colorbar for the contours, and labelled contours.

Examples from <http://matplotlib.org/gallery.html>

<!-- @export "generating-data" -->
### Generating Data

Here's how we generate the data we will use to plot:

{{ d["contour_demo.py|idio|pycon|pyg"]["generate-data"] }}

Delta is {{ d['vars.json']['delta'] }}.

<!-- @export "graphing-defaults" -->
### Graphing Defaults

We set up some Matplotlib defaults before we start making plots:

{{ d["contour_demo.py|idio"]["graphing-defaults"] }}

<!-- @export "simple-contour-plot" -->
### Simple Contour Plot

Create a simple contour plot with labels using default colors.  The
inline argument to clabel will control whether the labels are draw
over the line segments of the contour, removing the lines beneath
the label

{{ d["contour_demo.py|idio"]["simple-contour-plot"] }}

![contour plot](simple-contour-plot.png)
<!-- @end -->

### Contour Labels

Contour labels can be placed manually by providing list of positions (in data coordinate).

{{ d["contour_demo.py|idio"]["contour-labels"] }}

![contour plot](contour-plot-manual-labels.png)

### Negative Contours

You can set negative contours to be solid instead of dashed:

{{ d["contour_demo.py|idio"]["negative-contours"] }}

![contour plot](negative-contours-solid.png)

### Colormap

Or you can use a colormap to specify the colors; the default
colormap will be used for the contour lines

{{ d["contour_demo.py|idio"]["colormap"] }}

![colormap](colormap.png)
