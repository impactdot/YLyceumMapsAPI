import sys
import pygame
import requests


def show_map():
    response = requests.get(serv, params=params)
    if not response:
        print(response.status_code, response.reason)
        sys.exit(1)

    with open('map.png', "wb") as f:
        f.write(response.content)
    screen.blit(pygame.image.load('map.png'), (0, 0))
    pygame.display.flip()


serv = "http://static-maps.yandex.ru/1.x/"

lon = "0"
lat = "0"
spn = "80"

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
        if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_PAGEUP:
                spn = str(float(params["spn"].split(',')[0]) * 0.5)
                if float(spn) >= 0.001 and float(spn) <= 80:
                    params["spn"] = ",".join([spn, spn])
                    show_map()
            if event.key == pygame.K_PAGEDOWN:
                spn = str(float(params["spn"].split(',')[0]) * 2)
                if float(spn) >= 0.001 and float(spn) <= 80:
                    params["spn"] = ",".join([spn, spn])
                    show_map()
pygame.quit()