# File: Pancake.py

# Description: Homework 10

# Student's Name: Christopher Lee

# Student's UT EID: cl37976

# Course Name: CS 313E 

# Unique Number: 50725

# Date Created: 03/05/19

# Date Last Modified: 03/08/19

#gets index of where pancake was flipped
def flipIndex(stack, maxIndex, iteration, cur):
    if maxIndex == 0:
        flip_Index = iteration
    else:
        flip_Index = len(stack)-maxIndex
    return flip_Index

#sorts pancake
def pancakesort(stack):
    flip_list = []
    cur = len(stack)
    iteration = 1
    new_stack = stack
    while cur > 1:
        #index of maximum number in stack
        maxIndex = stack.index(max(stack[0:cur]))
        if maxIndex != cur-1:
            #if new_stack != stack:
            #flip index
            if cur != len(stack) or (cur == len(stack) and maxIndex != 0):
                flip_list.append(flipIndex(stack,maxIndex,iteration,cur))
            #reverses from 0 to maxIndex
            stack = stack[maxIndex::-1] + stack[maxIndex+1:len(stack)]
            maxIndex = stack.index(max(stack[0:cur-1]))
            #flip index
            if cur != 2:
                flip_list.append(flipIndex(stack,maxIndex,iteration,cur))
            #reverses the whole list
            stack = stack[cur-1::-1] + stack[cur:len(stack)]
        iteration += 1
        cur -= 1
    flip_list.append(0)
    flips =[]
    for i in flip_list:
        if len(flips):
            if flips[-1] != i:
                flips.append(i)
        else: flips.append(i)
    return flips
    
def main():
    
    pancakes = open("pancake.txt","r")
    stacks = pancakes.readlines()
    flips = 0
    for i in range(len(stacks)):
        s = stacks[i].split()
        print(' '.join(s))
        s = [int(j) for j in s]
        flips = pancakesort(s)
        flips = [str(k) for k in flips]
        print(' '.join(flips))
         
main()

