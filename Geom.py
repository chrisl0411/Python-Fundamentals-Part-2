#  File: Geom.py

#  Description: Homework 4

#  Student Name: Christopher Lee

#  Student UT EID: cl37976

#  Course Name: CS 313E

#  Unique Number: 57250

#  Date Created: 02/10/19

#  Date Last Modified: 02/11/19

import math

class Point (object):
    # constructor 
    # x and y are floats
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__ (self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-16
        return ((abs(float(self.x) - float(other.x)) < tol) and (abs(float(self.y) - float(other.y)) < tol))

class Circle (object):
    # constructor
    # x, y, and radius are floats
    def __init__ (self, radius = 1, x = 0, y = 0):
        self.radius = radius
        self.center = Point (x, y)

    # compute cirumference
    def circumference (self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area (self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside (self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside (self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    def circle_outside (self,c):
        distance = self.center.dist(c.center)
        return (self.radius + c.radius) < distance

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap (self, c):
        return self.circle_inside(c) == False and self.circle_outside(c) == False
              
    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe (self, r):
        center_x = (float(r.ul.x) + float(r.lr.x)) / 2
        center_y = (float(r.ul.y) + float(r.lr.y)) / 2
        radius_r = math.hypot(center_x-float(r.ul.x),center_y-float(r.ul.y))
        return Circle(format(radius_r,".2f"), center_x, center_y)
    
    # string representation of a circle
    # takes no arguments and returns a string
    def __str__ (self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)
    
    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__ (self, other):
        tol = 1.0e-16
        return (abs(self.radius - other.radius) < tol)

class Rectangle (object):
    # constructor
    def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
        if ((float(ul_x) < float(lr_x)) and (float(ul_y) > float(lr_y))):
            self.ul = Point (ul_x, ul_y)
            self.lr = Point (lr_x, lr_y)
        else:
            self.ul = Point (0, 1)
            self.lr = Point (1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length (self):
        self.len = float(self.lr.x) - float(self.ul.x)
        return self.len

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width (self):
        self.wid = float(self.ul.y) - float(self.lr.y)
        return self.wid

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter (self):
        self.perim = self.length()*2 + self.width()*2
        return self.perim
    
    # determine the area
    # takes no arguments, returns a float
    def area (self):
        self.a = (self.length() * self.width())
        return self.a

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def inside_rect (self, p):
        return (float(self.ul.x) < float(p.x) < float(self.lr.x)) and (float(self.ul.y) > float(p.y) > float(self.lr.y))
        
    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside (self, r):
        upperleft = r.ul
        lowerright = r.lr
        if self.ul == r.ul and self.lr == r.lr:
            return False
        else:
            return self.inside_rect(upperleft) and self.inside_rect(lowerright)
        
    def rectangle_outside (self, r):
        return (float(r.ul.x) > float(self.lr.x)) or (float(r.lr.x) < float(self.ul.x)) or (float(r.lr.y) > float(self.ul.y)) or (float(r.ul.y) < float(self.lr.y))
    
    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap (self, r):
        return self.rectangle_inside(r) == False and self.rectangle_outside(r) == False

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe (self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x,ul_y,lr_x,lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__ (self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__ (self, other):
        tol = 1.0e-16
        return (abs(self.length() - other.length()) < tol) and (abs(self.width() - other.width()) < tol)

def main():
    # open the file geom.txt
    shapes = open('geom-1.txt' , 'r')

    # create Point objects P and Q
    P_x = ""
    P_y = ""
    num = shapes.read(1)
    while num != " ":
        P_x += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != "\n":
        P_y += num
        num = shapes.read(1)

    Q_x = ""
    Q_y = ""
    num = shapes.read(1)
    while num != " ":
        Q_x += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != "\n":
        Q_y += num
        num = shapes.read(1)

    pointP = Point(float(P_x),float(P_y))
    pointQ = Point(float(Q_x),float(Q_y))

    # print the coordinates of the points P and Q
    print("Coordinates of P:", pointP.__str__())
    print("Coordinates of Q:", pointQ.__str__())

    # find the distance between the points P and Q
    print("Distance between P and Q:", Point.dist(pointP,pointQ))

    # create two Circle objects C and D
    C_r = ""
    C_x = ""
    C_y = ""
    num = shapes.read(1)
    while num != " ":
        C_r += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != " ":
        C_x += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != "\n":
        C_y += num
        num = shapes.read(1)

    D_r = ""
    D_x = ""
    D_y = ""
    num = shapes.read(1)
    while num != " ":
        D_r += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != " ":
        D_x += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != "\n":
        D_y += num
        num = shapes.read(1)

    circleC = Circle(float(C_r),float(C_x),float(C_y))
    circleD = Circle(float(D_r),float(D_x),float(D_y))

    # print C and D
    print("Circle C:",circleC)
    print("Circle D:",circleD)

    # compute the circumference of C
    print("Circumference of C:",format(circleC.circumference(),".2f"))

    # compute the area of D
    print("Area of D:",format(circleD.area(),".2f"))

    # determine if P is strictly inside C
    if circleC.point_inside(pointP):
        result = "is"
    else:
        result = "is not"
    print("P",result,"inside C")
    
    # determine if C is strictly inside D
    if circleD.circle_inside(circleC):
        result = "is"
    else:
        result = "is not"
    print("C",result,"inside D")

    # determine if C and D intersect (non zero area of intersection)
    if circleD.circle_overlap(circleC):
        result = "does"
    else:
        result = "does not"
    print("C",result,"intersect D") 

    # determine if C and D are equal (have the same radius)
    if circleC.__eq__(circleD):
        result = "is"
    else:
        result = "is not"
    print("C",result,"equal to D")

    # create two rectangle objects G and H
    G_ulx = ""
    G_uly = ""
    G_lrx = ""
    G_lry = ""
    num = shapes.read(1)
    while num != " ":
        G_ulx += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != " ":
        G_uly += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != " ":
        G_lrx += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != "\n":
        G_lry += num
        num = shapes.read(1)

    H_ulx = ""
    H_uly = ""
    H_lrx = ""
    H_lry = ""
    num = shapes.read(1)
    while num != " ":
        H_ulx += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != " ":
        H_uly += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != " ":
        H_lrx += num
        num = shapes.read(1)
    num = shapes.read(1)
    while num != "\n":
        H_lry += num
        num = shapes.read(1)

    rectangleG = Rectangle(G_ulx,G_uly,G_lrx,G_lry)
    rectangleH = Rectangle(H_ulx,H_uly,H_lrx,H_lry)

    # print the two rectangles G and H
    print("Rectangle G:", rectangleG)
    print("Rectangle H:", rectangleH)

    # determine the length of G (distance along x axis)
    print("Length of G:", rectangleG.length())

    # determine the width of H (distance along y axis)
    print("Width of H:", rectangleH.width())

    # determine the perimeter of G
    print("Perimeter of G:", rectangleG.perimeter())

    # determine the area of H
    print("Area of H:", rectangleH.area())

    # determine if point P is strictly inside rectangle G
    if rectangleG.inside_rect(pointP):
        result = "is"
    else:
        result = "is not"
    print("P",result,"inside G")

    # determine if rectangle G is strictly inside rectangle H
    
    if rectangleH.rectangle_inside(rectangleG):
        result = "is"
    else:
        result = "is not"
    print("G",result,"inside H")

    # determine if rectangles G and H overlap (non-zero area of overlap)
    if rectangleH.rectangle_overlap(rectangleG):
        result = "does"
    else:
        result = "does not"
    print("G",result,"overlap H")

    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle
    circumcircle = Circle.circle_circumscribe(Circle(),rectangleG)
    print("Circle that circumscribes G:",circumcircle)

    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle
    circumrectangle = Rectangle.rectangle_circumscribe(Rectangle(),circleD)
    print("Rectangle that circumscribes D:",circumrectangle)

    # determine if the two rectangles have the same length and width
    if rectangleG.__eq__(rectangleH):
        result = "is"
    else:
        result = "is not"
    print("Rectangle G",result,"equal to H")

    # close the file geom.txt
    shapes.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
