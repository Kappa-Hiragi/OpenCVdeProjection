import sys
import pygame
from pygame.locals import *
def main(x,y):
    pygame.init()
    screen = pygame.display.set_mode((2032, 1143),FULLSCREEN)
    pygame.display.set_caption("image")
    img1 = pygame.image.load("test.png")
    px=x
    py=y
    screen.blit(img1,(px,py))
    pygame.display.update()
if __name__ == "__main__":
    main()