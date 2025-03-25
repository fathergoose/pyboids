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
    _base_points = [0, 20, 10, 15, 20, 20, 10, 0]
    _center = [10, 15]
    _point_offsets = [-10, 5, 0, 0, 10, 5, 0, -15]
    radius = 10

    def __init__(self, position, speed, heading):
        self.position = Vector(*position)
        self.speed = speed
        self.heading = heading

    def points(self):
        return "translate center of mass into a polygon"


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="#eeeeee")
canvas.pack()
canvas.create_polygon([0, 20, 10, 15, 20, 20, 10, 0])

root.mainloop()
