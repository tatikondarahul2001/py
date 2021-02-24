def fac(N):
   count = 0
   for i in range(1, N + 1):

        if N % i == 0:
            if N >= 0:
                count = count + 1  
                print(count)
z = int(input())
T = 0
while T <= z:
    N = int(input())
    fac(N)
    T = T + 1
    if(T == z):
        break