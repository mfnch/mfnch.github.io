#!PYRTIST:VERSION:0:0:1
from pyrtist.lib2d import Point, Tri
#!PYRTIST:REFPOINTS:BEGIN
bbox1 = Point(-45.854831058159284, -13.860537098862526)
bbox2 = Point(30.88090215792002, 26.521841088055414)
p1 = Point(-26.688367968947343, 23.311799672530423)
p2 = Point(-31.608295297490038, 17.419825643973564)
p3 = Point(-42.33857321214607, 6.964113054313678)
p4 = Point(-23.698991186551567, 2.84105841648239)
p5 = Point(30.048992856242982, 18.77173062050121)
p9 = Point(11.706352696731152, 22.28391616776375)
#!PYRTIST:REFPOINTS:END
from pyrtist.lib2d import *

w = Window()

c23 = 0.5 * (p2 + p3)
v12 = p2 - p1


def draw(w, title, color1, color2, final_color, origin, *points):
  origin = origin - points[0]
  p = [Point(p) + origin for p in points]
  p[3].x = p[0].x
  q0 = Point(p[0].x, p[1].y)
  q1 = Point(2 * q0.x - p[2].x, p[2].y)
  q2 = Point(q0.x, 0.5 * (q0.y + q1.y))
  q3 = Point(q1.x, q0.y)
  r = 8

  border = Border(Color.black, 0.2)
  w << Args(
    Text(Font(2), Color.black, p[0], title),
    Rectangle(q0, p[2], color1),
    Text(0.5 * (q0 + p[2]), Font(1.8), Color.white, str(tuple(color1))),
    Rectangle(q0, q1, color2),
    Text(0.5 * (q0 + q1), Font(1.8), Color.black, str(tuple(color2))),
    Rectangle(p[2], q3, Color(0, 0, 0, 0), border),
    Color.black,
    Circles(q2, 1, 1.3),
    Line(0.5, q2 - Point(0, 1.2), p[3], Scale(0.8), arrows.triangle),
    Circle(p[3] - Point(0, r), r + 0.1, final_color),
    Text(p[3] - Point(0, r), Font(1.5), Color.black, str(tuple(final_color))),
    Circles(p[3] - Point(0, r), r, r + 0.3)
  )

# Checkerboard to show transparency.
def checkerboard(p, d, num_rows, num_cols):
  points = []
  x, y = p
  dx = 2 * num_cols * d
  for i in range(num_rows):
    points.extend([Point(x, y), Point(x + dx, y), Point(x + dx, y + d), Point(x, y + d)])
    y += 2 * d
  dy = 2 * num_rows * d
  for i in range(num_cols):
    points.extend([Point(x, y), Point(x, y - dy), Point(x + d, y - dy), Point(x + d, y)])
    x += 2 * d
  points.extend([Point(x, y), Point(x, y - dy)])
  return points
w << Poly(Grey(0.8), *checkerboard(bbox1, (bbox2 - bbox1).x / 22.0, 5, 11))

draw(w, "Without texture premultiplication",
     Color(1, 0, 0, 0.7), Color(0, 1, 0, 0.1), Color(0.5, 0.5, 0, 0.4),
     p1, p1, p2, p3, p4)
p9.y = p1.y
draw(w, "With texture premultiplication",
     Color(1, 0, 0, 0.7), Color(0, 1, 0, 0.1), Color(0.875, 0.125, 0, 0.4),
     p9, p1, p2, p3, p4)
w << BBox(bbox1, bbox2)
w.save('premultiplication.svg', width=19.5, unit='cm')

gui(w)
