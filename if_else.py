
age=int(input("Enter your age: "))

if age<100 and age>18:
    print("You are able to drive,Please collect your license from office")
elif age==18:
    print("We are not able to issue license to you,Please visit RTI office.")
elif age<18:
    print("Your age is not sufficient to drive.")
else:
    print("You are out of age limit")

# list=[1,2,3,4]
#
# if 3 in list:
#     print("given no. in the list" )
