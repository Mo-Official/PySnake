from typing import List, Tuple

import pygame as pg
import pygame.sprite as pgsprite
import pygame.draw as pgdraw

import pygame.math as pgmath
vec2 = pgmath.Vector2



class BaseItem(pgsprite.Sprite):
    """Class for the player's snake
    
    Attributes
    ----------
    - length: The amount of nodes the snake has
    - dir: the way the snake is facing
    - pos: the square, where the head of the snake is spawned
    """
   


    def __init__(self, pos=vec2(640, 640), value= 100, time_active=1000, image=pg.Surface((64,64))) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = self.pos
        self.value = value
        self.time_active = time_active
        

    def update(self):
        self.time_active -= 1
        if self.time_active == 0:
            self.kill()


class AppleItem(BaseItem):
    def __init__(self, pos, image) -> None:
        value=200
        time_active=400
        super().__init__(pos=pos, value=value, time_active=time_active, image=image)