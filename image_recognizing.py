# coding=utf-8

import os
import sys
from image_processing import (
    binarize_image, calculate_image_averages,
)
from utils import root, iterate_images_folder


def process_and_save_images(source_dir, dest_dir):
    for number, name, image in iterate_images_folder(source_dir):
        processed = binarize_image(image)
        
        save_dir = root(dest_dir, number)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        processed.save(root(save_dir, name))


def process_and_save_averages(source_dir, dest_dir):
    images_dict = {}
    
    for number, name, image in iterate_images_folder(source_dir):
        if not number in images_dict:
            images_dict[number] = []

        images_dict[number].append(image)

    averages = calculate_image_averages(images_dict)
    
    save_dir = root(dest_dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for key in averages:
        averages[key].save(root(save_dir, key + '.jpg'))


def main(*args):
    kind = sys.argv[1]
    main_dir = sys.argv[2]

    processed_dir = main_dir + '_processed'
    averages_dir = main_dir + '_average'

    if kind == 'process':
        process_and_save_images(main_dir, processed_dir)
    elif kind == 'average':
        if not os.path.exists(root(processed_dir)):
            process_and_save_images(main_dir, processed_dir)

        process_and_save_averages(processed_dir, averages_dir)


if __name__ == '__main__':
    main()
