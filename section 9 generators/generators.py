#generate 100
class FirstHundredGenerator:
    def __init__(self):
        self.number=0

    def __next__(self): #dunder method, same as next(myobject)
        if self.number < 100:
            current = self.number
            self.number +=1
            return current
        else:
            raise StopIteration() #to address case when self.number !< 100
#All object with def __next__(self) are called iterators
#All generators are iterators
#Not all iterators are generators
my_gen = FirstHundredGenerator()
#default syntax
# print(my_gen.number)
# my_gen.__next__()
# print(my_gen.number)

#Syntax used by generators
print(next(my_gen))
print(next(my_gen))

# my_gen object is iterator as in we can call "next" and get the next value. But it's not iterable
# as in: for i in my_gen: #won't work
#print(i)

#not generator below
class FirstFiveIterator: #doesn't generate anything, we keep track of i, which is list
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i = 0
    def __next__(self):
        if self.i <len(self.numbers):
            current = self.numbers[self.i] #we don't generate stuff, we take them from list
            self.i += 1
            return current
        else:
            raise StopIteration()