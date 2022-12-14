#!PYRTIST:VERSION:0:0:1
from pyrtist.lib2d import Point, Tri
#!PYRTIST:REFPOINTS:BEGIN
a1 = Point(6.546944497742956, 1.972522234997868)
af1 = Point(24.701997537112668, 13.752266058683167)
af2 = Point(22.379870903443, 6.61443996088539)
ai1 = Point(6.656473911451954, 9.762118161261606)
ai2 = Point(12.94230529261791, 7.719697551054905)
axis1 = Point(45.68537543081555, 22.500506912573893)
bbox1 = Point(-3.210913657391826, 24.051235044230708)
bbox2 = Point(49.817079679961466, -6.996937701211181)
origin1 = Point(16.50811104009687, -0.1497825072322314)
p6 = Point(1.8732865480355372, -5.121394918090672)
p8 = Point(4.99437083725779, 15.94642663797599)
p9 = Point(34.09659033571045, 13.908939751665095)
question1 = Point(29.588359236303056, 17.490474510018924)
question2 = Point(5.243609515000877, 14.045485844401899)
p3 = Tri(p6, Point(0.8250323768837546, 1.2245005760562506))
p4 = Tri(p8, Point(17.212571060952634, 18.819267346861547))
p5 = Tri(p9, Point(35.05620227563241, 4.5656202170512685))
#!PYRTIST:REFPOINTS:END
from pyrtist.lib2d import *

# Style settings
# Thickness
axis_tk = 0.08
vector_tk = 0.2
acc_tk = 0.4
point_tk = 0.3
curve_tk = 0.2
# Color
color_ini = Color(0.4, 0.7, 0.3)
color_fin = Color(1.0, 0.4, 0.3)
color_mid = Color(1.0, 0.7, 0.3)
# Line style
curve_style = StrokeStyle(curve_tk, Dash(0.5, 1.0), Cap.round)
# Text font
axis_font = Font('Palatino', 1.3)
font = Font('Palatino', 2.0)
question_font = Font('palatino', 3)

def generate(with_mid=True):
    w = Window()
    g = Gradient(Circles(origin1, 0, 50.0),
                 0.2, Grey(0.94),
                 Color(1.0, 0.95, 0.8),
                 1.0, Color(0.85, 0.82, 0.8))
    w << Rectangle(bbox1, bbox2, g)

    w << BBox(bbox1, bbox2)
    w << Color.black

    # Axes
    x_axis, y_axis = (Point(axis1.x, origin1.y), Point(origin1.x, axis1.y))
    w << Line(axis_tk, origin1, x_axis, Scale(1.5), arrows.line)
    w << Line(axis_tk, origin1, y_axis, Scale(1.5), arrows.line)
    w << Text(axis_font, origin1, "O", Offset(1.1, 1.3))
    w << Text(axis_font, x_axis, "x", Offset(0, 1.5))
    w << Text(axis_font, y_axis, "y", Offset(-0.2, 0))

    # Curve
    if with_mid:
      curve_ini = Curve(p3, p4, Close.no)
      w << color_ini << Stroke(curve_style, Path(curve_ini))
      w << Text(question_font, '?', question2, Offset(0, 0))
      curve_fin = Curve(p4, p5, Close.no)
      w << color_fin << Stroke(curve_style, Path(curve_fin))
      w << Text(question_font, '?', question1, Offset(0, 0))
    else:
      curve = Curve(p3, p4, p5, Close.no)
      w << Grey(0.65)
      w << Stroke(curve_style, Path(curve))
      w << Text(question_font, '?', question1, Offset(0, 0))

    # Velocity vectors
    w << color_ini << Line(vector_tk, p3.p, p3.op, arrows.triangle)
    w << Circle(p3.p, point_tk)
    w << Text(font, 0.5 * (p3.p + p3.op), "v_I", Offset(1.3, 1.5))
    w << Text(font, p3.p, "t_I", Offset(1.2, 1.1))

    if with_mid:
      w << color_mid << Line(vector_tk, p4.p, p4.op, arrows.triangle)
      w << Circle(p4.p, point_tk)
      w << Text(font, 0.5 * (p4.p + p4.op), "v_M", Offset(1.3, -0.1))
      w << Text(font, p4.p, "t_M", Offset(0.3, -0.4))

    w << color_fin << Line(vector_tk, p5.p, p5.op, arrows.triangle)
    w << Circle(p5.p, point_tk)
    w << Text(font, 0.5 * (p5.p + p5.op), "v_F", Offset(1.3, 1.5))
    w << Text(font, p5.p, "t_F", Offset(-0.3, -0.1))

    # Position vectors
    w << color_ini << Line(vector_tk, origin1, p3.p, arrows.triangle)
    w << Text(font, 0.5 * (p3.p + origin1), "r_I", Offset(0.5, 1.5))

    if with_mid:
      w << color_mid << Line(vector_tk, origin1, p4.p, arrows.triangle)
      w << Text(font, 0.5 * (p4.p + origin1), "r_M", Offset(-0.3, 0.5))

    w << color_fin << Line(vector_tk, origin1, p5.p, arrows.triangle)
    w << Circle(origin1, point_tk)
    w << Text(font, 0.5 * (p5.p + origin1), "r_F", Offset(0.5, 1.5))

    # Accelerations
    if with_mid:
      w << color_ini << Line(acc_tk, ai1, ai2, Scale(0.7), arrows.triangle)
      w << Text(font, 0.5 * (ai1 + ai2), "a_I", Offset(0.5, -0.5))
      w << color_fin << Line(acc_tk, af1, af2, Scale(0.7), arrows.triangle)
      w << Text(font, 0.5 * (af1 + af2), "a_F", Offset(-0.4, 0.5))

    return w

w1 = generate(with_mid=False)
w1.save('analytical-positioning-figure-1.svg', width=19.5, unit='cm')

w2 = generate(with_mid=True)
w2.save('analytical-positioning-figure-2.svg', width=19.5, unit='cm')

#gui(w1)
gui(w2)
