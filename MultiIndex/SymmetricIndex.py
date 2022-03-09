from math import sqrt
from . import Indexer


class SymmetricIndex(Indexer):
    def __init__(self, limit):
        self.limit = limit
        self.length = limit * (limit + 1) // 2

    def __len__(self):
        return self.length

    def get_index(self, *indices):
        i, j = indices
        return j + i * (i + 1) // 2

    def get_indices(self, index: int):
        i = int((-1 + sqrt(1 + 8 * index)) / 2)
        j = index - i * (i + 1) // 2
        return i, j


# def main():
#     converter = SymmetricIndex(4)
#     for i in range(4):
#         for j in range(i + 1):
#             I = converter.get_index(i, j)
#             print(f'({i}, {j}) -> {I} -> {converter.get_indices(I)}')
#
#
# if __name__ == '__main__':
#     main()
