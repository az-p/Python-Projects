""" Calculate distance between keys of a number pad https://redd.it/4bc3el"""
import math

def distance(a, b):
    return math.sqrt(math.pow((a[0]-b[0]), 2) + math.pow((a[1] - b[1]), 2))

if __name__ == "__main__":
    coord = {'1': (0, 0),
             '2': (1, 0),
             '3': (2, 0),
             '4': (0, 1),
             '5': (1, 1),
             '6': (2, 1),
             '7': (0, 2),
             '8': (1, 2),
             '9': (2, 2),
             '.': (0, 3),
             '0': (1, 3)}
    input_vals = ['7851', '2851', '219.45.143.143']

    for inp in input_vals:
        path_distance = 0
        #path = []
        for i in range(len(inp)-1):
            # path.append(distance(coord[inp[i]], coord[inp[i+1]]))
            path_distance += distance(coord[inp[i]], coord[inp[i+1]])
        print(inp, str(round(path_distance,2))+'cm', '\n', sep='\n')

