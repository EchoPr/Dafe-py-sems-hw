import numpy as np


def ldu_decompose(mat: np.ndarray) -> tuple[np.ndarray]:
    if mat.shape[0] != mat.shape[1]:
        raise ValueError('Matrix must be square') 
    
    s = mat.shape[0]
    L = np.zeros((s, s))
    D = np.zeros((s, s))
    U = np.zeros((s, s))

    for i in range(s - 1):
        for j in range(i + 1, s):
            U[i, j] = mat[i, j]
    
    for i in range(s - 1):
        for j in range(i + 1, s):
            L[j, i] = mat[j, i]

    for i in range(s):
        D[i, i] = mat[i, i]

    return L, D, U


if __name__ == '__main__':
    rnd = np.random.randint(1, 10, (3, 3))
    print(rnd, '\n')

    print(*ldu_decompose(rnd), sep='\n\n')
