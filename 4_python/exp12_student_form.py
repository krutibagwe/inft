import tkinter as tk
from tkinter import ttk

def submit():
    first_name = entry_firstname.get()
    last_name = entry_lastname.get()
    gender = gender_var.get()
    subject = subject_var.get()
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Gender:", gender)
    print("Subject:", subject)

# Create main window
root = tk.Tk()
root.title("Student Information")
root.configure(bg="green")
root.geometry("500x400")  

# Create frame
frame = ttk.Frame(root, padding=20)
frame.pack(pady=50, padx=50)

# First name
first_name_label = ttk.Label(frame, text="First name:")
first_name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_firstname = ttk.Entry(frame)
entry_firstname.grid(row=0, column=1, padx=5, pady=5)

# Last name
last_name_label = ttk.Label(frame, text="Last name:")
last_name_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_lastname = ttk.Entry(frame)
entry_lastname.grid(row=1, column=1, padx=5, pady=5)

# Gender
gender_label = ttk.Label(frame, text="Gender:")
gender_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
gender_var = tk.StringVar()
radiobutton_male = ttk.Radiobutton(frame, text="Male", variable=gender_var, value="Male")
radiobutton_male.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
radiobutton_female = ttk.Radiobutton(frame, text="Female", variable=gender_var, value="Female")
radiobutton_female.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

# Subject
subject_label = ttk.Label(frame, text="Subject:")
subject_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
subjects = ["EM-4", "COA", "AT", "OS", "Python"]
subject_var = tk.StringVar()
subject_dropdown = ttk.Combobox(frame, textvariable=subject_var, values=subjects, state="readonly")
subject_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Submit button
submit_button = ttk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
