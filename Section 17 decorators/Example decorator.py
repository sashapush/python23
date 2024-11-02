import functools
# decorator is higher order function (which takes in functions as argument) and they also RETURN a function
user = {'username': 'jose123', 'access_level': 'admin'}
# user = {    'username':'jose123', 'access_level': 'guest'}
def user_has_permission(func):
    @functools.wraps(func) #tells Python that secure_func() is wrapping around original "func" - to keep original function name and docstring 
    def secure_func(): #wrapper function
        if user.get("access_level") == 'admin':  # obv this code is returned when user level is admin
            return func()
    return secure_func
    # initial way of handling below
    # if user.get("access_level") == 'admin':
    #     return func
    # raise RuntimeError
@user_has_permission #this decorator removes the need for
#my_secure_function = user_has_permission(my_function) below
def my_function():
    """Allows us to retrieve password for the admin panel"""
    return 'Password for admin panel is 1234.'
@user_has_permission
def another_fuction():
    pass

 #my_secure_function = user_has_permission(my_function)
print(my_function())
print(my_function.__name__) #secure_func since it replaces my_function when running through the decorator
print(my_function.__doc__) #returns none, instead of "    """Allows us to retrieve passwrod for the admin panel""", because secure_func has no doc
print(another_fuction.__name__)