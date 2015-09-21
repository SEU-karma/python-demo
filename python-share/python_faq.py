# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

"""
compare the output with python_faq_import
"""

import os

print "__name__:", __name__
print "__file__:", __file__

print "#" * 50
print os.getcwd()
print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print os.path.basename(os.path.abspath(__file__))


class Horizon(object):

    """docstring for Horizon"""

    def __init__(self, arg):
        super(Horizon, self).__init__()
        self.arg = arg

print "Horizon.__module__:", Horizon.__module__
print "Horizon.__doc__:", Horizon.__doc__

# print __module__

if __name__ == "__main__":
    print "this file executes directly!"
