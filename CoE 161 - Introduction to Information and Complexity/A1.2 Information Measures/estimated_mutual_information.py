import math

def estimated_mutual_information(xy_samples):
     total = len(xy_samples)

     p_x,p_y={},{} # holds the probability of each value of x and y respectively
     for item in xy_samples: #get the count of each x and y value
          p_x[item[0]] = p_x.get( item[0], 0)  + 1
          p_y[item[1]] = p_y.get( item[1], 0)  + 1
     for key in p_x:
          p_x[key] = p_x[key]/total
     for key in p_y:
          p_y[key] = p_y[key]/total

     y_tot = {} #holds total count of y per set of x values, used to compute the p(x|y)
     xy = {} #hold y keys with lists of total count of corresponding x values
     for key_y in p_y:
          xy[key_y] = []
          for key_x in p_x: #iterate through and count all combinations of x an y t
               temp = xy_samples.count( (key_x,key_y) )  
               xy[key_y].append((key_x,temp)) #stores tuple with (x_value , x_count)
               y_tot[key_y] = y_tot.get( key_y , 0)  + temp 

     p_xy = {}
     for key in xy:
          for pair in xy[key]: 
               p_xy[ (pair[0] , key) ] = p_xy.get( (pair[0] , key), 0 ) + (pair[1] / y_tot[key])*(p_y[key]) #calculate and assign p(x|y)*p(y) to corresponding (x,y) pair
     
     ans = 0
     for key_x in p_x:
          for key_y in p_y:
               temp = p_xy[ (key_x,key_y) ]
               if (temp != 0):
                    ans += temp * math.log2( temp / (p_x[key_x] * p_y[key_y]) )
     return(ans)

print( estimated_mutual_information( [(0,0),(0,1),(1,0),(1,1)] ) )
print( estimated_mutual_information( [(0,0),(0,1),(1,0)] ) )
print( estimated_mutual_information( [(0,0),(1,1)] ) )
