import random, math

def exact_entropy(dist):
     return sum([-p*math.log2(p) for p in dist.values() if p > 0])

def estimated_entropy(samples, dist):
     return sum([-samples.count(x)/len(samples) * math.log2(dist[x]) for x in set(samples) if dist[x] > 0])

def jointly_typical(x, y, joint_dist, epsilon):
     if len(x) != len(y):
          raise ValueError('x and y must have equal lengths.')
     elif epsilon <= 0:
          raise ValueError('epsilon must be strictly positive.')
     else:
          row_length = [len(joint_dist[i]) for i in range(len(joint_dist))]
          if any([row_length[i] != row_length[0] for i in range(1, len(row_length))]):
               raise ValueError('All rows of joint_dist must have equal lengths.')
     
     xy = [(x[i], y[i]) for i in range(len(x))]
     x_alphabet = range(len(joint_dist))
     y_alphabet = range(len(joint_dist[0]))

     x_prob = {x: sum([joint_dist[x][y] for y in y_alphabet]) for x in x_alphabet}
     y_prob = {y: sum([joint_dist[x][y] for x in x_alphabet]) for y in y_alphabet}
     xy_prob = {(x,y): joint_dist[x][y] for x in x_alphabet for y in y_alphabet}

     Hx = exact_entropy(x_prob)
     Hy = exact_entropy(y_prob)
     Hxy = exact_entropy(xy_prob)

     return max([abs(Hx - estimated_entropy(x, x_prob)), abs(Hy - estimated_entropy(y, y_prob)), abs(Hxy - estimated_entropy(xy, xy_prob))]) < epsilon

def typical_set_codec(channel, x_dist, frame_len, block_len, num_frames, epsilon):
     two_to_k = pow(2,frame_len)
     k_s = range( 1 , len(channel) +1  )
     notebook = [ random.choices( k_s, weights=x_dist, k=block_len ) for num in range(two_to_k)  ]
     #[ [ random.choices( k_s, x_dist ) for a in range(block_len)] for num in range(two_to_k)  ]
     print (notebook)
     x1,y1 = [] , []
     x2,y2 = [] , []
     for num in range( num_frames ):
          x.append ( random.choice( notebook ) )
          y.append ( random.choices( channel[] )[0] )
     return ans

p = 0.001
channel = [ [( 1-p) , p ] , [ p , (1-p) ] ]
x = [ 0.5, 0.5 ]
frame = 1
block = 2
num = 10
e = 0.02
#print( typical_set_codec( channel, x, frame, block, num, e  ) )

print( y-x,' ', z-y )
