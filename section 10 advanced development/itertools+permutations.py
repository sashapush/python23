#we're going to look at a few more combinatoric iterators from the itertools module: permutations, combinations,
# and combinations_with_replacement.
#First, let's look at permutations. permutations is concerned with finding all the possible orderings for a given collection of items.
# For example, if we have the string "ABC", permutations will find all the ways we can reorder the letters in this string, so that each order is unique.

from itertools import permutations

p_1 = permutations("ABC")
# ('A', 'B', 'C') ('A', 'C', 'B') ('B', 'A', 'C') ('B', 'C', 'A')
# ('C', 'A', 'B') ('C', 'B', 'A')
#By default, permutations returns different orderings for the entire collection, but we can use the optional r parameter to limit the function
# to finding shorter permutations.
p_2 = permutations("ABC", r=2)
# ('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')
#Providing an r value greater than the length of the collection passed into permutations will yield an empty permutations object


#Now let's take a look at combinations. combinations returns an iterable object containing unique combinations of elements from a provided collection.
# Note that combinations isn't concerned with the order of elements, so combinations will treat ('A', 'B') as being identical to ('B', 'A') in its results.

#The length of the resulting combinations is controlled by the r parameter once again, but in the case of combinations, this argument is mandatory.

from itertools import combinations

c_1 = combinations("ABC", r=2)
# ('A', 'B') ('A', 'C') ('B', 'C')

c_2 = combinations("ABC", r=3)
# ('A', 'B', 'C')
#It is possible to get duplicate elements back from combinations, but only if the provided iterable contains multiple instances of a given element.
# (1, 2, 3, 1), for example.

c_3 = combinations((1, 2, 3, 1), r=2)
# (1, 2) (1, 3) (1, 1) (2, 3) (2, 1) (3, 1)
#In this case (1, 2) and (2, 1) are not simply the same elements in a different order, the 1s are in fact different elements in the original collection.

#It's possible to include instances where an item is paired with itself using the combinations_with_replacement function. It works just like combinations,
# but will also match every element to itself.

from itertools import combinations, combinations_with_replacement

c_4 = combinations((1, 2, 3), r=2)
# (1, 2) (1, 3) (2, 3)

c_5 = combinations_with_replacement((1, 2, 3), r=2)
# (1, 1) (1, 2) (1, 3) (2, 2) (2, 3) (3, 3)
#That wraps up the combinatoric iterators! I hope you learnt something new, and be sure to check out the official documentation for more details.