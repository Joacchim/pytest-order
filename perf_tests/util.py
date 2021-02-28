import time

from pytest_order import Sorter


class TimedSorter(Sorter):
    elapsed = 0

    def sort_items(self):
        self.__class__.elapsed = 0
        start_time = time.time()
        items = super().sort_items()
        self.__class__.elapsed += time.time() - start_time
        print("Time per test: {:.3f} ms".format(self.__class__.elapsed))
        return items
