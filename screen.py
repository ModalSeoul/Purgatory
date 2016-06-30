import pygame
import os
from utils.audio import play, music
from time import sleep


class Screen:
    """
    Screen object. Handles all data/objects
    related to the screen.
    """

    def __init__(self, x, y):
        pygame.init()
        self.blits = []
        self.fonts = []
        self.loaded_images = {}
        self.PATH = 'images/'
        self.size = self.x, self.y = x, y
        self.screen = pygame.display.set_mode(self.size)

        self.WHITE = (255, 255, 255)
        self.D_WHITE = (200, 200, 200)
        self.BLACK = (0, 0, 0)
        self.background = pygame.image.load(
            os.path.join("images", "menu_bg.png")).convert()

    def blit_storage(self, rect):
        self.blits.append(rect)

    def text_storage(self, rect):
        self.fonts.append(rect)

    def refresh_text(self):
        for string in self.fonts:
            self.screen.blit(string[0], string[1])

    def render_refresh(self):
        for blit in self.blits:
            self.screen.blit(blit[0], blit[1])

    def draw_string(self, text, x, y, size=None, color=None):
        if size is None:
            size = 24
        if color is None:
            color = self.WHITE

        font = pygame.font.Font('ostrich-regular.ttf', size)
        string = font.render(text, True, color)
        text_rect = string.get_rect()
        text_rect[0], text_rect[1] = x, y
        to_store = [string, text_rect, color]
        self.text_storage(to_store)
        self.screen.blit(string, text_rect)
        return text_rect

    def draw_sprite(self, image, x, y, scale=None):
        self.loaded_images[image]
        image = pygame.image.load('{}{}'.format(self.PATH, image))
        if scale is not None:
            image = pygame.transform.scale(image, scale)
        rect = image.get_rect()
        rect[0], rect[1] = x, y
        to_store = [
            image,
            rect
        ]
        self.blit_storage(to_store)
        self.screen.blit(image, rect)

    def refresh(self):
        self.screen.fill(self.BLACK)
        self.render_refresh()

    def draw_background(self, path=None):
        if path is None:
            path = 'background.png'
        self.draw_sprite(path, 0, 0)

    def frame(self):
        self.render_refresh()
        self.screen.blit(self.background, (0, 0))
        self.refresh_text()
        pygame.display.flip()

SCREEN = Screen(1400, 900)
