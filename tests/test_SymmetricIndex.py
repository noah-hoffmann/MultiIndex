from MultiIndex import SymmetricIndex
import pytest

index_indices_pair = [(0, (0, 0)),
                      (1, (1, 0)), (2, (1, 1)),
                      (3, (2, 0)), (4, (2, 1)), (5, (2, 2)),
                      (6, (3, 0)), (7, (3, 1)), (8, (3, 2)), (9, (3, 3))]


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_index_to_indices(index, indices):
    converter = SymmetricIndex(4)
    assert converter(index) == indices


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_indices_to_index(index, indices):
    converter = SymmetricIndex(4)
    assert index == converter(indices)
    assert index == converter(*indices)
