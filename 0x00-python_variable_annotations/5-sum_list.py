#!/usr/bin/env python3
""" Module that sums a list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes list in floats and returns the sum as float
    """
    return float(sum(input_list))
