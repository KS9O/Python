# Create a Calculator

# Get info from user
def main():
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
operator = input("Please enter one of the following operators: +, -, *, / :")

# Define our functions
def add(num1, num2):
    description = f"{num1} + {num2} "
    return f"The result of {description} = {num1 + num2}"

def sub(num1, num2):
    description = f"{num1} - {num2} "
    return f"The result of {description} = {num1 - num2}"

def mult(num1, num2):
    description = f"{num1} * {num2} "
    return f"The result of {description} = {num1 * num2}"

def div(num1, num2):
    description = f"{num1} / {num2} "
    return f"The result of {description} = {num1 / num2}"

def calc():
    allowed_calculations = {"+": add, "-": sub, "*": mult, "/": div}
    try:
        result = allowed_calculations[operator](first_num, second_num)
        print(result)
    except KeyError
    print("The parameter doesn't exist.")
    
    except ZeroDivisionError
    print("Can't divide by zero.")

def main():
    calc()


if __name__ == "__main__":
    main()