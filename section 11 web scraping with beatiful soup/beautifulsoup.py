#pip install beautifulsoup4 / File - Settings - Project - Project Interpreter
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = soup.find('h1')
    print(h1_tag.string) #only content. Wo string result will be <tag>value</tag>
def find_list_items():
    list_items = soup.find_all('li') #list of tags+value
    list_content = [e.string for e in list_items] #list comprehension to display list of values, wo tags
    print(list_content)
def find_paragraph():
    paragraph = soup.find('p', {'class': 'subtitle'}).string #only for paragraph with class subtitle
    print(paragraph)
def find_other_paragraph():
    paragraphs = soup.find_all('p') #find all paragraphs
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class',[])] #return empty list if we couldn't find the 'class' in this dictionary;since we are doing iteration - we can't iterate over nothing, but we can iterate over empty list. Alternative opinion here https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477874#questions/12385902
    """let suppose python goes with  1st one it gets the class which is ["subtitle"] so it won't do anything
then it goes with 2nd p tag which has no "class" attribute so p.attrs.get('class') gives value None
[ p for p in paragraphs if 'subtitle' not in None]
python can't search for string in None. None means nothing it's different from empty list
But if you do
[p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
it give a default value of empty list just like defaultdict (just giving you some comparision)
then it searches for 'subtitle' in empty list []
it can't find subtitle so new list is made with "p tag with no class" as the list member
I hope you found it helpful
    """
    # not in p.attrs.get('class') =  "not in p.attrs['class']", but get method doesn't raise key error if there is no key
    print(other_paragraph[0].string)


find_title()
find_list_items()
find_paragraph()
find_other_paragraph()