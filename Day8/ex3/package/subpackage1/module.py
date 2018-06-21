from ..subpackage2 import module
from ..external import external_method


def module_method():
	module.module_method('Called From SubPackage1')
	external_method('Called From SubPackage1')