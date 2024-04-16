import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_message():
    messagebox.showinfo("Message", "Button clicked!")

# Create main window
root = tk.Tk()
root.title("Image with Button")

# Load background image
background_image_path = "sky2.jpg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((400, 300), Image.LANCZOS)  
background_photo = ImageTk.PhotoImage(background_image)

# Create label to display background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

# Create button
button = tk.Button(root, text="Click Me!", command=show_message)
button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)  # Position button at the bottom center

root.mainloop()
