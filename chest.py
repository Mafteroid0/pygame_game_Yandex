import pygame

class Chest():
    def __init__(self, screen, dir, dir_closed, x, y, place, opened, stats):
        """инициализация обьекта"""
        self.opened = opened
        self.screen = screen
        self.image = pygame.image.load(dir) # загрузка спрайта обьекта
        self.image_closed = pygame.image.load(dir_closed)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.stats = stats
        self.place = place

    def draw(self):
        """вывод Обьекта на экран"""
        if self.stats.current_room == self.place:
            if self.opened:
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
                self.screen.blit(self.image, self.rect)
            else:
                self.rect = self.image_closed.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
                self.screen.blit(self.image_closed, self.rect)


