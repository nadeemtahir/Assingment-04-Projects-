# graphics.py
import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Graphics Canvas")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.canvas.update()

        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click = None

        self.canvas.bind("<Motion>", self._motion)
        self.canvas.bind("<Button-1>", self._click)

    def _motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _click(self, event):
        self.last_click = (event.x, event.y)

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def get_last_click(self):
        while self.last_click is None:
            self.canvas.update()
        click = self.last_click
        self.last_click = None
        return click

    def wait_for_click(self):
        return self.get_last_click()

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color)

    def moveto(self, item, x, y):
        coords = self.canvas.coords(item)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(item, x, y, x + width, y + height)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def update(self):
        self.canvas.update()
