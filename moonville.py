## Moonville

import pyglet
import pyglet.window

import model

class Moonville(pyglet.window.Window):
    def __init__(self):
        super(Moonville, self).__init__(width = 800, height = 600)

        self.__state__ = self.introduction
        self.load_images()

    def load_images(self):
        self.background_image = pyglet.image.load("background.png")

    def on_draw(self):
        self.__state__()
            
    # Scenes
    def introduction(self):
        self.clear()
        self.background_image.blit(0,0)

    # Event handlers
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.Q:
            pyglet.app.exit()

if __name__ == "__main__":
    moonville = Moonville()
    pyglet.app.run()
