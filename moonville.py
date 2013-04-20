## Moonville

import pyglet
import pyglet.window

class Moonville(pyglet.window.Window):
    def __init__(self):
        super(Moonville, self).__init__(width = 800, height = 600)

    # Event handlers
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.Q:
            pyglet.app.exit()

if __name__ == "__main__":
    moonville = Moonville()
    pyglet.app.run()
