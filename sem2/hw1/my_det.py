import random, time, winsound
import numpy as np
import matplotlib.pyplot as plt


def mdet(mat: np.ndarray) -> float:
    if mat.shape[0] != mat.shape[1]:
        raise ValueError('Marix must be square')

    if mat.shape == (1, 1):
        return mat[0, 0]
    
    w = mat.shape[1]
    res = 0
    for j in range(w):
        mask = np.full((w, w), True)
        mask[0] = False
        mask = mask.T
        mask[j] = False
        mask = mask.T

        res += (-1)**(1 + j + 1) * mat[0, j] * mdet(mat[mask].reshape(w - 1, w - 1))

    return res


def calc_test(tests_amount: int) -> None:    
    print('Determinant:')
    for t in range(tests_amount):
        size = random.randint(1, 6)
        mat = np.random.randint(-5, 5, (size, size))
        
        res_mdet = mdet(mat)
        res_linalg = np.linalg.det(mat)
        print(f'{(t + 1):03}: mdet: {res_mdet}; np.linalg.det: {res_linalg:.2f}; delta: {abs(res_linalg - res_mdet):.2f}')

    print()




def speed_test(max_size=5):
    size = np.arange(1, max_size + 1)
    time_func = np.zeros(max_size)
    time_np = np.zeros(max_size)

    fig, ax = plt.subplots(1, 2, figsize=(8, 5))
    for s in size:
        print(f'Iteration {s}')

        mat = np.random.randint(-5, 5, (s, s))

        start = time.time()
        res_mdet = mdet(mat)
        time_func[s - 1] = time.time() - start

        start = time.time()
        res_linalg = np.linalg.det(mat)
        time_np[s - 1] = time.time() - start

    plt.xlim(0, max_size + 1)
    plt.ylim(0, max(time_func) + 1)
    plt.subplots_adjust(wspace=.5, hspace=.5)
    fig.suptitle("Сравнение времени работы функций")
    ax[0].axis('equal')
    ax[0].set_title("mdet")
    ax[0].set_xlabel('Размер матрицы')
    ax[0].set_ylabel('Время, c')

    ax[1].axis('equal')
    ax[1].set_title("np.linalg.det")
    ax[1].set_xlabel('Размер матрицы')
    ax[1].set_ylabel('Время, c')

    ax[0].plot(size, time_func)
    ax[1].plot(size, time_np)

    plt.savefig('results')
    
    print('\n\033[42mPerformance tests done\033[0m')
    winsound.MessageBeep()
        


if __name__ == '__main__':
    calc_test(15)
    speed_test(8)