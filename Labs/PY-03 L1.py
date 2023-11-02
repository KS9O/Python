# Range Function
# range(stop) will make a number list from 0 to stop (non inclusive)
# range(start, stop) will make a list from start (inclusive) to stop (non inclusive)
# ramge(start, stop, step) will make a list from start to stop, by step

# Grab bounds from range and cast to int since inpuit returns a string
upper_bound = int(input("Choose the range upper bound --> "))

# loop
for x in range(1, upper_bound):
    print(f"The next number in line is {x}.")


