a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=' ')
