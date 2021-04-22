# f = open("name2.txt","w")
# a = f.write("Pravin Vargad")
# print(a)
# f.close()

def write_file(file_name,file_content):
    '''

     this function use to only write file,
     their is file name and file content need to specified..

    '''
    write_content = open(file_name,"w")
    write_file = write_content.write(file_content)
    write_content.close()


def read_write(filename, file_content):
    '''

     this function use to read and write file content,
     this must be append and also write file as well...

    '''
    content = open(filename, "r+")
    read = content.read()
    write = content.write(file_content)
    read2 = content.read()
    content.close()
    return read2

# write_file("name2.txt","pravin vargad!!!!!!")

# read_write("name2.txt","read and write function worked..\n")

print(read_write.__doc__)