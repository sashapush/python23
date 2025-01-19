from database import Database
class Store:
    def to_dict(self): #partially duplicated from admin
        pass

    def save(self): #fully duplicated from admin.py, that's why it's replaced by inheritance
        Database.insert(self.to_dict())
