class Spritesheet:
    def __init__(self, filepath) -> None:
        self.image = None
        self.load_image(filepath)

    def load_image(self, filepath):
        pass

    def get_image(self):
        pass


class ImageCollection:
    def __init__(self, folderpath) -> None:
        self.load_images(folderpath)
        self.images = {}

    def load_images(self, folderpath):
        pass

    def get_image(self, name):
        pass