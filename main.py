while True:
    try:
        inputOne = input("Please enter first number: ")
        inputOne = float(inputOne)
        break
    except ValueError:
        print("Invalid input. Please enter a valid float.")
while True:
    try:
        inputTwo = input("Please enter second number: ")
        inputTwo = float(inputTwo)
        break
    except ValueError:
        print("Invalid input. Please enter a valid float.")
while True:
    inputOp = input("Please enter an arithmetic operation (+, -, *, /, **): ")
    if inputOp in ['+', '-', '*', '/', '**']:
        break
    else:
        print("Invalid input. Please enter a valid arithmetic operation.")

if inputOp == '+':
    output = float(inputOne + inputTwo)
elif inputOp == '-':
    output = float(inputOne - inputTwo)
elif inputOp == '/':
    output = float(inputOne / inputTwo)
elif inputOp == '*':
    output = float(inputOne * inputTwo)
else:
    output = float(inputOne ** inputTwo)
print(str(inputOne) + str(inputOp) + str(inputTwo) + " = " + str(output))