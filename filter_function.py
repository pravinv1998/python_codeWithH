li = [1,2,3,4,5,6,7,8,9,0]

def is_greter_than(num1):
    return num1 > 5

greter_than = list(filter(is_greter_than,li))
print(greter_than)