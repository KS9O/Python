# While loops w/ conditonals
# improvements
    #1. when out of money sprint shopping shopping_cart
    #2. check and sanitize input

# intialize vairables
money = 50
fruits = {"Apple": 5 ,"Raspberry": 10, "Lemon": 20}

# create a shopping cart as a list
shopping_cart = []

# Loop until something
while True:
    # check our fat duckets
    if money <= 0:
        print("Don't want no scrubs, go away!")
        break
    else:
        # get players choice of fruit
        player_choice = input(f"Select a fruit{fruits}:").title()
        # check if players choice is valid( meaniing its in the dicitonary)
        if player_choice in fruits:
            # if valid does the user have enough money?
            if money >= fruits[player_choice]:
                shopping_cart.append(player_choice)
                money = money - fruits[player_choice]
                print(f"Shopping cart:{shopping_cart} \n Money left: {money}")
            else:
                print(" You do not have enough money, get a job!")
        else:
            print("Invalid choice.")