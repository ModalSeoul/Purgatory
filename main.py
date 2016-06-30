import sys
import pygame
from scenes.scene import MainMenu
from screen import SCREEN
from pygame.locals import *    # This needs to change.
from utils.audio import play


class Main:
    """
    Handles MainMenu & frame-by-frame.
    """

    def __init__(self):
        # Calling MainMenu object with title of 'Purgatory'
        self.main_menu = MainMenu('Purgatory')
        # List of menu entries.
        self.main_menu.menu_list = [
            'Play',
            'Options',
            'Exit'
        ]
        # Telling MainMenu instance to type our menu_list entries.
        self.main_menu.type_list()
        # Because main_menu.coords is too long.
        self.coords = self.main_menu.coords
        SCREEN.draw_sprite('ak-47.png', 5, 5)

    def reset(self, menu_entry):
        # Empty list that will contain active menu entries.
        self.inactive = []
        for entry in range(0, len(self.coords)):
            # If i == to the current menu entry.
            if entry == menu_entry:
                self.inactive.append(self.coords[entry])

    # Switches the key-circle according to currently active menu-entry.
    def switch(self, coord):
        self.reset(coord)
        for i in range(0, len(self.inactive)):
            pygame.draw.circle(
                SCREEN.screen, (255, 255, 255), (7, self.inactive[i][1] + 15), 5, 1)
            pygame.display.flip()

    # Checks main_menu.choice and calls switch() accordingly
    def check_choice(self):
        if self.main_menu.choice == 0:
            self.switch(0)
        elif self.main_menu.choice == 1:
            self.switch(1)
        elif self.main_menu.choice == 2:
            self.switch(2)

    # Shitty main function that shouldn't be in this class.
    def main(self):
        SCREEN.frame()
        self.check_choice()

# Instantiating the main object.
m = Main()


# Game loop.
while 1:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            play('keystroke.wav')
            if event.key == K_w:
                if m.main_menu.choice != 0:
                    m.main_menu.choice -= 1
            elif event.key == K_s:
                if m.main_menu.choice != 2:
                    m.main_menu.choice += 1
        m.main()
        if event.type == pygame.QUIT:
            sys.exit()
