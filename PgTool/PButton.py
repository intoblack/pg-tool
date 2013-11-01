#!/usr/bin/env python
# coding=utf-8

from Tkinter import Button
from pgconfig import PConfig
from Tkinter import Frame


class PButton(Button, PConfig):

    def __init__(self, master=None, title='', name = 0 , command = None):
        Button.__init__(self, master=master, text=title , command = command)
        self.__name = name


    def get_name(self):
    	return self.__name




class PNumButton(Frame):


    def __init__(self, master=None):
        Frame.__init__(self , master = master)
        self.__button_list = []
        for i in range(9):
        	__button = PButton(self , title = '%s' % i , name = i)
        	__button.grid(row = i / 3 , column = i % 3)
        	__button.bind('<ButtonRelease-1>', self.call_back)
        	self.__button_list.append(__button)


    def call_back(self , event):
    	self.__hit = e.widget.get_name()



