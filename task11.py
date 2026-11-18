a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

count = 1
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        count += 1

print(count)
