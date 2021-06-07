import cmath

two_pow = [1]
x = 1

for num in range (1,15):
     x *= 2
     two_pow.append(x)
print (two_pow)
#T = int(input())

signal = input().split(" ")
N = int(signal.pop(0))
length = N

for exp in two_pow:
     if length <= exp:
          length = exp
          break
     
for i in range(exp-N):
     signal.append(0)

print (length)

def rec_split (signal):
     if len(signal) == 2:
          print(signal)
          x = int( signal[0] )
          y  = int( signal[1] )
          #return( x+y + x-y )
          return( [x,y] )
     
     if len(signal) == 1:
          print(signal)
          return( [ int( signal[0] ) ] )
     
     even = rec_split(signal[::2])
     odd_1 = rec_split(signal[1::4])
     odd_2 = rec_split(signal[3::4])
     return( [even , odd_1 , odd_2 ] )

def rec_split_solve (signal):
     if len(signal) == 2:
          x = int( signal[0] )
          y  = int( signal[1] )
          return( [x+y, x-y] )
     if len(signal) == 1:
          print(signal)

     even = rec_split(signal[::2])
     odd_1 = rec_split(signal[1::4])
     odd_2 = rec_split(signal[3::4])

     
     
     return( [  even + w_n * odd_1  + w_n * odd_2 ] )
     
print( rec_split(signal) )

