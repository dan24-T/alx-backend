#!/usr/bin/env python3
"""
Define a function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The Actuall helper function
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
