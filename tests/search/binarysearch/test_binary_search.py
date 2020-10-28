import pytest
from algorithms.search.binarysearch.binary_search import binary_search_iter, binary_search_recurs


def test_empty_array_iter_alg():
    assert binary_search_iter([], 1) is None


def test_some_variants_of_arrays_iter_alg():
    # Gen arrays [0], [0, 1], ..., [0...7] and test search alg
    for s in range(1, 8):
        tmp_list = list(range(s))
        for i, v in enumerate(tmp_list):
            assert binary_search_iter(tmp_list, v) == i

        assert binary_search_iter(tmp_list, len(tmp_list)+1) is None


def test_empty_array_recurs_alg():
    assert binary_search_recurs([], 1) is None


def test_some_variants_of_arrays_recurs_alg():
    # Gen arrays [0], [0, 1], ..., [0...7] and test search alg
    for s in range(1, 8):
        tmp_list = list(range(s))
        for i, v in enumerate(tmp_list):
            assert binary_search_recurs(tmp_list, v) == i

        assert binary_search_recurs(tmp_list, len(tmp_list)+1) is None
