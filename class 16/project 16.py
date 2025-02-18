import tkinter as tk
import random

def generate_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = "".join(random.choices(characters, k=12))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

password_var = tk.StringVar()
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=20)

generate_btn = tk.Button(text="Generate", command=generate_password, width=15, height=2)
generate_btn.pack(pady=10)

root.mainloop()