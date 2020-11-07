"""This module should contain a Counter class"""


class Counter():
    def __init__(self):
        self._counter = 0

    def add(self):
        self._counter += 1

    def remove(self):
        self._counter -= 1

    def value(self):
        return self._counter
