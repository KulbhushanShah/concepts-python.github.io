

#!/bin/python3

import math
import os
import random
import re
import sys

from statistics import median
def quartiles(arr):
    
    # Write your code here
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) // 2
    else:
        return arr[n//2]

    # Find Q2 (median)
    q2 = median(arr)

    # Find Q1 (median of lower half)
    lower_half = arr[:len(arr)//2]
    q1 = median(lower_half)

    # Find Q3 (median of upper half)
    upper_half = arr[len(arr)//2 + (0 if len(arr) % 2 == 0 else 1):]
    q3 = median(upper_half)
    print('this is ', type(q3))

    return q1, q2, q3

if __name__ == '__main__':
    n = int(input('entr the n').strip())
    data = list(map(int, input().rstrip().split()))
    print('type of data', data)
    res = quartiles(data)
    print(type(res), 'type of res')
    print(res, 'res')