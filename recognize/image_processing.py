
from PIL import Image

from config import THRESHOLD, FILE_SIZE


def binarize_image(image):
    image_file = image.convert('L') # convert image to black and white

    width, height = image_file.size

    for x in range(width):
        for y in range(height):
            point = (x, y)
            pixel = image_file.getpixel(point)
            if pixel < THRESHOLD:
                image_file.putpixel(point, 255)
            else:
                image_file.putpixel(point, 0)

    return image_file


def sum_images(img1, img2):
    width, height = img1.size

    for x in range(width):
        for y in range(height):
            point = (x, y)
            pixel1 = img1.getpixel(point)
            pixel2 = img2.getpixel(point)

            img1.putpixel(point, pixel1 + pixel2)

    return img1


def divide_image_by(image, div):
    width, height = image.size

    for x in range(width):
        for y in range(height):
            point = (x, y)
            pixel = image.getpixel(point)

            image.putpixel(point, pixel/div)

    return image


def average_from_list(images):
    average = Image.new('L', FILE_SIZE, 'black')

    for image in images:
        itermediate = divide_image_by(image, len(images))
        average = sum_images(average, itermediate)

    return average


def calculate_image_averages(images_dict):
    averages = {}

    for key in images_dict:
        averages[key] = average_from_list(images_dict[key])

    return averages


def calculate_ditance(img1, img2):
    width, height = img1.size

    dist = 0

    for x in range(width):
        for y in range(height):
            point = (x, y)
            pixel1 = img1.getpixel(point)
            pixel2 = img2.getpixel(point)

            dist += abs(pixel1 - pixel2)
    
    return dist
