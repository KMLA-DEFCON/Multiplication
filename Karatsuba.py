from math import pow
def Karatsuba(n1, n2):
    if n1 < 10 or n2 < 10:
        return n1 * n2

    m = min(len(str(n1)), len(str(n2)))
    m = m // 2

    high1, low1 = divmod(n1, 10**m)
    high2, low2 = divmod(n2, 10**m)

    z0 = Karatsuba(low1, low2)
    z1 = Karatsuba(low1+high1, low2+high2)
    z2 = Karatsuba(high1, high2)

    return (z2*10**(m*2) + (z1-z0-z2)*10**m + z0)

A = int(input())
B = int(input())
print(Karatsuba(A,B))