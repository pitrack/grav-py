import pygame, sys, math
import planet, util

BG = (134, 100, 79)
WIDTH = 1000
HEIGHT = 600
ZERO = (0,0)
level0 = planet.Level(BG,
                      [planet.Planet((300, 300), ZERO, ZERO, 
                                     (255,255,120), 50, 300), 
                       planet.Planet((500, 300), ZERO, ZERO,
                                     (255, 120, 0), 30, 60),
                       planet.Planet((700, 300), ZERO, ZERO,
                                     (255, 255, 120), 50, 300)],
                      0, pygame.Rect(800, 500, 30, 30))

def main():
    screen = initGame((WIDTH, HEIGHT))
    while run(screen) == 0:
        pass

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
    fps = 60
    escape = math.sqrt(planet.GConstant*4000/100)
    ship = planet.Planet((200, 150), (0, 0), (0, 0), (255,255,255), 3, 
                         0.01)
    crash = False
    waitForInput = True
    draw(ship, screen)
    while(True):
        check_exit()
        if waitForInput:
            (success, val) = processInput(ship.pos)
            if success:
                ship.accelerate(val)
                print ship.vel
                waitForInput = False
        elif step(crash, ship, screen, fps):
            crash = True
            return 0
            
def step(crash, ship, screen, fps):
    clock = pygame.time.Clock()
    frameTime = 1.0/fps
    if not crash:
        flicked = ship.flick(level0, frameTime, 400)
        if (flicked == -1 or 
            ship.pos[0] < -WIDTH/2 or ship.pos[0] > 3*WIDTH/2 
            or ship.pos[1] < -HEIGHT/2 or ship.pos[1] > 3*HEIGHT/2):
            draw(ship, screen)
            crashMessage(screen)
            return True
        else:
            draw(ship, screen)
            if level0.inGoal(ship.pos):
                winMessage(screen)
                return True
        passed = clock.tick(fps)
        print ('%s %s') % (passed, ship.pos)
      


def processInput(pos):
    if pygame.mouse.get_pressed()[0]:
        (x, y) = pygame.mouse.get_pos()
        return (True, ((x-pos[0], y-pos[1]), (0,0)))
    else:
        return (False, ((0,0), (0,0)))

def draw(ship, screen):
    level0.drawLevel(screen)
    ship.draw(screen)
    pygame.display.update()

def crashMessage(screen):
    print "You crashed"
    raw_input("Continue? ")
    return True

def winMessage(screen):
    print "You wined"
    raw_input("Continue? ")
    return True


main()

