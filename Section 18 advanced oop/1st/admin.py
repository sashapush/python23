from user import User

#from database import Database - not needed since we moved save() to saveable and inherited from there

class Admin(User):  # inherits from User, and as continuation of User -  Saveable class
    def __init__(self, username, password, access):  # another init method in admin class.not inherited one
        super(Admin, self).__init__(username, password)  # calls the User's class init method.
        self.access = access  # sets the access level
    def __repr__(self):
        return f"<Admin {self.username}, access {self.access}>"
    def to_dict(self): #returns dictionary representation of this admin object
        #this method overrides the one from User parent class
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }
    #self.save() will be searched in:
    # Admin (this class)
    # User (first inherited from)
    # Saveable (second inherited from) - where it would be found

    #self.save() uses self.to_dict
    #self.to_dict will be searched for in Admin - where it will be found.

    # #removed due to inheritance from Saveable
    # def save(self):
    #     Database.insert(self.to_dict())