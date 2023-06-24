import sys
import math


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def find_kth_ancestor(matrix, node, k):
    power = math.floor(math.log(k, 2))
    node = matrix[node][power]
    k = k - (2 ** power)

    while node != - 1 and k > 0:
        power = math.floor(math.log(k, 2))
        node = matrix[node][power]
        k = k - (2 ** power)

    return node

def find_lca(matrix, depth, left, right):
    # keep right as the deeper one
    if depth[left] > depth[right]:
        left, right = right, left

    if depth[left] < depth[right]:
        k = depth[right] - depth[left]
        right = find_kth_ancestor(matrix, right, k)

    if left == right:
        return left

    for power in range(len(matrix[0]) - 1, -1, -1):
        left_ancestor = find_kth_ancestor(matrix, left, (2**power))
        right_ancestor = find_kth_ancestor(matrix, right, (2**power))

        if left_ancestor != right_ancestor:
            left = left_ancestor
            right = right_ancestor

    return matrix[left][0]


def main():
    s = sys.stdin

    n = s.readline()

    if not n:
        return

    n = int(n.rstrip())
    node_array = [Node(i) for i in range(n)]

    for i in range(n):
        row = s.readline().rstrip().split()

        count = int(row[0])

        for j in range(count):
            node_array[i].children.append(node_array[int(row[j + 1])])

    # make matrix
    depth = [0] * n
    matrix = [[-1] * (1 + math.floor(math.log(n, 2))) for _ in range(n)]

    def dfs(root, d):
        if not root:
            return

        for child in root.children:
            depth[child.val] = d + 1

            for power in range(1 + math.floor(math.log(n, 2))):
                if power == 0:
                    matrix[child.val][0] = root.val
                else:
                    ancestor = matrix[child.val][power - 1]
                    if ancestor != -1:
                        matrix[child.val][power] = matrix[ancestor][power - 1]

            dfs(child, d + 1)            

    dfs(node_array[0], 0)

    # loop through all the queries and
    # print the output at each iteration
    q = int(s.readline().rstrip())
    for i in range(q):
        l = s.readline()
        l = l.rstrip().split()
        print(find_lca(matrix, depth, int(l[0]), int(l[1])))

    return 0

if __name__ == '__main__':
    main()
    
