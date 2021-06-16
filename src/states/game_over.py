import pygame as pg

from .base import BaseState

class GameOver(BaseState):
    def __init__(self) -> None:
        super(GameOver, self).__init__()
        self.title = self.font.render("Game Over", True, pg.Color("white"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.instuctions = self.font.render("Press space to start again, or enter to got to the menu", True, pg.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 50)
        self.instuctions_text = self.instuctions.get_rect(center = instructions_center)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RETURN:
                self.next_state = "MENU"
                self.done = True

            elif event.key == pg.K_SPACE:
                self.next_state = "GAMEPLAY"
                self.done = True

            elif event.key == pg.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instuctions, self.instuctions_text)