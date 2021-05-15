T = int(input('Input number of messages: '))
if ( (T > 10) or (T<0) )(:
     print("Error: too many messages")
else:
     for num in range(T):
          params = ( input().split(" ") )
          if ( (params[0] != '1') or (params[0] != '2') or (params[1] != 'L') or (params[1] != 'M') or (params[1] != 'Q') or (params[1] != 'H') or (params[2] > '34') or (params[2] < '1'):
               print ('Error: invalid parameters')
          else:
               bytestring = ( input().split(" ") )
               print(params)
               print(bytestring)
