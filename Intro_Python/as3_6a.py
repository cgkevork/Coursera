import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_340379.json'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)

count = 0
sum = 0

length = len(info["comments"])

while count < length:
	num = info["comments"][count]["count"]
	sum = sum + num
	count += 1
	
print "Sum: ", sum
