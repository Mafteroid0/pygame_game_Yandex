import pygame

class MainButton():
    def __init__(self, screen, dir, x, y):
        """инициализация кнопки"""
        self.screen = screen
        self.image = pygame.image.load(dir) # загрузка спрайта врага
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.on = True

    def draw(self):
        """вывод кнопки на экран"""
        if self.on:
            self.screen.blit(self.image, self.rect)


