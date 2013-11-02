#!/usr/bin/env python
# coding=utf-8


from ttk import Combobox
from Tkinter import Frame
from Tkinter import StringVar
from PgException import IllegalArugments
from pgconfig import PConfig
from Tkinter import INSERT
from Tkinter import END


class PCombobox(Frame, PConfig):

    def __init__(self, master=None, combobox_callback=None):
        Frame.__init__(self, master=master)
        self.__cb_stringvar = StringVar()
        self.__combobox = Combobox(
            master=self, textvariable=self.__cb_stringvar)
        if combobox_callback and callable(combobox_callback):
            self.__cb_stringvar.trace('w', self.__combobox_chang)
            self.__user_call_back = combobox_callback
        self.__combobox.pack()

    def set_choices(self, choices=[]):
        if isinstance(choices, list):
            self.__combobox['values'] = choices
        else:
            self.__combobox['values'] = []

    def set_text_aliagen(self, aliagn='left'):
        if isinstance(aliagn, str) and aliagn in ['left', 'center', 'right']:
            self.__combobox['justify'] = aliagn
        else:
            raise IllegalArugments, aliagn

    def get_select_string(self):
        return self.__cb_stringvar.get()

    def set_select_string(self, msg):
        if msg and (isinstance(msg, str) or isinstance(msg, unicode)):
            self.__cb_stringvar.set(msg)
        else:
            raise IllegalArugments, msg

    def __combobox_chang(self, *args):
        if self.__user_call_back:
            self.__user_call_back(self.get_select_string(), *args)


class PAutocompleteCombobox(Combobox):

        def set_completion_list(self, completion_list):
                self._completion_list = sorted(completion_list, key=str.lower)
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)
                self['values'] = self._completion_list

        def autocomplete(self, delta=0):

                if delta:
                        self.delete(self.position, END)
                else:
                        self.position = len(self.get())

                _hits = []
                for element in self._completion_list:
                        if element.lower().startswith(self.get().lower()):
                                _hits.append(element)
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits = _hits
                if _hits == self._hits and self._hits:
                        self._hit_index = (
                            self._hit_index + delta) % len(self._hits)
                if self._hits:
                        self.delete(0, END)
                        self.insert(0, self._hits[self._hit_index])
                        self.select_range(self.position, END)

        def handle_keyrelease(self, event):
                if event.keysym == "BackSpace":
                        self.delete(self.index(INSERT), END)
                        self.position = self.index(END)
                if event.keysym == "Left":
                        if self.position < self.index(END):
                                self.delete(self.position, END)
                        else:
                                self.position = self.position - 1
                                self.delete(self.position, END)
                if event.keysym == "Right":
                        self.position = self.index(END)
                if len(event.keysym) == 1:
                        self.autocomplete()
