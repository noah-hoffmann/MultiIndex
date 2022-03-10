from MultiIndex import SymmetricIndex
import pytest

index_indices_pair = [(0, (0, 0)), (1, (0, 1)), (2, (0, 2)), (3, (0, 3)),
                      (4, (1, 1)), (5, (1, 2)), (6, (1, 3)),
                      (7, (2, 2)), (8, (2, 3)),
                      (9, (3, 3))]


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_index_to_indices(index, indices):
    converter = SymmetricIndex(4)
    assert converter(index) == indices


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_indices_to_index(index, indices):
    converter = SymmetricIndex(4)
    assert index == converter(indices)
    assert index == converter(*indices)
