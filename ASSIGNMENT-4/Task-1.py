filename = "sample.txt"
try:
    lineNumber = 1;
    with open(filename,"r") as file:
        for line in file:
            print(f'Line {lineNumber}: {line}')
            lineNumber+=1
except Exception as e:
    print(f"Error: The file '{filename}' was not found.")