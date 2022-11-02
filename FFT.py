import numpy as np

###help function to find nearest upper power of 2
###for example, if given n is 5, this function will find 8 which is 2^3
def nearPowerOf2(n):
    p = 1
    if (n and not(n & (n - 1))):
        return n
    while (p < n) :
        p <<= 1    
    return p

###our FFT algorithm using recursion
###length of input x(array or list) has to be power of 2
def FFT(x):
    N=len(x)
    #corner case
    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N)/ N)
        
        X = np.concatenate(\
                           [X_even+factor[:int(N/2)]*X_odd, 
                            X_even+factor[int(N/2):]*X_odd])
        return X

