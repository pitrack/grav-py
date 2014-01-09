import pygame, sys, math
import planet, util, level


WIDTH = 1000
HEIGHT = 600
ZERO = (0,0)


def main():
    screen = initGame((WIDTH, HEIGHT))
    lvl = 0
    while True:
        nextStage = run(screen, lvl)
        if nextStage == 1:
            if lvl < len(level.list)-1:
                lvl = lvl + 1
        if nextStage == -1:
            if lvl > 0:
                lvl = lvl - 1

def initGame(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(level.BG)
    pygame.display.update()
    return screen

def check_exit(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

def run(screen, lvl):
    fps = 60
    ship = planet.Planet(level.list[lvl].start, (0, 0), (0, 0), 
                         (255,255,255), 3,  0.01)
    crash = False
    waitForInput = True
    draw(ship, lvl, screen)
    while(True):
        events = pygame.event.get()
        check_exit(events)
        if waitForInput:
            (success, val) = processInput(ship.pos, events)
            if success:
                ship.accelerate(val)
                print ship.vel
                waitForInput = False
        else:
            (success, val) = processInput(ship.pos, events)
            if success:
                return 0
            win = step(crash, ship, lvl, screen, fps)
            if win == -1:
                crash = True
                return 0
            elif win == 1:
                return 1

def step(crash, ship, lvl, screen, fps):
    clock = pygame.time.Clock()
    frameTime = 1.0/fps
    if not crash:
        flicked = ship.flick(level.list[lvl], frameTime, 400)
        if (flicked == -1 or 
            ship.pos[0] < -WIDTH/2 or ship.pos[0] > 3*WIDTH/2 
            or ship.pos[1] < -HEIGHT/2 or ship.pos[1] > 3*HEIGHT/2):
            draw(ship, lvl, screen)
            endMessage(screen, -1)
            return -1
        else:
            draw(ship, lvl, screen)
            if level.list[lvl].inGoal(ship.pos):
                endMessage(screen, 1)
                return 1
        passed = clock.tick(fps)
        print ('%s %s') % (passed, ship.pos)
    return 0


def processInput(pos,events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            return (True, ((x-pos[0], y-pos[1]), (0,0)))
    else:
        return (False, ((0,0), (0,0)))

def draw(ship, lvl, screen):
    level.list[lvl].drawLevel(screen)
    ship.draw(screen)
    pygame.display.update()

def endMessage(screen, message):
    if message == -1:
        print "You crashed\n"
    elif message == 1:
        print "You won\n"
    while True:
        events = pygame.event.get()
        check_exit(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
    return False # shouldn't reach here


main()

