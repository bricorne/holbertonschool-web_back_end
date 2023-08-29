#!/usr/bin/env python3
"""type-annotated make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """that takes a float multiplier as argument and returns a function"""
    def multiplier_function(x: float) -> float:
        """multiplies a float by multiplier"""
        return x * multiplier
    return multiplier_function
