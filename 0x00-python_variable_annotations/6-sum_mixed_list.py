#!/usr/bin/env python3
"""Module that performs sum of mixed list"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of a mixed list as a float"""
    return float(sum(mxd_lst))
