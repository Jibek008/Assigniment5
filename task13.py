a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

i = 0
j = len(numbers) - 1
while i < j:
    t = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = t
    i += 1
    j -= 1

for i in numbers:
    print(i, end=' ')
