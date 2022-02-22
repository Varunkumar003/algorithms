import math
import os
import random
import re
import sys

def get_open(pag):
    return 1 + (pag//2)
def pageCount(n, p):
    return min(get_open(p) - get_open(1), get_open(n) - get_open(p))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
    
