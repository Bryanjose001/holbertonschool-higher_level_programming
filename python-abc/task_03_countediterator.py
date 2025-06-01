#!/usr/bin/python3


class CountedIterator():
    """An iterator that counts the number of items iterated over"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self.iterator)
            self._count += 1
            return value
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self._count
