# -*- coding: utf-8 -*-
import cmath
import numpy as np
import matplotlib.pyplot as plt

def custom_fft(x):
    length = len(x)
    if length <= 1:
        return x
    even = custom_fft(x[0::2])
    odd = custom_fft(x[1::2])
    twiddles = [cmath.exp(-2j * cmath.pi * k / length) * odd[k] for k in range(length // 2)]
    return [even[k] + twiddles[k] for k in range(length // 2)] + [even[k] - twiddles[k] for k in range(length // 2)]

def custom_fft_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # FFT per baris
    for i in range(rows):
        matrix[i] = custom_fft(matrix[i])

    # FFT per kolom
    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = custom_fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

# Contoh penggunaan
matrix_input = [
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31],
    [32, 33, 34, 35]
]

result_custom_fft = custom_fft_2d(matrix_input)

# Validasi menggunakan NumPy
import numpy as np

result_numpy_fft = np.fft.fft2(matrix_input)

# Perbandingan hasil
print("Custom FFT Implementation:")
print(np.round(result_custom_fft, decimals=2))
print("\nNumPy FFT Result:")
print(np.round(result_numpy_fft, decimals=2))

def display_matrix(matrix, title):
    plt.imshow(np.abs(matrix), cmap='plasma')
    plt.colorbar()
    plt.title(title)
    plt.show()

# Tampilkan matriks input
display_matrix(matrix_input, 'Input Matrix')

# Tampilkan hasil FFT implementasi sendiri
display_matrix(result_custom_fft, 'Custom FFT Implementation')

# Tampilkan hasil FFT NumPy
display_matrix(result_numpy_fft, 'FFT with NumPy')
