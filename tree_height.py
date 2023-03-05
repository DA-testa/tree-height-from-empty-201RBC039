# python3

import sys
import threading


def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def compute_depth(node):
        if not children[node]:
            return 1
        max_h = 0
        for child in children[node]:
            h = compute_node_h(child)
            max_h = max(max_h, h)
        return max_h + 1

    return compute_node_h(root)


def main():
    input_type = input()

    if 'i' in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        tree_h = compute_tree_h(n, parents)
        print(tree_h)
    elif 'F' in input_type:
        file = input()
        with open("test/" + file, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            tree_h = compute_tree_h(n, parents)
            print(tree_h)
    else:
        print("Error")
        exit()

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
