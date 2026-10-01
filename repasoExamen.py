def programa1(l, k):
    acc = 0
    for i in range(len(l) - 1):
        j = len(l) - 1
        while i < j:
            if (l[i] + l[j]) % k == 0:
                acc += 1
            j -= 1
    return acc

l = [1, 2, 3, 4, 5, 6]
k = 5
print(programa1(l, k))
            