import numpy as np
from . import Indexer
from typing import Union


class MultiIndex(Indexer):
    def __init__(self, *limits):
        self.limits = limits
        self.length = 1
        for i in limits:
            self.length *= i

    def get_index(self, *indices):
        index = indices[-1]
        factor = self.limits[-1]
        for i, limit in zip(indices[-2::-1], self.limits[-2::-1]):
            index += i * factor
            factor *= limit
        return index

    def get_indices(self, index: int):
        indices = []
        for limit in self.limits[::-1]:
            indices.append(index % limit)
            index //= limit
        return tuple(reversed(indices))

    def flatten_array(self, array: np.ndarray):
        flattened = np.zeros(self.length, dtype=array.dtype)
        for i in range(self.length):
            flattened[i] = array[self.get_indices(i)]
        return flattened

    def unflatten_list(self, flattened: Union[np.ndarray, list], dtype=None):
        if isinstance(flattened, np.ndarray):
            array = np.zeros(self.limits, dtype=flattened.dtype)
        else:
            array = np.zeros(self.limits, dtype=dtype)
        for i in range(self.length):
            array[self.get_indices(i)] = flattened[i]
        return array

    def __len__(self):
        return self.length


# def main():
#     limits = (3, 3, 3)
#     converter = MultiIndex(*limits)
#     for i, I in converter:
#         print(i, I)
#
#     array = np.zeros(limits)
#
#     for i in range(converter.length):
#         array[converter.get_indices(i)] = i
#
#     print(array)
#     print(converter.flatten_array(array))
#     print(converter.unflatten_list(converter.flatten_array(array)))
#
#     for i in converter:
#         print(i)
#
#     print(converter((2, 2, 2)))
#     print(converter(5))
#     print(converter(-1))
#     print(converter(-len(converter)))
#
#
# if __name__ == '__main__':
#     main()
