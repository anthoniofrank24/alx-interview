#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxs can be opened.

    Args:
    boxes (list of list of int): A list where each element is a list
    of keys contained in that box

    Return:
    bool: True if all boxes can be opened, else False
    """
    n = len(boxes)
    unlocked_boxes = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in unlocked_boxes:
            unlocked_boxes.add(current_box)
            for key in boxes[current_box]:
                if key not in unlocked_boxes and key < n:
                    stack.append(key)

    return len(unlocked_boxes) == n
