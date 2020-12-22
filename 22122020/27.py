import re
email_sample='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):
    if(re.search(email_sample,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
if __name__=='__main__' :
 email=str(input("enter your email ID : "))
 #email="rahul@gmail.com"
 check(email)
