import pygame
import sys
import datetime
from pytmx.util_pygame import load_pygame

def events(screen, mainbutton, stats, scores, cart, tovar, leave, player, robot_helper, tovar1, tovar2, tovar3, robot_helper1, robot_helper2):
    """Обработчик событий"""
    for event in pygame.event.get():  # получение всех событий (действий) пользователя
        if event.type == pygame.QUIT:  # если пользователь закрыл игру (нажал на крестик)
            with open("score.txt", "w") as f:
                f.write(str(stats.score))
                f.write("\n")
                f.write(str(stats.deg))
                f.write("\n")
                f.write(str(stats.robots_1))
                f.write("\n")
                f.write(str(stats.robots_lvl))
            sys.exit()  # окно закрывается

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position


            if mainbutton.rect.collidepoint(mouse_pos) and stats.maingame and mainbutton.on:
                stats.score += stats.deg
                scores.img_score()
                scores.show_score()

            elif cart.rect.collidepoint(mouse_pos) and not stats.shop:
                stats.maingame = False
                stats.shop = True

            elif leave.rect.collidepoint(mouse_pos) and stats.shop:
                stats.maingame = True
                stats.shop = False

            elif tovar.rect.collidepoint(mouse_pos):
                if stats.score >= tovar.price_num and stats.shop:
                    stats.score -= tovar.price_num
                    stats.deg += 1
                    tovar.price_num = stats.deg * 20 * 3
                    scores.img_score()
                    scores.show_score()
                    tovar.img_price()
                    tovar.draw()

            elif tovar1.rect.collidepoint(mouse_pos):
                if stats.score >= tovar1.price_num and stats.shop and stats.robots_1 < 3:
                    stats.score -= tovar1.price_num
                    stats.robots_1 += 1
                    tovar1.price_num = (stats.robots_1 ** 5 + 2) * 750
                    robot_helper.on = True

                    scores.img_score()
                    scores.show_score()
                    tovar1.img_price()
                    tovar1.draw()

            elif tovar2.rect.collidepoint(mouse_pos):
                if stats.score >= tovar2.price_num and stats.shop:
                    stats.score -= tovar2.price_num
                    stats.robots_lvl += 1
                    tovar2.price_num = (stats.robots_lvl ** 2 + 2) * 650
                    robot_helper.on = True

                    scores.img_score()
                    scores.show_score()
                    tovar2.img_price()
                    tovar2.draw()

            elif tovar3.rect.collidepoint(mouse_pos):
                if stats.score >= tovar3.price_num and stats.shop:
                    stats.score -= tovar3.price_num
                    stats.robots_1 += 1
                    tovar3.price_num *= 2
                    robot_helper.on = True

                    scores.img_score()
                    scores.show_score()
                    tovar3.img_price()
                    tovar3.draw()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                player.move_right = True
            elif event.key == pygame.K_a:  # нажатая клавиша - A
                player.move_left = True
            elif event.key == pygame.K_w:
                player.move_up = True
            elif event.key == pygame.K_s:  # нажатая клавиша - A
                player.move_down = True
            player.update_player(stats)



        elif event.type == pygame.KEYUP:  # если отжата клавиша
            if event.key == pygame.K_d:  # отжатая клавиша - D
                player.move_right = False
            elif event.key == pygame.K_a:  # отжатая клавиша - A
                player.move_left = False
            elif event.key == pygame.K_w:
                player.move_up = False
            elif event.key == pygame.K_s:  # нажатая клавиша - A
                player.move_down = False
            player.update_player(stats)

def blit_all_tiles(screen, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            x_pixel = tile[0] * 16 + world_offset[0]
            y_pixel = tile[1] * 16 + world_offset[1]

            screen.blit(tile[2], (x_pixel, y_pixel))


def update(bg_color, screen, mainbutton, scores, stats, cart, tovar, leave, player, shop_bg_color, robot_helper, tovar1, tmxdata, world_offset, tovar2, tovar3, robot_helper1, robot_helper2):
    """Обновление экрана"""
    if stats.maingame:
        # stats.render_room(player)
        blit_all_tiles(screen, tmxdata, world_offset)
        player.draw()
        mainbutton.draw()
        cart.draw()

        scores.show_score()
        if stats.robots_1 >= 1:
            robot_helper.draw()
        if stats.robots_1 >= 2:
            robot_helper1.draw()
        if stats.robots_1 >= 3:
            robot_helper2.draw()
    elif stats.shop:
        screen.fill(shop_bg_color)
        tovar.draw()
        tovar1.draw()
        tovar2.draw()
        tovar3.draw()
        leave.draw()
        scores.show_score()
    pygame.display.flip()
