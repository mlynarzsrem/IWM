import numpy as np

def func(x):
    print(x)
    return -1*x

arr = np.array([[1,3],[2,4],[3,5]])
mapped = list(map(func,arr))
print(np.array(mapped))