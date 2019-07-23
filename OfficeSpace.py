#  File: OfficeSpace.py

#  Description: Homework 5

#  Student Name: Christopher Lee

#  Student UT EID: cl37976

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 02/13/19

#  Date Last Modified: 02/15/19

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

class Rectangle (object):
    # constructor
    def __init__ (self, ll_x = 0, ll_y = 0, ur_x = 1, ur_y = 1):
        if ((int(ll_x) < int(ur_x)) and (int(ll_y) < int(ur_y))):
            self.ll = Point (ll_x, ll_y)
            self.ur = Point (ur_x, ur_y)
        else:
            self.ll = Point (0, 0)
            self.ur = Point (1, 1)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length (self):
        self.len = int(self.ur.x) - int(self.ll.x)
        return self.len

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width (self):
        self.wid = int(self.ur.y) - int(self.ll.y)
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
        return (float(self.ll.x) <= float(p.x) <= float(self.ur.x)) and (float(self.ur.y) >= float(p.y) >= float(self.ll.y))
        
    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside (self, r):
        #if self.ur == r.ur and self.ll == r.ll: #if the same rectangle
            #return True
        #else:
        return (self.inside_rect(r.ur) and self.inside_rect(r.ll)) or (r.inside_rect(self.ur) and r.inside_rect(self.ll))
        
    def rectangle_outside (self, r):
        return (float(r.ll.x) > float(self.ur.x)) or (float(r.ur.x) < float(self.ll.x)) or (float(r.ll.y) > float(self.ur.y)) or (float(r.ur.y) < float(self.ll.y))
    
    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap (self, r):
        return self.rectangle_inside(r) == False and self.rectangle_outside(r) == False

    # determine contested area of overlapping rectangles
    # takes a rectangle object r as an argument returns a value
    def corneroverlap_area (self, r):
        x = self.ur.x-r.ll.x
        y = r.ur.y-self.ll.y
        return x * y

    def contested_area (self, r, a = 0):
        if (self.ur.x < r.ur.x): #ur self is left of ur r
            if (self.ll.x < r.ll.x): #ll self is left of ll r
                if (self.ur.y > r.ur.y): #ur self is above ur r
                    if (self.ll.y > r.ll.y): #self's bottom right and r's top left corner contested
                        a = (self.ur.x - r.ll.x) * (r.ur.y-self.ll.y)
                    else: #self's ll.y is equal to or is lower than r's ll.y
                        a = (self.ur.x - r.ll.x) * (r.ur.y - r.ll.y)
                elif (self.ur.y < r.ur.y): #ur self is below ur r
                    if (self.ll.y > r.ll.y): #self's right and r's left contested
                        a = (self.ur.x - r.ll.x) * (self.ur.y-self.ll.y)
                    else: #self's ll.y is equal to or is lower than r's ll.y
                        a = (self.ur.x - r.ll.x) * (self.ur.y - r.ll.y)
            else: #ll self is either equal to or more to the right than r
                if (self.ur.y > r.ur.y): #ur self is above ur r
                    if (self.ll.y > r.ll.y): # ll self is above ll r
                        a = (self.ur.x-self.ll.x) * (r.ur.y-self.ll.y)
                    else: #self's ll.y is equal to or lower than r's ll.y
                        a = (self.ur.x-self.ll.x) * (r.ur.y-r.ll.y)

        elif (self.ur.x == r.ur.x and self.ll.x == r.ll.x):
            if (self.ur.y > r.ur.y):
                a = (self.ur.x-self.ll.x) * (r.ur.y-self.ll.y)
            else:
                a = (self.ur.x-r.ll.x) * (self.ur.y-r.ll.y)
        
        elif (self.ur.y == r.ur.y and self.ll.y == r.ll.y):
            if (self.ur.x > r.ur.x):
                a = (self.ur.x-r.ll.x) * (self.ur.y-self.ll.y)
            else:
                a = (r.ur.x-self.ll.x) * (r.ur.y-r.ll.y)

        return a

    def area_left (self, r, contestarea):
        self.newarea = self.area() - contestarea
        r.newarea = r.area() - contestarea
        return self.newarea, r.newarea

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__ (self):
        return "LL: " + str(self.ll) + ", UR: " + str(self.ur)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__ (self, other):
        tol = 1.0e-16
        return (abs(self.length() - other.length()) < tol) and (abs(self.width() - other.width()) < tol)


