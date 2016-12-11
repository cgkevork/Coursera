import urllib
fhand = urllib.urlopen('www.data.pr4e.org/intro-short.txt')
for line in fhand:
	print line.strip()