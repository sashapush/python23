# Define a PrimeGenerator class, refactor of Task1
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
                for x in range(2, n):
                    if n % x == 0:
                        break
                else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                    self.start = n+1  # next time we need to start from n + 1, otherwise we will be trapped on n
                    return n
        raise StopIteration()  # this is what tells Python we've reached the end of the generator

test = PrimeGenerator(100)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
