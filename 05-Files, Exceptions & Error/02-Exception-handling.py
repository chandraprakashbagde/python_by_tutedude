
try:
    number = int(input("Enter a number: "))
    print(number/0)
except Exception as e:
    print(e)
finally:
    print("Runs with no error..")

print("Runs with no error..")