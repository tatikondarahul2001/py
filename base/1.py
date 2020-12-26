print("1) Arithmetic operator")
print("2) Relational operator")
print("3) Logical operator")
print("4) Bitwise operator")
print("5) Assignment operator")
print("6) Special operator")
print("7) Membership operator")
print("8) Unary operator")
x=int(input("enter the number of operator set that you want to apply: "))
if(x==1):
 a=int(input("enter the value of a: "))
 b=int(input("enter the value of b: "))
 print("addition of two number is: ",(a+b))
 print("subtraction of two number is: ",(a-b))
 print("multiplication of two number is: ",(a*b))
 print("division of two number is: ",(b/a))
 print("modulus of two number is: ",(b%a))
 print("power function applied between two number is: ",(a**b))
 print("floor division applied for two number is: ",(b//a))
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
 a=str(input("type either true or false:"))
 b=str(input("type either true or false:"))
 print(a and b)
 print(a or b)
 print(not a)
 print(not b)
elif(x==4):
 a=int(input("enter the value of a: "))
 b=int(input("enter the value of b: "))
 print(a&b)
 print(a|b)
 print(~a)
 print(~b)
 print(a^b)
 print(b^a)
 print(a>>2)
 print(a<<2)
 print(b>>2)
 print(b<<2)
elif(x==5):
 a=int(input("enter the value of a: "))
 b=2
 print("value of b is : ",b) 
 a+=b
 print("sum ",a)
 a-=b
 print("difference ",a)
 a*=b
 print("multiplication ",a)
 a/=b
 print("division ",a)
 a//=b
 print("floor division ",a)
 a**=b
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
elif(x==8):
 a=input("enter the value of a : ")
 b=input("enter the value of b : ")
 
else:
 print("the set of operation that you want to perform does not exist......!!!")
