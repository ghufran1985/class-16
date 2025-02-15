from tkinter import *

window = Tk()
window.title("tkinter sample window ")
window.geometry('300x200')

greeting = Label(text="Hello user", fg='white', bg='black')
button = Button(text="click me", bg='blue', fg='white')
entry = Entry(fg="yellow", bg="blue", width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text="sample frame ")
label.pack()

textbox = Text(fg='white', bg='black')
textbox.pack()

window.mainloop()