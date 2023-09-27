#main file for the project
#main will contain the main loop and the main game logic
#main will call the other files and classes to run the game

import pygame

# create pygame window  and set title
pygame.init()

# set up the drawing window

screen = pygame.display.set_mode([600, 600])

# run until the user asks to quit
def main():
    running = True
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the background with grey
        screen.fill((128, 128, 128))

        # draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (300, 300), 120)

        # flip the display
        pygame.display.flip()

    # done! time to quit
    pygame.quit()

main()

    



