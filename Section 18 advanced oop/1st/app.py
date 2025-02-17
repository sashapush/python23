from admin import Admin
from database import Database
from user import User

a = Admin('sapushka', '1234', " access")
u = User('user1', 'password')

a.save()
u.save()
users = [a, u]

for user in users:
    user.save()

print(Database.find(lambda x: x['username'] == 'sapushka'))
