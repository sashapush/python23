accounts = {
    'checking': 1957.00,
    'savings': 36980
}
def add_balance(amount: float, name: str = 'checking') -> float: #returns float; name: str = 'checking' => set's the default value of parameter
    #or name = 'checking')
    #default argument should be AFTER non-default argument
    """Function to update the balance of an account and return the new balance""" #this is doc string
    accounts[name] += amount
    return accounts[name]

#Imagine we’ve got a list of transactions that we’ve downloaded from our bank page; and they look somewhat like this:
transactions = [
  (-180.67, 'checking'), #this tuple is iterable
  (-220.00, 'checking'),
  (220.00, 'savings'),
  (-15.70, 'checking'),
  (-23.90, 'checking'),
  (-13.00, 'checking'),
  (1579.50, 'checking'),
  (-600.50, 'checking'),
  (600.50, 'savings'),
]

#to apply this list of tuples we can do this:
for t in transactions:
    #new way, "Argument unpacking" to unpack the iterable into arguments
    add_balance(*t)
    #old way = add_balance(t[0],t[1])
    #amount, name = t
    add_balance(amount=t[0], name=t[1]) #named arguments

print(accounts['savings'])
print(accounts['checking'])




class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

# imagine these users are coming from a database...
users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]
user_objects = map(User.from_dict, users)
"""
The option of using a list comprehension is slightly uglier, I feel:
"""
user_objects = [User.from_dict(u) for u in users]

"""
Instead of having a `from_dict` method in there, we could do this, using named argument unpacking:
"""
#NEW WAY OF DOING THE SAME BUT WITH ARGUMENT UNPACKING
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]
#overcomplication below
user_objects = [User(username=data['username'],password=data['password'])for data in users]

#awesomness with arguments unpacking below
user_objects = [User(**data) for data in users]
# ** unpacks dictionary as named arguments for a function
"""
If our data was not in dictionary format, we could do:
"""

users = [
    ('rolf', '123'),
    ('tecladoisawesome', 'youaretoo')
]

user_objects = [User(*data) for data in users]