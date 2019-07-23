#  File: Palindrome.py

#  Description: Homework 7

#  Student Name: Christopher Lee

#  Student UT EID: cl37976

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 02/19/19

#  Date Last Modified: 02/22/19

#checks if current_string is a palindrome
def is_Palindrome(current_string):
    return list(current_string) == list(reversed(current_string))

#makes shortest palindrome possible by adding letters to the beginning of the string
def make_palindrome(string):
    add_list = []
    new_string = string
    for i in range(len(string)-1,-1,-1):
        add_list.append(string[i])
        new_string = add_list + list(string)
        if is_Palindrome(new_string):
            break

    return ''.join(new_string)


#opens palindrome.txt file and reads in words
#iterates through each word and determines if palindrome, if not, makes palindrome
def main():

    palindrome = open('palindrome.txt','r')
    line = palindrome.readline()
    string_list = []
    while line != "":
        line.split()
        string_list.append(line)
        line = palindrome.readline()
    string_list = [i.split('\n', 1)[0] for i in string_list]

    #checks if string is palindrome, if not, 
    for s in range(len(string_list)):
        current_string = string_list[s]
        if is_Palindrome(current_string):
            print(current_string)
        else:
            print(make_palindrome(current_string))

    palindrome.close()
            
main()
