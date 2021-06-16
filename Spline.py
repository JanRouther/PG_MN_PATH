import numpy as np
from copy import deepcopy


def spline(trasa):
    xn = []
    yn = []

    for row in trasa[1:]:
        xn.append(row[0])
        yn.append(row[1])

    h = xn[1] - xn[0]#zalozenie: x[i+1] - x[i] = h
    n = len(xn) - 1 #liczba podprzedzialow
    eq = 4*n #liczba rownan


    buff =[0] * eq
    rownanie =[0] * eq

    A = []
    x = [0] * eq
    b = [0] * eq


    #1
    #Sj(xj) =f(xj),j=0,1,...,n−1
    #aj =yj
    for j in range (n):# dobrze
        rownanie = [0] * eq
        rownanie[j*4] = 1
        b[j] = yn[j]
        A.append(rownanie)
    #2
    #Sj(xj + 1) = f(xj + 1), j = 0, 1, ..., n−1
    #aj + bj*h +cj*h^2 +dj*h^3 = y[j+1]
    for j in range (n):#dobrze
        rownanie = [0] * eq
        rownanie[j*4] = 1#aj
        rownanie[(j*4)+1] = h#bj*h
        rownanie[(j*4)+2] = h*h#cj*h^2
        rownanie[(j*4)+3] = h*h*h #dj*h^3
        b[j+n] = yn[j+1]
        A.append(rownanie)

    #3
    #xj:S′j−1(xj) =S′j(xj),j=1,...,n−1 wewnetrzne wezly
    #bj+1   =bj+ 2* cj *h +3*h^2*dj
    #0=bj+ 2* cj *h +3*h^2*dj -bj+1
    for j in range(0,n-1):
        rownanie = [0] * eq
        rownanie[(j*4)+1] = 1#bj
        rownanie[(j*4)+2] = 2*h#cj
        rownanie[(j*4)+3] = 3*h*h#dj
        rownanie[((j+1)*4)+1] = -1#bj+1
        A.append(rownanie)

    # 4
    # Dla węzłów wewnętrznychxj:S′′j−1(xj) =S′′j(xj),j=1,...,n−1
    # 2*cj+1=2*c0+ 6*d0*h
    # 0=2*cj+ 6*dj*h -2cj+1
    for j in range(0,n-1):
        rownanie = [0] * eq
        rownanie[(j*4)+2] = 2#cj
        rownanie[(j*4)+3] = 6*h#cj
        rownanie[((j+1)*4)+2] = -2#cj+1
        A.append(rownanie)
    # 5
    # 2 krawedzie
    # S′′0(x0) =0
    # S′′n−1(xn) =0
    # c0 =0
    # 2cn+6dn1h=0
    rownanie = [0] * eq
    A.append(rownanie)
    rownanie[2] = 2

    rownanie = [0] * eq
    rownanie[-1] = 6*h
    rownanie[-2] = 2
    A.append(rownanie)

    return lu_decomposition_pivot(A, b)


def forward_substitution(L,b):
    for i in range(L.shape[0]):
        for j in range(i):
            b[i] -= L[i,j]*b[j]
    return b


def backward_substitution (U,y):
    for i in range(U.shape[0]-1,-1,-1):
        for j in range(i+1, U.shape[1]):
            y[i] -= U[i,j]*y[j]
        y[i] = y[i]/U[i,i]
    return y


def lu_decomposition_pivot(A,b):
    A = np.array(A, float)
    b = np.array(b, float)
    n = A.shape[0]
    LU=deepcopy(A)
    pivot = np.arange(0,n)
    for k in range(n-1):

        # piv
        max_row_index = np.argmax(abs(LU[k:n,k])) + k
        pivot[[k,max_row_index]] = pivot[[max_row_index,k]]
        LU[[k,max_row_index]] = LU[[max_row_index,k]]

        # LU
        for i in range(k+1,n):
            LU[i,k] = LU[i,k]/LU[k,k]
            for j in range(k+1,n):
               LU[i,j] -= LU[i,k]*LU[k,j]

    b = b[pivot]
    y = forward_substitution(LU, b)
    x = backward_substitution(LU, y)

    return x
