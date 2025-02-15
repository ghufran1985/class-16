import tkinter as tk

root = tk.Tk()
root.title("Welcome Screen")

welcome = tk.Label(root, text="Welcome to our application")
welcome.pack(pady=10)

name = tk.Label(root, text="name")
name.pack(pady=10)

submit = tk.Button(root, text="submit")
submit.pack(pady=10)

thanks = tk.Label(root, text="Thanks for your reg")
thanks.pack(pady=10)

root.mainloop()