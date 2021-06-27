import pygame as pg
from pygame import image as pgimage

class Spritesheet():
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def get_image(self, x,y,w,h):
        pass

    def load(self):
        pass


class Img:
    def __init__(self, filepath, colorkey=(255,255,255)) -> None:
        try:
            self.image = pgimage.load(filepath).convert()
            self.image.set_colorkey((colorkey))
        except:
            print("Error loading ", filepath)
            self.image = pg.Surface((64,64))
