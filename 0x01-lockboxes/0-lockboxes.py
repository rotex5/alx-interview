#!/usr/bin/python3
"""
lockboxes solution
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes in the list can be unlocked,
    given that each box contains a set of keys to other boxes.

    Args:
        boxes (list[list[int]]): A list of boxes, where
        boxes[i] contains a set of keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
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
