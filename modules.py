import utility  #importing a module using the import statement

"""
Everytime I run a .py file with an imported module it will create a 
cache file with .pyc extension so when we run that code again it will run that
cache file rather than the original py module
"""

print(type(utility))  #it will print the type of utility which should be <class 'module'>
print(utility.add(2,3))  #using the functions the utility module offers us
print(utility.subtract(2,3))
print(utility.multiply(2,3))
print(utility.divide(2,3))