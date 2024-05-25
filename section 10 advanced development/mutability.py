friends_last_seen = {
    'Rolf': 31,
    'Abby': 1,
    'Eloy': 2
}

print(id(friends_last_seen))  # id returns address of object in memory , f.e. 1734653137344

#Let's create another dictionary
friends_last_seen = {
    'Rolf': 31,
    'Abby': 1,
    'Eloy': 2
}  # looks the same but is enterily new dictionary, objects are not the same as seen in id below.
print(id(friends_last_seen))

friends_last_seen["Rolf"] = 0 #BEHIND THE scenes the following is happening -> friends_last_seen__setItem__(self,'Rolf')
print(id(friends_last_seen)) #id will be THE SAME since we modify the object,mutate it as it called
#__________________________________________________________________________________________________________________________________
#integers though are immutable. Same as floats, strings and tuples
my_int = 5
print(id(my_int))
#5 has one value,
my_int = my_int +1 #behind the scenes - my_int.__add__(self,1): smth like return cls(self.value + 1) - new integer object in short
#my_int+=1 #my_int.__iadd__(self,1)
print(id(my_int))

################
friends = ['Jose', 'As']
print("Printing friends id")
print(id(friends))

friends.append("Jen")
print(id(friends))
#List updated with "Jen" is still the same list. We've mutated the list, not changed it