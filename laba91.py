def array_diff(a,b):
    c = []
    for x in a:
        if x not in b:
            c.append(x)
    return c

print(array_diff([1,2], [1]))
print(array_diff([1, 2, 2, 2, 3], [2]))
print(array_diff([1, 2, 3], [4, 5]))
