# scrape multiple pages from one link
import urllib.request

html = urllib.request.urlopen('https://www.whitehouse.gov/presidential-actions/').read()
print(html)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll('a')

for link in links:
    print(href)

collection = ['hey', 5, 'd']
for x in collection:
    print(x)

