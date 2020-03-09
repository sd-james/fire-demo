import pygame
from pygame.constants import DOUBLEBUF, K_q
import random

width = 300
height = 100
zoom = 3

screen = pygame.Surface((width, height))


# set the pixel value at a particular location. This is a special set to make things look more fire-like
def draw_pixel(x, y, value):
    red = value
    green = value * 2 // 3
    if green > 70:
        green = green * 2 // 3
    blue = green
    if blue > 60:
        blue = blue // 3
    pixel = (red, green, blue)
    screen.set_at((x, y), pixel)


# gets the intensity of the pixel at position x,y on the screen. In particular returns the RED components
def get_pixel(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0
    pixel = tuple(screen.get_at((x, y)))
    return pixel[0]


# Draw the fire.
def draw_fire():
    for x in range(width):
        draw_pixel(x, height - 1, random.randint(0, 255))
    for x in range(width):
        for y in range(height - 1):
            value = (get_pixel(x, y) + get_pixel(x + 1, y + 1) + get_pixel(x, y + 1) + get_pixel(x - 1, y + 1)) // 4 - 1
            if value < 0:
                value = 0
            draw_pixel(x, y, value)


if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()
    pygame.key.set_repeat()

    display = pygame.display.set_mode((width * zoom, height * zoom + 40), DOUBLEBUF)

    while True:
        clock.tick(50)
        display.fill((0, 0, 0))

        # draw the fire
        draw_fire()

        # draw the screen
        pygame.transform.scale(screen, (display.get_width(), display.get_height()), display)
        pygame.display.flip()

        # check if user quit by pressing Q
        inpt = pygame.key.get_pressed()
        if inpt[K_q]:
            break
        pygame.event.clear()
    pygame.display.quit()
