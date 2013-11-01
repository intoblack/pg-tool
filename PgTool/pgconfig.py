#!/usr/bin/env python
#coding=utf-8


from PgException import PGException
from PgException import NoRunableException


class PState(object):


    def __set_state(self , _state):
        self['state'] = _state


    def set_disable(self):
        self.__set_state('disable')


    def set_active(self):
        self.__set_state('active')

    def set_normal(self):
        self.__set_state('normal')

    def set_readonly(self):
        self.__set__state('readonly')


    def set_callback(self , _command = None):
        if _command and callable(_command):
            self['command'] = _command
        else:
            raise NoRunableException,'callback'



