import shopping.shopping_cart  #this is a module from a package 
from shopping.shopping_package.more_shopping import print_item   #we have a package inside of a package

"""
-> whenever we create a package it automatically 
creates a __init__.py file in the package which is empty,

-> one good practice is that you should always explicitly mention
what functions you are importing when you import a package
"""

print(type(shopping.shopping_cart))    #<class 'module>
print(shopping.shopping_cart.buy("Monitor"))

print(print_item("Apple"))
