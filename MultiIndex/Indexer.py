from abc import ABC, abstractmethod


class Indexer(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def get_indices(self, index: int):
        pass

    @abstractmethod
    def get_index(self, *indices: int):
        pass

    def __iter__(self):
        for i in range(len(self)):
            yield i, self.get_indices(i)

    def __call__(self, *arg):
        if len(arg) == 1:
            arg = arg[0]
            if type(arg) == int:
                return self.get_indices(arg)
            elif type(arg) == tuple:
                return self.get_index(*arg)
            else:
                raise TypeError(f'Type of arg must be int or tuple, but {type(arg)} was given!')
        else:
            return self.get_index(*arg)
