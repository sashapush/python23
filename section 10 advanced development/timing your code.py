import time


def measure_runtime(func): #this is a decorator (higher order function) cuz it takes in another function
    start = time.time()
    func()
    end = time.time()
    print(end-start)
def powers(limit): #first-class function, cuz it's being called
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(5000000)) #lambda allows to pass the argument, w/o it we can't pass argument

# print(powers(5))[0, 1, 4, 9, 16]
#reworked into measure function above
# start = time.time() #current time since 1970, so timestamp but with decimal
# powers(50000000)
# end = time.time()
#
# diff = end - start
#
# print(diff)

import timeit #used for timing code snippets

print(timeit.timeit("[x**2 for x in range(10)]")) #(is what we time)  #total across many iterations; it's list comprehension
print(timeit.timeit("list(map(lambda x: x**2, range(10)))")) # a bit slower than list comprehension

#if we want a list of things - use list comprehension; it'; much more readable
#if we want to use the item one by one - user list map
