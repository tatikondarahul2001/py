def GCD(a,b):
 while(b):
  a,b=b,a%b
 return a
a=int(input("enter the number: "))
b=int(input("enter the number: "))
print("the gcd of ",a,"and",b,"is : ",end=" ")
print(GCD(a,b))
