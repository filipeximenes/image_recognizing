# coding=utf-8

import os
from PIL import Image

from utils import root, iterate_images_folder
from image_processing import calculate_ditance


def get_average_images(dirname):
    dirname = root(dirname)

    averages = {}

    for number, name, image in iterate_images_folder(dirname):
        averages[number] = image

    return averages


def recognize_number_in_image(image, averages):
    recognized_number = None
    best_distance = float("inf")

    for number in averages:
        distance = calculate_ditance(image, averages[number])

        if distance < best_distance:
            best_distance = distance
            recognized_number = number

    return recognized_number


def execute_test_set(trainning_patterns_dir, test_set_dir):
    averages = get_average_images(trainning_patterns_dir)

    results = {}

    for test_number, name, image in iterate_images_folder(test_set_dir):
        recognized = recognize_number_in_image(image, averages)

        if not test_number in results:
            results[test_number] = {}
            results[test_number]['success'] = 0
            results[test_number]['error'] = 0

        if recognized == test_number:
            results[test_number]['success'] += 1
        else:
            results[test_number]['error'] += 1

    return results
