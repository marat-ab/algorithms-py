import math
from typing import Any, List, Optional


def binary_search_iter(arr: List[Any], item: Any) -> Optional[int]:
    """
    Binary search algorithm that uses an iterative algorithm

    Args:
        arr (List[Any]):  array for search
        item (Any): element that was searched in arr

    Returns:
        Optional[int]: index of item in arr or None if item was not finded        
    """

    # Contracts
    assert arr is not None

    # Alg realisation
    if len(arr) == 0:
        return None

    low = 0
    high = len(arr) - 1
    while low <= high:
        print(f"{low} {high}")
        mid = (high + low) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid

    return None


def binary_search_recurs(arr: List[Any], item: Any, low = -1, high = -1) -> Optional[int]:
    """
    Binary search algorithm that uses an recursion algorithm    

    Args:
        arr (List[Any]):  array for search
        item (Any): element that was searched in arr
        low (int): low bound of array
        high (int): high bound of array

    Returns:
        Optional[int]: index of item in arr or None if item was not finded        
    """

    # Contracts
    assert arr is not None

    # Alg realisation
    if len(arr) == 0 or low > high:
        return None
    else:
        if low == -1 and high == -1:
            low = 0
            high = len(arr) - 1
        
        mid = (low + high) // 2
        if arr[mid] < item:
            return binary_search_recurs(arr, item, mid+1, high)
        elif arr[mid] > item:
            return binary_search_recurs(arr, item, low, mid-1)
        else:
            return mid
