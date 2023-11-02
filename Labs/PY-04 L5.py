# OS module and file manipulation
import os

file_name = input("Choose a filname: ")

#for mac and linux add -c 4 flag
os.system(r'ping 8.8.8.8 >> "' + file_name + '".txt"')

# open file that was saved
with open(file_name+ '.txt', 'r') as file:
    if "ms" in file.read():
        print("You have an internet connection.")
    else:
        print("You do not have an internet connection.")
