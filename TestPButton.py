#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append("./PgTool")
from Tkinter import Tk
from PButton import PNumButton



if __name__ == "__main__":
	t = Tk()
	k = PNumButton(t)
	k.pack(side = 'left')
	t.mainloop()
