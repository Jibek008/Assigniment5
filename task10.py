a = input().split()
heights = []
for h in a:
    heights.append(int(h))

x = int(input())

place = 1
for h in heights:
    if h >= x:
        place += 1
    else:
        break

print(place)
