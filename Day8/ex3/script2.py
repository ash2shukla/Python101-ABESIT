# Name Clash
from package.subpackage1 import module as module1
from package.subpackage2 import module as module2

module1.module_method()

module2.module_method('Called From script2.py')