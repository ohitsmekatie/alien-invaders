
# Game Explanation

# In Alien Invasion, the player controls a ship that appears at the bottom center of the screen.
# The play can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
# When the game begins, a fleet of aliens fills the ski and moves across and down the screen.
# The player shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears
# that moves faster than the previous fleet. If any alien hits the player's ship or reaches the bottom
# of the screen, the player loses a ship. If the player loses three ships, the game ends.

import sys
import pygame
# import game settings for screen width,height,color
from settings import Settings
from ship import Ship

# the function that starts the game & defines the screen
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()
