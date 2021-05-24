# Assume 5 nodes
road_net = {0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: 
[0, 1, 3]}
visit_dist = [-1 for x in range(len(road_net))]
def dfs(this_dist, current_node):
if visit_dist[current_node] >= 0:
 return
 
print(current_node)
visit_dist[current_node] = this_dist
 
for each_nbr in road_net[current_node]:
 dfs(this_dist + 1, each_nbr)
start_node = 0
dfs(0, start_node)
