import unittest

import numpy as np

from src.main.util.util import select_letter_move


class TestUtil(unittest.TestCase):
    def test_select_letter_move(self):
        self.assertEqual(select_letter_move([1, 1], [1, 2]), "R")
        self.assertEqual(select_letter_move([1, 1], [1, 0]), "L")
        self.assertEqual(select_letter_move([1, 1], [0, 1]), "U")
        self.assertEqual(select_letter_move([1, 1], [2, 1]), "D")