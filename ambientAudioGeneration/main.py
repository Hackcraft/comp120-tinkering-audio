import math, pygame

"""
    ambience contains the different ambient noise scenarios,
    their sound files and the probability of them playing.
"""

ambience = {
    "Forests" : [
        # Sound one
        [
            # Load file
            # Probability of it playing
        ],
        # Sound two
        [
            # Load file
            # Probability of it playing
        ],
    ],
    "Towns" : [

    ],
    "Caves" : [

    ]
}

"""
    Gui
"""

pygame.init()
screenX, screenY = 800, 600
screen = pygame.display.set_mode((screenX, screenY))

blnRunning = True
while blnRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blnRunning = False
            pygame.quit()