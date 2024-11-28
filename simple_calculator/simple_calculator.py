def main():
    try:
        num1 = float(input("First number: "))
        operator = input("Operator: ")
        if operator not in "+-/*":
            raise ValueError("Please enter a valid operator")
        num2 = float(input("Second number: "))
    except ValueError as e:
        print(e)
    
    calculate(num1, operator, num2)

def calculate(num1, operator, num2):
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "/":
            result = num1 / num2
        case "*":
            result = num1 * num2
    print(result)

if __name__ == '__main__':
    main()