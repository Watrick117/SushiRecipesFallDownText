#!/usr/bin/python3
"""Patrick Woltman
Proff of concept for Matrix Font Rain Effect.
*** I want Multi monitor support

Sourses used:
    https://www.reddit.com/r/fonts/comments/391xhz/matrix_font/
    https://github.com/ssg/ssgmatrix
    https://en.wikipedia.org/wiki/Matrix_digital_rain

Color codes:
    https://www.schemecolor.com/matrix-code-green.php#:~:text=The%20Matrix%20Code%20Green%20Color,)%20and%20Malachite%20(%2300FF41).

Font:
    https://www.dafont.com/matrix-code-nfi.font

    Usable chars:
        1234567890abcdefghijklmnopqrstuvwxyz$+-*/÷=%‰"'#&_(),.;:?!|{}<>[]^~

Example:
    https://www.youtube.com/watch?v=kqUR3KtWbTk&ab_channel=thebiggysmith
    https://i.imgur.com/dVQZlnh.png
"""

#import asyncio
import argparse
import pygame
import random
from datetime import datetime

# TODO: ADD async io
# TODO: upload to github
# TODO: check that this runs on linux and mac

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-s', '--size', action='store', type=int, nargs=2,
    help="Takes in two arguments that represent the size of the screen.")

# Sanity checks user inputs
args = my_parser.parse_args()

for x in vars(args):
    print(getattr(args, x)) # TODO: add fancy print

if args.size is None:
    width = 1920
    height = 1080
else:
    width = args.size[0]
    height = args.size[1]

pygame.init()
pygame.font.init()

fontsize = 16 # might need to be set manually for continuity
font = pygame.font.Font("matrix code nfi.ttf", fontsize)

width10 = int(width/10)
height10 = int(height/10)

print(height10)

size = (width, height)

screen = pygame.display.set_mode(size)

framedark = pygame.Surface(size,)
framegreen = pygame.Surface(size)
framewhite = pygame.Surface(size)

clock = pygame.time.Clock()

#Create a displace surface object
DISPLAYSURF = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

random.seed(datetime.now())

"""
gly = glyph
col = color
mmt = momentum
"""

gly, col, mmt = (0, 1, 2)

rows, cols = (width10 , height10)

black = (13, 2, 8) # this is VampireBlack
#blackB = (11, 2, 6)
#vampireblackB = (8, 2, 3) # Not in use
raisinblack = (10, 2, 5)

darkgreen = (0, 59, 0)
darkgreenB = (0, 57, 0) # TODO: Not using
islamicgreen = (0, 143, 17)
malachite = (0, 255, 65)

murple = (128,0,128)

white = (255,255,255)

orange = (255,131,0)

framegreen.set_colorkey(black)

arr = [[[0 for k in range(3)] for j in range(height)] for i in range(rows)]

for x in range(0, rows):
    for y in range(0, height):
        arr[x][y][col] = black

framedark.fill(black)
#framedark.fill(orange)

def fade(tuplearray): #TODO: add Generators
    # TODO: add doc string
    # malachite = (0, 255, 65)
    # blackB = (8, 2, 3)
    #                                                (0 , 23, 2)))
    temp = tuple(map(lambda i, j: i - j, tuplearray, (0 , 25, 5)))
    if temp[1] <= 2 or temp[2] <= 3:
        return (black)
    return temp

def ranChar():
    # TODO: add doc string
    # '1234567890abcdefghijklmnopqrstuvwxyz$+-*/÷=%‰"\'#&_(),.;:?!|{}<>[]^~'
    chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c',
     'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '$', '+', '-', '*', '/', '÷',
       '=', '%', '‰', '"','\'', '#', '&', '_', '(', ')', ',', '.', ';', ':',
        '?', '!', '|', '{', '}', '<', '>', '[', ']', '^', '~']

    return chars[random.randint(0, len(chars)-1)]

def gameLoop():
    # TODO: add doc string
    mainLoop = True

    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESC Key Pressed")
                    mainLoop = False

        framegreen = pygame.Surface(size)
        framegreen.set_colorkey(black)
        framegreen.fill(black)

        framewhite = pygame.Surface(size)
        framewhite.set_colorkey(black)
        framewhite.fill(black)

        # prints array to screen
        for x in range(0, width10 - 1):
            for y in range(0, height - 1):
                
                # main background ---------------------------------------------
                if arr[x][y][col] != black and arr[x][y][col] != white:

                    txt = font.render(str(arr[x][y][gly]), True, arr[x][y][col])

                    temp = random.randint(1 , 100)
                    if temp == 1: # flips the char
                        txt = pygame.transform.flip(txt, False, True)
                        framegreen.blit(txt , (x*10, y))
                    elif temp == 50: # shrinks the char
                        txt = pygame.transform.scale(txt,(15,15))
                        framegreen.blit(txt , (x*10-2, y))
                    else:
                        framegreen.blit(txt , (x*10, y))
                if arr[x][y][col] != black:
                    txt = font.render(str(arr[x][y][gly]), True, arr[x][y][col])
                    framewhite.blit(txt , (x*10, y))
        
        screen.blit(framedark, (0,0))

        # TODO: finsih gaussian blur

        #framegreen = pygame.surfarray.make_surface(gaussian_filter(pygame.surfarray.array3d(framegreen), sigma=0, truncate=3.0)

        #filtered_data = scipy.ndimage.filters.gaussian_filter(data, sigma=s, truncate=t)

        #framegreen = pygame.surfarray.make_surface(gaussian_filter1d(pygame.surfarray.array3d(framegreen), sigma=1, axis=-1, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0))

        screen.blit(framegreen, (0,0))

        screen.blit(framewhite, (0,0))

        pygame.display.flip()

        # calculations TODO: clean this up / refactor / BIG O notation
        for x in range(width10 - 1, -1, -1):
            for y in range(height - 1, -1, -1):
                if arr[x][y][col] == white:
                    #next x, y + 1
                    if y <= height-arr[x][y][mmt]-2:
                        arr[x][y + arr[x][y][mmt]][gly] = arr[x][y][gly]
                        arr[x][y + arr[x][y][mmt]][col] = white
                        arr[x][y + arr[x][y][mmt]][mmt] = arr[x][y][mmt]

                    #current x, y
                    arr[x][y][gly] = ranChar()
                    arr[x][y][col] = malachite
                    arr[x][y][mmt] = 0

                elif arr[x][y][col] == malachite:
                    #next x, y + 1
                    if y <= height-12:
                        arr[x][y + 1][col] = fade(arr[x][y+1][col])
                        arr[x][y + arr[x][y][mmt]][mmt] = arr[x][y][mmt]

                    #current x, y
                    arr[x][y][col] = fade(arr[x][y][col])
                    if random.randint(1 , 20) == 20:
                        arr[x][y][gly] = ranChar()
                    else:
                        arr[x][y][gly] = arr[x][y][gly]

                elif arr[x][y][col] < malachite:
                    #next x, y + 1

                    #current x, y
                    if random.randint(1 , 3) == 3:
                        arr[x][y][col] = fade(arr[x][y][col])
        
        if random.randint(1 , 2) == 2:
            randomRunTime = random.randint(1 , int(width10/40))
            while randomRunTime < int(width10/40):
                temp = random.randint(1 , width10 - 1)
                arr[temp][1][col] = white
                arr[temp][1][gly] = ranChar()
                arr[temp][1][mmt] = random.randint(11 , 15)
                randomRunTime += 1
            
            randomRunTime = 3

        clock.tick(60)

def main():
    gameLoop()

main()

pygame.quit()

