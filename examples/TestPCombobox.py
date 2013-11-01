#!/usr/bin/env python
# coding=utf-8


import sys
sys.path.append("../PgTool")
from Tkinter import Tk
from PCombobox import PCombobox

def c(a , *x):
	print a,x


if __name__ == "__main__":

    tk = Tk()
    p = PCombobox(master = tk , combobox_callback = c)
    p.set_choices([12,23])
    p.pack()
    
    tk.mainloop()
