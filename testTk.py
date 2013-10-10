#-*- coding:utf-8 -*-
#!/usr/bin/env python

from    Tkinter import Tk
from Tkinter import mainloop
import time



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
    
    

if __name__ == "__main__":
    w = Window()
    w.set_title("x")
    w.set_window_size(100, 100)
    time.sleep(10)
    w.set_window_size(200, 200)
    mainloop()
    
    