import pygame

class Planet:
    # init: initializes physical aspects and color
    # pos (px), vel (px/s), acc(px/s^2) have x and y components.
    def __init__(self, pos, vel, acc, color, size, mass = -1):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.color = color
        self.size = size

    # int2: helper function 
    def int2(self, vec):
        (a,b) = vec
        return (int(a), int(b))
        
    # draw: draws planet onto the screen        
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, 
                     self.int2(self.pos) , int(self.size), 0)

    # flick: animates by one frame by recalculating pos, vel, acc
    def flick(self, level, time):
        (xp, yp) = self.pos
        (xv, yv) = self.vel
        (xa, ya) = self.acc
        self.pos = (xp + xv*time, yp + yv*time)
        self.vel = (xv + xa*time, yv + ya*time)
        #self.acc calculations unimplemented

    # printPlanet: debugging
    def printPlanet(self):
        print ("pos %s size %s \n" %  (self.pos, self.size))
        
        
        
class Level:
    # init: inputs are background color, planet list, int
    # initializes variables
    def __init__(self, color, existing, num):
        self.color = color
        self.existing = existing
        self.num = num
    

    # addPlanet: adds a planet to the planet list
    def addPlanet(self, shape):
        self.existing.append(shape)

    # drawLevel: draws all the planets in the planet list
    def drawLevel(self, screen):
        screen.fill(self.color)
        for i in self.existing:
            i.draw(screen)


    #printPlanets: debugging feature
    def printPlanets(self):
        print ("%s objects in list \n") % len(self.existing)
        for i in self.existing:
            i.printPlanet()

