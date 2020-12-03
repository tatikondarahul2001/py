print("press 1 for arithmetic operator")
print("press 2 for relational operator")
print("press 3 for logical operator")
print("press 4 for bitwise operator")
print("press 5 for assignment operator")
print("press 6 for special operator")
print("press 7 for membership operator")
x=int(input("enter the number of operator set that you want to apply: "))
if(x==1):
 a=int(input("enter the value of a: "))
 b=int(input("enter the value of b: "))
 print("addition of two number is: ",(a+b))
 print("subtraction of two number is: ",(a-b))
 print("multiplication of two number is: ",(a*b))
 print("division of two number is: ",(a/b))
 print("modulus of two number is: ",(a%b))
 print("power function applied between two number is: ",(a**b))
 print("floor division applied for two number is: ",(a//b))
elif(x==2):
 a=int(input("enter the value of a: "))
 b=int(input("enter the value of b: "))
 print(a>b)
 print(a<b)
 print(a>=b)
 print(a<=b)
 print(a==b)
 print(a!=b)
elif(x==3):
 a=str(input("type either true or false: "))
 b=str(input("type either true or false: "))
 print(a and b)
 print(a or b)
 print(not a)
 print(not b)
elif(x==4):
 a=int(input("enter the value of a: "))
 b=int(input("enter the value of b: "))
 print(a&b)
 print(a/b)
 print(~a)
 print(~b)
 print(a^b)
 print(b^a)
 print(a>>2)
 print(a<<2)
elif(x==5):
 a=int(input("enter the value of a: "))
 a+=2
 print("sum ",a)
 a-=2
 print("difference ",a)
 a*=2
 print("multiplication ",a)
 a/=2
 print("division ",a)
 a//=2
 print("floor division ",a)
 a**=2
 print("power function ",a)
 a%=2
 print("modulus ",a)
elif(x==6):
 a1=int(input("enter a number: "))
 b1=int(input("enter a number: "))
 a2=str(input("enter a string: "))
 b2=str(input("enter a string: "))
 print(a1 is not b1)
 print(a2 is b2)
 print(a3 is b3)
elif(x==7):
 x=str(input("enter a string: "))
 y={3:'a',4:'b'}
 print("G" in x)
 print("it-a" not in x)
 print("AGI" not in x)
 print(3 in y)
 print("b" in y)
