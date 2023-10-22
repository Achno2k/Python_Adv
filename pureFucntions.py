# from functools import reduce 
# # map(), filter(), zip() and reduce() --> all these are pure functions
my_list = [1,2,3]
your_list = [4,5,6]

# # 1. map()
# def multiply_by_2(item):
#     return item*2

# print(list(map(multiply_by_2, [1,2,3])))


# print(list(map(multiply_by_2, my_list)))
# print(my_list)  #dosen't change the original list

# #2. filter()
# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))
# print(my_list)

# #3. zip()
# print(list(zip(my_list, your_list)))

# #4. reduce()
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list, 0))

# #5. lambda expressions
# print(list(map(lambda item: item*2, my_list)))
# print(list(filter(lambda item: item % 2 != 0, my_list)))
# print(reduce(lambda acc, item: acc + item, my_list))



print(list(map(lambda item: item**2, my_list)))

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda x: x[1])
print(a)
 