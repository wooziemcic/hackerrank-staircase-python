import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    add = 1
    for tab in reversed(range(n-1)):
        print(" "*tab,"#"*add)
        tab -= 1
        add += 1
    print("#"*n)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
