import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Parse input into handle
url = input('Enter location:')
print('Retrieving', url)
# html = urlopen(url, context=ctx).read()
html = urllib.request.urlopen(url, context=ctx)
data = html.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count:', len(lst))

sum = 0
for item in lst:
    # print('Name', item.find('name').text)
    # print('Comments:', item.find('count').text)
    sum = sum + int(item.find('count').text)
print('Sum:',sum)