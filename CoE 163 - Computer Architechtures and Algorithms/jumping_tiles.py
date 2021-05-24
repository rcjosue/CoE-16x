#tiles = [1, 7, 8, 12, 15, 20, 25, 31, 37, 46, 54, 62, 69, 76]
tiles = [1,7,13,18,22,25,30,34,42,49,]
init = tiles[0]
curr_jump, min_jump, max_dist = init-1, init, init
for x in range( len(tiles) - 1 ):
     dist = tiles[x+1] - tiles[x]
     max_dist = max (dist, max_dist)
     min_jump = max (dist, min_jump)
     if dist-1 == curr_jump:
          if min_jump < max_dist+1:
               curr_jump += 1
               min_jump += 1
     if dist > curr_jump+1:
               curr_jump = min_jump
     if dist == curr_jump:
          curr_jump = dist - 1
     print (dist, curr_jump, min_jump)
     print ()
     
print (min_jump)
