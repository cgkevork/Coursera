import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_340375.xml'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print counts

#lst = tree.findall('comments/comment/count')
#print 'User count:', len(lst)
total = 0
#print lst
# 
for count in counts:
	total += float(count.text)
print "total: ", total


