
# def args(*name):
#     for i in name:
#         print(i)
#
# args("ram","pranav","kumar")

dic = {"pravin":"web developer","mayur":"Commers"}
def dic_args(*args,**kwargs):
    for key, value in kwargs.items():
        print(key," is ",value)

dic_args()