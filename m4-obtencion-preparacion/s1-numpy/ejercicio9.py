import numpy as np

arr1=np.random.randint(1,10,9)
arr2=np.random.randint(1,10,9)
mat1=arr1.reshape(3,3)
mat2=arr2.reshape(3,3)

print("mat1")
print(mat1)
print("mat2")
print(mat2)

print("\nSuma")
print(mat1+mat2)
print("\nResta")
print(mat1-mat2)
print("\nMultiplicacion")
print(mat1*mat2)
print("\nDivision")
print(mat1/mat2)