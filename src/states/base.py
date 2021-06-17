import pygame as pg

class BaseState(object):
    """A Base class for the state machine.

    How to use
    ----------
    * Set self.done to True to switch to self.next_state
    
    * Set self.quit to True to quit the game.

    * handel events in get_event the same way you would handel them in a basic event loop
    get_event(event) is simply called inside the main event loop, passing each event to get_event(event).

    """
    def __init__(self) -> None:
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
