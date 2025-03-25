from tkinter import Tk, Canvas

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

points = [30, 40, 40, 35, 50, 40, 40, 20]

canvas.create_polygon(points, fill="black")

root.mainloop()
