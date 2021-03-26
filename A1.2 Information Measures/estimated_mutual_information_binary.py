import math
def estimated_mutual_information(xy_samples):
     total = len(xy_samples)
     p_y, p_x, p_xy, xy = [],[],[],[]
     for y in range(2):
          for x in range(2):
               xy.append(xy_samples.count( (x,y) ))
          p_y.append( ( xy[ 2*y ] + xy[ 2*y+1 ] ) / total )
     for a in range(2):
          p_x.append( ( xy[ a ] + xy[ a+2 ] ) / total )
          p_xy.append( ( xy[2*a] / ( xy[2*a] + xy[2*a+1] ) ) * p_y[a] )
          p_xy.append( ( xy[2*a+1] / ( xy[2*a] + xy[2*a+1] ) ) * p_y[a] ) 
     #xy and p_xy= [ xy(0,0) , xy(1,0) , xy(0,1), xy(1,1) ]
     ans = 0
     for a in range(2):
          if ( p_xy[a] != 0 ):
               ans += p_xy[ a ] * math.log2( p_xy[ a ] / ( p_x[a] * p_y[0] )  )
          if ( p_xy[a+2] != 0 ):
               ans += p_xy[ a+2 ] * math.log2( p_xy[ a+2 ] / ( p_x[a] * p_y[1] )  )
     return ( ans )

'''
def estimated_mutual_information(xy_samples):
     total = len(xy_samples)
     p_y, p_x, p_xy, xy = [],[],[],[]
     for y in range(2):
          for x in range(2):
               xy.append(xy_samples.count( (x,y) ))
          p_y.append( ( xy[ 2*y ] + xy[ 2*y+1 ] ) / total )

     for a in range(2):
          p_x.append( ( xy[ a ] + xy[ a+2 ] ) / total )
          p_xy.append( ( xy[2*a] / ( xy[2*a] + xy[2*a+1] ) ) * p_y[a] )
          p_xy.append( ( xy[2*a+1] / ( xy[2*a] + xy[2*a+1] ) ) * p_y[a] ) 

     #xy and p_xy= [ xy(0,0) , xy(1,0) , xy(0,1), xy(1,1) ]
     ans = 0
     for a in range(2):
          if ( p_xy[a] != 0 ):
               ans += p_xy[ a ] * math.log2( p_xy[ a ] / ( p_x[a] * p_y[0] )  )
          if ( p_xy[a+2] != 0 ):
               ans += p_xy[ a+2 ] * math.log2( p_xy[ a+2 ] / ( p_x[a] * p_y[1] )  )
     return ( ans )
'''
print( estimated_mutual_information( [(0,0),(0,1),(1,0),(1,1)] ) )
print( estimated_mutual_information( [(0,0),(0,1),(1,0)] ) )
print( estimated_mutual_information( [(0,0),(1,1)] ) )
