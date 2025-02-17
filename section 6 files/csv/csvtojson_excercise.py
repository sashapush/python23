# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

# open file for reading
file = open('csv_file.txt', 'r')
file_contents = file.readlines()
file.close()
#process data and convert to json:
dict=[]
for line in file_contents:
    club,city,country = line.strip().split(",") #get rid of \n and split  
    # club = temp[0]
    # city = temp[1]
    # country = temp[2].strip()
    # string to dict
    my_json_string = {"club": club, "city": city, "country": country}
    dict.append(my_json_string)
print(dict)
# write to file
file_to_write = open('json_file.txt', "w")
json.dump(dict,file_to_write) #first is what we're dumping and 2nd - ABCs argument is where
file_to_write.close()


###shorter, elegant solution:
# import csv
# import json
#
# with open('csv_file.txt', 'r') as f:
#     reader = csv.DictReader(f, fieldnames=['club', 'city', 'country'])
#     data = list(reader)
#
# with open('json_file.txt', 'w') as f:
#     json.dump(data, f)


# import csv
# import json
#
# field_names = ("Club", "City", "Country")
#
# with open('csv_file.txt', 'r') as csv_file:
#     with open('json_file.txt', 'w') as json_file:
#         json.dump(list(csv.DictReader(csv_file, field_names)), json_file)
