def compare_tupeles(a, b):
    first = 0
    second = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            first += 1
            print(first)
        elif a[i] < b[i]:
            second += 1
            print(second)
        elif a[i] == b[i]:
            continue
    return first, second


a = (5, 6, 7)
b = (3, 6, 10)
result = compare_tupeles(a, b)
print(result)