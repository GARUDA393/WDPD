import requests, webbrowser, bs4
search = input("Enter what you want to search: ")
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + search)
res.raise_for_status()
#Retrieve top search result links
soup=bs4.BeautifulSoup(res.text, features="html.parser")
linkElems = soup.select('div#main > div > div > div > a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
