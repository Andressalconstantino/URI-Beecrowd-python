import sys
sys.setrecursionlimit(10**9)

def raizde2(n):
    if n == 0:
        return 0
    x = 1 / (6 + raizde2(n-1))
    return x

n = int(input())
z = 3+raizde2(n)
print('%.10f' %z)
