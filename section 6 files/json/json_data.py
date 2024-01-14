import json

file = open("friends_json.txt","r")
file_contents = json.load(file) #now it's a dictionary
file.close()

print(file_contents["friends"][0])

cars = [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Ass'}
]
#json.dump to save list on json file
#serializing - turning into string
file2 = open('cars.json.txt', 'w')
json.dump(cars, file2)
file2.close()
#print(file2)
#string to dict
my_json_string = '[{"name":"Ass","model":"Booba"}]'

incorrect_car = json.loads(my_json_string) #loads = loadstring
print(incorrect_car[0]['name'])

#json doesn't allow tuples