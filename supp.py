import numpy as np

#A bunch of linear algebra operations I wrote with numpy.

#A vector refers to a one dimensional numpy array, with 3 values, each correspoding to the x, y and z component of the vector respectively.
#All vector by defualt from [0,0,0].
#A point is the same as a vector, in the sense that vectors are just given as the point their head lies on.
def magnitude(vector):
    x, y, z= vector
    return (x**2+y**2+z**2)**(1/2)

def distance_formula(p1, p2):
    x1, y1, z1=p1
    x2, y2, z2=p2
    distance=(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))**(0.5)
    return distance

def projection(point, a, b):
    #this gives you the foot of a perendicular, from point onto a line from a to b
    ap=point-a
    ab=b-a
    projection=a+(np.dot(ap, ab)/magnitude(ab)**2)*ab
    return projection

def section(point1, point2, proportion):
    x1, y1, z1= point1
    x2, y2, z2= point2
    n=1-proportion
    x=proportion*x2+n*x1
    y=proportion*y2+n*y1
    z=proportion*z2+n*z1
    return [x, y, z]

def angle_bw(v1, v2):
    dot=np.dot(v1, v2)
    a, b= magnitude(v1), magnitude(v2)
    angle=(
        np.arccos(dot/(a*b))
    )
    return angle

def get_intersection(line1, line2):
    # A line is given as a 2 dimensional list. Meaning a line is a list of 2 points, and the 2 points are a list of coordinates
    # This does take in 2x3 matrices as a line, but I expect for the line to be on the x-y plane. Z coordinate is always to be 0
    p1, q1 = line1 # p1 and p1 are the 2 points that line 1 passes through
    p2, q2 = line2 # similarly.....

    x1, y1= p1 # x1, y1 ,x1 are the coordinates of one of the points on line1
    x2, y2= p2 # same as above.....

    a1=q1[0]-p1[0] #a1, b1, and c1 are the direction ratios of line1
    b1=q1[1]-p1[1]

    a2=q2[0]-p2[0]
    b2=q2[1]-p2[1]

    a_matrix=[[a1, -a2],[b1, -b2]]
    b_matrix=[[x2-x1], [y2-y1]]
    a_inverse=np.linalg.inv(a_matrix)
    final=np.matmul(a_inverse, b_matrix)
    returnval=np.transpose(final)
    return [returnval[0][0], returnval[0][1], 0]

