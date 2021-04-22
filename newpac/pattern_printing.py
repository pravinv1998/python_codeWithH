
num = int(input("Enter any number: "))
value = bool(input("value= "))
# for i in range(0,num):
#     print()
#     for j in range(0,i+1):
#         print("*",end="")


if value == True:
    for i in range(0,num):
        print()
        for j in range(0,i+1):
            print("*",end="")
else:
    for i in range(num,0):
        print()
        for j in range(i-1,0):
            print("*",end="")



