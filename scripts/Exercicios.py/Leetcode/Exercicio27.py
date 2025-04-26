

import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negative = 0
    positive = 0
    is_zero = 0

    for numero in arr:
        if numero > 0:
            positive += 1
        elif numero < 0:
            negative += 1
        elif numero == 0:
            is_zero += 1

    negative_final = negative / len(arr)
    positive_final = positive / len(arr)
    is_zero_final = is_zero / len(arr)

    print(f"{positive_final}")
    print(f"{negative_final}")
    print(f"{is_zero_final}")
    return 




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
