import unittest
import sys 

from Week5_Assignment_FloydWarshall import floyd_warshall
from Week5_Assignment_FloydWarshall_Base import floydWarshall


INF = sys.maxsize


class TestFWAlgo(unittest.TestCase):
    def test_normal(self):
        graph = [[0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floydWarshall(graph))

    def test_negative(self):
        graph = [[0, -7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floydWarshall(graph))

    def test_float(self):
        graph = [[0, 7.6, INF, 8.2],
    [INF, 0, 5, INF],
    [INF, INF, 0,   2],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floydWarshall(graph))

    def test_no_path(self):
        graph = [[0, INF, INF, INF],
    [INF, 0, INF, INF],
    [INF, INF, 0,  INF],
    [INF, INF, INF, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floydWarshall(graph))  


    def test_complete_path(self):
        graph = [[0, 1, 9, 8],
    [3, 0, 15, 7],
    [110, 54, 0,  12],
    [52, 12, 3, 0]
    ]



        self.assertEqual(floyd_warshall(graph), floydWarshall(graph))  



if __name__=='__main__':
    unittest.main()


