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

# Button text
buttonTextSize = screenX / len(ambience) / 2
buttonTextFont = pygame.font.SysFont("monospace", buttonTextSize)
label = buttonTextFont.render("Some text!", 1, (0,0,0))

buttonText = []
for place in ambience:
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
            pygame.quit()
