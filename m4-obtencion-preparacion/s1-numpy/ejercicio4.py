import numpy as np

arr=np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
arr_index=np.where(arr>0)
print(arr_index)