import json

#setup and teardown with open and close
# file = open("friends_json.txt","r")
# file_contents = json.load(file) #now it's a dictionary
# file.close()
#also can be achieved WITH (context manager)
with open("friends_json.txt","r") as file:
    file_contents = json.load(file)  # now it's a dictionary
print(file_contents["friends"][0])

cars = [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Ass'}
]
#json.dump to save list on json file
#serializing - turning into string
with open('cars.json.txt', 'w') as file2: #with
    json.dump(cars, file2)

#print(file2)
#string to dict
my_json_string = '[{"name":"Ass","model":"Booba"}]'

incorrect_car = json.loads(my_json_string) #loads = loadstring
print(incorrect_car[0]['name'])

#json doesn't allow tuples