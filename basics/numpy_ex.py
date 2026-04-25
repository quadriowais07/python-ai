import numpy as np

list1 = np.array([10,20,30,40,50])

print(list1) # [10 20 30 40 50]
print(list1.shape) # (5,)
print(list1.ndim) # 1
print(list1.dtype) # int64


list2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(list2) # [10 20 30 40 50]
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
print(list2.shape) # (3, 3)
print(list2.ndim) # 2
print(list2.dtype) # int64

print( np.zeros((2,3)) )
#[[0. 0. 0.]
# [0. 0. 0.]]
print( np.ones((2,3)))
#[[1. 1. 1.]
# [1. 1. 1.]]
print( np.eye(3))
#[[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]
print( np.arange(0, 10, 2))
# [0 2 4 6 8]
print(np.linspace(0,1,5))
# [0.   0.25 0.5  0.75 1.  ]


list1 = np.array([10,20,30,40,50])
print(list1[0]) # 10
print(list1[-5]) # 10
print(list1[1:3]) # [20 30]  -- 1 is included, 3 is excluded
print(list1[1:]) # [20 30 40 50] -- 1 till end
print(list1[:3]) # [10 20 30] --- 0 is included, 3 is excluded


list1 = np.array([[1,2,3],
                 [4,5,6]])
print( list1[0][0] ) # 1
print( list1[1][2] ) # 6
print( list1[:,0] ) # col1
print( list1[:,1] ) # col2
print( list1[:,2] ) # col3

print( list1[0] ) # row1
print( list1[1] ) # row2


print("------------------")
list1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print( list1[:,0] )
#[1 4 7]
print("------------------")
print( list1[:,0:2] )
#[[1 2]
# [4 5]
# [7 8]]
print("------------------")
print( list1[0:2] )
#[[1 2 3]
# [4 5 6]]


# vectorization (performing operation without using loops)
list1 = np.array([1,2,3])
print( list1 + 2 ) # [3 4 5]
print( list1 - 2 ) # [-1  0  1]
print( list1 * 2 ) # [2 4 6]
print( list1 / 2 ) # [0.5 1.  1.5]
print( list1 ** 2 ) # [1 4 9]


list1 = np.array([1,2,3,4,5])
print(f"min elements: {np.min(list1)}") # min element: 1
print(f"max elements: {np.max(list1)}") # max element: 5
print(f"sum of elements: {np.sum(list1)}") # sum of elements: 15
print(f"mean of elements: {np.mean(list1)}") # mean of elements: 3.0
print(f"squareroot of elements: {np.sqrt(list1)}")
# squareroot of element: [1.         1.41421356 1.73205081 2.         2.23606798]


list1 = np.array([1,2,3])
list2 = np.array([[10],[11],[12]])
print(list1 + list2)
#[[11 12 13]
# [12 13 14]
# [13 14 15]]


list1 = np.array([[1,2],
                  [3,4]])
list2 = np.array([[5,6],
                  [7,8]])
print(np.dot(list1,list2))
#[[19 22]
# [43 50]]


#A[0,0] * B[0,0] + A[0,1] * B[1,0] ------- A[0,0] * B[0,1] + A[0,1] * B[1,1]
#A[1,0] * B[0,0] + A[1,1] * B[1,0] ------- A[1,0] * B[0,1] + A[1,1] * B[1,1]

#1 * 5 + 2 * 7 ------- 1 * 6 + 2 * 8
#3 * 5 + 4 * 7 ------- 3 * 6 + 4 * 8

#5 + 14 -------- 6 + 16
#15 + 28 ------- 18 + 32

#19 ------- 22
#43 ------- 50

# allowed numbers in seed fn are 0 10 100 42
# these numbers are given by Python officially
print("---------------seed----------")
np.random.seed(10)
print("---------------rand----------")
print(np.random.rand(2,2))
#[[0.77132064 0.02075195]
# [0.63364823 0.74880388]]
print("---------------randint----------")
print(np.random.randint(1,10,(2,3)))
#[[1 2 9]
# [1 9 7]]
print("---------------rand----------")
print(np.random.rand(3))
# [0.68535982 0.95339335 0.00394827]


print(np.full((2,2),7))
#[[7 7]
# [7 7]]

print(np.full((2,2),100))
#[[100 100]
# [100 100]]


list1 = np.array([10,20,30,40,50])
print( list1[ list1>30])
# [40 50]
print( list1[ list1<30])
# [10 20]

list1 = np.array([ [1,2,3],
                  [4,5,6]
                  ])
print(np.sum(list1, axis=0)) # column wise sum
# [5 7 9]
print(np.sum(list1, axis=1)) # row wise sum
# [ 6 15]

list1 = np.arange(6)
print(list1)
# [0 1 2 3 4 5]
list2 = list1.reshape(2,3) # convert 1D to Multi-dimentional array
print(list2)
#[[0 1 2]
# [3 4 5]]

list3 = list2.flatten() # convert multi-dimentional to 1 dimentional array
print(list3)
# [0 1 2 3 4 5]

list1 = np.array([1,2])
print(list1.reshape(-1,1))
# [[1]
#  [2]]

list1 = np.array([1,2])
list2 = np.array([3,4])

print(np.vstack( (list1, list2) ))
# [[1 2]
#  [3 4]]

print( np.hstack( (list1, list2) ))
# [1 2 3 4]

list1 = np.array([1,2,3,4,5,6])
print( np.split(list1,3) )
# [array([1, 2]), array([3, 4]), array([5, 6])]

list1 = np.array([1,2,3,4,5,6,7,8])
new_list = np.split(list1,4)
# print(np.split(list1,3)) --- gives error
# array split does not result in an equal division
print(new_list[0])
# [1 2]

list1 = np.array([1,2,3])
list2 = list1 # ref copy

list1[0] = 1000
print(list1)
# [1000    2    3]
print(list2)
# [1000    2    3]

list1 = np.array([1,2,3])
list2 = list1.copy() # deep copy

list1[0] = 1000
print(list1)
# [1000    2    3]
print(list2)
# [1 2 3]

list1 = np.array([3,1,2])
print(np.sort(list1))
# [1 2 3]
print(np.argsort(list1))
# [1 2 0] -- print indexes of input array before sorting

list1 = np.array([[1,2],
                  [3,4]])
list2 = np.array([[5,6],
                  [7,8]])
new_list1 = np.dot(list1 ,list2)
print(new_list1)
# [[19 22]
#  [43 50]]

# Transpose a matrix - convert rows to col & col to rows
print(new_list1.T)
# [[19 43]
#  [22 50]]


"""
mean / average: sum of elements in list divided by total no. of elements in list is called mean

[10, 20, 20, 30]
mean = 80 / 4 = 20

Standard deviation: how list elements vary wrt mean value is called std deviation

Example of Std dvtn:
mean - each ele in list
20 - 10
20 - 20
20 - 20
20 - 30



"""







