# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

from package import *

def main():
    module1.module_method()
    module2.module_method() # Module2 wasn't exported so even when importing all we wont get module2

if __name__ == "__main__":
    main()
