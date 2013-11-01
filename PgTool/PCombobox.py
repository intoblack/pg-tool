#!/usr/bin/env python
# coding=utf-8


from ttk import Combobox
from Tkinter import Frame
from Tkinter import StringVar
from PgException import IllegalArugments
from pgconfig import PConfig

class PCombobox(Frame,PConfig):

    def __init__(self, master=None , combobox_callback = None):
        Frame.__init__(self, master=master)
        self.__cb_stringvar = StringVar()
        if combobox_callback and callable(combobox_callback):
        	self.__cb_stringvar.trace('w' , combobox_callback)
        self.__combobox = Combobox(master = self , textvariable = self.__cb_stringvar)

    def set_choices(self, choices=[]):
        if isinstance(choices, list):
            self.__combobox['values'] = choices
        else:
            self.__combobox['values'] = []

    def set_text_aliagen(self, aliagn='left'):
        if isinstance(aliagn ,str ) and aliagn in ['left', 'center', 'right']:
        	self.__combobox['justify'] = aliagn
        else:
        	raise IllegalArugments,aliagn



    def get_select_string(self):
    	return self.__cb_stringvar.get()


    def set_select_string(self , msg):
    	if msg and (isinstance(msg , str) or isinstance(msg ,unicode)):
    		self.__cb_stringvar.set(msg)
    	else:
    		raise IllegalArugments,msg
    








