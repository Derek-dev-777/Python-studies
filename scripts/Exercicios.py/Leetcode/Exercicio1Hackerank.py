import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    total = sum(arr)
    minimo = total - max(arr)
    maximo = total - min(arr)
    print(minimo, maximo)
            
    
            


    


arr = [1, 2, 3, 4, 5]

print(min(arr))
miniMaxSum(arr)
