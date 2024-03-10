#map function runs a function for an iterable
friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
friends_lower = map(lambda x: x.lower(), friends) #produces a generator
print(next(friends_lower))
print(list(friends_lower))
#as with filter() map should be used only if people on the project are used to it.
#otherwise generator comprehension is better option.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_fict(cls, data):
        return cls(data['username'], data['password'])

users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]
#map here is more readable in this case.
#users = [User.from_fict(users) for user in users]
users = map(User.from_fict, users)
print(users)
for user in users:
    print(user.username+" "+ user.password)
#print(f"Username: {next(users).username}, Password: {users.password}")
