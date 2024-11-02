# Exercise: decorators (Python 3.10)
# In the previous lecture, we learned about decorators, which are a very unique tool in Python.
# # In this exercise, we will see how to make use of decorators.
# # Suppose we have a function delete_database() that can delete our whole database:
# # def delete_database():
#     # perform deletion
#     print('Database deleted!')
# We want to limit the access to this function, since it's very dangerous. Suppose we have a user dictionary that stores the current user's identity information like this:
# # user = {
#     'id': 1,
#     'name': 'Jose',
#     'role': 'admin'
# }
# We want you to build a decorator check_permission() that checks the user's role  (access level) and only allows 'admin ' to delete the database. If the user is not an admin, the decorator will raise a PermissionError, which is a built-in Python error, like the ones we have already seen. You may include an error message like You are not an admin. along with the PermissionError.
# # Then you will need to create a function secure_delete_database() using the check_permission() decorator and the original delete_database() function.
# # Happy coding!
# # — Jose and the Teclado team


# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}

# delete_database() function, DO NOT CHANGE
def delete_database():
    # perform deletion
    print('Database deleted!')

# ---- Do not change the code above ----


# You code starts here:
# Define a check_permission() decorator:
def check_permission(func):
    def wrapper():
        if user.get('role') == 'admin':
            return func() #we return function, not variable so that the function can be executed
        else:
            raise PermissionError("You are not an admin, baka.")
    return wrapper
# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
secure_delete_database = check_permission(delete_database)
