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

# find all h2 tags in html
# append to empty list: a tags where href =True ALL within h2 tags
h2s = soup.find_all("h2")
link = []
for h2 in h2s:
    link.append(h2.find("a", href=True))

print(link)
# return all urls from page 1 in list

