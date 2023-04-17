from  typing import Iterable


class CyclicIterator:
    def __init__(self, iterable: Iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)

if __name__ == '__main__':
    my_list = [1,2,3]
    repeat = CyclicIterator(my_list)

    for el in repeat:
        print(el)
    print('Hello world!')