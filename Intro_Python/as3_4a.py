import urllib
#from bs4 import BeautifulSoup
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_340378.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('span')
#print tags
count =0
sum = 0
#/
for tag in tags:
    # Look at the parts of a tag

    #print 'Contents:',tag.contents[0]
    count +=1
    #print 'count: ', count
    sum = sum + float(tag.contents[0])

print "Count ",count    
print "Sum: ", sum

