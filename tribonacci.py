def tribonacci(signature, n):
    list1 = signature
    if n == 0:
        return []
    elif n == 1:
        return 1
    elif n == 2:
        return signature[:2]
    elif n>= 3:
        for a in range(n-3):
            list1.append(list1[-1]+list1[-2]+list1[-3])
    return list1


print(tribonacci([1, 1, 1], 3))