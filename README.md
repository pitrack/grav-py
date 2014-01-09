grav-py
=======

experience gravy using python (pygame)

grav-py is a 2D minigame implemented with python that is inspired by osmos, angry birds, and a poster I saw in wean. Hopefully it will be completed before the end of winter break.

**Instructions**
Welcome to space! 

You are in charge of reaching the "portal" at the other end of the sector. In your way are massive objects. Navigate around them.

click to launch. How far away your cursor is from the starting position is the related to your initial velocity. While the satellite is travelling, you can click to recall your satellite back to the initial starting position. Note: you lose your progress on that level. Upon either crashing, or being lost, you can click to restart the level. If your satellite is too fast, you can't safely enter the portal.

Currently, the last level loops


Most of it will be implemented with pygame

progress meter:
i) create canvas that can draw things, circles with pos/vel/acc attributes (in addition to color/size/mass)  - DONE

ii) allow mouse to control initial acceleration/velocity, simulate movement - DONE

iii) simulate physics (gravitational attraction) - DONE

iv) create levels - MOSTLY DONE

ivb) include instructions, and more user feedback so it is clear when the ship crashes.

v) "polish"
