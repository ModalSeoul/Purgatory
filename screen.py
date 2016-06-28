import pygame
from utils.audio import play, music
from time import sleep


class Screen:
    """
    Screen object. Handles all data/objects
    related to the screen.
    """

    def __init__(self, x, y):
        pygame.init()
        self.sprites = {}
        self.strings = {}
        self.PATH = 'images/'
        self.size = self.x, self.y = x, y
        self.screen = pygame.display.set_mode(self.size)

        self.WHITE = (255, 255, 255)
        self.D_WHITE = (200, 200, 200)
        self.BLACK = (0, 0, 0)

    def blit_storage(self, image, x, y, scale=None):
        img = image.split('.')
        if not self.sprites.get(img[0]):
            self.sprites[img[0]] = {
                'image': img[0],
                'x': x,
                'y': y,
                'ext': img[-1],
                'scale': None
            }
            if scale is not None:
                self.sprites[img[0]]['scale'] = scale
        else:
            if self.sprites[img[0]]['x'] != x:
                self.sprites[img[0]]['x'] = x
            if self.sprites[img[0]]['y'] != y:
                self.sprites[img[0]]['y'] = y

    def text_storage(self, text, x, y, size, color):
        ex, why = str(x), str(y)
        self.strings['{}{}'.format(ex, why)] = {
            'text': text,
            'x': x,
            'y': y,
            'size': size,
            'color': color
        }

    def refresh_text(self):
        for string in self.strings:
            string = self.strings[string]
            self.draw_string(
                string['text'],
                string['x'],
                string['y'],
                string['size'],
                string['color']
            )

    def render_refresh(self):
        for sprite in self.sprites:
            short_sprite = self.sprites[sprite]
            x, y = short_sprite['x'], short_sprite['y']
            if short_sprite['scale'] is not None:
                scale = short_sprite['scale']
                self.draw_sprite(
                    '{}.{}'.format(short_sprite['image'],
                                   short_sprite['ext']), x, y, scale)
            else:
                self.draw_sprite(
                    '{}.{}'.format(short_sprite['image'],
                                   short_sprite['ext']), x, y)

    def draw_string(self, text, x, y, size=None, color=None):
        if size is None:
            size = 24
        if color is None:
            color = self.WHITE

        self.text_storage(text, x, y, size, color)
        font = pygame.font.Font('ostrich-regular.ttf', size)
        string = font.render(text, True, color)
        text_rect = string.get_rect()
        text_rect[0], text_rect[1] = x, y
        self.screen.blit(string, text_rect)
        return text_rect

    def draw_sprite(self, image, x, y, scale=None):
        self.blit_storage(image, x, y, scale)
        self.image = pygame.image.load('{}{}'.format(self.PATH, image))
        if scale is not None:
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = (x, y, 32, 32)
        self.screen.blit(self.image, self.rect)

    def refresh(self):
        self.screen.fill(self.BLACK)
        self.render_refresh()

    def draw_background(self, path=None):
        if path is None:
            path = 'background.png'
        self.draw_sprite(path, 0, 0)

    def frame(self):
        self.render_refresh()
        self.draw_background('menu_bg.png')
        self.refresh_text()
        pygame.display.flip()

SCREEN = Screen(1400, 900)
