a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

last = numbers[-1]
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]
numbers[0] = last

for i in numbers:
    print(i, end=' ')
