import os
import time
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def printSlow(thisPrint,timeAmmount=0.5):
    print(thisPrint)
    time.sleep(timeAmmount)
def movingDisplay(ammount):
    for i in range(ammount):
        time.sleep(0.0)
        print("\n")
