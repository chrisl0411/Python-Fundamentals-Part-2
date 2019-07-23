#  File: Spiral.py
#  Description: Homework 1
#  Student Name: Christopher Lee
#  Student UT EID: cl37976
#  Course Name: CS 313E
#  Unique Number: 50725
#  Date Created: 01/28/19
#  Date Last Modified:02/01/19

#bordersum function takes in "number" as input and calculates the sum of bordering numbers in the spiral array.
def bordersum(dim,number,spiral):
    for rows in range(dim):
        for columns in range(dim):
            if number == spiral[rows][columns]:
                r = rows
                c = columns

    if r == 0 or r == dim-1 or c == 0 or c == dim-1: #numbers on the side or corners
        if r == 0 and c == 0: #top left corner
            n1 = spiral[r][c+1]
            n2 = spiral[r+1][c]
            n3 = spiral[r+1][c+1]
            sum = n1 + n2 + n3
        elif r == 0 and c == dim-1: #top right corner
            n1 = spiral[r][c-1]
            n2 = spiral[r+1][c]
            n3 = spiral[r+1][c-1]
            sum = n1 + n2 + n3
        elif r == dim-1 and c == 0: #bottom left corner
            n1 = spiral[r-1][c]
            n2 = spiral[r][c+1]
            n3 = spiral[r-1][c+1]
            sum = n1 + n2 + n3
        elif r == dim-1 and c == dim-1: #bottom right corner
            n1 = spiral[r-1][c]
            n2 = spiral[r][c-1]
            n3 = spiral[r-1][c-1]
            sum = n1 + n2 + n3
        elif r == 0 and (c != 0 or c != dim-1): #top bordering numbers
            n1 = spiral[r][c-1]
            n2 = spiral[r+1][c-1]
            n3 = spiral[r+1][c]
            n4 = spiral[r+1][c+1]
            n5 = spiral[r][c+1]
            sum = n1 + n2 + n3 + n4 + n5
        elif r == dim-1 and (c !=0 or c != dim-1): #bottom bordering numbers
            n1 = spiral[r][c-1]
            n2 = spiral[r-1][c-1]
            n3 = spiral[r-1][c]
            n4 = spiral[r-1][c+1]
            n5 = spiral[r][c+1]
            sum = n1 + n2 + n3 + n4 + n5
        elif (r != 0 or r != dim-1) and c == 0: #left bordering numbers
            n1 = spiral[r-1][c]
            n2 = spiral[r-1][c+1]
            n3 = spiral[r][c+1]
            n4 = spiral[r+1][c+1]
            n5 = spiral[r+1][c]
            sum = n1 + n2 + n3 + n4 + n5
        elif (r != 0 or r != dim-1) and c == dim-1: #right bordering numbers
            n1 = spiral[r-1][c]
            n2 = spiral[r-1][c-1]
            n3 = spiral[r][c-1]
            n4 = spiral[r+1][c-1]
            n5 = spiral[r+1][c]
            sum = n1 + n2 + n3 + n4 + n5
    else: #numbers inside the borders
        n1 = spiral[r-1][c-1]
        n2 = spiral[r-1][c]
        n3 = spiral[r-1][c+1]
        n4 = spiral[r][c+1]
        n5 = spiral[r+1][c+1]
        n6 = spiral[r+1][c]
        n7 = spiral[r+1][c-1]
        n8 = spiral[r][c-1]
        sum = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    return sum

#initializes and executes spiral creation, calculates and prints sum of bordering numbers        
def main():
    #imports data from text file and assigns variables
    spiral = open("spiral.txt", "r")
    dim = int(spiral.readline())
    num1 = int(spiral.readline())
    num2 = int(spiral.readline())
    num3 = int(spiral.readline())
    num4 = int(spiral.readline())

    #initial 2D list creation and sets center square to 1
    spiral = [[0]*dim for i in range(dim)]
    row = dim//2
    col = dim//2
    spiral[row][col] = 1

    #counters
    numcount = dim**2
    n = 1
    num = 2 

    #places num into spiral 2D list. Algorithm uses 
    while num <= numcount: #spiral values
        if n%2 != 0: #odd
            for j in range(n): #right
                if num <= numcount:
                    col += 1
                    spiral[row][col] = num
                    num += 1
            for k in range(n): #down
                if num <= numcount:
                    row += 1
                    spiral[row][col] = num
                    num += 1
            n += 1
        else: #even
            for l in range(n): #left
                if num <= numcount:
                    col -= 1
                    spiral[row][col] = num
                    num += 1
            for m in range(n): #up
                if num <= numcount:
                    row -= 1
                    spiral[row][col] = num
                    num += 1
            n += 1
    #print(spiral)
    print(bordersum(dim,num1,spiral))
    print(bordersum(dim,num2,spiral))
    print(bordersum(dim,num3,spiral))
    print(bordersum(dim,num4,spiral))
    
main()
