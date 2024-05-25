friends_last_seen = {
    'Rolf': 31,
    'Abby': 1,
    'Eloy': 2
} #dictionary itself is the value, while friends_last_seen is like post it note


def see_friend(friends, name):
    print(friends is friends_last_seen) #compares IDs unlike how == compares contetns
    print(id(friends)) #value is equal to this
    friends[name] = 0

print(id(friends_last_seen)) #value is equal to this
print(id(friends_last_seen["Rolf"]))
see_friend(friends_last_seen, "Rolf")
print(id(friends_last_seen["Rolf"]))

print(id(friends_last_seen)) #value is equal to this

######################
age = 20
def incr_age(current_age):
    current_age = current_age+1 #current_age id will change, age id will not

print(id(age))
incr_age(age)
print(id(age))

########################
print("NEWBLOCK\n")
primes = [2,3,5]
print(id(primes))
#primes = [2,3,5] +[7,1] #will give different ids\
#primes = primes +[7,1] #will give different ids
primes +=[7,1] #prines = prines.__iadd__([7,1]) So the object is modified; iadd is to modify self, when possible
print(primes)

print(id(primes))