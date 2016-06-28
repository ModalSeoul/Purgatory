import pygame
from time import sleep


def play(path, delay=None):
    sound_object = pygame.mixer.Sound('sounds/{}'.format(path))
    sound_object.play()
    if delay is not None:
        sleep(delay)


def music(path):
    pygame.mixer.music.load('sounds/{}'.format(path))
    pygame.mixer.music.play()
