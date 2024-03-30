#!/bin/python3

import math
import os
import random
import re
import sys



def groupDivision(levels, maxSpread):
    # Ordenar por log n
    levels.sort()
    
    # O(n)
    min_possible_groups = 0
    start = 0

    for end in range(len(levels)):
        if levels[end] - levels[start] > maxSpread:
            min_possible_groups += 1
            start = end

    min_possible_groups += 1  # Adiciona o último grupo

    return min_possible_groups

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    levels_count = int(input().strip())

    levels = []

    for _ in range(levels_count):
        levels_item = int(input().strip())
        levels.append(levels_item)

    maxSpread = int(input().strip())

    result = groupDivision(levels, maxSpread)

    fptr.write(str(result) + '\n')

    fptr.close()
