def main():
     alphas = alpha(2)
     print(alphas)
     validM = {'L', 'M', 'Q', 'H'}
     try:
          T = int(input('Input number of messages: '))
     except:
          print("Error: Invalid value")          
     if ( (T > 10) or (T<0) ):
          print("Error: too many messages")
     else:
          for num in range(T):
               params = ( input().split(" ") )
               print(params)
               if ( (( params[0] != '1') and (params[0] != '2')) or (params[1] not in validM) or ( (params[2] > '34') and (params[2] < '1') ) ):
                    print ('Error: invalid parameters')
               else:
                    bytestring = ( input().split(" ") )
                    print(bytestring)

def alpha(a):
     '''Takes an integer 'a' and generates 'a' number of alpha values'''
     alphas = []
     for num in range (8):
          x = pow(a,num)
          alphas.append(x)
     for num in range (8,256):
          x *=a
          if ( x > 255):
               x ^= 285
          alphas.append(x)
     return alphas

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



'''
