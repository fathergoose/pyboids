import tkinter as tk
import math

# 17ms ~= 60fps
DT = 17


def rotate(points, angle, center):
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points


class Boid:
    # [head, left, center, right]
    # [[5, 0], [0, 15], [5, 10], [10, 15]]
    # Pad 3 pxels from the canvas boundry
    _base_points = [[8, 3], [3, 18], [8, 13], [13, 18]]
    radius = 10

    def __init__(self, position, speed, heading):
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


def new_location(boid: Boid, dt):
    init_x, init_y = boid.position
    dx = boid.speed * math.cos(boid.heading)
    dy = boid.speed * math.sin(boid.heading)
    return (init_x + dx, init_y + dy)


# Add three pixel padding for macos
# base_points = [[8, 3], [3, 18], [8, 13], [13, 18]]


def update(boids):
    positions = [boid.position + DT * boid.velocity() for boid in boids]
    headings = [boid.heading + boid.turning() * DT for boid in boids]


def render(canvas, new_boids):
    return 0


def refresh(canvas, boids):
    new_boids = update(boids)
    render(canvas, new_boids)
    return 0


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500, bg="#eeeeee")
    canvas.pack()
    # canvas.create_polygon(flatten(base_points))
    b = Boid((50, 50), 10, 0)
    root.after(DT, refresh, canvas, [b])
    root.mainloop()


if __name__ == "__main__":
    main()
