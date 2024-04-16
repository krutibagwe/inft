import tkinter as tk

def draw_scene(canvas):
    # Draw sky (rectangle)
    canvas.create_rectangle(0, 0, 500, 400, fill="sky blue", outline="")

    # Draw sun (oval)
    canvas.create_oval(420, 20, 480, 80, fill="yellow", outline="")

    # Draw house (rectangle and triangle)
    canvas.create_rectangle(100, 250, 300, 400, fill="light pink", outline="black", width=2)
    canvas.create_polygon(100, 250, 200, 150, 300, 250, fill="light pink", outline="black", width=2)

    # Draw door (rectangle)
    canvas.create_rectangle(180, 300, 220, 400, fill="purple", outline="black", width=2)

    # Draw windows (rectangles)
    canvas.create_rectangle(120, 280, 160, 320, fill="light blue", outline="black", width=2)
    canvas.create_rectangle(240, 280, 280, 320, fill="light blue", outline="black", width=2)

    # Draw trees (rectangles and ovals)
    canvas.create_rectangle(30, 250, 60, 400, fill="brown", outline="")
    canvas.create_oval(0, 200, 80, 280, fill="forest green", outline="")
    canvas.create_rectangle(400, 250, 440, 400, fill="brown", outline="")
    canvas.create_oval(360, 200, 440, 280, fill="forest green", outline="")

# Create main window
root = tk.Tk()
root.title("Colorful Scenery Drawing using Canvas")

# Create Canvas widget
canvas_width = 500
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

draw_scene(canvas)

root.mainloop()
