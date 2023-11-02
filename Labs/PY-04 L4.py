# Extracting lines!

# Get file path
path = input(" Enter a directory path for the text file: ")
# get file name
filename = input("Enter full filename: ")

# open filename
try:
    # adding path and \ and filename for the file name
    file = open(path+"\\"+filename, "r")
    # read EACH line in the file
    for line in file:
        print(line)
except Exception as e:
    print(e)


file.close()