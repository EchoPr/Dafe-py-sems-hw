import numpy as np


def spiral_filling(r: int, c: int) -> np.ndarray:
    res = np.zeros((r, c))

    cnt = 1
    d_row = 0
    d_col = 1
    infi = infj = 0
    supi, supj = r - 1, c - 1
    i, j = 0, 0
    while cnt <= r * c:
        res[i, j] = cnt
        cnt += 1

        i += d_row
        j += d_col

        if i == infi and j == infj:
            d_row = 0
            d_col = 1

            supj -= 1
            if cnt != 1:
                supi -= 1

        elif i == infi and j == supj:
            d_row = 1
            d_col = 0
        elif i == supi and j == supj:
            d_row = 0
            d_col = -1

            infi += 1
            if cnt != c + r - 1:
                infj += 1

        elif i == supi and j == infj:
            d_row = -1
            d_col = 0

    
    return res


if __name__ == "__main__":
    print(spiral_filling(3, 3), end='\n\n')
    print(spiral_filling(1, 1), end='\n\n')
    print(spiral_filling(3, 2), end='\n\n')
    print(spiral_filling(4, 3), end='\n\n')
    print(spiral_filling(5, 7), end='\n\n')
