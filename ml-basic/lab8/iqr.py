#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
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
    
    return [q1,q2,q3]

def interQuartile(values, freqs):
    arr = []
    for index, value in enumerate(values):
        arr.extend([value]*freqs[index])
    q1 = quartiles(arr)[0]
    q3 = quartiles(arr)[2]
    return round(float(q3 - q1), 1)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print(interQuartile(val, freq))
