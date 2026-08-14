for i in range(3):
    for j in range(3):
        print("*", end="")
    print()




for i in range(1, 4):
    for j in range(1, 4):
        print(i, end="")
    print()


for i in range(1, 4):
    for j in range(1, 4):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range (1, 4):
    for j in range (1, 4):
        print(i*j, end ="")
    print()


for i in range(1, 5):
    for j in range(1, i+ 1):
        print("*", end="")
    print()


for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()


for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="")
    print()


for i in range(1, 4):
    for j in range(1, 4):
        print(i*j, end=" ")
    print()


number = int(input("Enter a number:"))

for i in range(1, 11):
    print(number*i)