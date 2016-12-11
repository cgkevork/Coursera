import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = 3
pos = 4
p=1
c=1

# Retrieve all of the anchor tags
while c <= count:
	tags = soup('a')
	for tag in tags:
		if p > pos: return
		address = tag.get('href', None)
    	
    	#print 'Contents:',tag.contents[0]
    	p += 1
    
    url = address
    html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
    c +=1

print address