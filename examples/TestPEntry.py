#!/usr/bin/env python
#coding=utf-8


from Tkinter import Tk
import sys
sys.path.append('../PgTool')
from PEntry import PEntry
from Tkinter import Button
from Tkinter import END
from Const import Const



t = Tk()
p = PEntry(t)
def get():
	# print p.insert(len(p.get()),'abcd')
	print p.index(END)
b = Button(t , command = get)
p.pack()
b.pack()
p.set_box_style(Const.relief.SUNKEN)
t.mainloop()