import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    print(node.val, end="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])


def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.val, end="")
    if node.right != ".":
        inorder(tree[node.right])


def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.val, end="")


if __name__ == "__main__":
    n = list(map(int, sys.stdin.readline().split()))[0]
    # pdb.set_trace()
    tree = {}
    for _ in range(n):
        val, left, right = sys.stdin.readline().split()
        tree[val] = Node(val, left, right)
    preorder(tree["A"])
    print()
    inorder(tree["A"])
    print()
    postorder(tree["A"])
    print()
