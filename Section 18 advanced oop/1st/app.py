from admin import Admin
from database import Database
a = Admin('sapushka','1234'," access")

a.save()
print(Database.find(lambda x: x['username'] == 'sapushka'))