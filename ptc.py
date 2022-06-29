import math
import os
import random
import re
import sys
# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    b = []
    for i in range(n):
        a = []
        for j in c:
            a.append(abs(i-j))
        b.append(min(a))
    return max(b)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    fptr.write(str(result) + '\n')
    fptr.close()