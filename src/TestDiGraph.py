import unittest
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    g1 = DiGraph()
    g1.add_node(1)
    g1.add_node(2)
    g1.add_node(3)

    def test_v_size(self):
        size = len(self.g1.nodes)
        self.assertEqual(size, 3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
