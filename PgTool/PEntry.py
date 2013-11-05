#!/usr/bin/env python
# coding:utf-8

from Tkinter import Entry
from pgconfig import PConfig
from Tkinter import END
from PgException import IllegalArugments
from Const import Relief
from Const import Const
import sys
sys.path.append("../util")
from PgUtils import judge_color


class PEntry(Entry, PConfig):

    def __init__(self, main_window=None, command=None, textvar=None):
        Entry.__init__(self, master=main_window, textvariable=textvar)

    def set_pass_word(self, mask='*'):
        if not isinstance(mask, str):
            return
        self['show'] = mask

    def clear_all(self):
    	self.delete(0, END)

    def get_text_index(self):
    	return self.index(END)

    def get_cursor_index(self):
    	# return len(self.)
    	pass

    def set_box_style(self, _style=Const.relief.RAISED):
		if _style and isinstance(_style, Relief):
			raise IllegalArugments, _style
		self['relief'] = _style


	def set_selectbg_color(self,color):
		if not judge_color(color):
			raise IllegalArugments,color
		self['selectbackground'] = color









