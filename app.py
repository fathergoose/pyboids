import tkinter as tk
import math

# Add three pixel padding for macos
# base_points = [[8, 3], [3, 18], [8, 13], [13, 18]]
# 17ms ~= 60fps
# canvas.create_polygon(flatten(base_points))
DT = 500


def rotate(poly_points, angle, center):
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


def new_location(boid: Boid):
    init_x, init_y = boid.position
    dx = boid.speed * math.cos(boid.heading)
    dy = boid.speed * math.sin(boid.heading)
    return (init_x + dx * DT / 1000, init_y + dy * DT / 1000)


def update(boids):
    positions = [new_location(boid) for boid in boids]
    # TODO: Include logic to "turn" the boid
    # headings = [boid.heading + boid.turning() * DT for boid in boids]
    # WARN: Will need to revise this, hard-coding for now
    return [Boid(pos, 10, math.pi) for pos in positions]


def render(canvas, new_boids):
    canvas.delete("all")
    for boid in new_boids:
        points = flatten(boid.polygon_points())
        print(points)
        canvas.create_polygon(points, fill="black")


def refresh(root, canvas, boids):
    print("refreshing")
    new_boids = update(boids)
    render(canvas, new_boids)
    root.after(DT, refresh, root, canvas, new_boids)


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500, bg="#eeeeee")
    canvas.pack()
    b = Boid((50, 50), 10, math.pi)
    root.after(DT, refresh, root, canvas, [b])
    root.mainloop()


if __name__ == "__main__":
    main()
