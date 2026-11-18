a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

max_num = numbers[0]
index = 0
for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        index = i

print(max_num, index)
