This project contains the documentation for three functions: `transpose2d`, `window1d`, and `convolution2d`. These functions perform matrix transposition, sliding window generation, and 2D convolution, respectively.

de2_1 directory contains the project files, whereas tests contains the tests files. 
This library was built using poetry and published to pypi.

The project can be installed from here https://pypi.org/project/de2-1/

## transpose2d

The `transpose2d` function transposes a 2D matrix by flipping its rows and columns. It takes a 2D list of floats as input and returns a 2D list of floats as output.

### Arguments

- `input_matrix` (List[List[float]]): The input matrix to be transposed. It is expected to be a 2D list of floats.

### Returns

- `List[List[float]]`: The transposed matrix as a 2D list of floats.

### Examples

- python input_matrix = [[1, 2, 3], [4, 5, 6]] 
- result = transpose2d(input_matrix) print(result) # [[1, 4], [2, 5], [3, 6]]

### Notes

- The input_matrix should be a 2D list of floats.
- The function uses the `zip(*input_matrix)` expression to perform the transpose operation.
- The rows of the input_matrix become the columns of the transposed matrix, and vice versa.
- The resulting transposed matrix has dimensions (number of columns, number of rows) compared to the input matrix.
- The function returns the transposed matrix as a 2D list of floats.

## window1d

The `window1d` function generates overlapping windows of a specified size from a 1D input array. It takes a 1D input array and optional parameters for window size, shift, and stride, and returns a list of windows, where each window is either a list or a 1D NumPy array.

### Arguments

- `input_array` (List | np.ndarray): The 1D input array.
- `size` (int): The size of the window.
- `shift` (int, optional): The shift value between windows. Default is 1.
- `stride` (int, optional): The stride value for moving the window. Default is 1.

### Returns

- `List[Union[List, np.ndarray]]`: A list of windows, where each window is either a list or a 1D NumPy array.

### Raises

- `TypeError`: If the input_array is not a list or a 1D NumPy array.
- `ValueError`: If the size, shift, or stride is not a positive integer.

### Examples

- python input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9] size = 3 shift = 2 stride = 1 
- result = window1d(input_array, size, shift, stride) 
- print(result) # [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]

### Notes

- The input_array should be a 1D array, either a list or a 1D NumPy array.
- The size represents the length of each window.
- The shift determines the step size for moving the window starting position.
- The stride determines the step size for moving the window elements.
- If the window cannot fit entirely within the input_array, it is skipped.
- The function returns a list of windows, where each window is either a list or a 1D NumPy array.


## convolution2d

The `convolution2d` function performs 2D convolution on an input matrix using a given kernel. at

### Arguments

- `input_matrix` (List[List[float]]): The input matrix to be convolved. and is expected to be a 2D list of floats.
- `kernel` (List[List[float]]): The 2D kernel to be used for the convolution., and is expected to be a 2D list of floats.

### Returns

- `List[List[float]]`: The convolved output matrix as a 2D list of floats.－

### Examples

- python input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
- kernel = [[1, 0], [0, 1]]
-  result = convolution2d(input_matrix, kernel) 
- print(result) # [[5, 9], [16, 27]]


### Notes

- The input_matrix should be a 2D list of floats. and the kernel should be a 2D list of floats. the convolved output matrix has the same number of rows as the input_matrix and one less column than the kernel. 
- The function returns the convolved output matrix as a 2D list of floats.

### Algorithm

1. Initialize an empty output matrix with the same number of rows as the input_matrix and one less column than the kernel.ommes. but not necessarily the same shape. The output matrix will have the same number of rows as the input_matrix and one less column than the kernel.
2. Iterate through each element in the input_matrix.
3. For each element, iterate through the kernel and apply the kernel to the corresponding element in the input_matrix.
4. Accumulate the results of the kernel application and store them in the output matrix.
5. Return the output matrix.

