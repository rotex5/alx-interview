#!/usr/bin/python3
"""
lockboxes solution
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be
    opened, else return False
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        curr_box = stack.pop()
        visited.add(curr_box)

        for key in boxes[curr_box]:
            if key not in visited and key < n:
                stack.append(key)

    return len(visited) == n
