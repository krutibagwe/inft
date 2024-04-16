import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def create_table():
    try:
        conn = sqlite3.connect("student_info.db")
        cursor = conn.cursor()

        # Create students table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          first_name TEXT,
                          last_name TEXT,
                          gender TEXT,
                          subject TEXT)''')

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error occurred while creating table: {e}")

def submit():
    # Retrieve form data
    first_name = entry_firstname.get()
    last_name = entry_lastname.get()
    gender = gender_var.get()
    subject = subject_var.get()

    # Validate form data
    if not first_name or not last_name or not gender or not subject:
        messagebox.showerror("Error", "Please fill out all fields.")
        return

    try:
        conn = sqlite3.connect("student_info.db")
        cursor = conn.cursor()

        # Insert new student record into the database
        cursor.execute('''INSERT INTO students (first_name, last_name, gender, subject)
                          VALUES (?, ?, ?, ?)''', (first_name, last_name, gender, subject))

        conn.commit()
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "Student information saved successfully.")

        # Display all student records
        display_students()

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error occurred while inserting data: {e}")
        if conn:
            conn.rollback()

def display_students():
    students_listbox.delete(0, tk.END)

    try:
        conn = sqlite3.connect("student_info.db")
        cursor = conn.cursor()

        # Fetch all student records from the database
        cursor.execute('''SELECT * FROM students''')
        rows = cursor.fetchall()

        for row in rows:
            student_info = f"{row[1]} {row[2]} - {row[3]} - {row[4]}"
            students_listbox.insert(tk.END, student_info)

        conn.close()

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error occurred while fetching data: {e}")

# Create main window
root = tk.Tk()
root.title("Student Information Form and Database Display")
root.configure(bg="green")
root.geometry("600x500")

# Create table if not exists
create_table()

# Create frame for form
frame_form = ttk.Frame(root, padding=20)
frame_form.pack(pady=20)

# First name
ttk.Label(frame_form, text="First name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_firstname = ttk.Entry(frame_form)
entry_firstname.grid(row=0, column=1, padx=5, pady=5)

# Last name
ttk.Label(frame_form, text="Last name:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_lastname = ttk.Entry(frame_form)
entry_lastname.grid(row=1, column=1, padx=5, pady=5)

# Gender
ttk.Label(frame_form, text="Gender:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
gender_var = tk.StringVar()
radiobutton_male = ttk.Radiobutton(frame_form, text="Male", variable=gender_var, value="Male")
radiobutton_male.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
radiobutton_female = ttk.Radiobutton(frame_form, text="Female", variable=gender_var, value="Female")
radiobutton_female.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

# Subject
ttk.Label(frame_form, text="Subject:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
subjects = ["EM-4", "COA", "AT", "OS", "Python"]
subject_var = tk.StringVar()
subject_dropdown = ttk.Combobox(frame_form, textvariable=subject_var, values=subjects, state="readonly")
subject_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Submit button
submit_button = ttk.Button(frame_form, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

# Create frame for displaying students
frame_display = ttk.Frame(root, padding=20)
frame_display.pack(pady=20)

# Listbox to display students
students_listbox = tk.Listbox(frame_display, width=50, height=10)
students_listbox.pack()

# Display existing student records initially
display_students()

root.mainloop()
