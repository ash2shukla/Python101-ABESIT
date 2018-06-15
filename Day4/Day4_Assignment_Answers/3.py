# lambda expression to check if a string is float
# if a string is float then the first character MUST be digit
# there must be only 1 dot (.)
# if we replace the 
isfloat = lambda string: (string[0].isdigit() and string.count('.')==1 and string.replace('.','',1).isdigit())

print(isfloat('1.2.3')) # False
print(isfloat('1.2')) # True
print(isfloat('.2')) # False
print(isfloat('a.b')) # False
print(isfloat('abcd')) # False
