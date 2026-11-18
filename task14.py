a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

i = 0
while i < len(numbers) - 1:
    t = numbers[i]
    numbers[i] = numbers[i + 1]
    numbers[i + 1] = t
    i += 2

for i in numbers:
    print(i, end=' ')
