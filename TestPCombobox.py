#!/usr/bin/env python
# coding=utf-8


import sys
sys.path.append("./PgTool")
from Tkinter import Tk
from PCombobox import PCombobox


def c():
    	print p.get_select_string() 

if __name__ == "__main__":

    tk = Tk()
    p = PCombobox(tk , combobox_callback = c)
    p.set_choices([12,23])
    p.pack(side='left' , fill = 'both')
    print p.config()
    tk.mainloop()
