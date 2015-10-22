__author__ = 'TeamA_000'
import unittest

from make_puzzle import RJP


class MyTestCase(unittest.TestCase):
    def test_generate_num(self):
        self.assertEquals(RJP.puzzle_gen.generate_num(3, 3, 5), 3)
        self.assertEquals(RJP.puzzle_gen.generate_num(0, 0, 5), 4)
        self.assertEquals(RJP.puzzle_gen.generate_num(0, 4, 5), 4)
        self.assertEquals(RJP.puzzle_gen.generate_num(1, 1, 5), 3)


    def test_check(self):
        array = [[2, 2, 1, 4, 1], [4, 3, 2, 3, 1], [2, 3, 2, 2, 2], [1, 2, 2, 1, 1], [3, 2, 4, 1, 0]]
        input = 5
        self.assertEquals(RJP.puzzle_evaluate.check_right(0, 0, 2, input), (2, 0))
        self.assertEquals(RJP.puzzle_evaluate.check_down(0, 0, 2, input), (0, 2))
        self.assertEquals(RJP.puzzle_evaluate.check_left(0, 0, 2, input), (-1, -1))


        self.assertEquals(RJP.puzzle_evaluate.check_right(1, 1, 1, input), (2,1))


    def test_evaluate(self):
        array = [[(-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1), (0 ,0)],
                 [(-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1)],
                 [(-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1)],
                 [(-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1)],
                 [(-1 ,-1), (-1 ,-1), (-1 ,-1), (-1 ,-1), (0 ,4)]]
        input = 5
        self.assertEquals(RJP.puzzle_evaluate.evaluate(array, input), ([(4, 4), (0, 4), (0, 0)], -2))

        array = [[(-1, -1), (-1, -1), (-1, -1), (-1, -1), (0, 0)],
                 [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                 [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                 [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                 [(0, 0), (-1, -1), (-1, -1), (-1, -1), (4, 0)]]
        self.assertEquals(RJP.puzzle_evaluate.evaluate(array, input), ([(4, 4), (4, 0), (0, 0)], -2))

    def test_bfs(self):
        array = [[2, 2, 1, 4, 1],
                 [4, 3, 2, 3, 1],
                 [2, 3, 2, 2, 2],
                 [1, 2, 2, 1, 1],
                 [3, 2, 4, 1, 0]]
        input = 5
        self.assertEquals(RJP.puzzle_evaluate.bfs_path(array, input), (-4))

        array_two = [[2, 2, 1, 4, 3],
                     [4, 3, 2, 3, 2],
                     [2, 3, 2, 2, 3],
                     [1, 2, 2, 1, 3],
                     [3, 2, 3, 3, 0]]
        self.assertEquals(RJP.puzzle_evaluate.bfs_path(array_two, input), 99999)

if __name__ == '__main__':
    unittest.main(verbosity=2)