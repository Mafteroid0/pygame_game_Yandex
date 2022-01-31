import pygame
from pygame.sprite import Group
from stats import Stats
import controls
from mainbutton import MainButton
from scores import Scores
from player import Player
from unclickable_object import Unclickable_object
from product import Product
from pytmx.util_pygame import load_pygame

def run():
    pygame.init()
    FPS = 40

    SCREEN_SIZE = (960, 544)
    screen = pygame.display.set_mode(SCREEN_SIZE)  # размер окна
    pygame.display.set_caption("Кликер")  # заголовок окна
    bg_color = (126, 242, 116)  # создание цвета заднего фона
    shop_bg_color = (116, 242, 238)  # создание цвета заднего фона
    stats = Stats(screen)
    world_offset = [0, 0]
    tmxdata = stats.tmxdata
    mainbutton = MainButton(screen, "sprites/main_button.png", 0, 445)
    cart = MainButton(screen, "sprites/cart.png", 0, 0)
    leave = MainButton(screen, "sprites/leave.png", 0, 0)
    tovar = Product(screen, 20, 75, 135, "sprites/products/cursor.png", "sprites/products/bwcursor.png", stats)
    tovar1 = Product(screen, 150, 275, 135, "sprites/products/addrobot.png", "sprites/products/bwaddrobot.png", stats)
    tovar2 = Product(screen, 500, 475, 135, "sprites/products/upgraderobot.png", "sprites/products/bwupgraderobot.png", stats)
    tovar3 = Product(screen, 1000, 675, 135, "sprites/products/chestt.png", "sprites/products/bwchestt.png", stats)
    player = Player(screen, "sprites/character.png", mainbutton)
    scores = Scores(screen, stats)
    # stats.render_room(player, mainbutton)
    robot_helper = Unclickable_object(screen, [
        "sprites/robots/robo_1.png",
        "sprites/robots/robo_2.png",
        "sprites/robots/robo_3.png",
        "sprites/robots/robo_4.png"], 750, 200, 0, stats, scores, 1)
    robot_helper1 = Unclickable_object(screen, [
        "sprites/robots/robo_1.png",
        "sprites/robots/robo_2.png",
        "sprites/robots/robo_3.png",
        "sprites/robots/robo_4.png"], 800, 300, 1, stats, scores, 1)
    robot_helper2 = Unclickable_object(screen, [
        "sprites/robots/robo_1.png",
        "sprites/robots/robo_2.png",
        "sprites/robots/robo_3.png",
        "sprites/robots/robo_4.png"], 200, 400, 2, stats, scores, 1)



    while True:
        pygame.time.delay(1000 // FPS)
        tmxdata = stats.tmxdata
        controls.events(screen, mainbutton, stats, scores, cart, tovar, leave, player, robot_helper, tovar1, tovar2, tovar3, robot_helper1, robot_helper2)
        controls.update(bg_color, screen, mainbutton, scores, stats, cart, tovar, leave, player, shop_bg_color, robot_helper, tovar1, tmxdata, world_offset, tovar2, tovar3, robot_helper1, robot_helper2)
        player.update_player(stats)


run()