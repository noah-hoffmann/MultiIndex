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
        return self.limit * i - i * (i + 1) // 2 + j

    def get_indices(self, index: int):
        x = (2 * self.limit + 1) / 2
        i = int(x - sqrt(x ** 2 - 2 * index))
        j = index - self.limit * i + i * (i + 1) // 2
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
