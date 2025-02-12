import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    dob = entry.get()
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        result_label.config(text=f"Your Age: {age} years", fg="green")
    except ValueError:
        messagebox.showerror("Invalid Date Format", "Please enter date in YYYY-MM-DD format")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")
root.config(bg="#f0f0f0")  # Background color for the window

# Title label
title_label = tk.Label(root, text="Age Calculator", font="Arial 16 bold", bg="#f0f0f0", fg="blue")
title_label.pack(pady=10)

# DOB entry label
dob_label = tk.Label(root, text="Enter Date of Birth (YYYY-MM-DD):", font="Arial 12", bg="#f0f0f0", fg="black")
dob_label.pack(pady=5)

# Entry for date of birth
entry = tk.Entry(root, font="Arial 14", bd=2, relief="solid", width=20)
entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate Age", font="Arial 12", bg="#4CAF50", fg="white", command=calculate_age, relief="raised", bd=2)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font="Arial 14 bold", bg="#f0f0f0")
result_label.pack(pady=5)

root.mainloop()
