﻿import tkinter as tk
win = tk.Tk()
win.geometry("100x100")
win.title("grid佈局")

one=tk.Button(win, width=20, text="January")
one.grid(column=0,row=0)
two=tk.Button(win, width=20, text="Februry")
two.grid(column=1,row=0)
three=tk.Button(win, width=20, text="March")
three.grid(column=2,row=0)
one=tk.Button(win, width=20, text="April")
one.grid(column=0,row=1)
two=tk.Button(win, width=20, text="May")
two.grid(column=1,row=1)
three=tk.Button(win, width=20, text="June")
three.grid(column=2,row=1)
one=tk.Button(win, width=20, text="July")
one.grid(column=0,row=2)
two=tk.Button(win, width=20, text="August")
two.grid(column=1,row=2)
three=tk.Button(win, width=20, text="September")
three.grid(column=2,row=2)
one=tk.Button(win, width=20, text="October")
one.grid(column=0,row=3)
two=tk.Button(win, width=20, text="November")
two.grid(column=1,row=3)
three=tk.Button(win, width=20, text="December")
three.grid(column=2,row=3)

win.mainloop()
