#1

'''
file1 = open("my_file.txt","r")
    print(file1.read())
    print(file1.readline())
    print(file1.readlines())
file1.close()
'''

#2

with open("my_file.txt","r+") as file1:
    print(file1.read())