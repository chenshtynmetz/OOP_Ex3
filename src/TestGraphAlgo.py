import os
import unittest
from GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):


    def test_load_from_json(self):
        graphAlgo = GraphAlgo(DiGraph())
        self.assertFalse(graphAlgo.load_from_json("somthing.json"))
        self.assertTrue(graphAlgo.load_from_json("./data/A0.json"))  # graph with pos

    def test_save_from_json(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.load_from_json("./data/A0.json")
        self.assertTrue(graphAlgo.save_to_json("temp.json"))
        # os.remove("./temp.json")

    def test_shortest_path(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.graph.add_node(0)
        graphAlgo.graph.add_node(1)
        graphAlgo.graph.add_node(2)
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 4)
        self.assertEqual(graphAlgo.shortest_path(0, 1), (1.0, [0, 1]))
        self.assertEqual(graphAlgo.shortest_path(0, 2), (5.0, [0, 1, 2]))
        graphAlgo.graph.remove_node(1)
        self.assertEqual(graphAlgo.shortest_path(0, 2), (5.0, [0, 1, 2]))

    def test_centerPoint(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.load_from_json("./data/100000.json")
        graphAlgo.centerPoint()
        # graphAlgo1 = GraphAlgo(DiGraph())
        # graphAlgo1.load_from_json("./data/A0.json")
        # x = graphAlgo1.centerPoint()
        # print(x)
        # self.assertEqual(x, (7, 6.806805834715163))
        # graphAlgo2 = GraphAlgo(DiGraph())
        # graphAlgo2.load_from_json("./data/A1.json")
        # y = graphAlgo2.centerPoint()
        # print(y)
        # self.assertEqual(y, (8, 9.925289024973141))
        # graphAlgo3 = GraphAlgo(DiGraph())
        # graphAlgo3.load_from_json("./data/A2.json")
        # self.assertEqual(graphAlgo3.centerPoint(), (0, 7.819910602212574))
        # graphAlgo4 = GraphAlgo(DiGraph())
        # graphAlgo4.load_from_json("./data/A3.json")
        # self.assertEqual(graphAlgo4.centerPoint(), (2, 8.182236568942237))
        # graphAlgo5 = GraphAlgo(DiGraph())
        # graphAlgo5.load_from_json("./data/A4.json")
        # self.assertEqual(graphAlgo5.centerPoint(), (6, 8.071366078651435))
        # graphAlgo6 = GraphAlgo(DiGraph())
        # graphAlgo6.load_from_json("./data/A5.json")
        # self.assertEqual(graphAlgo6.centerPoint(), (40, 9.291743173960954))

    def test_TSP(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 5)
        g.add_edge(3, 2, 4)
        g.add_edge(2, 5, 7)
        g.add_edge(4, 1, 3)
        g.add_edge(5, 2, 4)
        g.add_edge(3, 1, 9)
        g.add_edge(3, 4, 2)
        g.add_edge(5, 1, 2)
        alg = GraphAlgo(g)
        cities = [3, 5, 1, 2]
        ans = alg.TSP(cities)
        self.assertEqual(ans, ([3, 2, 5, 1], 13.0))



if __name__ == '__main__':
    unittest.main()
