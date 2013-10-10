#-*- coding:utf-8 -*-
#!/usr/bin/env python

from    Tkinter import Tk
from Tkinter import mainloop
from Tkinter import Label
from Tkinter import Button



class Window(Tk):
    _width = 0 
    _height = 0
    
    def set_title(self , title , width = 100 , height = 100):
        self.set_window_size(width, height)
        self.title(title)
        
    
    def set_window_size(self , width , height):
        if not (isinstance(width , int) and isinstance(height , int)):
            raise TypeError
        self._width = width
        self._height = height    
        self.geometry('%sx%s' % (width,height))
    
    



class TLabel(Label):
    
    def __init__(self , frame , text=''):
        if not ( isinstance(frame, Window) and text):
            raise TypeError
        Label.__init__(self, master = frame, text = text)
        self.pack()
    

class PButton(Button):
    
    def __init__(self , frame , text = ''  , command = None):
        if not ( isinstance(frame, Window) and text):
            raise TypeError
        if not command:
            command = frame.quit
        Button.__init__(self, frame , text = '' , fg = 'red' , command = command)
        self.pack()


    
    
    
    
    

if __name__ == "__main__":
    w = Window()
    w.set_title("x")
    w.set_window_size(200, 200)
    t = TLabel(w, 'hello')
    b = PButton(w , 'x')
    mainloop()
    
    