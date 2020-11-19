# my_file = open('test.txt')

# print(my_file.read())
#*set cursor to specific position
# my_file.seek(0)
# print(my_file.read())

#* read each by one line
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

#* read all lines, return a list

# !! ALWAYS close the file onces you finish
# my_file.close()


#* THIS IS THE "CORRECT" WAY OF FILE I/O
#* I DO NOT NEED TO BE AWARE OF .close()

modes:{
    'r': 'read',
    'r+': 'read & write, overwite the file starting at position 0. If the is more content than what u are writting, it will remain',
    'w': 'write, the filw will only have what u r writting. Also if the file doss not exist it will creat it.',
    'a': 'append, appends at the end of the file, without overwritting',
}

try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.readlines())
        # text = my_file.write("Heeeey it's me!!")
        # text = my_file.write(":(")
        # print(text)
except FileNotFoundError as err:
    print('Motherfuckeeer, enter the correct PATH!')
    raise err