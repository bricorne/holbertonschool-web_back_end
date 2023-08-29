#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """akes a list mxd_lst of integers and floats and returns their sum"""
    return sum(mxd_lst)
