from manim import *


def projection_point_line(point, line):
    """Projection of a point on a line"""
    p = np.array(point)
    a, b = np.array(line.get_start()), np.array(line.get_end())
    ap = p - a
    ab = b - a
    return a + np.dot(ap, ab) / np.dot(ab, ab) * ab


class all(Scene):
    def construct(self):
        #Setup
        tr = Triangle().scale(3).shift(DOWN*0.8)
        dot=Dot(ORIGIN)
        perps=VGroup(VMobject(), VMobject(), VMobject(), VMobject(), VMobject(), VMobject()) #vgroup of the 3 perpendiculars and foots.
        colors=['#FFC0CB', RED, GREEN]

        #updater to get the perpendicular lines
        def get_perps(grp):
            for i in range(3):
                side = Line(tr.get_vertices()[i], tr.get_vertices()[(i+1)%3])
                p = projection_point_line(dot.get_center(), side)
                grp[i+3].become(Dot(p, color=YELLOW))
                grp[i].become(Line(dot.get_center(), p, color=colors[i]))
        perps.add_updater(get_perps)
        
        path=Circle(radius=1).shift(DOWN*0.9) #circular path for the point to move along.
        self.add(perps, tr, path)

        #implementing a distance formula
        def distance(p1, p2):
            dist=(((p2.get_y()-p1.get_y())**2)+((p2.get_x()-p1.get_x())**2))**(1/2)
            return dist

        #This section creates an updater to get the lenghts of each perpendicular, into the a,b,c arrays and also displays the lenght values on screen.
        a=[]
        b=[]
        c=[]
        lenghts=VGroup(DecimalNumber(0), DecimalNumber(0), DecimalNumber(0))
        def get_lenght(grp):
            a.append(lenghts[0].get_value())
            b.append(lenghts[1].get_value())
            c.append(lenghts[2].get_value())
            for i in range(3):
                grp[i].set_value(distance(
                    dot, Dot(projection_point_line(dot.get_center(), Line(tr.get_vertices()[i], tr.get_vertices()[(i+1)%3])))
                    ))
        lenghts.add_updater(get_lenght)

        for i in range(3):
            lenghts[i].shift(RIGHT*3+UP*(i-1))

        self.add(lenghts)
        self.play(MoveAlongPath(dot, path, rate_func=linear), run_time=1)
        self.wait(2)