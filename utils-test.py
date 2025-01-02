from pickle import NONE
from utils import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == "__main__":
    arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, 3, 2]
    a = list2tree(arr, TreeNode)
    b = tree2list(a)
    display_tree(a)
