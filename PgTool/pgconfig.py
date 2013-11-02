#!/usr/bin/env python
# coding=utf-8


from PgException import NoRunableException
from PgException import IllegalArugments


class PConfig(object):

    def __set_state(self, _state):
        self['state'] = _state

    def get_state(self):
        return self['state']

    def set_disable(self):
        self.__set_state('disable')

    def set_active(self):
        self.__set_state('active')

    def set_normal(self):
        self.__set_state('normal')

    def set_readonly(self):
        self.__set__state('readonly')

    def __set_color(self, name, color):
        self[name] = color

    def set_fg(self, color):
        self.__set_color('fg', color)

    def set_bg(self, color):
        self.__set_color('bg', color)

    def set_callback(self, _command=None):
        if _command and callable(_command):
            self['command'] = _command
        else:
            raise NoRunableException, 'callback'

    def get_null_call_back(self, event):
        return

    def check_parment(value, _type, max=None, min=None):
        if isinstance(value, _type):
            if max:
                if value > max:
                    return False
            if min:
                if value < min:
                    return False
            return True
        else:
            return False

    def color(red, green, blue):
        if not (self.check_parment(red, int, 255, 0) and self.check_parment(green, int, 255, 0) and self.check_parment(blue, int, 255, 0)):
            raise IllegalArugments
        return '#%02s%02s%02s' % (red, green, blue)
