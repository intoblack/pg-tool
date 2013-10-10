#-*- coding:utf-8 -*-
#!/usr/bin/env python

from    Tkinter import Tk
from Tkinter import Label
from Tkinter import Button
from Tkinter import Widget


class Config(dict):
    
    _argname = []
    
    
    def __init__(self ,arglist = [] , arg_dict = {} ,*argname , **arg_value):
        dict.__init__(self)
        if len(arg_value):
            if arg_value.has_key('argname'):
                if isinstance(arg_value['argname'], list):
                    self._argname.extend(arg_value['argname'])
                else:
                    self._argname.append(arg_value['argname'])
            if arg_value.has_key('arg_value') and isinstance(arg_value['arg_value'], dict):
                for _key , _val in arg_value['arg_value'].items():
                    self.add(_key, _val)
    
    
    def add(self , key , value):
        if key and value and key in self._argname:
            self[key] = value


class TkConfig(Config):
    
    
    def __init__(self):
        Config.__init__(self,argname = ['background','bg','borderwidth','bd','class','clormap','container','cursor','height','highlightbackground','highlightcolor','padx','pady','relief','takefocus','visual','width',])
    
    def set_width(self , width):
        if self.is_value(width, int):
            self.add('width', width)
    
    
    def is_value(self , n , tp , _min = None , _max = None):
        if isinstance(n, tp):
            if _min:
                if n > _min:
                    return True
            elif _max:
                if n < _max:
                    return True
            else:
                return True
        return False

 
        
    
    
    
    
    


class Window(Tk):
    _width = 0 
    _height = 0
    _widgt = []
    
    def set_title(self , title , width = 100 , height = 100):
        self.set_window_size(width, height)
        self.title(title)
        
    
    def set_window_size(self , width , height):
        if not (isinstance(width , int) and isinstance(height , int)):
            raise TypeError
        self._width = width
        self._height = height    
        self.geometry('%sx%s' % (width,height))
    
    
    def add(self , widgt):
        if isinstance(widgt, Widget):
            self._widgt.append(widgt)
            widgt.pack()
    
    
        
    
    



class TLabel(Label):
    
    def __init__(self , frame = None , text=''):
        if  frame and not ( isinstance(frame, Window) and text):
            raise TypeError
        Label.__init__(self, master = frame, text = text)
        
    
    

class PButton(Button):
    
    def __init__(self , frame = None , text = ''  , command = None):
        if  frame and  not ( isinstance(frame, Window) and text):
            raise TypeError
        if not command and  frame:
            command = frame.quit
        Button.__init__(self, frame , text = '' , fg = 'red' , command = command)
        self.pack()


    
    
    
    
    

if __name__ == "__main__":
    t = TkConfig(argname = ['k','c'], value = {'k':1})
    print t
#     w = Window()
#     w.set_title("x")
#     w.set_window_size(200, 200)
#     t = TLabel( text = 'hello')
#     b = PButton( text = 'x')
#     w.add(t)
#     w.add(b)
#     
#     w.mainloop()
    
    