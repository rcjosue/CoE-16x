#Me                         : Ivan Gabriel P. Etorma
#Student Number             : 2018-10655
#Acknowledged by            : Ryan Izach C. Josue
#Student Number             : 2018-12231 
#Date                       : June 8, 2021
#------------------------------------------------------------------------

import math
import cmath

TwiddleFactorsList = []

#Gets the twiddle factor w_k(1, N)
def getTwiddleFactor(k,N):
    return cmath.exp(-2j * math.pi * (k/N))

#Initialzies the list of Twiddle Factors before using to avoid re computing
def initTwiddle(N):
    temp = {}
    level = int(math.log(N, 2)) + 1
    while level:
        level -= 1
        temp[2**level] = []
        for k in range(0, 2**level):
            temp[2**level].append(getTwiddleFactor(k, 2**level))
        

    #print (temp)
    return temp        

#This is the last part of the IFFT where you divide the whole formula with the number of data points
def outIFFT(lis, K, N):
    temp = [N]

    for i in range(0, N):
        temp.append(round(lis[i].real/K))
        
    return temp

def IFFT(points):
    
#These are the base cases, when the data length is only 1 or 2
    if len(points) == 2:
        return [points[0]+points[1] , points[0]-points[1]]
    
    elif len(points) == 1:
        return points
    
    else:
        e = []
        a = []
        b = []

#This part splits the data points int an even part and 2 odd parts (three parts in total)
#Recrusion occurs until the recursion tree reaches the base cases
        E = IFFT(points[0::2])
        A = IFFT(points[1::4]) 
        B = IFFT(points[3::4]) 

#Gets the twiddle factors, based on the number of the current data points       
        N = len(points)

        twiddleFactors = TwiddleFactorsList[N]

#Precompute variables before merging
        sumOdd = [(twiddleFactors[i]*A[i] + twiddleFactors[3*i] * B[i]) for i in range(0,len(A))]
        diffOdd = [(twiddleFactors[i]*A[i] - twiddleFactors[3*i] * B[i]) for i in range(0,len(A))]
        
        X0, X1, X2, X3 = [], [], [], []


#Computing each quarter
        for i in range((len(sumOdd))):
            X0.append(E[i]                  + sumOdd[i])
            X1.append(E[i + len(points)//4] - 1j * diffOdd[i])
            X2.append(E[i]                  - sumOdd[i])
            X3.append(E[i + len(points)//4] + 1j * diffOdd[i])


#Merge all quarters
        return X0 + X1 + X2 + X3

#This function converts a string of complex number into a list of complex numbers
def compProcess(inps, K):
    ret = []
    for inp in inps:
        processing = True
        pointer = 0
        currNum = ''
        sign = inp[0]
        
        coeff = []
        for char in inp:
            
            if (char.isdigit() or char == '.'):
                currNum += char
            else:
                if currNum != '':
                    coeff.append(sign + currNum)
                    currNum = ''
                    
                if (char == '+'):
                    sign = '+'
                elif (char == '-'):
                    sign = '-'
                    
                currNum = ''
        ret.append(complex((float)(coeff[0]), (float)(coeff[1])))

    return ret


repeat = int(input())
r = repeat
answers = []

while r:
    r -= 1

#Gets N, K, and the data points (in string)
    inp = input().split()
    N = int(inp[0])
    K = int(inp[1])
    compString = inp[2:]

#Converts string of input into list of complex numbers
    compNum = compProcess(compString, K)
    
#Initiating all Twiddle Factors before using
    TwiddleFactorsList = initTwiddle(K)

#Basically everything is the same as the FFT, except in IFFT, the data points in the frequency domain are conjugated before the transform
    for i in range(len(compNum)):
        compNum[i] = complex(compNum[i].real, -compNum[i].imag)

    answers.append(outIFFT(IFFT(compNum), K, N))

#Output Formatting
print (repeat)
for answer in answers:
    for i in range(len(answer)):
        if i != len(answer) - 1:
            print (answer[i], end = ' ')
        else :
            print (answer[i], end = '')

    print ()



