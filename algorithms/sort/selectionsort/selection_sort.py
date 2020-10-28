from typing import Any, List, TypeVar
import copy

T = TypeVar('T')


def find_min_element(arr: List[T]) -> int:
    """
    Find min element in arr. It is a example of algorithm

    Args:
        arr (List[T]): input array with data, T must support operation "<"

    Returns:
        int: index of min element in arr
    """

    assert arr is not None
    assert len(arr) > 0

    index = 0
    min_value = arr[index]
    for i, v in enumerate(arr):
        if v < min_value:
            min_value = v
            index = i

    return index


def selection_sort_immutable(arr: List[T]) -> List[T]:
    """
    Immutable realisation of selection sort algorithm

    Args:
        arr (List[T]): input array with data, T must support operation "<"

    Returns:
        List[T]: sorted arr
    """

    assert arr is not None

    out_arr = copy.deepcopy(arr)

    if len(arr) <= 1:
        return out_arr

    for i in range(len(out_arr)):
        min_i = find_min_element(out_arr[i:]) + i
        out_arr[i], out_arr[min_i] = out_arr[min_i], out_arr[i]

    return out_arr
