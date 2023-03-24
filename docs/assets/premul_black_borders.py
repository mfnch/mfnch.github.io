#!PYRTIST:VERSION:0:0:1
from pyrtist.lib2d import Point, Tri
#!PYRTIST:REFPOINTS:BEGIN
bbox1 = Point(-7.711908911905066, 7.580698993004244)
bbox2 = Point(7.523436704513685, -7.670398112973594)
p1 = Point(-0.8224402371949857, 2.4302209232852476)
p2 = Point(1.5828343872972148, -0.15060695223687137)
#!PYRTIST:REFPOINTS:END
'''
# This example shows how to draw a house in a cartoon-ish way.
# I had in mind the typical house here in England...

from pyrtist.lib2d import *

# We definitely need a brick pattern to draw the walls
# Try to change to gui(bricks) to see how this is done.

# Just one brick.
brick = Window()
brick << Args(
  Poly(Color(1.000, 0.496, 0.000), 0.5,
       p1, p2, p3, p4, p5, p6, p7, p8, p9, p10),
  Hot("center", p11)
)

# A brick pattern, which we save as a cairo surface.
bricks = Window()
bricks << Args(Put(brick),
               Put(brick, "t", Near("center", p12)),
               BBox(bbox1, bbox2))
surface = bricks.draw(mode="rgb24", resolution=50/25.4)

# We make a proper pattern using the cairo surface.
pat = Image(surface, Scale(3.5), Extend.reflect, Filter.best)

house = Window()
house << BBox(bbox3, bbox4)

# Colors used below.
panes_color = Color(0.85, 0.95, 1)
window_color = Grey(1)
door_color = Color(0.545, 0.272, 0.078)
border = Border(Color.black, 0.5, Join.round, Cap.round)

roof_color_bright = Color(0.9, 0.35, 0.3)
roof_color = Color(0.647, 0.165, 0.165)

# Roof.
house << Args(
  Poly(r1, r2, r3, r4, r5, r6, Style(roof_color, border)),
  Line(r7, r8, r9, roof_color_bright, Border(1, Cap.round)),
  Poly(r10, r11, r12, r13, roof_color.darken(0.3)),
  Poly(r14, r15, r16, r17, roof_color.darken(0.3)),
)

# Just to make the floor more regular...
q4.y = q5.y = q8.y = q1.y

# Now draw the door.
house << Args(
  Poly(q8, q7, q6, q5, q5, Style(border, door_color)),
  Poly(q10, q11, q12, q13, Style(border, door_color.darken(0.6))),
  Poly(q14, q15, q16, q17, Style(border, door_color.darken(0.6))),
  Poly(q1, q2, q9, q3, q4, q5, q6, q7, q8, Style(pat, border)),
  # And the door handle.
  Circle(q18, 1),
  Circle(q19, 0.3, Grey(0.5))
)

# Create a window.
window = Window()
window_marks = Border(Color.black, 0.3, Cap.round)
window << Args(
  Poly(p14, p15, p16, p17, Style(border, window_color)),
  Poly(p14, p17, p18, p19, p20, p21,
       Style(border, window_color.darken(0.8))),
  Poly(p22, p23, p24, p25, Style(panes_color.darken(0.9), border)),
  Poly(0.4, w1, w2, w3, w4, panes_color.darken(0.95)),
  Poly(0.4, w5, w6, w7, w8, panes_color),
  Hot("center", w9)
)
window << Args(Line(window_marks, *ab)
               for ab in [(w10, w11), (w12, w13), (w14, w15), (w16, w17)])

# And draw it twice.
house << Args(
  Put(window),
  Put(window, "t", Near("center", p26))
)

#house.save('house.png')

gui([house, bricks][0])
'''

from pyrtist.lib2d import *

pat = Image("premul_black_borders-orig.png", Scale(16), Offset(0.5, 0.5), Extend.none, Filter.nearest)

w = Window()

w << Args(
  Rectangle(bbox1, bbox2, Style(pat)),
  Color.white,
  Text(p1, "spurious\nblack border", Offset(0.55, -0.1)),
  Line(0.1, p1, p2, arrows.triangle),
  BBox(bbox1, bbox2)
)

w.save('premul_black_borders.png', resolution=25)
gui(w)
