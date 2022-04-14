import time

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
    [[5, 6]],
    ['i', 'j', 'k'],
    [[7,8,[9]],2],
    ]

class MyIterator():
    def __init__(self, nested_list):
        self.current_list = [nested_list]
        self.indexes = [0]
        self.iterators = [self.current_list[0][0].__iter__()]

    def __iter__(self):
        return self
    

    def __next__(self):
        time.sleep(0.2)
        try:
            n = next(self.iterators[-1])
            print(type(n))
            if isinstance(n, list):
                print('***')
                self.current_list.append(n)
                return n
            else:
                return n
        except StopIteration:

            self.indexes[-1] += 1
            if self.indexes[0] == len(self.current_list[0]):
                raise StopIteration 
            self.iterators[-1] = self.current_list[-1][self.indexes[-1]].__iter__()

            
            return next(self.iterators[-1])

        
       

iterator = MyIterator(nested_list)

for i in iterator:
    print(i)
