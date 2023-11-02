# User Dicitionary
# How can you change this so that it
    # 1. uses the ports as integers!
    #2. Checks to see if user wants to break w/o multiplel checks in time
# Create empty dicitionary
servicePorts = {}

# Create loop
while True:
        # get user input for service
        service = input("Please enter a service's name or type '0' to stop: ")

        # check to see if the user typed 0 to stop the loop
        if service == '0':
                # exit the loop
                break
        
    # Get port number from user
        port = input("Please enter a port number or '0' to stop: ")
        # check here to see if they want to exit
        if port == '0':
            break

            # Take input and insert key:value into the dictionary
        servicePorts[service] = port
print(servicePorts)
