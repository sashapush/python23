#decorator is higher order function (which takes in functions as argument) and they also RETURN a function
user = {    'username':'jose123', 'access_level': 'admin'}
#user = {    'username':'jose123', 'access_level': 'guest'}

def user_has_permission(func):
    def secure_func():
        if user.get("access_level") == 'admin': #obv this code is returned when user level is admin
            return func()
    return secure_func

    # initial way of handling below
    # if user.get("access_level") == 'admin':
    #     return func
    # raise RuntimeError

def my_function():
    return 'Password for admin panel is 1234.'

my_secure_function = user_has_permission(my_function)
print(my_secure_function())