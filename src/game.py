from . import settings
import pygame as pg

class Game(object):
    def __init__(self, screen, states, start_state) -> None:
        self.done = False
        self.screen = screen
        self.caption = settings.CAPTION
        self.clock = pg.time.Clock()
        self.fps = settings.FPS
        self.now = 0.0
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]


    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)


    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)


    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.events()
            self.update(dt)
            self.draw()
            pg.display.update()


    def events(self):
        for event in pg.event.get():
            self.state.get_event(event)

