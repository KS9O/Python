

count = 0
def recur(count): 
    # base case ( when to end)
    if count == 10:
        return
    
    # do something
    print("*" * count)

   # incremenet count
    count += 1
    # recursive call
    recur(count)

recur(count)