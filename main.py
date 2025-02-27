import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    createDisplay(player)


def createDisplay(player):
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    FPS = pygame.time.Clock()

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = FPS.tick(60) / 1000


if __name__ == "__main__":
    main()