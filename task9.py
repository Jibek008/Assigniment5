a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

min_num = 0
for i in numbers:
    if i % 2 != 0:
        if min_num == 0:
            min_num = i
        elif i < min_num:
            min_num = i

print(min_num)
