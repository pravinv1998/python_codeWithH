
def read_file(filename):
    '''
    'This function use only for read content
    from file and display on command line'
    '''
    file_content = open(filename)
    read_data = file_content.read()
    file_content.close()
    return read_data


n=read_file("name.txt")
print(n)

print(read_file.__doc__)


# read the content from file

