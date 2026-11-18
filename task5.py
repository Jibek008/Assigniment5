a = input().split()
numbers = []
for i in a:
    numbers.append(int(i))

for i in range(1, len(numbers)):
    if numbers[i] > 0 and numbers[i - 1] > 0:
        print(numbers[i - 1], numbers[i])
        break
    elif numbers[i] < 0 and numbers[i - 1] < 0:
        print(numbers[i - 1], numbers[i])
        break
