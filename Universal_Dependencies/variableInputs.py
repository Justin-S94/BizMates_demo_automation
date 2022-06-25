import time

epoch_time = str(int(time.time()))
print("The current time in epoch is: "+epoch_time)

class variableInputs:
    websiteURL = 'https://www.demoblaze.com/index.html'
    username = 'test_justin'
    password = 'test_justin_password'
    unique_username = username+epoch_time
    unique_password = password+epoch_time
    waitDelay = 1000