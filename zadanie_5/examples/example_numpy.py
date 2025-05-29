import numpy as np

# Example 1: Basic array operations
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
print("Array squared:", arr ** 2)

# Example 2: Matrix operations
matrix = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix)
print("Matrix:")
print(matrix)
print("Inverse:")
print(inverse)

# Example 3: Statistics
data = np.random.normal(loc=0, scale=1, size=1000)
print("Mean:", np.mean(data))
print("Standard deviation:", np.std(data))
