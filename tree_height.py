# python3

import sys
import threading

def compute_tree_height(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def compute_node_hg(node):
        if not children[node]:
            return 1
        max_height = 0
        for child in children[node]:
            height = compute_node_hg(child)
            max_height = max(max_height, height)
        return max_height + 1

    return compute_node_hg(root)


def main():
    input_source = input()

    if 'i' in input_source:
        n = int(input())
        parents = list(map(int, input().split()))
        tree_height = compute_tree_height(n, parents)
        print(tree_height)
    elif 'F' in input_source:
        filename = input()
        with open("test/" + filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            tree_height = compute_tree_height(n, parents)
            print(tree_height)
    else:
        print("Input error")
        exit()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
