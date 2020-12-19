from time import sleep
import os

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")
    

# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

# Print each name 5 times.
for name in names:
    display_title_bar()

    print("\n\n")
    for x in range(0,5):
        print(name.title())
    
    # Pause for 1 second between batches.
    sleep(1)
