from manim import *

class cool(Scene):
    def construct(self):
        pos=0.1

        #creating the octagon
        cir=Circle(3.5)
        octagon=[]
        for i in range(8):
            point=cir.point_at_angle((PI/4)+(2*PI*i/8))
            octagon.append(point)
        self.add(Polygon(
            octagon[0], octagon[1], octagon[2], octagon[3], octagon[4], octagon[5], octagon[6], octagon[7], color=BLUE
        ))
        octagon.append(cir.point_at_angle(PI/4))

        #we divide the octagon into 4 quadrilaterals. the quad lists contain the vertices. 3 on the octagon itself, and one is the center of the octagon
        quad1=[cir.get_center()]
        for i in range(3):
            quad1.append(octagon[i])

        quad2=[cir.get_center()]
        for j in range(3):
            quad2.append(octagon[j+2])

        quad3=[cir.get_center()]
        for k in range(3):
            quad3.append(octagon[k+4])
        
        quad4=[cir.get_center()]
        for l in range(3):
            quad4.append(octagon[l+6])

        all_quads=[quad1, quad2, quad3, quad4] #list of all the quadrilateral in the form of constituent vertices
        n=4

        #this group will contain 4 vgroups, each corresponding to a quadrilateral. Each vgroup contains all the lines to be created within that quadrilateral.
        fr=Group(VGroup(), VGroup(), VGroup(), VGroup())
        #this loop loops over the 4 quads, making lines for each quad individually.
        for t in range(4):
            linelist=[]
            for p in range(3):#this loop just takes the array of vertices and gives back an array of edges.
                line=[all_quads[t][p], all_quads[t][(p+1)%n]]
                linelist.append(line)
            
            #this is the part which actually makes the inner lines. the range number corresponds to the numbers of inner lines created.
            for i in range(300):
                lines=VGroup()
                for l in linelist:
                    lines.add(
                        Line(l[0], l[1], color=BLUE)
                    )
                first_line=lines[0]
                last_line=lines[2]
                new_line=Line(
                    last_line.get_end(), first_line.point_from_proportion(pos), color=WHITE, stroke_width=0.8
                )
                linelist.pop(0)
                linelist.append([last_line.get_end(), first_line.point_from_proportion(pos)])
                fr[t].add(new_line)

                for q in lines:
                    lines.remove(q)

        #Now 'fr' contains the 4 quads, and the quads contain 300 inner lines each. This loop goes through all 4 quads together, creating the lines onto the scene.        
        for s in range(300):
            self.play(
                Create(fr[0][s]),
                Create(fr[1][s]),
                Create(fr[2][s]),
                Create(fr[3][s]),
                run_time=0.1
            )
