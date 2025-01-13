import numpy as np

# 1 Array operations
array = np.array([5, 8, 11, 0, 10, 0, 9, 23, 5, 99])
print("array len:", array.shape)
random_array = np.random.randint(0, 30, size=10)
print("random array:", random_array)

array_average = np.average(array)
print("average:", array_average)

array_mean = np.mean(array)
print("mean:", array_mean)

array_median = np.median(array)
print("median:", array_median)

standard_deviated_array = np.std(array)
print("Standard Deviation:", standard_deviated_array)

array[array % 2 == 1] = 0
print(array)

# 2 NumPy indexing and slicing
array_2D = np.array([[9, 3, 6],
                     [22, 1, 22]])
print("Matrix 1st line:", array_2D[0])
print("Matrix last line:", array_2D[-1])
print("Matrix diagonal elements, start from first element:", np.diag(array_2D))

# 3 Broadcasting, Add 1D array to 2D array
array_1D = np.array([8, 7, 5])
broadcasted_2d_array_with_1d_array = array_2D + array_1D
print("Broadcasted 2D array with 1D array: \n", broadcasted_2d_array_with_1d_array)

# 4 5D massive
# array_2D_5_elem = np.append(array_2D, [[4, 7], [9, 5]], axis=1)
array_2D_5_elem = np.hstack((array_2D, np.array([[4, 7], [9, 5]])))
print("2D Matrix with 5 elements:\n", array_2D_5_elem)

unique_values = np.unique(array_2D_5_elem)
print("Unique values:", unique_values)

# for row in array_2D_5_elem:
#     if np.sum(row) > 30:
#         print("Row with the sum that more than 30:", row)

rows_with_sum_gt_30 = array_2D_5_elem[np.sum(array_2D_5_elem, axis=1) > 30]
print("Row with the sum that more than 30:", rows_with_sum_gt_30)

#5 1D array with 20 numbs
array_1D_20_elem = np.arange(1, 21)
print("20:", array_1D_20_elem)

array_1D_20_elem.shape = (4, 5)
print("Array shape:", array_1D_20_elem.shape)