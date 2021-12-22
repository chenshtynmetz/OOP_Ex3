import os
import unittest
from GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph

class MyTestCase(unittest.TestCase):

    def test_load_from_json(self):
        graphAlgo = GraphAlgo(DiGraph())
        # self.assertFalse(graphAlgo.load_from_json("somthing.json")) #
        self.assertTrue(graphAlgo.load_from_json("A0.json"))  # graph with pos
        # self.assertTrue(graphAlgo.load_from_json("T0.json"))  # graph without pos

    def test_save_from_json(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.load_from_json("A0.json")
        self.assertTrue(graphAlgo.save_to_json("temp.json"))
        os.remove("./temp.json")

    def test_shortest_path(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.graph.add_node(0)
        graphAlgo.graph.add_node(1)
        graphAlgo.graph.add_node(2)
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 4)
        self.assertEqual(graphAlgo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(graphAlgo.shortest_path(0, 2), (5, [0, 1, 2]))
        graphAlgo.graph.remove_node(1)
        self.assertEqual(graphAlgo.shortest_path(0, 2), (float('inf'), []))

    def test_centerPoint(self):
        graphAlgo1 = GraphAlgo(DiGraph())
        graphAlgo1.load_from_json("A0.json")
        x = graphAlgo1.centerPoint()
        print(x)
        self.assertEqual(x, (7, 6.806805834715163))
        graphAlgo2 = GraphAlgo(DiGraph())
        graphAlgo2.load_from_json("A1.json")
        y = graphAlgo2.centerPoint()
        print(y)
        self.assertEqual(y, (8, 9.925289024973141))
        graphAlgo3 = GraphAlgo(DiGraph())
        graphAlgo3.load_from_json("A2.json")
        self.assertEqual(graphAlgo3.centerPoint(), (0, 7.819910602212574))

        # graphAlgo.load_from_json("./data/A3.json")
        # self.assertEqual(graphAlgo.centerPoint(), (2, 8.182236568942237))
        #
        # graphAlgo.load_from_json("./data/A4.json")
        # self.assertEqual(graphAlgo.centerPoint(), (6, 8.071366078651435))
        #
        # graphAlgo.load_from_json("./data/A5.json")
        # self.assertEqual(graphAlgo.centerPoint(), (40, 9.291743173960954))

    # def test_centerPointOn1000Nodes(self):
    #     graphAlgo = GraphAlgo(DiGraph())
    #     graphAlgo.load_from_json("1000Nodes.json")
    #     self.assertEqual(graphAlgo.centerPoint(), (362, 1185.9594924690523))



if __name__ == '__main__':
    unittest.main()
