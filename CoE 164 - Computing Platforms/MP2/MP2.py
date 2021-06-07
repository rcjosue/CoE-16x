#Author             : Ryan Izach C. Josue
#SN                 : 2018-12231 
#Acknowledged by    : Ivan Gabriel P. Etorma
#SN                 : 2018-10655
#Date               : June 8, 2021

import cmath

def fft (signal):
     '''Recursive function for solving split radix fast fourier transform'''
     #Discrete fourier transform of base cases where signal length is one or two
     if len(signal) == 2:
          x = ( signal[0] )
          y = ( signal[1] )
          return( [ x+y , x-y ] )
     
     if len(signal) == 1:
          return( signal )
     
     #Recursive splitting of arrays
     fft_even = fft(signal[0::2]) #array e
     fft_odd1 = fft(signal[1::4]) #array a
     fft_odd2 = fft(signal[3::4]) #array b

     #Precomputation of Twiddling factors w_{N} with N = signal length and k 
     twiddling_factor = [ cmath.exp((-2j*cmath.pi*k)/ len (signal) ) for k in range( len (signal) ) ]

     #Precomputation of quarters (sum and difference of odd parts of the split) using w_{N}(1, k) * a +- w_{N}(1, 3k) * b
     sum_odd = [(twiddling_factor[i]*fft_odd1[i] + twiddling_factor[i*3]*fft_odd2[i]) for i in range( len(fft_odd1) ) ] #List comprehension for computation of 
     diff_odd = [(twiddling_factor[i]*fft_odd1[i] - twiddling_factor[i*3]*fft_odd2[i]) for i in range( len(fft_odd1) ) ]

     X0,X1,X2,X3 = [],[],[],[]

     for i in range( len(sum_odd) ):
          '''Computation of DFT quarters'''
          X0.append(fft_even[i] + sum_odd[i])
          X1.append(fft_even[i + len(signal)//4] - 1j*diff_odd[i])
          X2.append(fft_even[i] - sum_odd[i])
          X3.append(fft_even[i + len(signal)//4] + 1j*diff_odd[i])          

     return( X0 + X1 + X2 + X3 )

powers_of_two = [1]
x = 1
for num in range (1,15):
     '''Create an array for the powers of 2 from 1 to 14'''
     x *= 2
     powers_of_two.append(x)
   
T = int(input())
print( T )
for t in range(T):
     signal = list(map(int, input().split(" ") ) )
     N = signal.pop(0)
     length = N

     for exp in powers_of_two:
          '''Gets the closest power of 2 that is equal or greater than N'''
          if length <= exp:
               length = exp
               break
          
     for i in range(length-N):
          '''Appends zeroes to resize signal to a length equal to a power of two'''
          signal.append(0)

     transformed = fft(signal) 
     output = ''

     for i in range(length):
          '''Formats output of complex numbers from the list containing the transformed signal'''
          if (transformed[i].real)>=0:
                output +='+'
          output += str(round(transformed[i].real, 6)) 
          if (transformed[i].imag)>=0:
                output +='+'
          output +=str( round(transformed[i].imag, 6)*1j.imag ) + 'j '

     print( str(N) + ' ' + str(length) + ' ' + output )

