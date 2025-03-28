import tkinter as tk
import math

# 17ms ~= 60fps
DT = 17
pointer_loc = (0, 0)


def rotate(poly_points, angle, center):
    angle += math.pi / 2
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for points in poly_points:
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
    return new_points


class Boid:
    # [head, left, center, right]
    # With 3 px padding
    _base_points = [[8, 3], [3, 18], [8, 13], [13, 18]]
    radius = 10

    def __init__(self, position, heading, speed=10):
        self.position = position
        self.speed = speed
        self.heading = heading

    def polygon_points(self):
        translation = (
            [
                [bp[0] + self.position[0], bp[1] + self.position[1]]
                for bp in self._base_points
            ],
        )
        return rotate(
            translation,
            self.heading,
            # WARN: align location to head point?
            self.position,
        )


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


def new_location(boid: Boid):
    init_x, init_y = boid.position
    dx = boid.speed * math.cos(boid.heading)
    dy = boid.speed * math.sin(boid.heading)
    return (init_x + dx * DT / 1000, init_y + dy * DT / 1000)


def point_to_mouse(position):
    normalized_pos = (pointer_loc[0] - position[0], pointer_loc[1] - position[1])
    heading = 0
    if normalized_pos[0] < 0:
        heading = math.atan(normalized_pos[1] / normalized_pos[0]) + math.pi
    else:
        heading = math.atan(normalized_pos[1] / normalized_pos[0])
    return heading


def update(boids):
    return [Boid(new_location(boid), point_to_mouse(boid.position)) for boid in boids]


def render(canvas, new_boids):
    canvas.delete("all")
    for boid in new_boids:
        points = flatten(boid.polygon_points())
        canvas.create_polygon(points, fill="black")


def refresh(root, canvas, boids):
    new_boids = update(boids)
    render(canvas, new_boids)
    root.after(DT, refresh, root, canvas, new_boids)


def get_mouse_xy(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    global pointer_loc
    pointer_loc = (x, y)
    return x, y


def setup():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500, bg="#eeeeee")
    canvas.pack()
    canvas.bind("<Motion>", get_mouse_xy)
    return root, canvas


def init_boids():
    return [Boid((50, 50), 10, 1)]


def main():
    root, canvas = setup()
    boids = init_boids()
    refresh(root, canvas, boids)
    root.mainloop()


if __name__ == "__main__":
    main()
