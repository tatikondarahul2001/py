def palin(num):
 print(num)
num=input("enter a value : ")
print("The original number is : "+str(num))
res=str(num)==str(num)[::-1]
print("Is the number palindrome ? : " +str(res))
