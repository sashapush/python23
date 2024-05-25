"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque

The main purpose of this video is to make you aware that these things exist, in case we have to use them later on (or when you encounter a situation where using one of these would be useful).

Normally what happens in those situations is we struggle to build our own thing to do what we need it to do. Knowing that these exist could save you a lot of effort!
"""
# COUNTER
from collections import Counter

device_temps = [13.0, 14.0, 15.0, 17.0, 18.5, 19.5, 14.0, 14.5, 15.0]

temps_counter = Counter(device_temps)
# print(temps_counter[14.0]) #returns number of entities - 2

# print(Counter({'hello':5, "hi":3})['hi'])returns 3



# defaultdict
###defaultdict, never returns key error. It returns the value specified when the object was instantiated
# dict = {'hello': 5}
# print(dict) = key error
from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'),
             ('Charlie', 'Manchester')]  # Rolf got a master's
alma_maters = defaultdict(list)  # list()

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

# to add exception handling for missing key:
alma_maters.default_factory = None
# print(alma_maters["Rolf"])
# print(alma_maters["Anne"])
########################################################ANOTHER EXAMPLE
my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]
# defaultdict takes in a function, so we can't directly use the value
coworker_companies = defaultdict(lambda: my_company)  # {"Jen": "Teclado", etc}
for person, company in other_coworkers:
    coworker_companies[person] = company
# print(coworker_companies[coworkers[0]])
# print(coworker_companies[other_coworkers[0][0]]) #= print(coworker_companies['Rolf'])

# ORDEREDDICT
from collections import OrderedDict

# not so useful lol
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 10
o['Jen'] = 3

# print(o)  # keys are always in the order in which they were inserted
# OrderedDict([('Rolf', 6), ('Jose', 10), ('Jen', 3)])

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)  # as if move to the start
# OrderedDict([('Jose', 10), ('Jen', 3), ('Rolf', 6)])
# print(o)

o.popitem()  # remove last item

# print(o)

###########################################################
# namedtuple; Useful with data which doesn't  warrant creating classes

from collections import namedtuple

#account = ('checking', 1850.9)

Account = namedtuple('Account', ['name', 'balance']) #type, list of fields in the tuple
#Account is like class name/ type, but a tuple :)
account = Account(name='checking', balance=1850.9) #we're using named tuple instance/ new instance of Account type. We can use fiedl anems
# print(account.name) #checking
# print(account.balance) #1850.9
# print(account) #Account(name='checking', balance=1850.9)
#we can still do tuple destructuring
#name, balance = account

# print(account[0]) #name
# print(account[1]) #balance
# type Account. _make takes in tuple and will associate respective field
# accountNamedTuple = Account._make(account) #is the same as
# accountNamedTuple = Account(*account)
# print(accountNamedTuple._asdict())
# print(accountNamedTuple._asdict()['balance']) # to access property

##DEQUE double-ended queue
#Useful for operations with threads, see asynchronous development in the future.
from collections import deque

friends = deque(('Rolf','Ass','Booba')) #tuple is appending deque object 1 by 1
friends.append('Jose')
friends.appendleft('Juan')
print(friends)
friends.pop() #remove from the end
friends.popleft() #remove from start
print(friends)
