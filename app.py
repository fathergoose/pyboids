import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="#eeeeee")
canvas.pack()


# NOTE: I should seperate the converns of drawing boid glyphs from regular point geometry drawing
# A boid should have a circle that acts as its boundries and position, etc. then the triangle/cheveron
# should be drawn in the center of the circle 
def rotate(boid):
    # Bunch of trigonometry
    return False


def drawBoid(boid, canvas):
    # For a boid with position=(x,y)
    # [10+x, 20+y, 20+x... ]
    dx = boid["position"]["x"]
    dy = boid["position"]["y"]
    points = [10 + dx, 20 + dy, 20 + dx, 15 + dy, 30 + dx, 20 + dy, 20 + dx, dy]
    # Well that's cool and all, but what about rotation?
    canvas.create_polygon(points, fill="black")



class Vector(object):

    def __init__(self, x=0, y=0, z=0):
        self._x, self._y, self._z = x, y, z

    def setx(self, x): self._x = float(x)
    def sety(self, y): self._y = float(y)        
    def setz(self, z): self._z = float(z)     

    x = property(lambda self: float(self._x), setx)
    y = property(lambda self: float(self._y), sety)
    z = property(lambda self: float(self._z), setz)

class Boid:
    __init__(self, init_pos):
        self.position = Vector(*init_pos)

# boid_o.position.x
# boid = {"position": {"x": 10, "y": 15}}

drawBoid(boid, canvas)
root.mainloop()
