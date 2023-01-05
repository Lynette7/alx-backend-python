#!/usr/bin/env python3
'''Module for function that returns a function that multiplies a float by a multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
