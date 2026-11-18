a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

for i in numbers:
    if i % 2 == 0:
        print(i, end=' ')
