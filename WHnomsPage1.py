#this page scrapes all of the urls from page 1 of the presidential action announcements
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
link = []
for a in soup.find_all('a', href=True): 
    link.append(a)
print(link)
