#https://blog.teclado.com/python-itertools-part-1-product/
# The product function is one of several handy combinatoric iterators included in the itertools module.
# Combinatoric iterators are related to an area of mathematics called enumerative combinatorics, which is concerned
# with the number of ways a given pattern can be formed.
from itertools import product

#that's how we get all possible roll dice combinations for 2 6-sided dices with list comprehension
roll_combinations = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
print(roll_combinations)

#from itertools import product

dice_combinations = product(range(1, 7), repeat=2)
print(list(dice_combinations))
#The product function accepts any number of iterables as positional arguments,
# and has an optional keyword only parameter called repeat.
#When we provide two or more iterables as arguments, the product function will find all the ways we can match an element from one
#   of these iterables to an item in every other iterable. For example, we might have a pair of lists like so:
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
#When we pass these lists to the product function, we get the following:

cartesian_product = product(list_1, list_2)
print(list(cartesian_product))
print('\n')
# ('a', 1) ('a', 2) ('a', 3) ('b', 1) ('b', 2) ('b', 3) ('c', 1) ('c', 2) ('c', 3)

#If we were to add a third iterable, every one of these tuples would be matched up to an item in this third iterable. For example, if we had a third list containing "x", "y", and "z", we would get output like this:

# ('a', 1, 'x') ('a', 1, 'y') ('a', 1, 'z') ('a', 2, 'x') ... etc.
#The repeat parameter is most useful for when we want to use the same iterable multiple times.
# We can see an example of this in our code for finding roll combinations. We can easily add more and more dice by increasing the value of repeat.
#If we set a repeat value of 2 or more when we have multiple iterables, product will duplicate all of the iterables for the purposes of finding the
# cartesian product. The following functions are identical in terms of functionality:
c_product_1 = product(["a", "b", "c"], [1, 2, 3], repeat=2)
c_product_2 = product(["a", "b", "c"], [1, 2, 3], ["a", "b", "c"], [1, 2, 3])
