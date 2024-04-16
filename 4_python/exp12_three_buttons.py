import tkinter as tk
from tkinter import ttk
from tkinter import *

def submit():
    first_name = entry_firstname.get()
    last_name = entry_lastname.get()
    print("First name:", first_name)
    print("Last name:", last_name)

def reset():
    entry_firstname.delete(0, tk.END)
    entry_lastname.delete(0, tk.END)

def exit_window():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Student Information")
root.configure(bg="blue")

window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set the geometry of the window to the calculated position
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# First name
first_name_label = ttk.Label(frame, text="First name:")
first_name_label.grid(row=0, column=0, sticky=tk.W)
entry_firstname = ttk.Entry(frame)
entry_firstname.grid(row=0, column=1)

# Last name
last_name_label = ttk.Label(frame, text="Last name:")
last_name_label.grid(row=1, column=0, sticky=tk.W)
entry_lastname = ttk.Entry(frame)
entry_lastname.grid(row=1, column=1)

# Submit button
submit_button = ttk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Reset button
reset_button = ttk.Button(frame, text="Reset", command=reset)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

# Exit button
exit_button = ttk.Button(frame, text="Exit", command=exit_window)
exit_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
