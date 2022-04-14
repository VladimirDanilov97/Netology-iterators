import time


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
    [[5, 6], [[7,8,[9]],2]]
]

class MyIterator():
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.index = 0
        self.iterator = self.nested_list[self.index].__iter__()
        

    def __iter__(self):
        return self
    

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.index += 1
            if self.index == len(nested_list):   
                raise StopIteration
            else:
                self.iterator = self.nested_list[self.index].__iter__()
                return next(self)


def generator(nested_list):
    for list_ in nested_list:
        if isinstance(list_, list):
            for item in list_:
                if isinstance(item, list):
                    for j in generator(list_):
                        yield j
                else:
                    yield item
        else:
            yield list_
iterator = MyIterator(nested_list)
g = generator(nested_list)
for i in g:
    print(i)
# for i,j in zip(iterator, generator):
#     print(f'{i}; {j};')