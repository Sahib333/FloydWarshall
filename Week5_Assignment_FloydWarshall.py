import sys

# Make pathsize max if no path exists
INF = sys.maxsize



def floyd_warshall(graph):

    """
    Algorithm to finding the shortest path between two nodes
    by recursively looking at the shortest distance between each path    
    """

    # Automatically get dimensions of graph
    # Declare as global to be used in subsequent function
    global vertex_number
    vertex_number = len(graph)

    
    # Create an array with dimenions equal to the graph
    #  to update with the minimum path length

    dist=[0 * vertex_number for _ in range(vertex_number)]

    #  Populate the array with the given graph values 
    for i in range(vertex_number):
        dist[i]=graph[i]

    # Iterate over each row by using adding on the path distance
    # and determining if the path has shortened with the new node
     
    for k in range(vertex_number):
        for i in range(vertex_number):
            for j in range(vertex_number):
                if dist[i][k]>=0 and dist[k][j]>=0:
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
                elif (dist[i][k]<0 or dist[k][j]<0) and dist[i][k]!=INF and dist[k][j]!=INF:
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
                else:
                    min(dist[i][j],INF)    
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

# Run the code for the desired graph
if __name__=='__main__':
    #  Graph for testing 
    graph = [[0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]

    """ 
            7
    (1)---------->(2)
     |             |
     |             | 5 
   8 |             |
     V             V
    (4)<----------(3)
            2
    
    """


    floyd_warshall(graph)