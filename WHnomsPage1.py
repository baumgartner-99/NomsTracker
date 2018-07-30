#scrape urls from first page

import requests

raw_html = requests.get('https://www.whitehouse.gov/presidential-actions/')
raw_html

# print html tree
from bs4 import BeautifulSoup
soup = BeautifulSoup(raw_html.content, 'html.parser')
print(soup.prettify())

# list all children of html
list(soup.children)
[type(item)for item in list(soup.children)]

html = list(soup.children)
list(html)

#pull all of urls from first page
# link = []
# for a in soup.find_all('a', href=True): 
    # link.append(a)

h2s = soup.find_all("h2")
link = []
for h2 in h2s:
    link.append(h2.find("a", href=True))
# link = list(h2s.find_all("a", href=True))

print(link)