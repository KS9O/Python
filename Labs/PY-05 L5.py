import random
# lock random number
random.seed(0)
def generate_random():
    return random.randint(1, 100)




def main():
    guessed_number = int(input("Please enter a number between 1 and 100: "))
    random_num = generate_random()
    while guessed_number != random_num:
        print("Unsuccessful Guess!")
        guessed_number = int(input("Please enter a number between 1 and 100: "))
    
    print(f"successful guess random number was {random_num}")

if __name__ == "__main__":
    main()