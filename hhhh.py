x = int(input())
y = int(input())
count = 0
for b in range(x,y):
    if (str(b[-1]) == 2):
        count = 1
    if (str(b[-1]) == 3):
        count = count + 1
    if (str(b[-1]) == 9):
        count = count + 1
print(count)