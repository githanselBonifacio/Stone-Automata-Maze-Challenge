import random
import secrets

import numpy as np

from src.main.cell_propagation.cell_propagation import propagate_cell, \
    calculate_next_step, end, cell_init, distance_end
from src.main.util.util import create_image_cell, create_video, select_letter_move, write_road_txt, \
    create_init_imagen, clean_images_file, write_summry_json

if __name__ == '__main__':
    summary = {'roads': []}
    for i in range(5):
        clean_images_file("assets/images/propagation")
        pos_actual = [0, 0]
        cell = cell_init
        next_cell = np.zeros((65, 85), dtype='uint8')

        states_cell = []
        road = []
        updates_pos_actual = []

        states_cell.append(cell)
        updates_pos_actual.append(pos_actual)
        print("iteration ", i + 1)
        print("|" * 1000)
        create_init_imagen()

        for j in range(1000000):
            retro_step = random.randint(5, 15)
            distance_to_goal = distance_end(pos_actual=pos_actual)
            next_cell = propagate_cell(cell=cell)  ##calculate next_cell
            moves = calculate_next_step(pos_actual, next_cell)
            if len(moves) == 0:
                print("no movement road closed")
                print("actual ", pos_actual)
                print(updates_pos_actual)
                print("return to position")

                updates_pos_actual = updates_pos_actual[:-retro_step]
                road = road[:-retro_step]
                states_cell = states_cell[:-retro_step]

                pos_actual = updates_pos_actual[-1]
                cell = states_cell[-1]

                print("new position ", pos_actual, " ", len(updates_pos_actual), " steps :: distance to the goal  ",
                      distance_to_goal)

                print("-" * 500)

            else:
                pos_before = pos_actual
                pos_actual = secrets.choice(moves)
                updates_pos_actual.append(pos_actual)
                cell = np.copy(next_cell)
                states_cell.append(cell)
                road.append(select_letter_move(post_before=pos_before, post_actual=pos_actual))
                create_image_cell(name_image=str(j + 1), cell=next_cell, pos_actual=pos_actual)

            if pos_actual == end:
                print("reach the end")
                print(road, " steps")
                write_road_txt(road, i)
                summary['roads'].append({
                    'steps': len(road),
                    'move': road})
                create_video(j)
                break
        write_summry_json(summary)
        print("|" * 1000)
