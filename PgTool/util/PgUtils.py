# coding=utf-8
#!/usr/bin/env python


import re


color_reg = re.compile('^#([\w\d]{1,2}){0,3}$').match
color_list = ['red', ' blue', 'yellow', 'black', 'white', 'green', 'gray']


def judge_color(color):
    if not (color and isinstance(color, str)):
        raise TypeError, color
    if color in color_list:
    	return True
    _match = color_reg(color)
    if _match:
        return True
    else:
        return False


if __name__ == '__main__':
    print judge_color("#2333cc")
    print judge_color("sdfasdf")
