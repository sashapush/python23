#not needed for lambda
# def starts_with_r(friend):
#     return friend.startswith('R')

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
#another_starts_with_r = (f for f in friends if f.startswith("R"))
#filter function below = generator comprehension above (it's faster in this case, since we don't need to create lambma funciotn
start_with_r = filter(lambda friend: friend.startswith("R"), friends)
#rework with lambda above"
#start_with_r = filter(starts_with_r, friends) #arg 1- filter function which returns True/False
#print(start_with_r)  # returns generator!

#to return all in list:
print(list(start_with_r))

#to print results individually:
# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

#another filter function


def my_custom_filter(function,iterable):
    for i in iterable:
        if function(i): #return i if the function(i) is True
            yield i

start_with_r2 = my_custom_filter(lambda friend: friend.startswith("R"), friends)
print(next(start_with_r2))
print(next(start_with_r2))
print(next(start_with_r2))
#OR
#print(list(start_with_r2))
