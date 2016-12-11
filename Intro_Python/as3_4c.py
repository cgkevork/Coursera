import urllib
from bs4 import *
url = raw_input('Enter - ')
position=int(raw_input('Enter Position'))
count=int(raw_input('Enter Count'))

#perform the loop "count" times.
for _ in xrange(0,count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags=soup.findAll('a')
    for tag in tags:
        url= tag.get('href')
        tags=soup.findAll('a')
        # if the link does not exist at that position, show error.
        if not tags[position-1]:
            print "A link does not exist at that position."
        # if the link at that position exist, overwrite it so the next search will use it.
        url = tags[position-1].get('href')
print url