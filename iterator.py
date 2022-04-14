class MyIterator():
    def __init__(self, nested_list):
        self.iterated_list = [nested_list]
        self.indexes = [0]
        self.iterators = [self.iterated_list[0][0].__iter__()]

    def __iter__(self):
        return self

    def __next__(self):
       
        try:
            n = next(self.iterators[-1])
            if isinstance(n, list):
                self.iterated_list.append([n])
                self.indexes.append(0)
                self.iterators.append(n.__iter__())
                return next(self)
            else:
                return n

        except StopIteration:
            if len(self.iterated_list) > 1 and (
              self.indexes[-1] == len(self.iterated_list[-1])-1):
                self.iterated_list.pop()
                self.indexes.pop()
                self.iterators.pop()
                return next(self)

            self.indexes[-1] += 1
            if self.indexes[0] == len(self.iterated_list[0]):
                raise StopIteration
            self.iterators[-1] = self.iterated_list[-1][self.indexes[-1]].__iter__()
            return next(self)


def generator(nested_list):
    for list_ in nested_list:
        if isinstance(list_, list):
            for item in list_:
                if isinstance(item, list):
                    for j in generator([item]):
                        yield j
                else:
                    yield item
        else:
            yield list_


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        [[5, 6], [[7, 8, [9]], 2]], 
    ]

    iterator = MyIterator(nested_list)
    g = generator(nested_list)

    for i, j in zip(iterator, g):
        print(f'{i}; {j};')
