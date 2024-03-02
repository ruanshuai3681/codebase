import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)

arr = np.fix([-3.1666, 3.6667])
print(arr)

arr3 = np.ceil([-3.1666, 3.6667])
print(np.floor(arr3))
print(np.ceil(arr3))


arr2 = np.around(3.1666, 2)
print(arr2)

