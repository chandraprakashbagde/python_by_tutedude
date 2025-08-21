operand_1 = int(input("Enter operand 1: "));
operand_2 = int(input("Enter operand 2: "));
operator  = input("Enter operator (+, -, *, /)")

resultMessage = f'Result of {operand_1} {operator} {operand_2} = ';
result = ''
if operator=="+":
    result = operand_1+operand_2;
elif operator=="-":
    result = operand_1-operand_2;
elif operator=="*":
    result = operand_1*operand_2;
elif operator=="/":
    result = operand_1/operand_2;
else:
    result = "None"

if(result != "None"):
    print(f'{resultMessage}{result}')
else:
    print(result)
    
print("Thank you")