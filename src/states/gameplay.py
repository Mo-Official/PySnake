from src.img_manager import Img
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
        self.image_data = {}

    def startup(self, persistent):

        if "img_data" in persistent:
            self.image_data = persistent["img_data"]
        else:
            self.load_images()

        self.all_sprites = pgsprite.Group()
        self.all_food = pgsprite.Group()

        self.snake = Player(vec2(64,0))
        self.foods = []

        self.last_update = pg.time.get_ticks()

        self.all_sprites.add(self.snake)
        self.all_sprites.add(self.foods)

        self.all_food.add(self.foods)

    def load_images(self):
        self.image_data["food_orange"] = Img("data/img/food_orange.png", pg.Color("white"))
        self.image_data["food_banana"] = Img("data/img/food_banana.png", pg.Color("white"))
        


    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:

            self.snake.get_key_up(event=event)


    def update(self, dt):

        if self.snake.rect.collidelistall(self.snake.tail_rects):
            self.persist["death_by"] = "You bit yourself!!"
            self.done = True

        # move the sanke
        self.snake.update()

        food_hits = pgsprite.spritecollide(self.snake, self.all_food, True)
        for hit in food_hits:
            if self.snake.length > 15:
                self.snake.speed += 0.1
            self.snake.length += 1

        if len(self.all_food) == 0:
            for _ in range(random.randint(3, 6)):

                allowed = False
                while not allowed:
                    x = max(0, 64*random.randint(0,10))
                    x = min(x, settings.WINDOW_WIDTH)

                    y = max(0, 64*random.randint(0,10))
                    y = min(y, settings.WINDOW_HEIGHT)

                    # check if food overlaps with snake
                    snake_parts_check = True
                    for part_rect in self.snake.tail_rects:
                        if part_rect.x == x and part_rect.y == y:
                            snake_parts_check = False
                            break
                    if not snake_parts_check:
                        continue

                    # check if food overlaps with other food
                    food_overlap_check = True
                    for food in self.all_food:
                        if food.rect.x == x and food.rect.y == y:
                            food_overlap_check = False
                            break
                    if not food_overlap_check:
                        continue

                    # if all checks succeed, then its allowed
                    if snake_parts_check\
                            and food_overlap_check:
                        allowed = True
                    

                food_image = random.choice(
                    [self.image_data["food_orange"].image,
                    self.image_data["food_banana"].image

                    ])
                
                food = BaseItem((x, y),100,1000, food_image)
                self.all_food.add(food)
                self.all_sprites.add(food)

        

        

        # check if snake collided with a wall
        snake_rect = self.snake.rect
        if snake_rect.left < 0 or\
               snake_rect.right > settings.WINDOW_WIDTH or\
               snake_rect.top < 0 or\
               snake_rect.bottom > settings.WINDOW_HEIGHT:
            self.persist["death_by"] = "You hit a wall!!"
            self.done = True



    def draw(self, surface):
        surface.fill(pg.Color("black"))
        self.all_sprites.draw(surface)
        self.snake.draw(surface)

