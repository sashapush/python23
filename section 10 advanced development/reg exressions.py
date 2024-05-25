#
# . is anything (1 character) except new lines \n
# + 1 or more of
# * 0 or more of
# ? 0 or one of
#
# https://regexr.com/
# [] character set
# [abc] any of the set
# [a-z] range from a to z
# [A-z] range from A to Z and a to z (matches each character indvidiaull)
# [A-z]+ matches the entire word
# [A-z\.]+  matches  jo.se (dot as dot, not as anything)
# [A-z]+  matches  jo se
#
# emaisl
# [A-z]+@[A-z]+.[a-z]+  = jose@test.com
#
# [A-z]+@[A-z]+\.(com|me) = jose@test.com  jose@test.me

import re
email = "sashapush@tut.by"
#expression = '[a-z]+'#@[a-z]+.[a-z]+' #list ['sashapush', 'tut', 'by']
expression = '[a-z\.]+'#@[a-z]+.[a-z]+' #list ['sashapush', 'tut', 'by']

matches = re.findall(expression,email)
name = matches[0] #sashapush
domain= matches[1] #tut.by

#print(name)
#print(domain)

#if we want to extract email only - no need to use regex
mail = "sashapush@tut.by"
parts = mail.split("@")
#print(parts) ['sashapush', 'tut.by']
name = parts[0]
domain = parts[1]


import re
price = "Price: $1689.50"
#expression = "Price: \$(189.50)"# '189.50' => matches =  189.50; $ means something in regex so need to be ecraned,
# (is a group we extracted via brackets)
expression = "Price: \$([0-9]*\.[0-9].*)"# further improving - any amount of [0-9] followed by . and any number of [0-9] character
matches = re.search(expression, price)
print(matches.group(0)) #entire match
print(matches.group(1)) #first thing in brackets

price_number = float(matches.group(1)) #this way we have extracted python number
print(price_number)


#price = "Price: $16,89.50"
#expression = "Price: \$([0-9,]*\.[0-9].*)"
#price_wo_comma = matches.group(1).replace(",","") #to remove comma from $16,89.50 and get 1689.50
#price_number2 = float(matches.group(1))
#print(price_number2)