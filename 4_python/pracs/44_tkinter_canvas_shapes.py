#Write a python program to design canvas and create different shapes
import tkinter as tk

def draw_rectangle():
    canvas.create_rectangle(50, 50, 150, 100, fill="blue")

def draw_circle():
    canvas.create_oval(200, 50, 300, 100, fill="red")

def draw_line():
    canvas.create_line(50, 150, 250, 200, fill="green")

def draw_triangle():
    canvas.create_polygon(300, 150, 350, 50, 400, 150, fill="yellow")

def draw_star():
    points = [(450, 100), (470, 180), (400, 130), (500, 130), (430, 180)]
    canvas.create_polygon(points, fill="orange")

def clear_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("Drawing Shapes")

canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

btn_texts = ["Rectangle", "Circle", "Line", "Triangle", "Star", "Clear"]
btn_commands = [draw_rectangle, draw_circle, draw_line, draw_triangle, draw_star, clear_canvas]

for text, command in zip(btn_texts, btn_commands):
    btn = tk.Button(root, text=text, command=command, width=10, height=2)
    btn.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
