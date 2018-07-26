urls = [1, 2, 3]

...
parse a url
return p tags
...


==============

nomination_urls = []


def getUrls(url):
    ...
    code to parse list of nominations for their urls
    return list of urls as a list
    ...

# to get page numbers
first_page = requests.get('firstpageurl.html').text
make first page into soup
parse the soup for the a tags at the bottom of the page
get the last number in that list of tags

for index in range(1,70):
    list_of_urls = getUrls("whitehouse.gov/.../page/" + index)
    nomination_urls.append(list_of_urls)



...
def parsePage(url):
    # parse a url
    # requests.get("http://...")
    requests.get(url)
    # return p tags
    return str(p tags combined)
...

list_of_nomination_text = []

for url in nomination_urls:
    parsedPage = parsePage(url)
    list_of_nomination_text.append(parsedPage)

# writes the variable to a textfgile called filename in same folder you're working in
with open(filename, "w") as ofile:
    ...
    write list_of_nomination_text into a file here
    ...

    