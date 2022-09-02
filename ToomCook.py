def toomcook(A,B):

    cut = max(len(str(A))//3, len(str(B))//3) + 1
    cut = 10**cut

    a = [] # p(x) = a[2]x^2 + a[1]x + a[0]
    for i in range(3):
        a.append(A % cut)
        A = A // cut

    b = [] # q(x) = b[2]x^2 + b[1]x + b[0]
    for i in range(3):
        b.append(B % cut)
        B = B // cut

    # p(x) * q(x) = r(x)

    ta = a[0] + a[2]
    p_0 = a[0]
    p_1 = ta + a[1]
    p_m1 = ta - a[1]
    p_m2 = 2*(p_m1 + a[2]) - a[0]
    p_inf = a[2]

    tb = b[0] + b[2]
    q_0 = b[0]
    q_1 = tb + b[1]
    q_m1 = tb - b[1]
    q_m2 = 2*(q_m1 + b[2]) - b[0]
    q_inf = b[2]

    r_0 = toomcook(p_0, q_0)
    r_1 = toomcook(p_1, q_1)
    r_m1 = toomcook(p_m1, q_m1)
    r_m2 = toomcook(p_m2, q_m2)
    r_inf = toomcook(p_inf, q_inf)

    r = [0,0,0,0,0] # r(x) = r[4]x^4 + ... + r[0]
    r[0] = r_0
    r[4] = r_inf
    r[3] = (r_m2 - r_1) // 3
    r[1] = (r_1 - r_m1) // 2
    r[2] = r_m1 - r_0
    r[3] = (r[2]-r[3]) // 2 + 2*r_inf
    r[2] = r[2] + r[1] - r_inf
    r[1] = r[1] - r[3]

    s = 0
    for i in range(5):
        s += r[i] * (cut**i)
    return s

A = int(input())
B = int(input())
print(toomcook(A,B))
