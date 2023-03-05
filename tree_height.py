# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)
    
    memo = {}
    def height(node):
        if node in memo:
            return memo[node]
        if not nodes[node]:
            memo[node] = 0
            return 0
        h = max(height(child) for child in nodes[node]) + 1
        memo[node] = h
        return h

input_type = input().strip()
if input_type == 'F':
    filename = input().strip()
    if 'a' in filename:
        print("Invalid filename!")
        sys.exit()
    with open("/home/runner/work/tree-height-from-empty-201RBC039/tree-height-from-empty-201RBC039/" + filename) as f:
        n = int(f.readline())
        parents = list(map(int, f.readline().split()))
else:
    n = int(input())
    parents = list(map(int, input().split()))


#sys.setrecursionlimit(10**7)  
#threading.stack_size(2**27)
#threading.Thread(target=main).start()
print(compute_height(n, parents))
