
from tkinter import *

root = Tk()
col = StringVar()
l = Label(text="Pick a color name")
l.pack()
e = Entry(root)
e.config(textvariable=col)
e.pack()
btn = Button(root, text="OK", command=root.quit)
btn.pack()
root.mainloop()
print(col.get())
