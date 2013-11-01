#!/usr/bin/env python
# coding=utf-8

from Tkinter import Button
from pgconfig import PConfig
from Tkinter import Frame


class PButton(Button, PConfig):

    def __init__(self, master=None, title='', command=None):
        Button.__init__(self, master=master, text=title, command=command)
        self.__name = title

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__name


class PNumButton(Frame, PConfig):

    def __init__(self, master=None, hit_call_back=None, button_names=[] , row_count = 3 , clounm_count = 3):
        Frame.__init__(self, master=master)
        self.__button_list = []
        if isinstance(button_names, dict) and len(button_names) != 0 and len(button_names) >= (row_count * clounm_count):
        	for i in range(row_count * clounm_count):
        		__button = PButton(self, title='%s' % button_names[i])
        		__button.grid(row=i / row_count, column=i % row_count)
        		__button.bind('<ButtonRelease-1>', self.call_back)
        		self.__button_list.append(__button)
            # tk回调是不能传递参数的 ， 所以只能利用监
        else:
        	for i in range( row_count * clounm_count):
        		__button = PButton(self, title='%s' % i)
        		__button.grid(row=i / row_count, column=i % row_count)
        		__button.bind('<ButtonRelease-1>', self.call_back)
        		self.__button_list.append(__button)
            
        self.__call_back = hit_call_back

    def call_back(self, event):
        __index = event.widget.get_title()
        if self.__call_back:
            self.__call_back(__index, event.widget)
        # self.hit_button(__index , event.widget )

    # def hit_button(self , name , widget):
    # 	pass
