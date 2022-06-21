
"""
my_list = [1,2,3]
arr = np.array(my_list)
print(arr)
my_mat = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(my_mat)
print(arr)
arr = np.arange(0,11,2)
print(arr)
arr = np.zeros(3)
print(arr)
arr = np.zeros((2,3))
print(arr)
arr = np.ones((2,3))
print(arr)
arr = np.eye(4)
print(arr)
arr = np.random.rand(5,5)
print(arr)
arr = np.random.randn(2,5)
print(arr)
arr = np.random.randint(1,100,10)
print(arr)

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr.reshape(5,5))

print(ranarr)
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())
print(arr.shape)

arr = np.arange(0,11)
print(arr)

print(arr[8])
print(arr[1:5])
print(arr[0:5])
print(arr[:6])
print(arr[5:])
arr[:5] = 100
arr = np.arange(0,11)
slice_of_arr = arr[:6]
print(slice_of_arr)
slice_of_arr[:] = 99
print(slice_of_arr)
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)

arr_2d = np.array([[5,10,15], [20,35,30], [35,40,45]])
print(arr_2d)
print(arr_2d[0][0])
print(arr_2d[2,1])
print(arr_2d[1:,:2])

arr = np.arange(1,11)
print(arr)
bool_arr = arr > 5
print(bool_arr)
print(arr[bool_arr])
print(arr[arr < 3])

arr2d = np.arange(100).reshape(10,10)
print(arr2d)
print(arr2d[6:7,4:6])
"""
import numpy as np
arr = np.zeros(10)
print(arr)
arr = np.ones(10)
print(arr)
arr = np.zeros(10) + 5
print(arr)
arr = np.arange(10,51,2)
print(arr)
arr = np.arange(0,9).reshape(3,3)
print(arr)
print(np.eye(3))
arr = np.random.rand(0,2)
print(arr)
