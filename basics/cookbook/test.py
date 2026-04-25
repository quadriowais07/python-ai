import numpy as np

list1 = np.array([10,20,30,40,50])
print(list1.shape) # (5,)
print(list1.ndim) # 1

list2 = np.array([[10,20,30,40,50],
                 [1,2,3,4,5]])

print(list2.shape) # (2, 5)
print(list2.ndim) # 2

list3 = np.array([[10],
                  [11],
                  [12]])
print(list3.shape) # (3, 1)
print(list3.ndim) # 2

list1 = np.array([[1,2,3],
                 [4,5,6]])
print( list1[0][0] ) # 1
print( list1[1][2] ) # 6
print( list1[:,0] ) # col1
print( list1[:,1] ) # col2
print( list1[:,2] ) # col3
print( list1[1:,1] )
