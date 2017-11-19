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

buttonText = []
for place in sorted(ambience.items()): # Go through the dictionary in alphabetical order
    buttonText.append(buttonTextFont.render(place[0], 1, (0,0,0)))

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
        # Button actions
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseY < buttonTextSize:
                print sorted(ambience.items())[0][0] # Caves
            elif mouseY < buttonTextSize * 2:
                print sorted(ambience.items())[1][0] # Forests
            elif mouseY < buttonTextSize * 3:
                print sorted(ambience.items())[2][0] # Towns
