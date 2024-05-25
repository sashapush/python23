import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    #regex = '^([a-zA-Z0-9]+[-_()]*)+(\.jpg|\.jpeg|\.png|\.gif)$' my not fully correct way
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    return re.match(regex, filename) is not None


list = ["ass.jpg","a","(aer3244c12.jpg","b","c","test.gif.jpg","Ass",".jpg","Ada.jpg","1.jpg","a1.jpg","a1-a_2(1).jpg","123as","12sas"]

#print(is_filename_safe(list))

# to test locally - let's rewrite is_filename_safe
def is_filename_safe(list):
    # you only need to change the regular expression (regex) below
    #regex = '^([a-zA-Z0-9]+[-_()]*)+(\.jpg|\.jpeg|\.png|\.gif)$' my not fully correct way
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    matches = []
    for item in list:
        s = re.match(regex,item)
        if s is not None:
            matches.append(s)
    return matches

print(is_filename_safe(list))

# Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
#
# If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).