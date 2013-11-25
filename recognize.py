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


def iterate_over_test_images():

    averages = get_average_images('trainning_average')

    results = {}

    for test_number, name, image in iterate_images_folder('tests_processed'):

        distances = {}
        for number in averages:
            distances[number] = calculate_ditance(image, averages[number])

        best = float("inf")
        chosen = 0
        for number in distances:
            if distances[number] < best:
                chosen = number
                best = distances[number]

        if not test_number in results:
            results[test_number] = {}
            results[test_number]['success'] = 0
            results[test_number]['error'] = 0

        if chosen == test_number:
            results[test_number]['success'] += 1
        else:
            results[test_number]['error'] += 1

    print results


iterate_over_test_images()
