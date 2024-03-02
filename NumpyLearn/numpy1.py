#NumPy is a Python library used for working with arrays.NumPy stands for Numerical Python.
#NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
#Arrays are very frequently used in data science, where speed and resources are very important.
#Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.
#NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
#This behavior is called locality of reference in computer science.
#it is optimized to work with latest CPU architectures.
#NumPy is usually imported under the np alias.
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
#nested array: are arrays that have arrays as their elements.
#We can also define the step, like this: [start:end:step].
#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
#Every NumPy array has the attribute base that returns None if the array owns the data.
#
import numpy as np

arr = np.array([0,1, 2, 3, 4, 5])
newarr = arr.astype('S')
x = arr.copy()
x = arr.view()

print(arr)
print(arr[0])
print(type(arr))
print(arr.dtype)
#array slicing
print(arr[0:2])
print(arr[::2])
print(newarr.dtype)
newarr2 = arr.reshape(2, 3)

for idx, x in np.ndenumerate(arr):
  print(idx, x)

print("-----------")

arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2.ndim)

arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr3[0, 1])

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr4[0, 1, 2])
print(arr4.shape)
newarr3 = arr4.reshape(-1)
print(newarr3)
#Flattening array means converting a multidimensional array into a 1D array. We can use reshape(-1) to do this.

