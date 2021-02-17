import os
import sys

import pygame
import requests

api_server = "http://static-maps.yandex.ru/1.x/"
lon = "37.530887"
lat = "55.703118"
delta = "0.002"
counter = 0
params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": 'map'
}
pygame.init()
screen = pygame.display.set_mode((720, 450))
width = screen.get_width()
height = screen.get_height()
running = True
# button
color = (255, 255, 255)
button = pygame.Rect(610, 100, 100, 50)
sfont = pygame.font.SysFont('Corbel', 25)
while running:  # главный игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # обработка остальных событий
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                counter += 1
                counter = counter % 3
        if counter == 0:
            params['l'] = 'map'
            text = sfont.render('схема', True, color)
        elif counter == 1:
            params['l'] = 'sat'
            text = sfont.render('спутник', True, color)
        else:
            params['l'] = 'sat,skl'
            text = sfont.render('гибрид', True, color)
        response = requests.get(api_server, params=params)
        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        else:
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            screen.blit(pygame.image.load(map_file), (0, 0))
        os.remove(map_file)
        pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
        screen.blit(text, (610, 100))
        pygame.display.flip()
