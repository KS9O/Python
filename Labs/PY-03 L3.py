# Loops w/ Conditionals
import random
random.seed(22)
# initalize the counter
counter = 0

# Generate a list of 1000 random ints
myList = []
for random_num in range(0, 1001):
    # get random number
    my_rand = random.randint(0, 10000000)
    if my_rand not in myList:
        myList.append(my_rand)
print(myList) 



# 10 is not equal to 10 so that stops at 9
while counter < 10:
   
    # conditional to check chounter == to 6
    print(f"counter:{counter}")
    if counter == 6:
        print("Found!")
        # exit the loop
        break

     # increment counter to avoid infinity and beyond
    counter = counter + 1 # equivalent to counter += 1