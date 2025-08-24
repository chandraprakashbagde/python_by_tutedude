filename = "output.txt"
file = open(filename,"a")

fileContent = input("Enter text to write to the file: ")
additionalFileContent = ""

file.write(fileContent+"\n")
print(f"Data successfully written to {filename}\n")

additionalFileContent = input("Enter additional text to append: ")
file.write(additionalFileContent+"\n")
file.close()
print("Data successfully appended.\n")

file = open(filename,"r")
print(f"Final content of {filename}:")
print(file.read())
