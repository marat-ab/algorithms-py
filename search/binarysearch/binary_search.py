import math
from typing import Any, List, Optional


def binary_search_iter(arr: List[Any], item: Any) -> Optional[int]:
    """
    Binary search alg that using iter alg(in while construction)

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


def binary_search_recurs(arr: List[Any], item: Any) -> Optional[int]:
    """
    Binary search alg that using recursion alg

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
    else:
        low = 0
        high = len(arr) - 1
        mid = (low + high) // 2
        if arr[mid] < item:
            return binary_search_recurs(arr[mid+1:], item)
        elif arr[mid] > item:
            return binary_search_recurs(arr[:mid], item)
        else:
            return mid
