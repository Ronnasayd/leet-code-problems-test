from curses.ascii import isdigit
from typing import *


# from utils import list2tree, tree2list, display_tree

# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if len(token) > 1 or isdigit(token):
                stack.append(token)
            else:
                p1 = int(stack.pop(-1))
                p2 = int(stack.pop(-1))
                if token == "+":
                    stack.append(p1 + p2)
                if token == "-":
                    stack.append(p2 - p1)
                if token == "*":
                    stack.append(p1 * p2)
                if token == "/":
                    stack.append(int(float(p2) / float(p1)))
        return stack[0]
