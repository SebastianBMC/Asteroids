import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    createDisplay()


def createDisplay():
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()