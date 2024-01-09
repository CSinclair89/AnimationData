from pygooglechart import PieChart3D


# initialize chart object, 250 x 250 pixels
chart = PieChart3D(250, 250)

# pass your data to the chart object
chart.add_data([398, 294, 840, 462])

# make labels for the slices
chart.set_pie_labels("Lithuania Bulgaria Ukraine Romania".split())

# render the image
chart.download('revenue_east_europe.png')


