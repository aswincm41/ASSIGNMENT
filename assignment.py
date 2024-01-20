for x in range(6):
    for i in range(x):
     print("*", end="     ")
    print()

  
num = 1
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end="   ")
        num += 1
    print()

n = 4 
for i in range(n):
    char = ord('A') 
    for j in range(i + 1):
        print(chr(char), end="   ")
        char += 1
    print()

n = 4
char = ord('A')
for i in range(n):
    for j in range(i + 1):
        print(chr(char), end="   ")
        char += 1
    print()

n = 4  
num = 2

for i in range(n):
    for j in range(i + 1):
        print(num, end="   ")
        num += 2
    print()

n = 4
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("#", end=" ")
    print()