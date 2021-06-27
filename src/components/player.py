from src import settings
from typing import List, Tuple

import pygame as pg

import pygame.sprite as pgsprite
import pygame.draw as pgdraw

import pygame.math as pgmath
vec2 = pgmath.Vector2


class Player(pgsprite.Sprite):
    """Class for the player's snake
    
    Attributes
    ----------
    - length: The amount of nodes the snake has
    - dir: the way the snake is facing
    - pos: the square, where the head of the snake is spawned
    """
    dir = "right"
    points = 0
    length = 3
    last_move = 0

    speed = 2.


    def __init__(self, pos) -> None:
        """
        Param
        -----
            - groups: optional parameter for the sprite's groups

                Default: None
        """
        super().__init__()
        self.image = pg.Surface((54,54))
        self.image.fill(pg.Color("blue"))
        self.rect = self.image.get_rect()

        

        # a simple tail
        self.tail_image = pg.Surface((54,54))
        self.tail_image.fill(pg.Color("red"))
        self.tail_rects = []
        
        self.pos : pgmath.Vector2 = pos
        self.rect.topleft = self.pos
        self.movement_vec = vec2(0,0)
        self.last_move = 0

        self.last_pos = []

    def get_key_up(self, event):
        if event.key == pg.K_UP:
            self.dir = "up"
        elif event.key == pg.K_DOWN:
            self.dir = "down"
        elif event.key == pg.K_LEFT:
            self.dir = "left"
        elif event.key == pg.K_RIGHT:
            self.dir = "right"

    def move(self):
        last_move_vec = self.movement_vec # last movement passed to the pos of the next snake part

        if self.dir == "left":
            self.movement_vec = (-64, 0)
        if self.dir == "right":
            self.movement_vec = (64, 0)
        if self.dir == "up":
            self.movement_vec = (0, -64)
        if self.dir == "down":
            self.movement_vec = (0, 64)
        

        self.last_pos.append(pgmath.Vector2(self.pos))
        if len(self.last_pos) > self.length:
            self.last_pos.pop(0)


        self.pos += self.movement_vec
        self.rect.topleft = self.pos

        self.tail_rects = [pg.Rect(pos.x, pos.y, 54, 54) for pos in self.last_pos]




    def update(self):
        self.last_move += self.speed
        if self.last_move > 60:
            self.move()
            self.last_move = 0
        
        


    def eat(self, food):
        if self.length < 10:
            self.length += 1
            self.speed += 0.1
        else:
            self.speed += 0.2
        food.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for rect in self.tail_rects:
            surface.blit(self.tail_image, rect)
