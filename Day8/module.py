# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

import script3

def module_method():
    print('Module method called')


def _hidden_method():
    print('Should not be imported when import *')