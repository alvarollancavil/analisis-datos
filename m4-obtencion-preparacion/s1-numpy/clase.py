import numpy as np

vector=np.array([1,2,3])

v1=1.5*np.arange(10,20,2)
v2=np.zeros((2,3))
v3=1.5*np.ones((2,4))
v4=np.eye(3)
v5=v1[v1>15]
v6=np.random.randint(1,10,(3,2))
v7=np.arange([1,2,3])
v8=np.arange([4,5,6])


print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

print("===============================")
arr = np.array([1, 2, 3, 4])

def custom_func(x):
    return x + 10

vec_func = np.vectorize(custom_func)

arr2 = vec_func(arr)
arr3 = arr ** 2

print(arr2)
print(arr3)
