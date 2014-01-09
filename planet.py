import pygame
import util

GConstant = 20000

class Crash(Exception):
    def __init__(self, crashed):
        self.crashed = crashed


class Planet:
    # init: initializes physical aspects and color
    # pos (px), vel (px/s), acc(px/s^2) have x and y components.
    def __init__(self, pos, vel, acc, color, size, mass = 0.0):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.color = color
        self.size = size
        self.mass = mass
        
    def accelerate(self, vecs):
        self.vel = vecs[0]
        self.acc = vecs[1]


    # draw: draws planet onto the screen        
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, 
                     util.int2(self.pos) , int(self.size), 0)

    # flick: animates by one frame by recalculating pos, vel, acc
    # performs integration by recalculating precision-1 times since
    # it appears to naturally overestimate.
    # todo: take average of before and after since that might be 
    # easier/more accurate and faster
    def flick(self, level, time, precision):
        time = time/precision
        for _ in xrange(0, precision-1):
            (xp0, yp0) = self.pos
            (xv0, yv0) = self.vel
            (xa0, ya0) = self.acc
            
            tupleList = map(self.calcAcc, level.existing)
            (good, self.acc) = reduce(lambda (a, x),(b,y):
                                 ((a and b), (x[0] + y[0], x[1]+y[1]))
                          , tupleList, (True, (0,0)))
            if not good:
                return -1
            self.vel = (xv0 + xa0*time, yv0+ya0*time)
            self.pos = (xp0 + xv0*time, yp0+yv0*time)
        return 0
           


    # calcAcc: self * planet -> (bool, (float, float))
    # calcAcc(x,y) calculates the acceleration of x due to y.
    # helper function
    def calcAcc(self, y):
        radius = util.distance(self.pos, y.pos)
        # to be fixed: calculate mass based on density
        if radius < y.size + self.size:
            return (False,(0,0))
        force = GConstant*(self.mass*y.mass)/(radius**2)
        unit = ((y.pos[0]-self.pos[0])/radius, (y.pos[1]-self.pos[1])/radius)
        return (True, (force*unit[0]/self.mass, force*unit[1]/self.mass))
        


    # printPlanet: debugging
    def printPlanet(self):
        print ("pos %s size %s \n" %  (self.pos, self.size))
        
        
        
class Level:
    # init: inputs are background color, planet list, int
    # initializes variables
    def __init__(self, color, existing, num, start, goal):
        self.color = color
        self.existing = existing
        self.num = num
        self.start = start
        self.goal = goal   # type pygame.Rect
    

    # addPlanet: adds a planet to the planet list
    def addPlanet(self, shape):
        self.existing.append(shape)

    # drawLevel: draws all the planets in the planet list
    def drawLevel(self, screen):
        screen.fill(self.color)
        pygame.draw.rect(screen, (0,0,0), self.goal, 3)
        for i in self.existing:
            i.draw(screen)
    #inGoal: determine if a particular point is in the goal
    def inGoal(self, pos):
        return (self.goal[0] <= pos[0] and self.goal[0]+self.goal[2] >= pos[0]
            and self.goal[1] <= pos[1] and self.goal[1]+self.goal[3] >= pos[1])

    #printPlanets: debugging feature
    def printPlanets(self):
        print ("%s objects in list \n") % len(self.existing)
        for i in self.existing:
            i.printPlanet()

            

