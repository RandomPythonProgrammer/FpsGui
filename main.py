import pyglet
import threading


class App(pyglet.window.Window):
    def __init__(self, width, height):
        super(App, self).__init__(width, height, resizable=True)
        self.map = pyglet.image.load('map.png')
        self.background = pyglet.sprite.Sprite(self.map)
        self.items = []
        self.interval = self.background.width/10
        self.scale = self.interval/5.12 # meters per tile
        # Gamertag, position, level
        # Letter is x
        # Top left start for letter and number
        # Coords are top left of square
        # finished 11:19

    def project(self, x_axis, y_axis, x_coord, y_coord):
        pos_x = (ord(x_axis) - 65) * self.interval + x_coord * self.scale
        pos_y = self.height - (y_axis * self.interval + y_coord * self.scale)
        return pos_x, pos_y

    def update(self):
        items = []
        while True:
            ip = input()
            if ip == '':
                break
            items.append(ip)
        self.items.clear()
        for item in items:
            self.items.append(item.split(','))

    def render(self, dt):
        self.clear()
        self.background.draw()
        for item in self.items:
            tag, x_axis, y_axis, x_coord, y_coord = item
            x, y = self.project(x_axis, float(y_axis), float(x_coord), float(y_coord))
            circle = pyglet.shapes.Circle(radius=5, x=x, y=y, color=(255, 0, 0, 255))
            text = pyglet.text.Label(text=tag, x=x, y=y, color=(0, 0, 0, 255))
            text.x -= text.content_width/2
            text.y += text.content_height/2
            circle.draw()
            text.draw()


if __name__ == '__main__':
    app = App(708, 705)
    threading.Thread(target=app.update).start()
    pyglet.clock.schedule(app.render)
    pyglet.app.run()
