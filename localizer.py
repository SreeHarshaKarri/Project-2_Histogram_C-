# import pdb
import numpy as np
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    #new_beliefs = beliefs

    #
    # TODO - implement this in part 2
    #
    print("Beliefs", beliefs)
    print("p HIT", p_hit)
    print("p MISS", p_miss)
    
    height = len(grid)
    width = len(grid[0])
    row = []
    
    for i in range(height):
        row = []
        for j in range(width):
#             print("i is ", i)
#             print("j is ", j)
#             print("Color", color)
#             print("belief entry is ", beliefs[i][j])
            #detect = (beliefs[i][j] == 'r')
            #detect = (beliefs[i][j] == grid[i][j])
            detect = (grid[i][j] == 'r')
            #print("Detect", detect)
            row.append((detect * p_hit * beliefs[i][j]) + ((1 - detect) * p_miss * beliefs[i][j]))
        new_beliefs.append(row)
        
    #print(new_beliefs)
        
    sum = 0
    i = 0
    j = 0
    
    for i in range(height):
        for j in range(width):
            sum = sum + new_beliefs[i][j]
            #print("Sum is ", sum, new_beliefs[i][j])
            
    i = 0
    j = 0
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j] = new_beliefs[i][j]/sum
            
    #print(new_beliefs)
            
    return new_beliefs 


def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
#     print("height", height)
#     print("width", width)
#     print("d x", dx)
#     print("d y", dy)
#     print(beliefs)
#     print("blu rring", blurring)
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
#             print("i", i)
#             print("j", j)
            
            if(i + dy) >= 0 and (i + dy) < height:
                new_i = (i + dy ) % width
            else:
                new_i = ((i + dy) % width) - width
                
            if(j+dx) >= 0 and (i + dy) < width:    
                new_j = (j + dx ) % height
            else:
                new_j = ((j + dx) % height) - height
#             print("new_i", new_i)
#             print("new_j", new_j)
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)