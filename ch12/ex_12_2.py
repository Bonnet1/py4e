# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Take input from user
url = input('Enter URL:')
html = urllib.request.urlopen(url, context=ctx).read()
count = input('Enter count:')
position = input('Enter position:')
cnt = int(count)
loc = int(position)-1
print('Retrieving: ', url)

# Click through all links to pull final name
while cnt > 0:
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    names = []
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None))
    print('Retrieving: ', links[loc])
    html = urllib.request.urlopen((links[loc]), context=ctx).read()
    cnt -= 1