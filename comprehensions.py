#list
my_list1 = [char for char in 'hello']
print(my_list1)

my_list2 = [num for num in range(0,21)]
print(my_list2)

my_list3 = [num*2 for num in range(21)]
print(my_list3)

my_list4 = [num*2 for num in range(21) if num % 2 == 0]
print(my_list4)

#for set --> just change the [] to {}

# dictionary
simple_dict = {
    'a' : 1,
    'b' : 2
}

my_dict = {key:value**2 for key, value in simple_dict.items()}
print(my_dict)

my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)


#Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'n']
duplicates = []
duplicates =list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)