import sys
import pygame

from src.states.menu import Menu
from src.states.gameplay import Gameplay
from src.states.game_over import GameOver
from src.states.splash import Splash
from src.game import Game
from src import settings


pygame.init()
screen = pygame.display.set_mode((settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT))
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver()
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()
