#!PYRTIST:VERSION:0:0:1
from pyrtist.lib2d import Point, Tri
#!PYRTIST:REFPOINTS:BEGIN
bbox1 = Point(-42.922205241458, 7.0); bbox2 = Point(11.44486546282149, -9.0)
p1 = Point(-14.590651556701694, 4.193243140678511)
p2 = Point(-7.779194223295555, -1.9538922573424884)
p3 = Point(-31.465035560117702, -2.5486180792070385)
p4 = Point(-8.490516285908624, -1.9594335578171727)
p5 = Point(-10.674343839374924, -3.2728012901528114)
p6 = Point(-18.593145985943423, 0.35017322092811654)
p7 = Point(-10.339895054496466, 1.5977532199355622)
#!PYRTIST:REFPOINTS:END
from pyrtist.lib2d import *

def body(position, size, lw, n=3, highlight=set()):
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
  for i in (-1, 1):
   for j in (-1, 0, 1):
     color = (Color.red if (i, j) in highlight else Color.black)
     args.append(Circle(color, 1.5 * lw,
                        position + 0.5 * Point(size.x *i, size.y * j)))

  return Args(*args)

def draw(destination, label_position, label_offset):
  w = Window()
  w << BBox(bbox1, bbox2)

  lw = 0.2
  font = Font(1.5)
  small_font = Font(1.25)
  size = Point(10, 10)

  pos2 = Point(p1.x, p2.y)
  p3.y = pos2.y
  c_size = Point(0.5 * size.x, size.y)
  w << Line(p3, pos2, Border(Color.black, lw * 0.5, Dash(0.5)))
  w << body(pos2, c_size, lw, highlight={destination})
  w << Color.red
  w << Line(p1, Point(p2.x, p1.y), Border(lw * 1.25), Scale(0.75), arrows.triangle)
  w << Circle(p1, lw * 1.5)

  p = Point(pos2.x + 0.5 * c_size.x, pos2.y)
  dr = 0.5
  w << Color.red
  w << Line(2 * lw, p - Point(dr, dr), p + Point(dr, dr))
  w << Line(2 * lw, p - Point(dr, -dr), p + Point(dr, -dr))

  info_color = (1, 0.4, 0)
  w << Circle(Style(Color(*info_color, 0.3), Border(Color(*info_color, 0.6), lw * 0.5, Dash(0.4))),
              p, (p5 - p).norm())
  dr = 2.2
  w << Line(Border(1.2, Color(1, 1, 1, 0.4), Cap.round), p4 - Point(dr, 0), p4 + Point(dr, 0))
  w << Text(small_font, p, Offset(-0.2, 0.4), "collision")

  w << Color(info_color)
  w << Text(small_font, Color.red, Point(0.5 * (p1.x + p2.x), p1.y), Offset(0.5, -0.2), "velocity")

  p = pos2 + 0.5 * Point(c_size.x * destination[0], c_size.y * destination[1])
  w << Color.red
  w << Line(0.5 * lw, p, label_position)
  w << Text(small_font, label_position, Offset(*label_offset), "destination")
  return w

draw_table = [
  [(-1, 0), p6, (1.03, -0.1)],
  [(1, 1), p7, (-0.01, 0.8)],
  #[(-1, 1), p6, (1.02, 0.8)],
]

def draw_numbered(number):
  return draw(*draw_table[number])

w = draw_numbered(1)

if not gui.is_connected():
  for i in range(len(draw_table)):
    file_name = f'dynamics-latency-{i + 3}.svg'
    w = draw_numbered(i)
    print(f'Saving picture {file_name}')
    w.save(file_name, width=19.5, unit='cm')

gui(w)
