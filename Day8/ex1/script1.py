# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

import module

def main():
    print(dir(module))
    print(globals())
    module.module_method()

if __name__ == "__main__":
    main()
