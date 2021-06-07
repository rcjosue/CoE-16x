import cmath

powers_of_two = [1]
x = 1
for num in range (1,15):
     x *= 2
     powers_of_two.append(x)
   
def fft (signal):
     if len(signal) == 2:
          x = ( signal[0] )
          y = ( signal[1] )
          return( [ x+y , x-y ] )
     
     if len(signal) == 1:
          return( signal )
     
     fft_even = fft(signal[0::2])
     fft_odd1 = fft(signal[1::4])
     fft_odd2 = fft(signal[3::4])

     twiddling_factor = [ cmath.exp((-2j*cmath.pi*i)/ len (signal) ) for i in range( len (signal) ) ]

     sum_odd = [(twiddling_factor[i]*fft_odd1[i] + twiddling_factor[i*3]*fft_odd2[i]) for i in range( len(fft_odd1) ) ]
     diff_odd = [(twiddling_factor[i]*fft_odd1[i] - twiddling_factor[i*3]*fft_odd2[i]) for i in range( len(fft_odd1) ) ]

     X0 = []
     X1 = []
     X2 = []
     X3 = []

     for i in range( len(sum_odd) ):
          X0.append(fft_even[i] + sum_odd[i])
          X1.append(fft_even[i + len(signal)//4] - 1j*diff_odd[i])
          X2.append(fft_even[i] - sum_odd[i])
          X3.append(fft_even[i + len(signal)//4] + 1j*diff_odd[i])          

     return( X0 + X1 + X2 + X3 )

T = int(input())
print( T )
for t in range(T):
     signal = list(map(int, input().split(" ") ) )
     N = signal.pop(0)
     length = N

     for exp in powers_of_two:
          if length <= exp:
               length = exp
               break
          
     for i in range(exp-N):
          signal.append(0)

     transformed = fft(signal)
     output = ''
     for i in range(length):
          if (transformed[i].real)>=0:
                output +='+'
          output += str(round(transformed[i].real, 6)) 
          if (transformed[i].imag)>=0:
                output +='+'
          output +=str( round(transformed[i].imag, 6)*1j.imag ) + 'j '

     print( str(N) + ' ' + str(length) + ' ' + output )

