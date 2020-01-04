import sqlite3
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://download.bls.gov/pub/time.series/jt/jt.data.0.Current'

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Dataset''')

cur.execute('''CREATE TABLE IF NOT EXISTS Dataset
    (series_id TEXT, year INTEGER,
     period TEXT, value NUMBER, footnote_codes TEXT)''')

many = 0
count = 0
fail = 0
l = list()

# Open with a timeout of 30 seconds
document = urllib.request.urlopen(url, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split()
    t = list()
    for word in words:
        t.append(word)
    if(len(t)) < 5:
        t.append('X')
    l.append(t)
if document.getcode() != 200 :
    print("Error code=",document.getcode(), url)

# for series, year, period, value, footnote in l[:10]:
#     print(series, year)

for series, year, period, value, footnote in l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Dataset (series_id, year, period, value, footnote_codes) 
            VALUES ( ?, ?, ?, ?, ? )''', ( series, year, period, value, footnote) )
            count = count + 1
            conn.commit()

print(count)