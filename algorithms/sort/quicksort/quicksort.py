import copy
from typing import Any, List, TypeVar

T = TypeVar('T')


def quicksort(arr: List[T], comparer=lambda a, b: a <= b) -> List[T]:
    """
    Realisation of QuickSort algorithm

    Args:
        arr (List[T]): input array with data, T must support operation "<"
        comparer (Callalble[[T, T], bool]): function for compare values that has type T,
            must return True, if first arg <= second arg, else False

    Returns:
        List[T]: sorted input array
    """

    assert arr is not None

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low_subarr = [v for v in arr[1:] if comparer(v, pivot)]
        high_subarr = [v for v in arr[1:] if not comparer(v, pivot)]
        return quicksort(low_subarr) + [pivot] + quicksort(high_subarr)
