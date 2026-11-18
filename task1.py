a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

for i in range(0, len(numbers), 2):
    print(numbers[i], end=' ')