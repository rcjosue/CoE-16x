import math

def count_bad_channels(blocklength, erasure_prob):
     tree= [ [erasure_prob] ]
     depth = int(math.log(blocklength,2))
     
     for level in range(1 , depth+1 ):
          tree.append([])
          for elem in tree[level-1]:
               left = 2*elem - elem**2
               right = elem**2
               tree[level].append(left)
               tree[level].append(right)

     count=0
     for item in range( blocklength-1 ) :
          if ( tree[-1][item] > erasure_prob ):
               count += 1
     return( count )

print( count_bad_channels(16 ,0.8) )

'''
     for item in tree:
          print(item)

     def tree_traversal( e, depth ):
          left = 2*e - e**2
          right = e**2
          tree.append( tree_traversal(left), tree_traversal(right) )
'''
