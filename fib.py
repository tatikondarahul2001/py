
def fib(n):
 if(n<2):
  return 1
 return (fib(n-1)+fib(n-2))
n=int(input("enter the number of terms: "))

for i in range(n):
 print(fib(i))
