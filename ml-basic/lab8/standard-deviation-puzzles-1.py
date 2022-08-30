# Array test
import math


arr = [1,2,3]

def standard_deviation(arr):
    mean = sum(arr)/len(arr)
    for i in range(len(arr)):
        arr[i] = (arr[i] - mean)**2
    return math.sqrt(sum(arr)/len(arr))

def mean(arr):
    return sum(arr)/len(arr)

print(mean(arr))
print(standard_deviation(arr))