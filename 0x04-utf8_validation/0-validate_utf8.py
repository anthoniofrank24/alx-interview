#!/usr/bin/python3
"""
This module contains a function that validates UTF-8 encoding
"""


def validUTF8(data):
    """
    This function is a method that determines
    if a given data set represents a valid UTF-8 encoding
    Args:
        data (List[int]): A list of integers where each integer
        represents 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
