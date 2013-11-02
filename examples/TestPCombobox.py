#!/usr/bin/env python
# coding=utf-8


import sys
sys.path.append("../PgTool")
from Tkinter import Tk
from PCombobox import PAutoCompleteCombobox

def c(a , *x):
	print a,x


if __name__ == "__main__":

    tk = Tk()
    p = PAutoCompleteCombobox(tk)
    p.set_choices([12,23])
    p.pack()
    
    tk.mainloop()
