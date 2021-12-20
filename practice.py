import tkinter as tk
from tkinter.constants import CENTER

root = tk.Tk()

canvas = tk.Canvas(root, bg='blue')
canvas.pack()

frame = tk.Frame(root, bg='#CBDEA6')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text='this is a label', bg='yellow')

button = tk.Button(frame, text='Makes', bg='#424242', fg='silver')

button.pack()

root.mainloop()
