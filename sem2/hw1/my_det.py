import random, time, winsound

import numpy as np
import matplotlib.pyplot as plt


def det_by_row(mat_src: np.ndarray) -> float:
    mat = mat_src
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

        res += (-1)**(1 + j + 1) * mat[0, j] * det_by_row(mat[mask].reshape(w - 1, w - 1))

    return res


def det_by_gauss(mat_src: np.ndarray) -> float:
    mat = mat_src

    if mat.shape[0] != mat.shape[1]:
        raise ValueError('Marix must be square')
    w = mat.shape[1]
    
    for i in range(w - 1):            
        if mat[i, i] == 0:
            search_row = i + 1
            while search_row < w:
                if mat[search_row, i] != 0:
                    mat[i], mat[search_row] = mat[search_row], mat[i]
                    break
                search_row += 1
            else:
                return 0
        
        for j in range(i + 1, w):
            mat[j] -= mat[i] * (mat[j, i] / mat[i, i])
                

    return mat.diagonal().prod()


def calc_test(tests_amount: int) -> None:    
    print('Calculations (print_precision=2)')

    for t in range(tests_amount):
        size = random.randint(1, 6)
        min_value, max_value = -5, 5
        mat = (max_value - min_value) * np.random.random_sample((size, size)) + min_value
        
        res_det_by_row = det_by_row(mat)
        res_det_by_gauss = det_by_gauss(mat)
        res_linalg = np.linalg.det(mat)

        print(
            f'{(t + 1):03}: '
            f'matrix size: {size} | '
            f'det_by_row: {res_det_by_row:.2f}; | '
            f'det_by_gauss: {res_det_by_gauss:.2f}; | '
            f'np.linalg.det: {res_linalg:.2f};\n'
        )


def speed_test(max_size=5):
    size = np.arange(1, max_size + 1)
    time_det_by_row = np.zeros(max_size)
    time_det_by_gauss = np.zeros(max_size)
    time_det_by_linalg = np.zeros(max_size)

    fig, ax = plt.subplots(1, 3, figsize=(8, 5))
    for s in size:
        print(f'Iteration {s} | Started at {time.strftime("%H:%M:%S")}')

        min_value, max_value = -5, 5
        mat = (max_value - min_value) * np.random.random_sample((s, s)) + min_value

        start = time.time()
        res_det_by_row = det_by_row(mat)
        time_det_by_row[s - 1] = time.time() - start

        start = time.time()
        res_det_by_gauss = det_by_gauss(mat)
        time_det_by_gauss[s - 1] = time.time() - start

        start = time.time()
        res_det_by_linalg = np.linalg.det(mat)
        time_det_by_linalg[s - 1] = time.time() - start

    plt.xlim(0, max_size + 1)
    plt.ylim(0, max(time_det_by_row) + 1)
    plt.subplots_adjust(wspace=.5, hspace=.5)
    fig.suptitle("Сравнение времени работы функций")

    ax[0].axis('equal')
    ax[0].set_title("det_by_row")
    ax[0].set_xlabel('Размер матрицы')
    ax[0].set_ylabel('Время, c')

    ax[1].axis('equal')
    ax[1].set_title("det_by_gauss")
    ax[1].set_xlabel('Размер матрицы')
    ax[1].set_ylabel('Время, c')

    ax[2].axis('equal')
    ax[2].set_title("np.linalg.det")
    ax[2].set_xlabel('Размер матрицы')
    ax[2].set_ylabel('Время, c')

    ax[0].plot(size, time_det_by_row)
    ax[1].plot(size, time_det_by_gauss)
    ax[2].plot(size, time_det_by_linalg)

    plt.savefig('results')
    
    print('\n\033[42mPerformance tests done\033[0m ' + f'Finished at {time.strftime("%H:%M:%S")}')
    winsound.MessageBeep()


if __name__ == '__main__':
    calc_test(15)
    speed_test(10)
