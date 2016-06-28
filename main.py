import sys
import pygame
from scenes.scene import MainMenu
from screen import SCREEN
from pygame.locals import *
from utils.audio import play


# Main game loop
clock = pygame.time.Clock()


class Main:

    def __init__(self):
        self.main_menu = MainMenu('Purgatory')
        self.main_menu.menu_list = [
            'Play',
            'Options',
            'Exit'
        ]
        self.main_menu.type_list()
        self.coords = self.main_menu.coords
        self.inactive = []

    def reset(self, coord):
        # Cleaning inactive out to remain in range
        self.inactive = []
        for i in self.coords:
            if i != coord:
                self.inactive.append(i)

    def switch(self, coord):
        self.reset(coord)
        for i in range(0, len(self.inactive)):
            SCREEN.strings[self.coords[i]]['color'] = (255, 255, 255)
        SCREEN.strings[self.coords[coord]]['color'] = (150, 150, 150)

    def check_choice(self, ):
        if self.main_menu.choice == 0:
            self.switch(0)
        elif self.main_menu.choice == 1:
            self.switch(1)
        elif self.main_menu.choice == 2:
            self.switch(2)

    def main(self, ):
        SCREEN.frame()
        self.check_choice()

m = Main()

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
