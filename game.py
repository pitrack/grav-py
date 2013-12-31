import pygame, sys
import planet

BG = (0, 125, 125)
ZERO = (0,0)
level0 = planet.Level(BG,
                      [planet.Planet((200, 300), ZERO, ZERO, 
                                     (255,255,120), 100), 
                       planet.Planet((500, 300), ZERO, ZERO,
                                     (255, 120, 0), 50),
                       planet.Planet((800, 300), ZERO, ZERO,
                                     (255, 255, 120), 100)],
                      0)

def main():
    screen = initGame((1000, 600))
    run(screen)

def initGame(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(BG)
    pygame.display.update()
    return screen

def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

def run(screen):
    clock = pygame.time.Clock()
    fps = 60

    ship = planet.Planet((200, 200), (100, 0), (-10, -1), (255,255,255), 5)
    while(True):
        check_exit()
        ship.flick(level0, 1.0/fps)
        level0.drawLevel(screen)
        ship.draw(screen)
        pygame.display.update()
        passed = clock.tick(fps)
        

main()

