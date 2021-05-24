#Ryan Izach Josue, 2018-12231
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

def alpha(a):
     '''Takes an integer a or alpha and generates 255 alpha values'''
     x = 1
     alphas = [1]
     for num in range (1,256):
          x *= a
          if ( x > 255):
               x ^= 285
          alphas.append(x)
     return alphas


def generator(c):
     '''Makes a generator polynomial as a list of coefficient with c+1 elements and x^c to be the highest order'''
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
     '''Long division of generator and message polynomials, returns the remainder as a list of coefficients'''
     m_x += ( [0]*(c) )
     for x in range( n ):
          if (m_x[0] == 0):
               del (m_x[0])
               continue
               #g_prime = g_x.copy()
          else:
               h = alphas.index( m_x[0] ) #takes coefficent of highest term of message and looks for exponent in alpha
               g_prime = list ( map (lambda item: alphas[ ( (item+h) % 255 ) ], g_x) )
          for elem in range( c+1 ):
               m_x[elem] ^= g_prime[elem]
          del (m_x[0])
     return (m_x)
     
if __name__ == "__main__":
     main()
