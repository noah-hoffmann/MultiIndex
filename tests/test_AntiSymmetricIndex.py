from MultiIndex import AntiSymmetricIndex
import pytest

index_indices_pair = [(0, (0, 1)), (1, (0, 2)), (2, (0, 3)),
                      (3, (1, 2)), (4, (1, 3)),
                      (5, (2, 3))]


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_index_to_indices(index, indices):
    converter = AntiSymmetricIndex(4)
    assert converter(index) == indices


@pytest.mark.parametrize("index,indices", index_indices_pair)
def test_indices_to_index(index, indices):
    converter = AntiSymmetricIndex(4)
    assert index == converter(indices)
    assert index == converter(*indices)
