## Moonville

import pyglet
import pyglet.window

import model

class Moonville(pyglet.window.Window):
    def __init__(self):
        super(Moonville, self).__init__(width = 800, height = 600)

        self.__state__ = Introduction()
        self.load_images()

    def load_images(self):
        self.background_image = pyglet.image.load("background.png")

    # Event handlers
    def on_draw(self):
        self.__state__.on_draw(self)
            
    def on_key_press(self, symbol, modifiers):
        self.__state__.on_key_press(self, symbol, modifiers)
            
## Scenes
class Introduction(object):
    def on_draw(self, window):
        window.clear()
        window.background_image.blit(0,0)

    def on_key_press(self, window, symbol, modifiers):
        if symbol == pyglet.window.key.Q:
            pyglet.app.exit()


if __name__ == "__main__":
    moonville = Moonville()
    pyglet.app.run()
