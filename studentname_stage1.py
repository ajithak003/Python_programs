def calculateresult(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Modulo by zero is not allowed."
    else:
        return "Error: Invalid operator."

    return result

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")
    result = calculateresult(num1, num2, operator)
    print("The result of", operator, "between", num1, "and", num2, "is:", result)
