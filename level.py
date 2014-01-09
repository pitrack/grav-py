import pygame, planet


BG = (134, 100, 79)
ZERO = (0,0)
list = [ planet.Level(BG,
                      [],
                      0, (100, 300), pygame.Rect(800, 300, 50, 50)),
         
         planet.Level(BG,
                      [planet.Planet((300, 300), ZERO, ZERO, 
                                     (255,255,120), 50, 300), 
                       ],
                      0, (100, 300), pygame.Rect(800, 300, 50, 50)),
         planet.Level(BG,
                      [planet.Planet((300, 300), ZERO, ZERO, 
                                     (255,255,120), 50, 300), 
                       planet.Planet((500, 300), ZERO, ZERO,
                                     (255, 120, 0), 30, 36),
                       planet.Planet((700, 300), ZERO, ZERO,
                                     (255, 255, 120), 50, 300)],
                      0, (200, 150), pygame.Rect(800, 500, 40, 40))
           ,
            planet.Level(BG,
                      [planet.Planet((350, 300), ZERO, ZERO, 
                                     (255, 120, 0), 50, 300), 
                       planet.Planet((500, 300), ZERO, ZERO,
                                     (255, 255, 120), 50, 100),
                       planet.Planet((650, 300), ZERO, ZERO,
                                     (255, 120, 0), 30, 108)],
                      0, (405, 300), pygame.Rect(800, 500, 25, 25))
           ,
           planet.Level(BG,
                      [planet.Planet((200, 300), ZERO, ZERO, 
                                     (160,255,20), 30, 300), 
                       planet.Planet((500, 300), ZERO, ZERO,
                                     (240, 140, 160), 50, 200),
                       planet.Planet((800, 300), ZERO, ZERO,
                                     (222, 111, 222), 40, 250),
                       planet.Planet((400, 400), ZERO, ZERO,
                                     (40, 40, 40), 25, 500),
                       planet.Planet((600, 400), ZERO, ZERO,
                                     (40, 40, 40), 25, 500),
                       planet.Planet((400, 250), ZERO, ZERO,
                                     (240, 240, 240), 25, 100),
                       planet.Planet((600, 250), ZERO, ZERO,
                                     (240, 240, 240), 25, 100)
                       ], 
                        0, (500, 150), pygame.Rect(485, 450, 30, 30)),
         planet.Level(BG,
                      [ planet.Planet((650, 460), ZERO, ZERO,
                                      (140, 140, 140), 25, 100)
                        ], 
                        0, (50, 50), pygame.Rect(675, 485, 12, 12))

           ]
