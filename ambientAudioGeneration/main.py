import math
import pygame

from tunes import *

"""
    ambience contains the different ambient noise scenarios,
    their sound files and the probability of them playing.
    
    Classes:
        CreateWave
            Make sound - No cache
        Notes
            Contains notes - No cache
        SoundFunctions
            Contains echo etc - No cache
        Tunes
            Contains tunes - Cached
        
        Main
            Writes file for the selected atmosphere at set length using random tunes suitable for the atmosphere.
"""

ambienceTags = [
    "Caves",
    "Forests",
    "Towns"
]

tunes = Tunes()

"""
    Gui
"""

pygame.init()
screenX, screenY = 800, 600
screen = pygame.display.set_mode((screenX, screenY))

# Button text
buttonTextSize = screenX / len(ambienceTags) / 2
buttonTextFont = pygame.font.SysFont("monospace", buttonTextSize)

buttonText = []
for place in ambienceTags: # Go through the dictionary in alphabetical order
    buttonText.append(buttonTextFont.render(place, 1, (0,0,0)))

blnRunning = True
while blnRunning:

    # Plain white screen
    screen.fill((255, 255, 255))

    # Button text
    for i in xrange(len(buttonText)):
        screen.blit(buttonText[i], (0, i * buttonTextSize))

    # Update screen
    pygame.display.update()

    # Allow the user to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blnRunning = False
        # Button actions
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseY < buttonTextSize:
                print ambienceTags[0] # Caves
            elif mouseY < buttonTextSize * 2:
                print ambienceTags[1] # Forests
            elif mouseY < buttonTextSize * 3:
                print ambienceTags[2] # Towns

pygame.quit()