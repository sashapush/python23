from functools import wraps
# decorator is higher order function (which takes in functions as argument) and they also always RETURN a function
user = {'username': 'jose123', 'access_level': 'admin'}
# user = {    'username':'jose123', 'access_level': 'guest'}
def third_level(access_level):
    def user_has_permission(func):
        @wraps(func) #tells Python that secure_func() is wrapping around original "func" - to keep original function name and docstring
        def secure_func(panel): #wrapper function; #needs to have param, since without it my_function() will give 1 param when 0 expected
            if user.get("access_level") == access_level:  # obv this code is returned when user level is admin
                return func(panel)  #same, param should be returned
        return secure_func
    return user_has_permission


@third_level('admin') #it's a function call, but decorator
#essentially it's
#user_has_permission = third_level('admin')
#my_function=user_has_permission(my_function)
def my_function(panel):
    """Allows us to retrieve password for the admin panel"""
    return f'Password for {panel} panel is 1234.'

def another_function():
    return "Hello there"
#print(my_function())
#print(my_function.__name__) #secure_func since it replaces my_function when running through the decorator
#print(my_function.__doc__) #returns none, instead of "    """Allows us to retrieve passwrod for the admin panel""", because secure_func has no doc
#print(another_fuction.__name__)

print(my_function.__name__)
print(my_function('movies'))
print(my_function('user'))
#another_fuction() #TODO there's a challenge to use decorator with different functions having different number of arguments

user_has_permission = third_level('admin')
'''we're calling a function, giving it 'access_level' parameter;
which creates another function "def user_has_permission" and that's our decorator
decorator acts as normal - takes in a function "func", wraps around it and returns another function "def secure_func"
and calls original function "func(panel)" with any arguments'''

#my_function = third_level('admin')(my_function)