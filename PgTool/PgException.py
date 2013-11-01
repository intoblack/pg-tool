#!/usr/bin/env python
#coding=utf-8



class PGException(Exception):


    def __init__(self , msg = None, code = None):
        Exception.__init__(self)
        if msg and isinstance(msg , str) or isinstance(msg , unicode):
            self.__msg = msg
        else:
            self.__msg = None
        if code and isinstance(code , int) or isinstance(code , long):
            self.__code = code
        else:
            self.__code = None

    def __str__(self):
        if self.__msg and self.__code:
            return '%s,%s' % (self.__msg , self.__code)
        elif self.__msg and not self.__code:
            return self.__msg
        else:
            return ''



class NoRunableException(TypeError):
    pass

