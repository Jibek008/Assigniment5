a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

min_num = 1001
for i in numbers:
    if i > 0 and i < min_num:
        min_num = i

print(min_num)
