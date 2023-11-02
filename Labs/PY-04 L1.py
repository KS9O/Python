# handling divison by zero w/ try/execpt
# start try
try:
    # get user input for maths
    num1 = int(input("Please enter a number: "))
    num2 = 0
    # try to divide
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Can't calculate it")
except ValueError:
    print("Something went wrong!")