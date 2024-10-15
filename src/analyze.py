import networkx
import scipy.stats as sps
from gen import Graph_generator
from random import randint


def get_nodes_degrees(d, n, k) -> float:
    size = 20
    result = 0

    for _ in range(size):
        distribution = sps.norm.rvs(loc=0, scale=n, size=k) if d else sps.levy.rvs(loc=0, scale=n, size=k)
        dist = (max(distribution) - min(distribution)) / 10
        if not d: print(dist)
        lol = Graph_generator(distribution, dist)
        res = lol.generate()
        arr = networkx.degree_histogram(res)
        mx = len(arr) + 1
        result += mx


    return result / size

def get_edges_number(d, n, k) -> float:
    size = 20
    edges = 0

    for _ in range(size):
        distribution = sps.norm.rvs(loc=0, scale=n, size=k) if d else sps.levy.rvs(loc=0, scale=n, size=k)
        dist = (max(distribution) - min(distribution)) / 10
        lol = Graph_generator(distribution, dist)
        res = lol.generate()

        edges += networkx.number_of_edges(res)

    return edges / size


def get_components_number(d, n, k) -> float:
    size = 20
    components = 0

    for _ in range(size):
        distribution = sps.norm.rvs(loc=0, scale=n, size=k) if d else sps.maxwell.rvs(loc=0, scale=n, size=k)
        dist = (max(distribution) - min(distribution)) / 1000
        lol = Graph_generator(distribution, dist)
        res = lol.generate()

        components += networkx.number_connected_components(res)

    return components / size

def main() -> None:
    for _ in range(100):
        k, n = randint(100, 1000), randint(3, 1000)
        print(f"scale = {n}, size = {k}")
        print(get_nodes_degrees(True, n, k) / get_nodes_degrees(False, n, k), end='\n')
        print(get_nodes_degrees(True, n, k), get_nodes_degrees(False, n, k), end='\n\n')
        

if __name__ == "__main__":
    main()

### NUMBER OF EDGES IN NORMAL DISTRIBUTION size = (200 -> 1000, STEP = 100), scale = 3
###############################
# 1118.2
# 2495.05
# 4453.25
# 7039.2
# 10010.4
# 13672.65
# 17839.4
# 22440.1
# 28265.2
###############################


### NUMBER OF EDGES IN UNIFORM DISTRIBUTION size = (200 -> 1000, STEP = 100), scale = 3
###############################
# 333.3
# 735.4
# 1306.7
# 2070.7
# 2985.25
# 4009.55
# 5255.75
# 6736.75
# 8242.55
###############################

##--------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------


#------- NUMBER OF COMPONENTS IN NORMAL DISTRIBUTION size = (200 -> 1000, STEP = 100), scale = 3-----------
###############################
# 9.825
# 8.9
# 8.06
# 8.065
# 7.615
# 7.655
# 7.245
# 7.29
# 7.045
###############################


#------- NUMBER OF COMPONENTS IN UNIFORM DISTRIBUTION size = (200 -> 1000, STEP = 100), scale = 3-----------
###############################
# 38.95
# 25.91
# 15.52
# 9.015
# 4.89
# 3.08
# 1.995
# 1.555
# 1.22
###############################

##--------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------------

#------- MAX DEGREE IN NORMAL DISTRIBUTION size = (200 -> 1000, STEP = 100), scale = 3-----------
###############################
# 24.0
# 32.85
# 41.0
# 51.3
# 59.9
# 68.5
# 75.9
# 86.15
# 95.15
###############################

#------- MAX DEGREE IN UNIFORM DISTRIBUTION size = (200 -> 1000, STEP = 100), scale = 3-----------
###############################
# 10.1
# 12.7
# 15.15
# 19.25
# 21.35
# 22.65
# 25.55
# 27.7
# 29.95
###############################




#NORM
# nodes degres
# 0 4.65
# 1 4.3
# 2 5.75
# 3 7.45
# 4 7.8
# 5 6.8
# 6 9.3
# 7 9.25
# 8 11.0
# 9 11.0
# 10 11.95
# 11 12.0
# 12 13.05
# 13 14.45
# 14 12.35
# 15 12.65
# 16 10.7
# 17 8.85
# 18 8.15
# 19 6.05
# 20 4.55
# 21 1.8
# 22 1.5
# 23 1.35
# 24 1.05
# 25 0.75
# 26 0.35
# 27 0.75
# 28 0.05
# 29 0.35

# edges number = 1112.5

# numberOfComponents = 9.65

# UNIFORM

#nodes degrees
# 0 8.05
# 1 22.6
# 2 43.95
# 3 43.2
# 4 35.25
# 5 23.7
# 6 12.6
# 7 6.5
# 8 2.9
# 9 0.75
# 10 0.35
# 11 0.15

# edges number = 329.1

# number of components = 39.435
