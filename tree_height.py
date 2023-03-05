# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    adj = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] != -1:
            adj[parents[i]].append(i)
    
    def height(node):
        if not adj[node]:
            return 1
        return 1 + max(height(child) for child in adj[node])
    
    return height(parents.index(-1))


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == '__main__':
    sys.setrecursionlimit(10**7)  
    threading.stack_size(2**27)
    threading.Thread(target=main).start()
    main()
