import numpy as np
def lu_factor(A):
    n = A.shape[0]
    piv = np.arange(0,n)
    for k in range(n-1):

        # piv
        max_row_index = np.argmax(abs(A[k:n,k])) + k
        piv[[k,max_row_index]] = piv[[max_row_index,k]]
        A[[k,max_row_index]] = A[[max_row_index,k]]

        # LU
        for i in range(k+1,n):
            A[i,k] = A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j] -= A[i,k]*A[k,j]

    return [A,piv]

def ufsub(L,b):
    for i in range(L.shape[0]):
        for j in range(i):
            b[i] -= L[i,j]*b[j]
    return b

def bsub(U,y):
    for i in range(U.shape[0]-1,-1,-1):
        for j in range(i+1, U.shape[1]):
            y[i] -= U[i,j]*y[j]
        y[i] = y[i]/U[i,i]
    return y

def lu(A,b):
    A = np.array(A, float)
    b = np.array(b, float)
    LU, piv = lu_factor(A)
    b = b[piv]
    y = ufsub( LU, b )
    x = bsub(  LU, y )
    return x