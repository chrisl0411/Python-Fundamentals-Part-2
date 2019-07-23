#  File: Intervals.py
#  Description: Homework 2
#  Student Name: Christopher Lee
#  Student UT EID: cl37976
#  Course Name: CS 313E
#  Unique Number: 50725
#  Date Created: 02/01/19
#  Date Last Modified: 02/04/19

#executes sorting intervals, collapsing overlapping intervals and printing non-intersecting intervals 
def main():
    #sort through the [0] index and [1] index 
    intervals = open("intervals.txt","r")
    char = intervals.read(1)
    intervallist = []

    while char != "":
        intervaltuple = ()
        start = ""
        while char != " ":
            start += char
            char = intervals.read(1)
        char = intervals.read(1)
        end = ""
        while char != "\n":
            end += char
            char = intervals.read(1)
        char = intervals.read(1)
        intervaltuple = (int(start),int(end))
        intervallist.append(intervaltuple)
    intervallist.sort()
    
    #initializers
    start = intervallist[0][0]
    end = intervallist[0][1]
    newlist = []

    #constructs non-intersecting interval list with tuples
    for i in range(len(intervallist)):
        if end >= intervallist[i][0]:
            if end >= intervallist[i][1]:
                start = start
                end = end
                if i == len(intervallist)-1:
                    newlist.append((start,end))
            else:
                end = intervallist[i][1]
                if i == len(intervallist)-1:
                    newlist.append((start,end))
        else: #end < intervallist[i][0]
            newlist.append((start,end))
            start = intervallist[i][0]
            end = intervallist[i][1]
    #prints out last interval again and checks if redundant, then removes if it is
    newlist.append((start,end))
    if newlist[-1] == newlist[-2]:
        newlist.remove(newlist[-1])
    
    print("Non-intersecting Intervals:")
    for j in range(len(newlist)):
        print(newlist[j])

    intervals.close()
    
main()
