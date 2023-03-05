# python3

import sys
import threading

def comp_h(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def comp_v(node):
        if not children[node]:
            return 1
        max_v = 0
        for child in children[node]:
            v = comp_v(child)
            max_v = max(max_v, v)
        return max_v + 1

    return comp_v(root)


def main():
    input_type = input()

    if 'I' in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        h = comp_h(n, parents)
        print(h)
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            h = comp_h(n, parents)
            print(height)
    else:
        print("Error")
        exit()

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
