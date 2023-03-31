import math
import secrets

import numpy as np

from src.main.util.util import load_cell

cell_init = load_cell()
end = [cell_init.shape[0] - 1, cell_init.shape[1] - 1]


def calculate_available_moves(pos_cell, actual_cell):
    pos_ul = [pos_cell[0] - 1, pos_cell[1] - 1]
    pos_u = [pos_cell[0] - 1, pos_cell[1]]
    pos_ur = [pos_cell[0] - 1, pos_cell[1] + 1]

    pos_l = [pos_cell[0], pos_cell[1] - 1]
    pos_r = [pos_cell[0], pos_cell[1] + 1]

    pos_dl = [pos_cell[0] + 1, pos_cell[1] - 1]
    pos_d = [pos_cell[0] + 1, pos_cell[1]]
    pos_dr = [pos_cell[0] + 1, pos_cell[1] + 1]

    adjacent_cells = [pos_ul, pos_u, pos_ur, pos_l, pos_r, pos_dl, pos_d, pos_dr]
    adjacent_cells_no_diagonales = [pos_u, pos_l, pos_r, pos_d]

    adjacent_cells_filter = list(
        filter(lambda x: 0 <= x[0] < actual_cell.shape[0] and 0 <= x[1] < actual_cell.shape[1], adjacent_cells))
    adjacent_cells_no_diagonales_filter = list(
        filter(lambda x: 0 <= x[0] < actual_cell.shape[0] and 0 <= x[1] < actual_cell.shape[1],
               adjacent_cells_no_diagonales))
    return adjacent_cells_filter, adjacent_cells_no_diagonales_filter


def calculate_suma_cell(pos_cell, actual_cell):
    adjacent_cells, _ = calculate_available_moves(pos_cell, actual_cell)
    sum_adjacent_cells = 0

    for c in adjacent_cells:
        sum_adjacent_cells += actual_cell[c[0]][c[1]]

    return sum_adjacent_cells


def calculate_new_value_cell(value_cell, sum_adjacent_cells):
    if value_cell == 0:
        if 1 < sum_adjacent_cells < 5:
            return 1
        else:
            return 0

    if value_cell == 1:
        if 3 < sum_adjacent_cells < 6:
            return 1
        else:
            return 0


def propagate_cell(cell):
    next_cell = np.zeros((65, 85), dtype='uint8')
    for i in range(cell.shape[0]):
        for j in range(cell.shape[1]):
            sum_adjacent_cells = calculate_suma_cell([i, j], cell)
            next_cell[i][j] = calculate_new_value_cell(value_cell=cell[i][j], sum_adjacent_cells=sum_adjacent_cells)

    return next_cell


def calculate_next_step(pos_cell, next_cell_propagation):
    _, available_moves = calculate_available_moves(pos_cell, next_cell_propagation)
    valid_move = []
    for move in available_moves:
        if next_cell_propagation[move[0]][move[1]] == 0:
            valid_move.append(move)

    return valid_move


def select_shortest_step_distance_to_goal(move):
    coor = []
    for p in move:
        d = math.sqrt((end[0] - p[0]) ** 2 + (end[1] - p[1]) ** 2)
        coor.append(d)

    min_indexs = [index for index, c in enumerate(coor) if c == min(coor)]
    return move[secrets.choice(min_indexs)]


def distance_end(pos_actual):
    return math.sqrt((end[0] - pos_actual[0]) ** 2 + (end[1] - pos_actual[1]) ** 2)
