from math import sqrt
from . import Indexer


class AntiSymmetricIndex(Indexer):
    def __init__(self, limit):
        self.limit = limit
        self.length = limit * (limit - 1) // 2

    def __len__(self):
        return self.length

    def get_index(self, *indices):
        i, j = indices
        return self.limit * i - (i + 2) * (i + 1) // 2 + j

    def get_indices(self, index):
        x = (2 * self.limit - 1) / 2
        i = int(x - sqrt(x ** 2 - 2 * index))
        j = index - self.limit * i + (i + 2) * (i + 1) // 2
        return i, j


# def main():
#     n = 10
#     converter = AntiSymmetricIndex(n)
#     lines = []
#     for i in range(n):
#         lines.append('  '.join(
#             [f'{i, j} -> {converter.get_index(i, j):2} -> {converter.get_indices(converter.get_index(i, j))}' for j in
#              range(i + 1, n)]))
#     length = len(lines[0])
#     for line in lines:
#         print(f'{{line: >{length}}}'.format(line=line))
#
#
# if __name__ == '__main__':
#     main()
