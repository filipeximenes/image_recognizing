# coding=utf-8

import os
from PIL import Image

from utils import root, iterate_images_folder
from image_processing import calculate_ditance

images_confusion_matrix_one = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_two = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_three = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_four = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_five = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_six = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_seven = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_eight = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_nine = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix_zero = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0};
images_confusion_matrix = {'0': images_confusion_matrix_zero, '1': images_confusion_matrix_one, '2': images_confusion_matrix_two, '3': images_confusion_matrix_three, '4': images_confusion_matrix_four, '5': images_confusion_matrix_five, '6': images_confusion_matrix_six, '7': images_confusion_matrix_seven, '8': images_confusion_matrix_eight, '9': images_confusion_matrix_nine};

def process_and_save_averages(number, realNumber):

    images_confusion_matrix[realNumber][number] = images_confusion_matrix[realNumber][number] + 1;

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

def process_and_save_averages(number, realNumber):

    images_confusion_matrix[realNumber][number] = images_confusion_matrix[realNumber][number] + 1;
	
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
		
		process_and_save_averages(recognized, test_number)
    return results
