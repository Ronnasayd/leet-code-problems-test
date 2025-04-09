from typing import *
from collections import deque
from random import randint


def tree2list(root: any) -> List:
    arr = []
    if not root:
        return arr
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current:
            arr.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            arr.append(None)
    while arr[-1] is None:
        arr.pop(-1)
    return arr


def list2tree(arr: List, class_: any):
    def adjustNull(root):
        if root.val is None:
            root = None
            return root
        if root.left:
            root.left = adjustNull(root.left)
        if root.right:
            root.right = adjustNull(root.right)
        return root

    def insert(root, val):
        new_node = class_(val)
        if not root:
            return new_node
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current and current.val is not None:
                if not current.left:
                    current.left = new_node
                    return root
                else:
                    queue.append(current.left)
                if not current.right:
                    current.right = new_node
                    return root
                else:
                    queue.append(current.right)

    if arr:
        root = insert(None, arr[0])
    else:
        return None
    for i in range(1, len(arr), 1):
        insert(root, arr[i])
    root = adjustNull(root)
    return root


def list2ll(arr: List, class_: any):
    prev = class_(val=arr[0])
    head = prev
    size = len(arr)
    for i in range(1, size, 1):
        curr = class_()
        curr.val = arr[i]
        curr.next = None
        prev.next = curr
        prev = curr
    return head


def ll2list(ll: any) -> List:
    arr = []
    while ll:
        arr.append(ll.val)
        ll = ll.next
    return arr


def display_tree(root):
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)


def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = "%s" % self.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = _display_aux(self.left)
        s = "%s" % self.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = _display_aux(self.right)
        s = "%s" % self.val
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(self.left)
    right, m, q, y = _display_aux(self.right)
    s = "%s" % self.val
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [n * " "] * (q - p)
    elif q < p:
        right += [m * " "] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def generate_random_array(length, lower, upper):
    ans = [0] * length
    for i in range(length):
        ans[i] = randint(lower, upper)
    return str(ans).replace(" ", "")
