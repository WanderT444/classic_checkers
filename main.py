#main file for the project
#main will contain the main loop and the main game logic
#main will call the other files and classes to run the game

import pygame

# create pygame window  and set title
pygame.init()

# set up the drawing window
Width, Height = 600, 600
screen = pygame.display.set_mode([Width, Height])

#title of the gaame for screen 
pygame.display.set_caption("Checkers+")  

# title for display 

game_title = "Checkers+"
message = " Coming Soon!"

title_font = pygame.font.Font(None, 64)
message_font = pygame.font.Font(None, 32)


title_text = title_font.render(game_title, True, (255, 255, 255))
title_rect = title_text.get_rect(center=(Width // 2, 50))

#quick message !!!
message_text = message_font.render(message, True, (255, 255, 255))

message_rect = message_text.get_rect(center=(Width // 2, 120))


# run until the user asks to quit
def main():
    running = True
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the background with grey
        screen.fill((0, 0, 0))
        
        
        #tile the background
        screen.blit(title_text, title_rect)
        screen.blit(message_text, message_rect)

        # flip the display
        pygame.display.flip()

    # done! time to quit
    pygame.quit()

main()

    



