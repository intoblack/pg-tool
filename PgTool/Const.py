# coding=utf-8
#!/usr/bin/env python

from PgException import IllleaglJob


class ConstObject(object):

    def __setattr__(self, name, value):
        return

    def __delattr__(self, name):
        raise IllleaglJob, 'delete const type'


class Relief(object):

    FLAT = "flat"
    SUNKEN = "sunken"
    RAISED = "raised"
    GROOVE = "groove"
    RIDGE = "ridge"


class Const(object):

	relief = Relief()
