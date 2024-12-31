from typing import *
from collections import deque


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


if __name__ == "__main__":
    pass
