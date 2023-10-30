from collections import Counter, defaultdict, OrderedDict
from array import array

"""
Recently, pyhton made dictionaries ordered
by default, so you dont need to use orderedDict
"""

li = [1,2,3,5,3,1]
print(Counter(li))

sentence = "I am thinking about Python"
print(Counter(sentence))

# dict1 = {'a' : 1, 'b' : 2}
# print(dict['c'])        #this should give an error because c doesn't exist

dict2 = defaultdict(lambda : 5, {'a' : 1, 'b' : 2})
print(dict2['c'])        #this will give a non existent key a default value of 5

dict3 = OrderedDict()
dict3['a'] = 1
dict3['b'] = 2

dict4 = OrderedDict()
dict4['b'] = 2
dict4['a'] = 1

print(dict3 == dict4)



arr = array('i', [1,2,3])
print(arr)
print(arr[0])       #arr[0] = 1


