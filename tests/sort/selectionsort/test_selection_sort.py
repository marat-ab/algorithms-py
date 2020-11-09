import random

import algorithms.sort.selectionsort.selection_sort as ss
import pytest


def test_immutable_ssort_empty_and_one_element_arr():
    assert ss.selection_sort_immutable([]) == []
    assert ss.selection_sort_immutable([1]) == [1]


def test_immutable_ssort_simple_arr():
    assert ss.selection_sort_immutable([3, 2, 5, 1, 6, 8, 9, 4, 7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ss.selection_sort_immutable([1, 2, 1, 2, 4, 3, 4, 3]) == [1, 1, 2, 2, 3, 3, 4, 4]


def test_immutable_ssort_some_arrays():
    # Gen arrays [0], [0, 1], ..., [0...7], shuffle it and test sort alg
    for s in range(1, 10):
        arr = list(range(s))
        tmp_arr = arr.copy()
        random.shuffle(tmp_arr)
        assert ss.selection_sort_immutable(tmp_arr) == arr


def test_mutable_ssort_empty_and_one_element_arr():
    arr = []
    ss.selection_sort_mutable(arr)
    assert arr == []

    arr = [1]
    ss.selection_sort_mutable(arr)

    assert arr == [1]


def test_mutable_ssort_simple_arr():
    arr = [3, 2, 5, 1, 6, 8, 9, 4, 7]
    ss.selection_sort_mutable(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    arr = [1, 2, 1, 2, 4, 3, 4, 3]
    ss.selection_sort_mutable(arr)
    assert arr == [1, 1, 2, 2, 3, 3, 4, 4]


def test_mutable_ssort_some_arrays():
    # Gen arrays [0], [0, 1], ..., [0...7], shuffle it and test sort alg
    for s in range(1, 10):
        arr = list(range(s))
        tmp_arr = arr.copy()
        random.shuffle(tmp_arr)
        ss.selection_sort_mutable(tmp_arr)
        assert tmp_arr == arr
