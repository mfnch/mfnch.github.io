#!PYRTIST:VERSION:0:0:1
from pyrtist.lib2d import Point, Tri
#!PYRTIST:REFPOINTS:BEGIN
bbox1 = Point(-42.922205241458, 20.346858333782937)
bbox2 = Point(11.44486546282149, -10.869692244746801)
p1 = Point(-19.78700635764263, 14.247307094742332)
p2 = Point(-13.008087321371441, 0.25075195056037813)
p3 = Point(-36.693928658193585, -0.343973871304172)
p4 = Point(-16.41847374214873, -5.245628926220732)
p5 = Point(-14.709764401277038, -8.209783371112152)
p6 = Point(-16.111857939650438, 0.9527658354152173)
#!PYRTIST:REFPOINTS:END
from pyrtist.lib2d import *

w = Window()
w << BBox(bbox1, bbox2)


def body(position, size, lw, n=3):
  args = []
  corner = position - 0.5 * size
  style = Style(Grey(0.75), Border(Color.black, lw, Join.round, Cap.round))
  args.append(Rectangle(corner, position + 0.5 * size, style))

  style = Border(Color.black, lw)
  for iy in range(1, n):
    y = corner.y + size.y * iy / n
    args.append(Line(Point(corner.x, y), Point(corner.x + size.x, y), style))
  for ix in range(1, n):
    x = corner.x + size.x * ix / n
    args.append(Line(Point(x, corner.y), Point(x, corner.y + size.y), style))

  return Args(*args)

lw = 0.2
font = Font(1.5)
small_font = Font(1.25)
size = Point(10, 10)

w << Text(font, p1 + Point(size.x, 0), Offset(0, 0.5),
          "Body at rest:\nuncontracted")
w << body(p1, size, lw)

pos2 = Point(p1.x, p2.y)
p3.y = p2.y
c_size = Point(0.5 * size.x, size.y)
w << Text(font, pos2 + Point(size.x, 0), Offset(0, 0.5),
          "Body moving to the right:\nLorentz-contracted")
w << body(pos2, c_size, lw)
w << Line(p3, pos2, Border(Color.black, lw * 0.5, Dash(0.5)))
w << Color.red
w << Line( pos2, p2, Border(lw * 1.25), Scale(0.75), arrows.triangle)
w << Circle(pos2, lw * 1.5)

x = pos2.x + 0.5 * c_size.x
w << Color.black
w << Line(lw * 0.5, Point(x, p4.y), Scale(1.25), arrows.line, Point(x, p5.y), p5)
w << Text(small_font, p5, Offset(-0.1, 0.5), "front\n(predestined)")

m5 = Point(2 * p1.x - p5.x, p5.y)
x = pos2.x - 0.5 * c_size.x
w << Line(lw * 0.5, Point(x, p4.y), Scale(1.25), arrows.line, Point(x, m5.y), m5)
w << Text(small_font, m5, Offset(1.1, 0.5), "             back\n(changeable)")

text = Window()
text << Text(small_font, Color.red, p6, Offset(0, 0.5), "velocity")
w << Put(text, Center(p6), AngleDeg(45))

if not gui.is_connected():
  print('Saving picture')
  w.save('dynamics-latency-1.svg', width=19.5, unit='cm')

gui(w)
