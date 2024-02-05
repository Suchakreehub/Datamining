import numpy as np
def single_point_crossover (A,B,X):
    A_new = np.append(A[:X], B[X:])
    B_new = np.append(B[:X], A[X:])
    return A_new, B_new

A = np.array([4,8,6,5,9,2,6,9,2,3])
B = np.array([9,8,7,4,5,2,3,5,8,7])
X = 2
single_point_crossover(A,B,X)
print(single_point_crossover(A,B,X))
