def prime_generator(bound):
    # your code starts here (delete the pass):
    for x in range(2, bound): # x starts from 2 to bound
        for y in range(2, x):  # check if there is a number x (1<x<n) that can divide n
            if x % y == 0:  # as long as we can find any such x, then n is not prime
                break
        else:# # if no such x is found after exhausting all 1<x<n
            yield x # generate this prime


g = prime_generator(100)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))