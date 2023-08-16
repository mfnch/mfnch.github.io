#!PYRTIST:VERSION:0:0:1
from pyrtist.lib2d import Point, Tri
#!PYRTIST:REFPOINTS:BEGIN
bbox1 = Point(-42.922205241458, 7.0); bbox2 = Point(11.44486546282149, -9.0)
p1 = Point(-19.99614157881298, 6.0)
p2 = Point(-13.217222542541794, 0.4572903945182496)
p3 = Point(-36.90306387936394, -0.13743542734630054)
p4 = Point(-14.117950590193516, -2.7363741787141542)
p5 = Point(-17.15575708384514, -5.275289388497956)
p6 = Point(-14.443905430366186, 0.8156894951568585)
p7 = Point(-15.119643922286553, -7.05535218469992)
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
  #args.append(Circle(Color.black, 1.5 * lw,
  #            position + 0.5 * Point(size.x *i, size.y * j))
  #            for i in (-1, 1) for j in (-1, 1))

  return Args(*args)

lw = 0.2
font = Font(1.5)
small_font = Font(1.25)
size = Point(10, 10)

pos2 = Point(p1.x, p2.y)
p3.y = p2.y
c_size = Point(0.5 * size.x, size.y)
w << body(pos2, c_size, lw)
w << Line(p3, pos2, Border(Color.black, lw * 0.5, Dash(0.5)))
w << Color.red
w << Line( pos2, p2, Border(lw * 1.25), Scale(0.75), arrows.triangle)
w << Circle(pos2, lw * 1.5)


pos4 = Point(pos2.x + 0.5 * c_size.x, p4.y)
dr = 0.5
w << Color.red
w << Line(2 * lw, pos4 - Point(dr, dr), pos4 + Point(dr, dr))
w << Line(2 * lw, pos4 - Point(dr, -dr), pos4 + Point(dr, -dr))

info_color = (1, 0.4, 0)
w << Circle(Style(Color(*info_color, 0.3), Border(Color(*info_color, 0.6), lw * 0.5, Dash(0.4))),
            pos4, (p5 - pos4).norm())
dr = 2.2
w << Line(Border(1.2, Color(1, 1, 1, 0.4), Cap.round), p4 - Point(dr, -0.05), p4 + Point(dr, -0.05))
w << Text(small_font, pos4, Offset(-0.08, 0.4), "collision at time t_0")

w << Color(info_color)
w << Line(0.5 * lw, p5, p7)
w << Text(small_font, p7, Offset(-0.02, 0.5),
          "collision information propagating\nspherically at the speed of light")
w << Text(small_font, Color.red, p6, Offset(0.5, 0.0), "velocity")

if not gui.is_connected():
  print('Saving picture')
  w.save('dynamics-latency-2.svg', width=19.5, unit='cm')

gui(w)
