import math
from pyaxidraw import axidraw
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.units = 2        # Set mm units
if not ad.connect():        # Open serial port to AxiDraw;
    quit()                  #   Exit, if no connection.

# Make a list of points to draw a square, 1 cm on a side:
vertices = []
for vertex in range(1000):
    x_position = vertex/10
    y_position = 25 + 10 * math.sin(math.tau * vertex / 100)
    vertices.append([x_position, y_position])
ad.draw_path(vertices)      # Plot the path
ad.moveto(0, 0)             # Return Home
ad.disconnect()             # Close serial port