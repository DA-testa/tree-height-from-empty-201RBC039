# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    depths = [0] * n
    for i in range(n):
        depth = 0
        j = i
        while j != -1:
            if depths[j] != 0:
                depth += depths[j]
                break
            depth += 1
            j = parents[j]
        depths[i] = depth
    return max(depths)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
