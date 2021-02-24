def repeat():
    count = 0
    for b in range(x,y+1):
        last_digit = b % 10
        if (last_digit == 2):
            count = count + 1
        if (last_digit == 3):
            count = count + 1
        if (last_digit == 9):
            count = count + 1
    print(count)
z = int(input())
T = 0
while T <= z:
    x,y = [int(x) for x in input().split()]
    repeat()
    T = T + 1
    if(T == z):
        break

