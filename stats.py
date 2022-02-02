import pygame
from pytmx.util_pygame import load_pygame
class Stats():
    """отслеживание статистики"""

    def __init__(self, screen):
        """инициализация статистики"""
        # self.run_game = True
        self.screen = screen
        with open("score.txt", "r") as f:
            self.score = int(f.readline())
            self.deg = int(f.readline())
            if self.deg <= 0:
                self.deg = 1
            self.robots_1 = int(f.readline())
            self.robots_lvl = int(f.readline())
            if self.robots_lvl <= 0:
                self.robots_lvl = 1
            self.chests_opened = int(f.readline())

        self.tmxdata = load_pygame("loc2.tmx")

        self.maingame = True
        self.shop = False
        self.current_room = 0
        self.bg = pygame.image.load("sprites/backgrounds/bg_1.png")
        self.bg_rect = self.bg.get_rect()
        self.coming_pos = 5 # 0 - right; 1 - left; 2 - up; 3 - bottom; 4 - center (default)

    def render_room(self, player, mainbutton):
        if self.current_room == 0:
            self.tmxdata = load_pygame("loc2.tmx")
            # self.bg = pygame.image.load("sprites/backgrounds/bg_0.png")
            # self.bg_rect = self.bg.get_rect()
            # self.screen.blit(self.bg, self.bg_rect)
            # player.draw()
        elif self.current_room == 1:
            self.tmxdata = load_pygame("loc4.tmx")
            # self.bg = pygame.image.load("sprites/backgrounds/bg_1.png")
            # self.bg_rect = self.bg.get_rect()
            # self.screen.blit(self.bg, self.bg_rect)
            # player.draw()

        elif self.current_room == 2:
            self.tmxdata = load_pygame("loc5.tmx")

        elif self.current_room == 3:
            self.tmxdata = load_pygame("loc3.tmx")
