a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i], end=' ')
