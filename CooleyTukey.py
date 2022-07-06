from cmath import exp,pi

def fft(x):

    N = len(x)
    
    if N <= 1: return x

    even = x[0:N//2:2]
    odd  = x[1:N//2:2]

    even = fft(even)
    odd = fft(odd)

    for k in range(N//2):
        x[k       ] = even[k] + exp(-2j*pi*k/N)*odd[k]
        x[k + N//2] = even[k] - exp(-2j*pi*k/N)*odd[k]

    return x

