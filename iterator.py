import time

from numpy import inner 
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
<<<<<<< HEAD
    [[5, 6]],
    ['i', 'j', 'k'],
    [[7,8,[9]],2],
    ['a', 'b', 'c']]

=======
    
]
>>>>>>> parent of 4aaf308... Generator work for all type of lists

class MyIterator():
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.index = 0
        self.iterator = self.nested_list[self.index].__iter__()
        self.indexes = [self.index]
        self.iterators = [self.iterator]

    def __iter__(self):
        return self
    

    def __next__(self):
        time.sleep(0.3)
        # print(self.indexes)
        try: 
            n = next(self.iterators[-1])
            # print(f'n = {n}')

            if isinstance(n, list):
                self.indexes.append(0)
                self.iterators.append(n.__iter__())
                return next(self.iterators[-1])
            else: 
                
                return n
        except StopIteration:
            if len(self.indexes) > 1:
                self.indexes.pop() 
                self.iterators.pop() 

            self.indexes[-1] += 1

            if self.indexes[0] == len(self.nested_list):  
                raise StopIteration
            else:
                self.iterators[0] = self.nested_list[self.indexes[0]].__iter__()
            #     print('*')
                #  next(self.iterators[-1])
            
        # try:
        #     if isinstance(next(self.iterator), list):
        #         self.iterator = next(self.iterator).__iter__()
        #     else:
        #         return next(self.iterator)
        # except StopIteration:
        #     self.index += 1
        #     if self.index == len(nested_list):   
        #         raise StopIteration
        #     else:
        #         self.iterator = self.nested_list[self.index].__iter__()
        #         return next(self)

def my_generator(nested_list):
    for list_ in nested_list:
        for item in list_:
            yield item 

iterator = MyIterator(nested_list)
<<<<<<< HEAD
g = generator(nested_list)
for i in iterator:
    print(i)
# for i,j in zip(iterator, generator):
#     print(f'{i}; {j};')
=======
generator = my_generator(nested_list)
for i,j in zip(iterator, generator):
    print(f'{i}; {j};')
>>>>>>> parent of 4aaf308... Generator work for all type of lists
