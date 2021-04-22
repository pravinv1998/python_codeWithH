'''
 this program is use to log perticular persons food data
'''
def getdate():
    import datetime
    return datetime.datetime.now()

# print(getdate())

try:

    def write_log(name,food_item):
        '''
         this function use for only write file at append mode
        :param name: name and food_item
        :param food_item: get food name as string
        :return: nothing to return just write log file
        '''
        if name == 1:
            pravin_log = open("pravin.txt", "a")
            pravin_log.write(str([str(getdate())]) + " : " + food_item + "\n")
            pravin_log.close()
        elif name == 2:
            mayur_log = open("mayur.txt", "a")
            mayur_log.write(str([str(getdate())]) + " : " + food_item + "\n")
            mayur_log.close()
        elif name == 3:
            pranav_log = open("pranav.txt", "a")
            pranav_log.write(str([str(getdate())]) + " : " + food_item + "\n")
            pranav_log.close()
        else:
            pass


    def read_log(name):
        if name == 1:
            pravin_log = open("pravin.txt")
            data = pravin_log.read()
            for i in data:
                print(i, end="")
            pravin_log.close()
        elif name == 2:
            mayur_log = open("mayur.txt")
            data = mayur_log.read()
            for i in data:
                print(i, end="")
            mayur_log.close()
        elif name == 3:
            pranav_log = open("pranav.txt")
            data = pranav_log.read()
            for i in data:
                print(i, end="")
            pranav_log.close()
        else:
            pass


    def health_management_system():
        '''
        this function use to read and write function,
        write_log() and read_log() function used...

        :return:
        '''
        act = int(input("Enter \n 1.Add Log \n 2.Read Log\n"))

        if act == 1:
            inp = int(input("Enter\n 1.Pravin\n 2.Mayur\n 3.Pranav"))
            food_item = input("Enter Food Item: ")
            write_log(inp,food_item)
            value = input("Do You Want to add or view log y or n\n ")
            if value == "y":
                health_management_system()
            elif value == "n":
                pass
            else:
                pass

        elif act == 2:
            inp = int(input("Enter\n 1.Pravin\n 2.Mayur\n 3.Pranav"))
            read_log(inp)
            value = input("Do You Want to add or view log  y or n\n ")
            if value == "y":
                health_management_system()
            elif value == "n":
                pass
            else:
                pass

        else:
            pass

    # call main function
    health_management_system()


except Exception as a:
    print(a)
