#this code scrapes all text from a single announcement
import requests

raw_html = requests.get('https://www.whitehouse.gov/presidential-actions/ten-nominations-sent-senate-today-4/')
raw_html

# print html tree
from bs4 import BeautifulSoup
soup = BeautifulSoup(raw_html.content, 'html.parser')
print(soup.prettify())

# list all children of html
list(soup.children)
[type(item)for item in list(soup.children)]

html = list(soup.children)[2]
list(html.children)

# find all p tags within html tree, indexed 2-13 to grab all relevant items
text = soup.find_all('p') [2:13]
print(text)













