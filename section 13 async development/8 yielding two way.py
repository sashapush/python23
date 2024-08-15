from collections import deque
##DEQUE double-ended queue
#Useful for operations with threads, see asynchronous development
friends = deque(("Rolf","Jose","Charlie","Jen","Anna"))

def get_friend(): #generator
    yield from friends #

# c = get_friend()
# print(next(c))
# print(next(c))

def greet(g): #also generator
    while True:
        try:
            friend = next(g)
            yield f"Hello {friend}"
        except StopIteration:
            print("It's Joever, Anakin!")
            quit()

friends_generator = get_friend() #on this generator we can call next()
g = greet(friends_generator)  #we are giving above generator to greet()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))