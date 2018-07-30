import requests
from requests import get

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


#parse p tags from one url
page1 = requests.get('https://www.whitehouse.gov/presidential-actions/president-donald-j-trump-announces-intent-nominate-personnel-key-administration-posts-55/')
page1

soup2 = BeautifulSoup(page1.content, 'html.parser')
print(soup2.prettify())

list(soup2.children)
[type(item)for item in list(soup2.children)]

html = soup2.find("div", {"class": "page-content"})
print(html)

ptags = list(html.find_all("p"))
print(ptags)

#define function to list urls from each page
h2s = soup.find_all("h2")
nominations_urls = []
def get_Urls(url, index):
    for h2 in h2s:
        nominations_urls.append(h2.find("a", href=True))
print(nominations_urls)

#to get multiple pages
first_list = requests.get('https://www.whitehouse.gov/presidential-actions/').text
soup3 = BeautifulSoup(first_list, 'html.parser')
print(soup3.prettify())

#print a tags - need to print without class or href showing
pageNum = soup3.find("div", {"class": "pagination"})
#page 1 is different tag than others
spanTag = pageNum.find("span", {"class": "page-numbers current"})
print(spanTag)
atags = list(pageNum.find_all("a", {"class": "page-numbers"}))
print(atags)
print(atags[-1])

## need to combine links from page 1 to list of links in rest of the pages

#all URLs from page 2 on
for index in range(0,70):
    list_of_urls = get_Urls("https://www.whitehouse.gov/presidential-actions/page/2/", index)
    nominations_urls.append(list_of_urls)
    time.sleep(3)
print(nominations_urls)

#create function to parse individual announcement
html = soup2.find("div", {"class": "page-content"})
ptags = list(html.find_all("p"))
def parsePage(url):
    requests.get('https://www.whitehouse.gov/presidential-actions/president-donald-j-trump-announces-intent-nominate-appoint-personnel-key-administration-posts-15/')
    return str()

list_of_noms_text = []

for url in nominations_urls:
    parsedPage = parsePage(url)
    list_of_noms_text.append(parsedPage)
#here, I hit enter in the terminal and the code stops?
print(list_of_noms_text)
    
with open("Nomination.txt", "w") as ofile:
    ofile.write('\n'.join(list_of_noms_text))
