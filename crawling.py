import re
import urllib2
url="https://www.google.com/finance?q="
print url
stock=raw_input("Enter stock")
url=url+stock
print url
data=urllib2.urlopen(url).read()
#data1=data.decode("utf-8")
print data
k=re.search('meta itemprop="price"',data)

print newString
#print k
