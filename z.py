import numpy as np
import math

def X(nums, z):
    X_z = 0
    for i in range(len(nums)):
        j = - i
        X_z += nums[i] * math.pow(z, j)
    return X_z

def reverseX_z(N, X_z, z):
    V = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if j == 0:
                V[i][j] = 1
            else:
                V[i][j] = math.pow(z[i], -j)
    myX_z = np.zeros(N)
    for i in range(N):
        myX_z[i] = X_z[i]
    V_inv = np.linalg.inv(V)
    res = np.dot(V_inv, myX_z)
    print(res)



def T(nums, z):
    T_z = 0.4 * X(nums, z) + 0.8 * X(nums, z) * math.pow(z, -1) + 0.47 * X(nums, z) * math.pow(z, -2)
    noise = np.random.normal(0, 0.2)
    return T_z + T_z * noise

def Q(nums, z):
    Q_z = T(nums, z) / X(nums, z)
    return Q_z

def X_new_test(Xz_train,Xz_test,z):
    N = len(Xz_train)
    X_new_test = reverseX_z(N, Xz_test, z)
    return X_new_test
    

N = 3
myNums = np.random.random(N) * 2 * np.pi
print(myNums)
z = np.arange(2, 3, 1 / N)
X_Z = []
for z_i in z:
    X_Z.append(X(myNums, z_i))
print(X_Z)
reverseX_z(N, X_Z, z)


