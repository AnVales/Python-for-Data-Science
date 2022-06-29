# Q1: What is the result of the following operation: np.array([1,-1])*np.array([1,1])?
import numpy as np
print(np.array([1,-1])*np.array([1,1]))

# Q2:What is the result of the following operation: np.dot(np.array([1,-1]),np.array([1,1]))?
print(np.dot(np.array([1,-1]),np.array([1,1])))

# Q3:How many rows are in the following numpy array?
A = np.array([[1,2],[3,4],[5,6],[7,8]])
print(len(A)) 
# 2

# Q4: Is it possible to perform the following operation?
A = np.array([[1,2],[3,4],[5,6],[7,8]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.dot(A,B))
# No

# Q5:What is the result of the following lines of code:
a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
print(a*b)

# Q6:What is the result of the following lines of code:
a=np.array([0,1])
b=np.array([1,0])
print(np.dot(a,b))

# Q7: What is the result of the following lines of code:
a=np.array([1,1,1,1,1])
print(a+10)

# Q8: What is the correct code to perform matrix multiplication on the matrix A and B?
np.dot(A,B)

