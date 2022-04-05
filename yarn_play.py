################################################################################
# original by Aaron Penne
# 2018-09-16
# https://github.com/aaronpenne
################################################################################
# adapted by Liam Timms

from p5 import *
import datetime
import math
import random
import sys
import os

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

sneed = 1171989
random.seed(sneed)
random_seed(sneed)

anchors = []
len_anchors = 0
count = 0

pal = [(348.7, 50.4, 94.9),  # bright salmon
       (306.6, 40.8, 96.1), # bright pink
       (45.7, 78.8, 94.1),  # yellow
       (16.3, 28.6, 96.1),  # salmon
       (358.7, 75.6, 94.9), # red
       ]

w = 1000  # width
h = 1000  # height

# Number of positions across canvas
step = 5

# Number of points around individual circle
num_anchors = 15

# Radius of individual circle
r_mult = 0.75  # Decimal multiplier is pct of space to fill
radius = w/(2*step) * r_mult

# Size of lines
stroke_weight = 1

# Size of empty space between edge and piece
w_pad = 2
h_pad = 2

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    global anchors, len_anchors
    anchors = range_float(0+math.pi/2, 2*math.pi+math.pi/2, 2*math.pi/num_anchors)
    len_anchors = len(anchors)
    no_loop()

def draw():
    # Loop counter to control number of draw() runs
    global count
    print(count)
    if count >= len_anchors-1:
        sys.exit(0)
    count += 1

    background(0, 0, 100)

    w_step = w/step
    h_step = h/step

    no_stroke()
    fill(16.3, 28.6, 96.1, 4)

    for j in range(10):
        x = random(0, w)
        y = random(0, h)
        for i in range(10):
            begin_shape()
            draw_yarn_ball(x, y, w/2*0.7)
            end_shape()

def draw_yarn_ball(x_center, y_center, radius):
    # Get three start/end points. The curve needs to retrace these 3 points to connect in a smooth loop
    # https://forum.processing.org/two/discussion/14849/how-to-form-a-smooth-loop-using-curve
    x_0, y_0 = circle_points(x_center, y_center, radius, random_list_value(anchors))
    curve_vertex(x_0, y_0)
    x_1, y_1 = circle_points(x_center, y_center, radius, random_list_value(anchors))
    curve_vertex(x_1, y_1)
    x_2, y_2 = circle_points(x_center, y_center, radius, random_list_value(anchors))
    curve_vertex(x_2, y_2)
    random.shuffle(anchors)
    for a in anchors:
        x, y = circle_points(x_center, y_center, radius, a)
        curve_vertex(x, y)
    curve_vertex(x_0, y_0)
    curve_vertex(x_1, y_1)
    curve_vertex(x_2, y_2)

def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves each frame with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_{}_####.png'.format(timestamp, filename, rand_seed))
    save_frame(output_filename)
    print(output_filename)

def save_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves image with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.png'.format(timestamp, filename))
    save(output_filename)
    print(output_filename)

def random_list_value(val_list):
    '''Returns a random value from a list'''
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value


def random_centered(value_og, offset=5):
    '''Randomly varies value_og within the offset range'''
    value = random(value_og-offset, value_og+offset)
    return value


def random_gaussian_limit(min_val, max_val):
    '''Same as built-in randomGaussian but truncated to within a range'''
    new_val = max_val*random_gaussian()+min_val
    if new_val < min_val:
        new_val = min_val
    elif new_val > max_val:
        new_val = max_val
    return new_val


def circle_points(origin_x, origin_y, r=50, a=0):
    '''Returns cartesian coordinates given a circle origin, radius, and angle'''
    x = origin_x + (r * cos(a))
    y = origin_y + (r * sin(a))
    return x, y

def range_float(start_val, end_val, inc_val):
    '''
    Allows for similar functionality to built-in range() but with float step values
    Adapted from http://code.activestate.com/recipes/66472/
    '''
    start_val = float(start_val)
    end_val = float(end_val)
    inc_val = float(inc_val)

    count = int(math.ceil((end_val - start_val) / inc_val))

    L = [None,] * count

    L[0] = start_val
    for i in range(1,count):
        L[i] = L[i-1] + inc_val
    return L


if __name__ == '__main__':
    run()
