import sys
import pygame
import requests


def show_map():
    response = requests.get(serv, params=params)
    if not response:
        print(response.status_code, response.reason)
        sys.exit(1)

    with open('map.png', "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load('map.png'), (0, 0))
    pygame.display.flip()


serv = "http://static-maps.yandex.ru/1.x/"

lon = "0"
lat = "0"
spn = "90"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([spn, spn]),
    "l": "sat"
}
pygame.init()
screen = pygame.display.set_mode((600, 450))
show_map()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    show_map()
pygame.quit()