#  File: Cipher.py
#  Description: Homework 3
#  Student Name: Christopher Lee
#  Student UT EID: cl37976
#  Course Name: CS 313E
#  Unique Number: 57250
#  Date Created: 02/07/19
#  Date Last Modified: 02/08/19

import math

#takes a string and returns the encrypted string
def encrypt(string):
    N = string.readline() #N is the number of strings that need to be encrypted
    encrypted = []
    for i in range(int(N)):
        message = string.readline()
        messagelist = list(message)
        if '\n' in messagelist:
            messagelist.remove('\n')
        L = len(message)-1
        if math.sqrt(L)/int(math.sqrt(L)) == 1:
            K = int(math.sqrt(L)) #K is one dimension of the square 2D list
            M = K**2 #M is the smallest square number greater than or equal to L
        else:
            K = int(math.sqrt(L))+1
            M = K**2
        A = M-L #number of asteriks needed to fill K by K 2D list

        #adds asteriks to end of string list
        for asteriks in range(A):
            messagelist.append('*')
        squarelist = [[0]*K for j in range(K)] #K by K 2D list filled with zeros

        #fills in string list from top right to bottom left of list
        lettercount = 0
        for col in reversed(range(K)):
            for row in range(K):
                squarelist[row][col] = messagelist[lettercount]
                lettercount += 1

        #extract letters reading left to right, top to bottom and joins all strings into new list
        encryptlist = []
        encryptstr = ''
        for r in range(K):
            for c in range(K):
                if squarelist[r][c] != '*':
                    encryptlist.append(squarelist[r][c])
                else:
                    continue
        encryptstr = ''.join(encryptlist)
        encrypted.append(encryptstr)
    return encrypted
        

#takes an encrypted string and returns the plain text version
def decrypt(string):
    N = string.readline()
    decrypted = []
    for i in range(int(N)):
        message = string.readline()
        messagelist = list(message)
        if '\n' in messagelist:
            messagelist.remove('\n')
        L = len(messagelist)

        if math.sqrt(L)/int(math.sqrt(L)) == 1:
            K = int(math.sqrt(L))
            M = K**2
        else:
            K = int(math.sqrt(L))+1 #M is the smallest square number greater than or equal to L
            M = K**2
            
        A = M-L #number of asteriks needed to fill K by K 2D list
        #adds asteriks to end of string list
        squarelist = [[0]*K for j in range(K)]
        for asteriks in range(A):
            messagelist.append('*')
            
        #places asteriks in squarelist first    
        asterikscount = 1
        if asterikscount <= A:
            for cl in range(K):
                if asterikscount <= A:
                    for rw in reversed(range(K)):
                        if asterikscount <= A:
                            squarelist[rw][cl] = '*'
                            asterikscount += 1
                        else:
                            break
        
        #fills in the rest of the spaces in list with letters
        lettercount = 0
        for row in range(K):
            for col in range(K):
                if squarelist[row][col] != '*':
                    squarelist[row][col] = messagelist[lettercount]
                    lettercount += 1
                else:
                    continue
        
        #extract letters reading top to bottom, right to left
        decryptlist = []
        decryptstr = ''
        for c in reversed(range(K)):
            for r in range(K):
                if squarelist[r][c] != '*':
                    decryptlist.append(squarelist[r][c])
                else:
                    continue
        decryptstr = ''.join(decryptlist)
        decrypted.append(decryptstr)
    return decrypted

def main():
    # open file encrypt.txt
    encrypttext = open('encrypt.txt','r')

    # encrypt and output all lines in file encrypt.txt
    encrypted = encrypt(encrypttext)
    print("Encryption:")
    for e in range(len(encrypted)):
        print(encrypted[e])
        
    #space between encrypted and decrypted
    print('')
    
    # open file decrypt.txt
    decrypttext = open('decrypt.txt','r')
    
    # decrypt and output all lines in file decrypt.txt
    decrypted = decrypt(decrypttext)
    print("Decryption:")
    for d in range(len(decrypted)):
        print(decrypted[d])

    encrypttext.close()
    decrypttext.close()

main()
