#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else :
        return arr[len(arr)//2]
    
def quartiles(arr):
    arr.sort()
    q1_arr = []
    q3_arr = []
    if len(arr) % 2 == 0:
        q2 = (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
        q1_arr = arr[:len(arr)//2]
        q3_arr = arr[len(arr)//2:]
    else:
        q2 = arr[len(arr)//2]
        q1_arr = arr[:len(arr)//2]
        q3_arr = arr[len(arr)//2 + 1:]
    q1 = median(q1_arr)
    q3 = median(q3_arr)
    
    return [int(q1),int(q2),int(q3)]
    
   

if __name__ == '__main__':
    arr = [3, 7, 8, 5, 12, 14, 21, 13, 18]
    print(quartiles(arr))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # data = list(map(int, input().rstrip().split()))

    # res = quartiles(data)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
