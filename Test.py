import unittest
import sys 

from Week5_Assignment_FloydWarshall import floyd_warshall
from Iterative_FW import floyd


INF = sys.maxsize


class TestFWAlgo(unittest.TestCase):


    def test_normal(self):
        graph = [[0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))



    def test_negative(self):
        graph = [[0, -7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))




    def test_float(self):
        graph = [[0, 7.6, INF, 8.2],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))




    def test_no_path(self):
        graph = [[0, INF, INF, INF],
    [INF, 0, INF, INF],
    [INF, INF, 0,  INF],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))  




    def test_complete_path(self):
        graph = [[0, 1, 9, 8],
    [3, 0, 15, 7],
    [110, 54, 0,  12],
    [52, 12, 3, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))  


    def test_more_node(self):
        graph = [[0, 1, 9, 8,7],
    [3, 0, 15, 7,9],
    [110, 54, 0,  12,13],
    [52, 12, 3, 0,4],
    [INF,INF,INF,7,0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))  




    def test_less_node(self):
        graph = [[0, 1, 9],
    [3, 0, 15],
    [110, 54, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph))  

    def test_large_number(self):
        graph = [[0, 1, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999],
    [3, 0, 15],
    [110, 54, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floyd(graph)) 

if __name__=='__main__':
    unittest.main()


