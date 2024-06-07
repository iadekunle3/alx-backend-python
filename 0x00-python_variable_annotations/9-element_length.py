#!/usr/bin/env python3
"""Module that annotate a func"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuples"""
    return [(i, len(i)) for i in lst]
