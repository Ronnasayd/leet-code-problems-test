from pickle import NONE
from utils import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == "__main__":
    arr = [18, 2, 22, None, None, None, 63, None, 84, None, None]
    a = list2tree(arr, TreeNode)
    b = tree2list(a)
    display_tree(a)
