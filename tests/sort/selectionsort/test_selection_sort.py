import pytest
import algorithms.sort.selectionsort.selection_sort as ss


def test_immutable_ssort_empty_and_one_element_arr():
    assert ss.selection_sort_immutable([]) == []
    assert ss.selection_sort_immutable([1]) == [1]


def test_immutable_ssort_simple_arr():
    assert ss.selection_sort_immutable([3, 2, 5, 1, 6, 8, 9, 4, 7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
