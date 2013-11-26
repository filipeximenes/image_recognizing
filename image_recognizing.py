# coding=utf-8

import os
import sys
from image_processing import (
    binarize_image, calculate_image_averages,
)
from utils import root, iterate_images_folder
from recognize import execute_test_set


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
    
    for key in averages:
        save_dir = root(dest_dir, key)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        averages[key].save(root(save_dir, key + '.jpg'))


def main(*args):
    if len(sys.argv) >= 3:
        kind = sys.argv[1]
        main_dir = sys.argv[2]

        processed_dir = main_dir + '_processed'
        averages_dir = main_dir + '_average'

    if len(sys.argv) >= 4:
        test_dir = sys.argv[3]

        test_processed_dir = test_dir + '_processed'

    if kind == 'process':
        process_and_save_images(main_dir, processed_dir)
    elif kind == 'average':
        if not os.path.exists(root(processed_dir)):
            process_and_save_images(main_dir, processed_dir)

        process_and_save_averages(processed_dir, averages_dir)
    elif kind == 'test_sets':
        if not os.path.exists(root(processed_dir)):
            process_and_save_images(main_dir, processed_dir)

        if not os.path.exists(root(averages_dir)):
            process_and_save_averages(processed_dir, averages_dir)

        if not os.path.exists(root(test_processed_dir)):
            process_and_save_images(test_dir, test_processed_dir)

        results = execute_test_set(averages_dir, test_processed_dir)
        print results


if __name__ == '__main__':
    main()
