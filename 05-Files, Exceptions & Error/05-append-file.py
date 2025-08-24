with open("my_file.txt","a") as file:
    file.write("\nwelcome to the course")

with open("my_file.txt","r") as file:
    print(file.read())
