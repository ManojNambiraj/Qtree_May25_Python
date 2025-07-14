# Numpy:

# Installation

    # py -m pip install numpy

import numpy as np

# Ex: 1

    # a = np.array([1, 2.5, 3, 4, 5], dtype=int)

    # print(a)

# Ex: 2

    # a = np.array([[1, 2, 3], [4, 5, 6]])

    # print(a)

# Ex: 3

    # a = np.zeros((2, 4))
    # a = np.ones((2, 4))

    # print(a)

# Ex: 4

    # a = np.arange(0, 10, 2)

    # print(a)

# Ex: 5

    # a = np.random.rand(8, 2)

    # print(a)

# Ex: 6

    # a = np.array([3, 2, 1])
    # b = np.array([4, 5, 6])

    # print(a + b)
    # print(a * b)
    # print(a - b)
    # print(a / b)

# Ex: 7

    # x = np.array([1, 2, 3, 4])

    # print(np.mean(x))  # Average
    # print(np.sum(x))   # Sum
    # print(np.max(x))   # Max
    # print(np.min(x))   # Min

# Ex: 8

    # a = np.array([10, 20, 30, 40, 50])

    # print(a[0])          # First element --> indexing
    # print(a[1:4])        # Elements from index 1 to 3 --> Range of indexing

# Example Excercise:

    # a = np.array([1, 2, 3, 4, 5])

    # b = a * 5

    # print(b)