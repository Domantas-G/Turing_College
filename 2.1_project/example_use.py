import numpy as np
from turing_21_matrix_operations import (
    convolution2d,
    window1d,
    transpose2d,
    create_random_matrix,
)

# Transposition
random_matrix = create_random_matrix(3, 4)

print(random_matrix)

input_matrix = [[1, 2], [4, 5], [2, 15]]

print(transpose2d(input_matrix=random_matrix))
print(transpose2d(input_matrix=input_matrix))

# Windowing
windowed = window1d(list(range(10)), size=2, shift=2, stride=2)
print(windowed)

input_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
windowed = window1d(input_array=input_array, size=2, shift=2, stride=2)
print(windowed)

# Convolution
input_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
kernel = np.array([[1, 1.2], [0, 1]])
convolved = convolution2d(input_matrix=input_matrix, kernel=kernel, stride=2)
print(convolved)
