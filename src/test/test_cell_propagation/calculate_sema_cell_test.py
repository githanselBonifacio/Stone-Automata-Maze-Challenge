import unittest

import numpy as np
from src.main.cell_propagation.cell_propagation import calculate_suma_cell, calculate_new_value_cell


class TestCellPropagation(unittest.TestCase):
    def test_calculate_cell_contour(self):
        cell = np.zeros((3, 3))
        cell[0][1] = 1
        self.assertEqual(calculate_suma_cell([0, 0], cell), 1,
                         "error with top left cell with 1 adjacent cell \n" + str(cell))

        cell[0][2] = 1
        self.assertEqual(calculate_suma_cell([0, 0], cell), 1,
                         "error with top left cell with 1 adjacent cell and 1 no-adjacent cell \n" + str(cell))

        cell[1][0] = 1
        self.assertEqual(calculate_suma_cell([0, 0], cell), 2,
                         "error with top left cell with 2 adjacent cell \n" + str(cell))
        cell[1][1] = 1
        self.assertEqual(calculate_suma_cell([0, 0], cell), 3,
                         "error with top left cell with 3 adjacent cell \n" + str(cell))

        cell[2][0] = 1
        self.assertEqual(calculate_suma_cell([2, 2], cell), 1,
                         "error with bottom right cell with 1 adjacent cell and 4 no-adjacent cell \n" + str(cell))

        self.assertEqual(calculate_suma_cell([0, 2], cell), 2,
                         "error with top right cell with 2 adjacent cell and 2 no-adjacent cell \n" + str(cell))

        self.assertEqual(calculate_suma_cell([1, 2], cell), 3,
                         "error with bottom center cell with 3 adjacent cell and 2 no-adjacent cell \n" + str(cell))

    def test_calculate_cell_central(self):
        cell = np.zeros((3, 3))
        cell[1][1] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 0, "error with 0 adjacent cells\n" + str(cell))

        cell[0][0] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 1, "error with 1 adjacent cells\n" + str(cell))

        cell[0][1] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 2, "error with 2 adjacent cells\n" + str(cell))

        cell[0][2] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 3, "error with 3 adjacent cells\n" + str(cell))

        cell[1][0] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 4, "error with 4 adjacent cells\n" + str(cell))

        cell[1][2] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 5, "error with 5 adjacent cells\n" + str(cell))

        cell[2][0] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 6, "error with 6 adjacent cells\n" + str(cell))

        cell[2][1] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 7, "error with 7 adjacent cells\n" + str(cell))

        cell[2][2] = 1
        self.assertEqual(calculate_suma_cell([1, 1], cell), 8, "error with 8 adjacent cells\n" + str(cell))

    def test_calculate_new_value_cell(self):
        self.assertEqual(calculate_new_value_cell(0, 1), 0, "error, cell off, should not be on because there are 1 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(0, 2), 1, "error, cell off, should be on because there are 2 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(0, 4), 1, "error, cell off, should be on because there are 4 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(0, 5), 0, "error, cell off, should not be on because there are 5 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(1, 3), 0, "error, cell on, should not be deactivated because there are 3 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(1, 4), 1, "error, cell on, should be deactivated because there are 4 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(1, 5), 1, "error, cell on, should be deactivated because there are 5 adjacent"
                                               "active cells")

        self.assertEqual(calculate_new_value_cell(1, 6), 0, "error, cell on, should not deactivated on because there are 6 adjacent"
                                               "active cells")




if __name__ == '__main__':
    unittest.main()
