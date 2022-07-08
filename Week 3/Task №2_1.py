class CyclicIterator:
    def __init__(self, iterable):
        if type(iterable) is not dict:
            self.iterable = list(iterable)
        else:
            self.iterable = [(key, iterable[key]) for key in iterable]
        self.index = -1

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index < len(self.iterable) - 1:
            self.index += 1
            return self.iterable[self.index]
        else:
            self.index = 0
            return self.iterable[self.index]


def main():
    cyclic_iterator = CyclicIterator({1: 5, 7: 3, 0: 2})
    for i in cyclic_iterator:
        print(i)


if __name__ == "__main__":
    main()