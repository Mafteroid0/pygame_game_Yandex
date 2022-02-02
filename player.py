import pygame

class Player():
    """Игрок"""

    def __init__(self, screen, dir, mainbutton):
        """инициализация игрока"""
        self.screen = screen
        self.image = pygame.image.load(dir)  # загрузка спрайта врага
        self.rect = self.image.get_rect()  # новый прямоугольник из спрайта
        self.screen_rect = screen.get_rect()  # новый прямоугольник из окна
        self.rect.centerx = self.screen_rect.centerx  # приравнивание пушки к середине окна по оси x
        self.rect.centery = self.screen_rect.centery  # приравнивание пушки к середине окна по оси y
        self.center_x = float(self.rect.centerx)  # сделать пиксели вещественным числом
        self.center_y = float(self.rect.centery)  # сделать пиксели вещественным числом
        self.mainbutton = mainbutton
        self.inv_rect = pygame.Rect((0, 0), (20, 20))


        self.stay = pygame.image.load("sprites/walks/down_1_1.png")
        self.moveRight = [pygame.image.load("sprites/walks/right_1.png"),
                          pygame.image.load("sprites/walks/right_2.png"),
                          pygame.image.load("sprites/walks/right_3.png"),
                          pygame.image.load("sprites/walks/right_4.png"),
                          pygame.image.load("sprites/walks/right_5.png"),
                          pygame.image.load("sprites/walks/right_6.png"),
                          pygame.image.load("sprites/walks/right_7.png"),
                          pygame.image.load("sprites/walks/right_8.png"), ]
        self.moveLeft = [pygame.image.load("sprites/walks/left_1.png"),
                          pygame.image.load("sprites/walks/left_2.png"),
                          pygame.image.load("sprites/walks/left_3.png"),
                          pygame.image.load("sprites/walks/left_4.png"),
                          pygame.image.load("sprites/walks/left_5.png"),
                          pygame.image.load("sprites/walks/left_6.png"),
                          pygame.image.load("sprites/walks/left_7.png"),
                          pygame.image.load("sprites/walks/left_8.png"), ]
        self.moveUp = [pygame.image.load("sprites/walks/up_1.png"),
                         pygame.image.load("sprites/walks/up_2.png"),
                         pygame.image.load("sprites/walks/up_3.png"),
                         pygame.image.load("sprites/walks/up_4.png"),
                         pygame.image.load("sprites/walks/up_5.png"),
                         pygame.image.load("sprites/walks/up_6.png")]
        self.moveDown = [pygame.image.load("sprites/walks/down_1.png"),
                       pygame.image.load("sprites/walks/down_2.png"),
                       pygame.image.load("sprites/walks/down_3.png"),
                       pygame.image.load("sprites/walks/down_4.png"),
                       pygame.image.load("sprites/walks/down_5.png"),]

        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.animcount = 0

    def update_player(self, stats):
        """обновление позиции пушки"""

        if self.move_right:
            if self.center_x <= self.screen_rect.right:
                self.center_x += 5.5
            if stats.current_room == 1 and self.center_x >= self.screen_rect.right:
                stats.current_room = 0
                self.center_x = 0
                self.center_y = 272
                stats.render_room(self, self.mainbutton)
            self.image = self.moveRight[self.animcount // 3]
            self.rect = self.image.get_rect()
            self.draw()
            self.animcount += 1



        elif self.move_left:
            if self.center_x > self.screen_rect.left:
                if stats.current_room == 1:
                    if self.center_x > self.screen_rect.left + 530:
                        self.center_x -= 5.5
                else:
                    self.center_x -= 5.5
            if stats.current_room == 0 and self.center_x <= self.screen_rect.left and stats.chests_opened >= 1:
                stats.current_room = 1
                self.center_x = 960
                self.center_y = 272
                stats.render_room(self, self.mainbutton)

            self.image = self.moveLeft[self.animcount // 3]
            self.rect = self.image.get_rect()
            self.animcount += 1


        elif self.move_up:

            if self.center_y >= self.screen_rect.top:
                self.center_y -= 5.5
            if stats.current_room == 0 and self.center_y <= self.screen_rect.top and stats.chests_opened >= 2:
                stats.current_room = 2
                self.center_x = 480
                self.center_y = 544
                stats.render_room(self, self.mainbutton)
            if stats.current_room == 3 and self.center_y <= self.screen_rect.top:
                stats.current_room = 0
                self.center_x = 480
                self.center_y = 544
                stats.render_room(self, self.mainbutton)

            self.image = self.moveUp[self.animcount // 5]
            self.rect = self.image.get_rect()
            self.draw()
            self.animcount += 1


        elif self.move_down:
            if self.center_y < self.screen_rect.bottom:
                self.center_y += 5.5
            if stats.current_room == 2 and self.center_y >= self.screen_rect.bottom:
                stats.current_room = 0
                self.center_x = 480
                self.center_y = 0
                stats.render_room(self, self.mainbutton)

            elif stats.current_room == 0 and self.center_y >= self.screen_rect.bottom and stats.chests_opened >= 3:
                stats.current_room = 3
                self.center_x = 480
                self.center_y = 0
                stats.render_room(self, self.mainbutton)



            self.image = self.moveDown[self.animcount // 5]
            self.rect = self.image.get_rect()
            self.draw()
            self.animcount += 1

        else:
            self.image = self.stay
            self.rect = self.image.get_rect()
            self.draw()

        if self.animcount >= 24:
            self.animcount = 0


        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def draw(self):
        """вывод игрока на экран"""
        self.screen.blit(self.image, self.rect)
