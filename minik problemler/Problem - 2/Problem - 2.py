import numpy as np

# Make array
numbers = np.arange(36)

# 6x6 array
numbers = numbers.reshape(6,6)

# Slicing
for i in range(6):
    slice = numbers[i,i]
    print(slice)
