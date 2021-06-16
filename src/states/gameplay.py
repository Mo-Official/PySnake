from .game_over import GameOver
from ..game import Game
import pygame as pg

from .base import BaseState

class Gameplay(BaseState):
    def __init__(self) -> None:
        super(Gameplay, self).__init__()
        self.rect = pg.Rect((0,0), (50,50))
        self.next_state = "GAME_OVER"

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.rect.move_ip(0, -10)
            elif event.key == pg.K_DOWN:
                self.rect.move_ip(0, 10)
            elif event.key == pg.K_LEFT:
                self.rect.move_ip(-10, 0)
            elif event.key == pg.K_RIGHT:
                self.rect.move_ip(10, 0)
            elif event.key == pg.K_SPACE:
                self.done = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        pg.draw.rect(surface, pg.Color("blue"), self.rect)