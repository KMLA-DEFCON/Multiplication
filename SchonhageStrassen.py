def multiply(x,y):

    n = len(str(x))
    m = len(str(y))

    LC = [0 for _ in range(0,n+m-1)] #Linear Convolution of x*y

    temp = x
    for i in range(0,m):
        x = temp
        for j in range(0,n):
            LC[i+j] += (y%10) * (x%10)
            x = x // 10
        y = y // 10
    print(LC)
    sum, carry, base = 0, 0, 1
    for i in range(len(LC)):
        LC[i] += carry
        sum += base * (LC[i]%10)
        carry = LC[i]//10
        base *= 10

    sum += base * carry
    print(LC)
    return sum

a = int(input())
b = int(input())
print(multiply(a,b))