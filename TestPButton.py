#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append("./PgTool")
from Tkinter import Tk
from PButton import PNumButton

def p(index , widget):
	widget.set_disable()
		

if __name__ == "__main__":
	t = Tk()
	k = PNumButton(t , hit_call_back = p, row_count = 7)
	k.pack(side = 'left')
	t.mainloop()
