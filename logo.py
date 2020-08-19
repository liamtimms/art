from p5 import *

l = 50
w = l # until debug
d = 5
c = 10
c_offset = 0

L = 4*l + 4*d
W = 3*w + 3*d

def setup():
    size(W+d, L+d)
    no_stroke()
    no_loop()

def draw():
    background(255)

    # T
    fill(c+c_offset)
    rect((d,d), 3*w+2*d, l)
    rect((2*d+l, d),  w, 3*l+2*d)
    # L
    fill(c+2*c_offset)
    rect((d, 2*d+w),  w, 3*l+2*d)
    rect((d,3*l+4*d), 2*w+d, l)
    # !
    fill(c+3*c_offset)
    rect((3*d+2*w, l+2*d),  w, 2*l+d)
    rect((3*d+2*w, 3*l+4*d), w, l)
    # for x in range(0, int(W/w)):
    #     square((x*w+(1+x)*d, d), w)
    #     for y in range(0, int(L/l)):
    #         square((x*w+(1+x)*d, d), w)

if __name__ == '__main__':
    run()
