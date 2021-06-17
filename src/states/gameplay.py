from src import settings
from src.components.player import Player
from src.components.item_sprites import BaseItem

from .game_over import GameOver
from ..game import Game
import pygame as pg

import pygame.sprite as pgsprite
import pygame.draw as pgdraw

import pygame.math as pgmath
vec2 = pgmath.Vector2

import random

from .base import BaseState

class Gameplay(BaseState):
    def __init__(self) -> None:
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"

    def startup(self, persistent):
        self.all_sprites = pgsprite.Group()
        self.all_food = pgsprite.Group()

        self.snake = Player(vec2(64,0))
        self.foods = []

        self.last_update = pg.time.get_ticks()

        self.all_sprites.add(self.snake)
        self.all_sprites.add(self.foods)

        self.all_food.add(self.foods)


    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:

            self.snake.get_key_up(event=event)


    def update(self, dt):

        if self.snake.rect.collidelistall(self.snake.tail_rects):
            self.persist["death_by"] = "You ate yourself!!"
            self.done = True

        # move the sanke
        self.snake.update()

        food_hits = pgsprite.spritecollide(self.snake, self.all_food, True)
        for hit in food_hits:
            if self.snake.length > 15:
                self.snake.speed += 0.1
            self.snake.length += 1

        if len(self.all_food) == 0:
            print("OKAY")
            for _ in range(random.randint(3, 6)):
                x = max(0, 64*random.randint(0,10))
                x = min(x, settings.WINDOW_WIDTH)

                y = max(0, 64*random.randint(0,10))
                y = min(y, settings.WINDOW_HEIGHT)

                food = BaseItem((x, y),100,1000)
                self.all_food.add(food)
                self.all_sprites.add(food)
                print("YAY")

        

        

        # check if snake collided with a wall
        snake_rect = self.snake.rect
        if snake_rect.left < 0 or\
               snake_rect.right > settings.WINDOW_WIDTH or\
               snake_rect.top < 0 or\
               snake_rect.bottom > settings.WINDOW_WIDTH:
            self.persist["death_by"] = "You hit a wall!!"
            self.done = True



    def draw(self, surface):
        surface.fill(pg.Color("black"))
        self.all_sprites.draw(surface)
        self.snake.draw(surface)

