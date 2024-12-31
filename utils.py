from typing import *
from collections import deque

from source import TreeNode


def tree2list(root: any) -> List:
    arr = []
    if not root:
        return arr
    queue = deque([root])
    while queue:
        current = queue.popleft()
        arr.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return arr


def list2tree(arr: List, class_: any):
    def insert(root, val):
        new_node = class_(val=val)
        if not root:
            return new_node
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current.val and not current.left:
                current.left = new_node
                return root
            else:
                queue.append(current.left)
            if current.val and not current.right:
                current.right = new_node
                return root
            else:
                queue.append(current.right)

    root = insert(None, arr[0])
    for i in range(1, len(arr), 1):
        insert(root, arr[i])
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


def display(root):
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


if __name__ == "__main__":
    pass
    # root = list2tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], TreeNode)
    # display(root)
