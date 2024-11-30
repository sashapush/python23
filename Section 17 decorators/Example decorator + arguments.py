#copied from Example decorator.py

import functools
# decorator is higher order function (which takes in functions as argument) and they also always RETURN a function
user = {'username': 'jose123', 'access_level': 'admin'}
#commented to comply with learning code
#def third_level(access_level):
def user_has_permission(func):
    @functools.wraps(func) #tells Python that secure_func() is wrapping around original "func" - to keep original function name and docstring
    def secure_func(*args, **kwargs): #*args(tuple) takes in any number of positional arguments and **kwargs(dictionary) takes in any number of named arguments
        if user.get("access_level") == "admin":  # obv this code is returned when user level is admin
            return func(*args, **kwargs)  #same, param should be returned
    return secure_func

@user_has_permission
#essentially it's
#user_has_permission = third_level('admin')
#my_function=user_has_permission(my_function)
def my_function(panel):
    """Allows us to retrieve password for the admin panel"""
    return f'Password for {panel} panel is 1234.'

@user_has_permission
def another_function():
    return "Hello there"


print(my_function.__name__)
print(my_function('movies'))
print(my_function('user'))
print(another_function())
