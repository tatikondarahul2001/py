def FindFact(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
    print()

print("Enter a Number: ", end="")
try:
    num = int(input())
    print("\nFactors of " +str(num)+ " are: ", end="")
    FindFact(num)
except ValueError:
    print("\nInvalid Input!")