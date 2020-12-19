

from time import sleep
import os

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

# Display a title bar.
print("\t**********************************************")
print("\t***  Greeter - Hello old and new friends!  ***")
print("\t**********************************************")

# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

# Print each name 5 times.
for name in names:
    # Clear the screen before listing names.
    os.system('clear')
    
    # Display the title bar.
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")

    print("\n\n")
    for x in range(0,5):
        print(name.title())
    
    # Pause for 1 second between batches.
    sleep(1)

