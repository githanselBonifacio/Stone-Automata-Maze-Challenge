import numpy as np
import cv2
import os

from src.config import PATH_PROJECT

PATH_DATA = PATH_PROJECT + "\\assets\data\cell.csv"
PATH_IMAGE_PROPAGATION = PATH_PROJECT + "\\assets\images\propagation\\"
PATH_VIDEO = PATH_PROJECT + "\\assets\\video\\"


def load_cell():
    cell = np.loadtxt(PATH_DATA, delimiter=';', dtype='uint8')
    cell[0][0] = 0
    cell[64][84] = 0
    return cell


def create_init_imagen():
    cell = load_cell()
    cell_img = np.full((cell.shape[0], cell.shape[1], 3), 255)
    for i in range(cell.shape[0]):
        for j in range(cell.shape[1]):
            if cell[i][j] != 0:
                cell_img[i][j] = [0, cell[i][j] * 255, 0]

    cv2.circle(cell_img, (0, 0), 1, (0, 0, 255), -1)
    name = PATH_IMAGE_PROPAGATION + "0.jpg"
    cv2.imwrite(name, cell_img)
    res = cv2.resize(cv2.imread(name), dsize=(255, 195), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(name, res)


def create_image_cell(name_image, cell, pos_actual=None):
    if pos_actual is None:
        pos_actual = [0, 0]

    cell_img = np.full((cell.shape[0], cell.shape[1], 3), 255)
    for i in range(cell.shape[0]):
        for j in range(cell.shape[1]):
            if cell[i][j] != 0:
                cell_img[i][j] = [0, cell[i][j] * 255, 0]

    cv2.circle(cell_img, (pos_actual[0], pos_actual[1]), 1, (0, 0, 255), -1)
    name = PATH_IMAGE_PROPAGATION + name_image + ".jpg"
    cv2.imwrite(name, cell_img)
    res = cv2.resize(cv2.imread(name), dsize=(255, 195), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(name, res)


def create_video(id):
    print("creating video "+str(id))
    image_folder = PATH_IMAGE_PROPAGATION
    video_name = PATH_VIDEO + "propagation_"+str(id)+".avi"
    images = [img for img in os.listdir(image_folder) if img.endswith('.jpg')]
    images = sorted(images, key=lambda x: int(os.path.splitext(x)[0]))
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layer = frame.shape
    video = cv2.VideoWriter(video_name, 0, 5, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    video.release()


def select_letter_move(post_before, post_actual):
    if post_before[0] < post_actual[0] and post_before[1] == post_actual[1]:
        return "D"
    elif post_before[0] > post_actual[0] and post_before[1] == post_actual[1]:
        return "U"

    elif post_before[1] < post_actual[1] and post_before[0] == post_actual[0]:
        return "R"
    elif post_before[1] > post_actual[1] and post_before[0] == post_actual[0]:
        return "L"
    else:
        print("Error en funcion post_before= ", post_before, ", post_actual= ", post_actual)
        return None


def write_road_txt(road, id):
    print("creating solution")
    path = PATH_PROJECT + '\\assets\\data\\road_' + str(id) + ".txt"
    with open(path, 'w') as temp_file:
        for item in road:
            temp_file.write("%s " % item)


def write_summry_json(json):
    with open('assets/data/summary.json', 'w') as file:
        json.dump(json, file, indent=5, sort_keys="steps")


def clean_images_file(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))
