# coding=utf-8

import os
from os.path import join, abspath, dirname
from PIL import Image

from config import FILE_SIZE, IMAGES_FOLDER


root = lambda *x: join(abspath(join(dirname(__file__), IMAGES_FOLDER)), *x)


def iterate_images_folder(dirname):
    source = root(dirname)

    for number in os.listdir(source):
        image_dir = join(source, number)
        if os.path.isdir(image_dir):
            for image_name in os.listdir(image_dir):
                image_path = root(dirname, number, image_name)
                try:
                    image_file = Image.open(image_path)
                    image_file = image_file.resize(FILE_SIZE)
                    yield number, image_name, image_file
                except:
                    pass
