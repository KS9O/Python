# Recursive Search

myList = [1, 2, "a", [4, 5, "b", 6],[7, [8, "d", 9]]]

def print_numbers(item_list):
    #crawl list
    for item in item_list:
        # search for nmumb
        if type(item) == int:
            print(item)
        elif type(item) == list:
            print_numbers(item)
            
                


print_numbers(myList)
