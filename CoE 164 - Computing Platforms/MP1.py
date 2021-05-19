def main():
     global alphas
     alphas = alpha(2)
     validM = {'L', 'M', 'Q', 'H'} #turn into 2 dicts (v1, v2) with value = # of codewords
     codewords = [ {'L':7 , 'M':10, 'Q':13, 'H':17} , {'L':10 , 'M':16, 'Q':22, 'H':28}]
     ans = []

     try:
          T = int(input())
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
                    C = codewords[ int(params[0])-1 ] [params[1] ]
                    polynomial = generator( C )
                    message = list( map( int , input().split(" ") ) )
                    remainder = divide (polynomial, message, N, C)
                    ans.append( " ".join(map(str, remainder)) )
     for item in ans:
          print( item )
     '''
     #File output
     import datetime
     now = datetime.datetime.now()
     filename = 'out_' + str(now.strftime("%Y%m%d_%H%M%S")) + '.txt'
     f = open(filename, "w")
     for item in ans:
          f.write(item + '\n')
     f.close()
     '''

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
     '''Makes the the generator polynomial'''
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
          
def divide( g_x , m_x, n, c):
     '''Long division of generator and message polynomials, returns the remainder'''
     m_x += ( [0]*(c) )
     for x in range( n ):
          if (m_x[0] == 0):
               g_prime = g_x.copy()
          else:
               h = alphas.index( m_x[0] ) #takes coefficent of highest term of message and looks for exponent in alpha
               g_prime = list ( map (lambda item: alphas[ ( (item+h) % 255 ) ], g_x) )
          for elem in range( len(m_x) ):
               try:
                    m_x[elem] ^= g_prime[elem]
               except:
                    m_x[elem] ^= 0
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
