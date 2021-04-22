
# def ab(no):
#     return no*no
#
# list_num = [1,2,3,4,5,6]
#
# square = list(map(ab,list_num))
# print(square)

# list_num = [1,2,3,4,5,6]
# square = list(map(lambda no:no*no,list_num))
# print(square)

def square(x):
    return x*x

def cube(x):
    return x*x

func = [square, cube]

for i in range(6): # tis loop use to calculate functions of list
    val = list(map(lambda x:x(i), func))
    print(val)