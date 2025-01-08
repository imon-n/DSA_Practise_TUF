arr = [12, 35, 1, 10, 34, 1]

large = second_large = float('-inf')

for i in arr:
    if i > large:
        second_large = large
        large = i

    elif i > second_large and i != large:
        second_large = i

if second_large == float('-inf'):
    second_large = -1

print(second_large)