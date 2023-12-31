#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The function should return a tuple of size two containing a index"""
    start = (page - 1) * page_size
    end = page * page_size
    return(start, end)
