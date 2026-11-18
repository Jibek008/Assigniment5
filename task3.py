a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

count = 0
for i in numbers:
    if i > 0:
        count += 1

print(count)
