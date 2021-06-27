import pygame as pg
from .base import BaseState

class GameOver(BaseState):
    def __init__(self) -> None:
        super(GameOver, self).__init__()
        self.title = self.font.render("Game Over", True, pg.Color("white"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        

        

    def startup(self, persistent):
        self.texts = []

        self.instuctions = self.font.render("Press space to start again, or enter to got to the menu", True, pg.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 50)
        self.instuctions_text = self.instuctions.get_rect(center = instructions_center)
        self.texts.append((self.instuctions, self.instuctions_text))

        self.death_by = self.font.render(persistent["death_by"], True, pg.Color("white"))
        death_by_center = (self.screen_rect.center[0], self.screen_rect.center[1] - 100)
        self.death_by_text = self.death_by.get_rect(center = death_by_center)
        self.texts.append((self.death_by, self.death_by_text))
        

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
        for text in self.texts:
            surface.blit(*text)