import sys


def solve(inorder, preorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        solve(inorder[0:index], preorder)  # left subtree
        solve(inorder[index + 1 :], preorder)  # right subtree
        print(inorder[index], end=" ")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        preorder = list(map(int, sys.stdin.readline().split()))
        inorder = list(map(int, sys.stdin.readline().split()))
        solve(inorder, preorder)
        print("")
