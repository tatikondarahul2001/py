n = int(input("enter the age of the person:"))
if(n >= 18):
    print("the person is eligible to vote !!!")
else:
    print("the person is not eligble to vote ")
    years = 18 - n
    print("you should wait for atleast " + str(years) + " years")