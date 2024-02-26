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

    #optimise by adding __iter__ into class
    def __iter__(self):
        return FirstHundredGenerator() #returns iterator


# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator() #returns iterator

# print(sum(FirstHundredGenerator()))
#
# for i in FirstHundredGenerator():
#     print(i)

class AnotherIterable:
    def __init__(self):
        self.cars = ['Car1','Car2']

    def __len__(self):  #if object has __len__ and __getItem__ -it's iterable
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

for car in AnotherIterable():
    print(car)

my_num = [x for x in [1,2,3,4,5]] #list comprehension
my_num_gen = (x for x in[1,2,3,4,5]) #generator comprehension, not tuple

print(next(my_num_gen))
print(next(my_num_gen))