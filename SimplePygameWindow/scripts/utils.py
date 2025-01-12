import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    """This one is for loading the images"""
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    """This one is for loading images"""
    images = []
    # os.listdir return a list of string, where each string is the name of a file or a directory
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images