def main():
    #open office.txt file to read
    office = open("office.txt", "r")

    #reads file and extracts information
    char = office.read(1)
    while char != "":
        #assigns length and width
        l = ""
        w = ""
        while char != " ":
            l += char
            char = office.read(1)
        char = office.read(1)
        while char != "\n":
            w += char
            char = office.read(1)

        #assigns number of employees
        n = ""
        char = office.read(1)
        while char != "\n":
            n += char
            char = office.read(1)
        char = office.read(1)

        #reads in employees names and requested office coordinates (x1,x2,y1,y2) 
        namelist = []
        employeecoord = []

        #organizes names and coordinates into list
        for i in range(int(n)):
            coordlist = []
            name = ""
            while char != " ":
                name += char
                char = office.read(1)
            namelist.append(name)
            char = office.read(1)
            for j in range(3):
                point = ""
                while char != " ":
                    point += char
                    char = office.read(1)
                char = office.read(1)
                coordlist.append(int(point))
                
            point = ""
            while char != "\n":
                point += char
                char = office.read(1)
            char = office.read(1)
            coordlist.append(int(point))
            employeecoord.append(coordlist)

        #find contested space
        rectangles = []
        rectarea = []
        contestarea = 0
        contestlist = []
        #all rectangles in "rectangles" list
        for e in range(len(namelist)):
            rect = Rectangle(employeecoord[e][0],employeecoord[e][1],employeecoord[e][2],employeecoord[e][3])
            rectarea.append(rect.area())
            rectangles.append(rect)

        for g in range(len(rectangles)-1):
            for h in range(g+1, len(rectangles)):
                #if rectangles overlap (includes sharing border)
                if rectangles[g].rectangle_overlap(rectangles[h]) or rectangles[h].rectangle_overlap(rectangles[g]):
                    if rectangles[g].contested_area(rectangles[h]):
                        contestarea = rectangles[g].contested_area(rectangles[h])
                        rectg_area, recth_area = rectangles[g].area_left(rectangles[h],contestarea)
                    elif rectangles[h].contested_area(rectangles[g]):
                        contestarea = rectangles[h].contested_area(rectangles[g])
                        recth_area, rectg_area = rectangles[h].area_left(rectangles[g],contestarea)
                    rectarea[g] = rectg_area
                    rectarea[h] = recth_area
                    contestlist.append(contestarea)
                    
                #if one rectangle inside the other
                elif rectangles[g].rectangle_inside(rectangles[h]) or rectangles[h].rectangle_inside(rectangles[g]):
                    if rectangles[g].area() <= rectangles[h].area():
                        contestarea = rectangles[g].area()
                        rectg_area, recth_area = rectangles[g].area_left(rectangles[h],contestarea)
                    else:
                        contestarea = rectangles[h].area()
                        rectg_area, recth_area = rectangles[g].area_left(rectangles[h],contestarea)
                    rectarea[g] = rectg_area
                    rectarea[h] = recth_area
                    contestlist.append(contestarea)
                else:
                    contestlist.append(0)  

        #calculate area of office space
        area = int(l) * int(w)
        contestarea = sum(contestlist)
        unallocated = area - contestarea

        for r in range(len(rectarea)):
            unallocated -= rectarea[r]
        
        #print statements
        print("Total", area)
        print("Unallocated", unallocated)
        print("Contested", contestarea)
        for k in range(len(namelist)):
            print(namelist[k], rectarea[k])
        print('')

        if char == "\n":
            break
    
    office.close()    

main()
