import numpy as np

#Problem 1 and #Question 2
a_ndarray = np.array([[-1, 2, 3], 
                      [4, -5, 6], 
                      [7, 8, -9]])
b_ndarray = np.array([[0, 2, 1],
                        [0, 2, -8],
                        [2, 9, -1]])

C1=np.matmul(a_ndarray,b_ndarray)
C2=np.dot(a_ndarray,b_ndarray)
C=a_ndarray @ b_ndarray
# C11 = -1*0 + 2*0 + 3*2    = 6
# C12 = -1*2 + 2*2 + 3*9    = 29
# C13 = -1*1 + 2*-8 + 3*-1  = -20

# C21 = 4*0 + (-5)*0 + 6*2   = 12
# C22 = 4*2 + (-5)*2 + 6*9   = 52
# C23 = 4*1 + (-5)*-8 + 6*-1 = 38

# C31 = 7*0 + 8*0 + (-9)*2    = -18
# C32 = 7*2 + 8*2 + (-9)*9    = -51
# C33 = 7*1 + 8*-8 + (-9)*-1  = -48
print(C1)
print(C2)
print(C)

#Problem 3
#Manual calculation
a= np.array([[-1, 2, 3], 
            [4, -5, 6], 
            [7, 8, -9]])
b= np.array([[0, 2, 1],
            [0, 2, -8],
            [2, 9, -1]])

c=np.zeros((3,3))

for i in range (3):
    for j in range(3):
       for k in range(3):
            c[i][j]+=a[i][k]*b[k][j]

print(c)

#Problem 4
def Matrix(x):
    d=np.zeros((x,x))
    for i in range (x):
        for j in range(x):
            for k in range(x):
                d[i][j]+=a[i][k]*b[k][j]

    return print(d)

print(Matrix(3))

#Problem 5
d_ndarray = np.array([[-1, 2, 3],
                       [4, -5, 6]])
e_ndarray = np.array([[-9, 8, 7],
                       [6, -5, 4]])

def checker(d_ndarray, e_ndarray):
    if d_ndarray.shape[1] != e_ndarray.shape[0]:
        print("Error: Cannot multiply these matrices! The number of columns in E must match the number of rows in D.")
        return None 
    F = np.zeros((d_ndarray.shape[0], e_ndarray.shape[1]))

    # Perform matrix multiplication
    for i in range(d_ndarray.shape[0]):  
        for j in range(e_ndarray.shape[1]): 
            for k in range(d_ndarray.shape[1]):
                F[i][j] += d_ndarray[i][k] * e_ndarray[k][j]

    return F

print(checker(d_ndarray,e_ndarray))

#Problem 6
e_transposed=np.transpose(e_ndarray)

print(checker(d_ndarray,e_transposed))