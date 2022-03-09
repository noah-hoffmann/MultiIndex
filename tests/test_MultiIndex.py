import numpy as np
import pytest
from MultiIndex import MultiIndex

index_indices_pair = [(0, (0, 0, 0)),
                      (1, (0, 0, 1)),
                      (2, (0, 0, 2)),
                      (3, (0, 1, 0)),
                      (4, (0, 1, 1)),
                      (5, (0, 1, 2)),
                      (6, (0, 2, 0)),
                      (7, (0, 2, 1)),
                      (8, (0, 2, 2)),
                      (9, (1, 0, 0)),
                      (10, (1, 0, 1)),
                      (11, (1, 0, 2)),
                      (12, (1, 1, 0)),
                      (13, (1, 1, 1)),
                      (14, (1, 1, 2)),
                      (15, (1, 2, 0)),
                      (16, (1, 2, 1)),
                      (17, (1, 2, 2)),
                      (18, (2, 0, 0)),
                      (19, (2, 0, 1)),
                      (20, (2, 0, 2)),
                      (21, (2, 1, 0)),
                      (22, (2, 1, 1)),
                      (23, (2, 1, 2)),
                      (24, (2, 2, 0)),
                      (25, (2, 2, 1)),
                      (26, (2, 2, 2))]


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_index_to_indices(index, indices):
    converter = MultiIndex(3, 3, 3)
    assert converter(index) == indices


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_indices_to_index(index, indices):
    converter = MultiIndex(3, 3, 3)
    assert converter(indices) == index
    assert converter(*indices) == index


def test_flatten_array():
    converter = MultiIndex(3, 3, 3)
    array = np.array([
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
        [[18, 19, 20], [21, 22, 23], [24, 25, 26]],
    ])
    flattend = np.array(list(range(27)))
    assert np.array_equal(flattend, converter.flatten_array(array))


def test_unflatten_array():
    converter = MultiIndex(3, 3, 3)
    array = np.array([
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
        [[18, 19, 20], [21, 22, 23], [24, 25, 26]],
    ])
    flattend = list(range(27))
    assert np.array_equal(array, converter.unflatten_list(flattend))
