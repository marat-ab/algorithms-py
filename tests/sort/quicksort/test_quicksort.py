import random

import pytest
from algorithms.sort.quicksort.quicksort import quicksort


def test_quicksort_on_trivial_arrays():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]


def test_quicksort_on_simple_arrays():
    assert quicksort([3, 5, 1, 2, 4, 7, 6, 9, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert quicksort([1, 2, 1, 2, 4, 3, 4, 3]) == [1, 1, 2, 2, 3, 3, 4, 4]


def test_quicksort_on_some_arrays():
    for i in range(1, 30):
        origin_arr = list(range(1, i))
        tmp_arr = origin_arr.copy()
        random.shuffle(tmp_arr)
        assert quicksort(tmp_arr) == origin_arr
