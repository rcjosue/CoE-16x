def main():
     global alphas
     alphas = alpha(2)
     validM = {'L', 'M', 'Q', 'H'} #turn into 2 dicts (v1, v2) with value = # of codewords
     try:
          T = int(input('Input number of messages: '))
     except:
          print("Error: Invalid value")          
     if ( (T > 10) or (T<0) ):
          print("Error: too many messages")
     else:
          for num in range(T):
               params = ( input().split(" ") )
               #turn error handling of M into dictionary error? thing 
               if ( (( params[0] != '1') and (params[0] != '2')) or (params[1] not in validM) or ( (params[2] > '34') and (params[2] < '1') ) ):
                    print ('Error: invalid parameters')
               else:
                    N = int(params[2]) 
                    polynomial = generator( N )
                    message = ( input().split(" ") )
                    remainder = divide (polynomial, message, N)
                    print( " ".join(map(str, remainder)) )

def alpha(a):
     '''Takes an integer 'a' and generates 'a' number of alpha values'''
     alphas = []
     for num in range (8):
          x = pow(a,num)
          alphas.append(x)
     for num in range (8,256):
          x *= a
          if ( x > 255):
               x ^= 285
          alphas.append(x)
     return alphas

def generator(c):
     '''Make the a polynomial'''
     G = [0]
     for i in range(1 , c):
          G.append(0)
          Gb = [ (x+i) % 255 for x in G]
          for j in range( -1, -len(Gb), -1 ):
               G[j] = alphas.index( alphas[ Gb[j] ] ^ alphas[ G[j-1] ] )
          G[0] = Gb[0]
     G.append(0)
     G.reverse()
     return G
          
def divide( g_x , m_x, n):
     m_x += ( [0]*n )
     for x in range(n+1):
          h = alphas.index( m_x[0] ) #takes coefficent of highest term of message and looks for exponent in alpha
          g_prime = list( map (lambda item: alphas[ item + h ], g_x) )
          for elem in range( len(g_prime) ):
               m_x[elem] ^= g_prime[elem]
          del (m_x[0])
     return (m_x)
     

if __name__ == "__main__":
     main()


'''
Short Journal Draft

The program was written in Python 3.9.
If else statements were used to handle errors in value and the try except was used to handle type errors

Alpha computation
for loop from 0 to 7 then 8 onwards as the pattern changes from taking alpha raised to a number into the previous alpha times alpha
if the current value if higher than 255 it takes the value of itself XOR 285. This calculates all the values of alpha and stores
into an array returned to the main function
pow was shown to be faster than **

Generation


'''
