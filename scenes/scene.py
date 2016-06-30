import pygame
from utils.audio import play, music
from screen import SCREEN
from time import sleep


class MainMenu:
    """
    Base scene object. Extended by all
    other scenes in the game.

    or a main menu for now.
    """

    def __init__(self, title):
        # music('bgmusic.mp3')
        self.coords = []
        self.typed_text(title, 5, 100, 72)
        self.menu_list = None
        self.choice = 0

    def type_list(self):
        if self.menu_list is None:
            print('ERROR: Set MainMenu.menu_list!')
        else:
            item_y = 175
            for item in self.menu_list:
                self.typed_text(item, 20, item_y, 52)
                self.coords.append((5, item_y))
                item_y += 45

    def typed_text(self, text, x, y, size=None):
        if size is None:
            size = 24
        foundation_string = ''
        loop_amount = len(text)
        for loop in range(0, loop_amount):
            SCREEN.frame()
            foundation_string += text[loop]
            SCREEN.draw_string(
                foundation_string,
                x,
                y,
                size,
                (255, 255, 255)
            )
            sleep(0.1)
            pygame.display.flip()
            if loop != loop_amount - 1:
                play('keystroke.wav')
            SCREEN.render_refresh()
        play('return.wav')
