while 1>0:
    numeros = []
    nums, mod = map(int, input().split())
    if nums==0 and mod==0:
        print(nums, mod)
        break
    for i in range(nums):
        n = int(input())
        if n < 0:
            x = -(-n % mod)
        else:
            x = n % mod
        number = (n, x, False)
        if n%2==0:
            number = (n, x, True)
        numeros.append(number)
    numeros.sort(key= lambda x: (x[1], x[2], x[0] if x[2] else -x[0]))
    print(nums, mod)
    for i in numeros:
        print(i[0])