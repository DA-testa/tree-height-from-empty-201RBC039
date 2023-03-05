# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        tree[i] = []
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def height(node):
        if not tree[node]:
            return 1
        else:
            return max(height(child) for child in tree[node]) + 1

    return height(root)


def main():
    input_type = input()
    n = 0
    parents = []
    if input_type.upper() == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)
threading.Thread(target=main).start()
