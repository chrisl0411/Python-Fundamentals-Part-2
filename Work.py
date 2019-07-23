#  File: Work.py

#  Description: Homework 9

#  Student Name: Christopher Lee

#  Student UT EID: cl37976

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 03/02/19

#  Date Last Modified: 03/04/19

def calc_n (num_list,k):
    n_list = []

    for i in num_list:
        n = 0
        p = 0
        v = num_list[i]
        if v//(k**p) != 0:
            while v//(k**p) != 0:
                n += v//(k**p)
                p += 1
        else:
            n = 0
        n_list.append(n)
    return n_list

def binary_search(a,n):
    lo = 0
    hi = len(a)-1
    while (lo <= hi):
        mid = (lo+hi)//2
        if (n > a[mid]):
            lo = mid + 1
        elif (n < a[mid]):
            hi = mid - 1
        else:
            return mid
    if lo > hi:
        mid = lo
        return mid

def main():

    work = open("work.txt","r")
    T = work.readline() #number of test cases/first line of txt file
    trial_list = []
    case = work.read(1)

    for i in range(int(T)):
        n = ''
        k = ''
        while case != " ": #read n
            n += case
            case = work.read(1)
        case = work.read(1)
        while case != '\n': #read k
            k += case
            case = work.read(1)
        n = int(n)
        k = int(k)
        #make list of numbers 0 to n
        num_list = list(range(0,n+1))
        #calculate the sum, v based on n for each into new list
        n_list = calc_n(num_list,k)
        #try to find v in the array using binary search
        print(binary_search(n_list,n))

        case = work.read(1)

main()
