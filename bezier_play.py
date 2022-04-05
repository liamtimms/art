#
# Bezier
#
# The first paramtere for the bezier() function specifies the first
# point in the curve and the last parameter specifies the last point.
# The middle parameters set the control points that define the shape
# of the curve.
#

from p5 import *
w = 1640
h = 900

def setup():
    size(w, h)
    no_fill()

def draw():
    background(0)
    for i in range(0, 200, 10):
        control_1 = (410+i, -20)
        control_2 = (-440, 300-i*2)

        stroke(0+i)
        start_point_1 = (mouse_x - (i / 2.0), mouse_y + i)
        end_point_1 = (w/2 - (i / 26), 30 + (i / 8))
        bezier(start_point_1, control_1, control_2, end_point_1)

        start_point_2 = end_point_1
        end_point_2 = (mouse_x - (i / 2.0), mouse_y + i)
        stroke(255-i)
        bezier(start_point_2, control_1, control_2, end_point_2)

run()
