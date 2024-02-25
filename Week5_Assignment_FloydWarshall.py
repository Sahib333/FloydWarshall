import sys

# Make pathsize max if no path exists
INF = sys.maxsize

#  Graph for testing 
graph = [[0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0],
    ]
# Automatically detect number of vertices
vertex_number = len(graph)

def floyd_warshall(graph):

    """
    Algorithm to finding the shortest path between two nodes
    by recursively looking at the shortest distance between each path    
    """

    # Identify the dimensions of the graph
  

    # Create an array with dimenions equal to the graph
    #  to update with the minimum path length

    dist=[0 * vertex_number for _ in range(vertex_number)]

    #  Populate the array with the given graph values 
    for i in range(vertex_number):
        dist[i]=graph[i]

    print(dist)
    # Iterate over each row by using adding on the path distance
    # and determining if the path has shortened with the new node
     
    for k in range(vertex_number):
        for i in range(vertex_number):
            for j in range(vertex_number):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    
    print_solution(dist)
    


# Create a matrix for the solution to be printed and replace the maxvalue
#  with N for clarity and improving formatting of output
def print_solution(dist):
    for i in range(vertex_number):
        for j in range(vertex_number):
            if(dist[i][j] == INF):
                print("N", end=" | ")
            else:
                print(dist[i][j], end=" | ")
        print(" ")


floyd_warshall(graph)
