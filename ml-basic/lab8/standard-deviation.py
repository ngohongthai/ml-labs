#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # find mean
    mean = sum(arr)/len(arr)
    for i in range(len(arr)):
        arr[i] = (arr[i] - mean)**2
    # find standard deviation
    return math.sqrt(sum(arr)/len(arr))
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(vals))
