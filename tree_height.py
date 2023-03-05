# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    node_children = {i: [] for i in range(n)}
    
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            node_children[parent].append(i)
    
    
    def height(node):
        if not node_children[node]:
            return 1
        else:
            return 1 + max(height(child) for child in node_children[node])
    
    return height(root)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    main()
