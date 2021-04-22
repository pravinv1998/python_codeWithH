'''
 reduce function use
'''
from functools import reduce

list1 = [1,2,3,4,5]

# add all the numbers
# num = 0
# for i in list1:
#     num = num + i
# print(num)

# using reduce function

reduce_value = reduce(lambda x,y:x + y,list1)
print(reduce_value)

