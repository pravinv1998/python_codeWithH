# check given list ,check given data is number and it is greter than 6

list=[1,2,3,6,8,9,76,88,3,90,45]
for item in list:
    if str(item).isnumeric() and item>6:
       print(item)

