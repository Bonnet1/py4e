import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'https://www.py4e.com/code3/geoxml.py'
parms = dict()
parms['address'] = address
url = urllib.parse.urlencode(parms)
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print(data)
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('count')
print('Comments count:', len(counts))