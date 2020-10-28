# Algorithms on Python
## Search algorithms
### Binary search
algorithms/search/binarysearch/binary_search.py

Binary search algorithm that uses an iterative algorithm:
```python
binary_search_iter(arr: List[Any], item: Any) -> Optional[int]
```

Binary search algorithm that uses an recursion algorithm:
```python
binary_search_recurs(arr: List[Any], item: Any, low = -1, high = -1) -> Optional[int]
```

## Sort algorithms
### Selection sort
algorithms/sort/selectionsort/selection_sort.py

Immutable version of algorithm (return sorted array)
```python
def selection_sort_immutable(arr: List[T]) -> List[T]
```

Mutable version of algorithm (mutate income array)
```python
def selection_sort_mutable(arr: List[T]) -> None
```
