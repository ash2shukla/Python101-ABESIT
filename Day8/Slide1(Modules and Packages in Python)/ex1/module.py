# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

def main():
    pass

def module_method():
    print('Module method called')


def _hidden_method():
    print('Should not be imported when import *')

if __name__ == "__main__":
    main()
