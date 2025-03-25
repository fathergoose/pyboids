import tkinter as tk


class Vector(object):
    def __init__(self, x=0, y=0, z=0):
        self._x, self._y, self._z = x, y, z

    def setx(self, x):
        self._x = float(x)

    def sety(self, y):
        self._y = float(y)

    def setz(self, z):
        self._z = float(z)

    x = property(lambda self: float(self._x), setx)
    y = property(lambda self: float(self._y), sety)
    z = property(lambda self: float(self._z), setz)


class Boid:
    # [head, left, center, right]
    _base_points = [[5, 0], [0, 15], [5, 10], [10, 15]]
    radius = 10

    def __init__(self, position, speed, heading):
        self.position = Vector(*position)
        self.speed = speed
        self.heading = heading

    # I just want to translate [60,230] into [[65, 230],[60,245], [65, 240], [70, 245]]
    def points(self):
        [[bp[0] + self.position.x, bp[1] + self.position.y] for bp in self._base_points]


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="#eeeeee")
canvas.pack()
canvas.create_polygon([0, 15, 5, 10, 10, 15, 5, 0])

root.mainloop()
