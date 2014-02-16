# coding=utf-8

import os
import numpy
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


def create_probabilities_matrix(confusion):

    probabilities = numpy.zeros(shape=(10,10))

    for (i, row) in enumerate(confusion):
        row_sum = row.sum()
        for (j, item) in enumerate(row):
            if row_sum > 0:
                probabilities[i][j] = confusion[i][j] / row_sum

    return probabilities


def execute_test_set(trainning_patterns_dir, test_set_dir):
    averages = get_average_images(trainning_patterns_dir)

    confusion = numpy.zeros(shape=(10,10))

    for test_number, name, image in iterate_images_folder(test_set_dir):
        recognized = recognize_number_in_image(image, averages)

        confusion[int(test_number)][int(recognized)] += 1

    probabilities = create_probabilities_matrix(confusion)

    return confusion, probabilities
