import pygame.font
import stats

class Product():
    """вывод товара вместе с ценой"""
    def __init__(self, screen, price_num, x, y, dir, dir_inactive, stats):
        """инициализация цены"""
        self.screen = screen
        self.stats = stats
        self.image = pygame.image.load(dir)
        self.image_inactive = pygame.image.load(dir_inactive)
        self.text_color = (116, 92, 157)
        self.all_sold = False
        self.font = pygame.font.SysFont(None, 60)
        self.price_num = price_num + price_num * stats.robots_1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sold = pygame.image.load("sprites/products/sold.png")
        self.sold_rect = self.sold.get_rect()
        self.sold_rect.x = x
        self.sold_rect.y = y
        self.img_price()

    def img_price(self):
        """преобразовывает текст из счёта в изображение"""
        if not self.all_sold:
            self.price_image = self.font.render(f"{self.price_num}", True, self.text_color)
            self.price_rect = self.price_image.get_rect()
            self.price_rect.centerx = self.rect.centerx
            self.price_rect.centery = self.rect.y + 175


    def draw(self):
        """вывод счёта на экран"""
        if self.all_sold:
            self.screen.blit(self.image_inactive, self.rect)
            self.screen.blit(self.sold, self.sold_rect)
        else:
            if self.stats.score >= self.price_num:
                self.screen.blit(self.image, self.rect)
            else:
                self.screen.blit(self.image_inactive, self.rect)
            self.screen.blit(self.price_image, self.price_rect)


