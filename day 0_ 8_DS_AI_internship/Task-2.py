#Task 2


import numpy as np


#1. Create a 1D array with values 0 to 23

data = np.arange(24)


# 2. Reshape into a 3D array of shape (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)


#3. Transpose to get shape (4, 2, 3)
final_data = reshaped_data.transpose(0, 2, 1)


#4. Print the final shape and array
print(final_data.shape)


print(final_data)
