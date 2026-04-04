import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length = 10, complexity = "medium"):
    length = password_length.get()
    complexity = complex_ity.get()
    combination = ""
    password = ""
    
    if not length.isdigit():
        messagebox.showerror("Error", "Enter a Integer number.")
        return
    length = int(length)
    if length <= 8:
        messagebox.showwarning("Warning", "Length must be 8 or more")
        return
    
    if complexity.lower() == "high":
        combination = string.ascii_letters + string.digits + string.punctuation
    elif complexity.lower() == "medium":
        combination = string.ascii_letters + string.digits 
    elif complexity.lower() == "low":
        combination = string.ascii_letters 
    else:
        messagebox.showwarning("Warning", "! Invalid Input Enter only [High / Medium / Low]")
        return None
    
    for i in range(length):
        password += random.choice(combination)
        
    show_password.set(password)
    password_length.delete(0, tk.END)
    complex_ity.delete(0, tk.END)

main_page = tk.Tk()
main_page.title("🧮 Password Generator Application")
main_page.geometry("410x350")
main_page.config(bg="crimson")

tk.Label(main_page, text= "🔐PASSWORD GENERATOR", font=("Georgia", 20, "bold"), bg="gray", fg="white", width=40).pack(pady=0)

tk.Label(main_page, text = "Enter Length", font=("Georgia", 10, "bold"), bg="crimson", fg="White",).pack()
password_length = tk.Entry(main_page,font=("Courier", 13), bg="white", fg="crimson", width=30, bd=0,)
password_length.pack(pady=10, ipady=5)

tk.Label(main_page, text = "Complexity: (Ex: High / Medium / Low)", font=("Georgia", 10, "bold"), bg="crimson", fg="White",).pack()
complex_ity = tk.Entry(main_page,font=("Courier", 13), bg="#f0f0f0", fg="crimson", width=30, bd=0,)
complex_ity.pack(pady=10, ipady=5)

tk.Button(main_page, text="Generate Password", width=20, font=("Georgia", 10, "bold"), bg = "gray", fg= "white", bd = 0, command=generate_password).pack(pady=5, ipady=5)

show_password = tk.StringVar()
tk.Entry(main_page, textvariable=show_password, width=30, font=("Georgia", 10, "bold"), bg = "Gold", fg= "Crimson", bd = 0,).pack(pady=10, ipady=5)

main_page.mainloop()
