import random
import networkx as nx
from decimal import *
import numpy as np
import matplotlib.pyplot as plt
grid_size = 20
grid = [[0 for i in range(grid_size)] for i in range(grid_size)] #0: no location 1: location but not home 2: home
num_home = 25
num_loc = 50
edge = [[0 for i in range(num_loc)] for i in range(num_loc)]

arr_locs = random.sample(list(range(grid_size**2)), num_loc)
arr_homes = random.sample(arr_locs, num_home)

def printGrid(twod_arr):
    for i in range(len(twod_arr)):
        print(twod_arr[i])
def computeDist(point1, point2, v1, v2):
    if (v1 == 2 and v2 == 2):
        #return 'x' changed it for nx
        return 0
    #res = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** (0.5)
    res = abs((point1[0] - point2[0])) + abs((point1[1] - point2[1]))
    #return 'x' if res==0 else res changed it for nx
    return 0 if res==0 else res


locs = {}
ind = 0
for loc in arr_locs:
    grid[loc % grid_size][loc // grid_size] = 1
    locs[(loc % grid_size,loc // grid_size)] = [1,ind]
    ind += 1

for home in arr_homes:
    grid[home % grid_size][home // grid_size] = 2
    locs[(home % grid_size,home // grid_size)][0] = 2

loc_str = ""
home_str = ""
for l1,v1 in locs.items():
    loc_str += "Loc"+str(v1[1])+" "
    if(v1[0] == 2):
        home_str += "Loc"+str(v1[1])+" "
    for l2,v2 in locs.items():
        dist = computeDist(l1, l2, v1[0], v2[0])
        edge[v1[1]][v2[1]], edge[v2[1]][v1[1]] = dist, dist

adj_matrix = np.array(edge)
G = nx.from_numpy_matrix(adj_matrix)
nx.draw(G, with_labels=True, font_weight='bold')
#np.savetxt('50.txt', edge, delimiter = ' ', fmt="%s")


print(loc_str)
print("fuck")
print(home_str)
