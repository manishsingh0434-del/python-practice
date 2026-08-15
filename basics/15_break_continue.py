for i in range(1, 11):
    if i == 5:
        break
    print(i)

    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


for i in range(1, 11):
    if i == 7:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)


for i in range(1, 11):
    if i == 3:
        continue
    if i == 7:
        continue
    if i == 9:
        break
    print(i)