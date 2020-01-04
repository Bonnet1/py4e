import sqlite3
import urllib.request
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Series''')
cur.execute('''DROP TABLE IF EXISTS Dataset''')

cur.execute('''CREATE TABLE IF NOT EXISTS Series
    (series_id TEXT, survey_abbr TEXT, season_code TEXT,
     industry_code INTEGER, region_code TEXT, dataelement_code TEXT,
     ratelevel_code TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Dataset
    (series_id TEXT, year INTEGER, period TEXT, value NUMBER, footnote_codes TEXT)''')

conn_1 = sqlite3.connect('content.sqlite')
cur_1 = conn_1.cursor()

l = list()
count = 0
d = list()
count2 = 0

# cur_1.execute(''' SELECT series_id FROM Dataset ''')
cur_1.execute(''' SELECT DISTINCT series_id FROM Dataset ''')
for row in cur_1:
    id = row[0]
    sur = id[:2]
    sea = id[2]
    ind = id[3:9]
    reg = id[9:11]
    dat = id[11:13]
    rat = id[13]
    t = (id, sur, sea, ind, reg, dat, rat)
    l.append(t)

cur_1.execute(''' SELECT * FROM Dataset ''')
for row in cur_1:
    series_id = row[0]
    year = row[1]
    period = row[2] 
    value = row[3]
    footnote_codes = row[4]
    f = (series_id, year, period, value, footnote_codes)
    d.append(f)

for id, sur, sea, ind, reg, dat, rat in l:
            cur.execute('''INSERT OR IGNORE INTO Series (series_id, survey_abbr , season_code ,
            industry_code , region_code , dataelement_code , ratelevel_code )
            VALUES ( ?, ?, ?, ?, ?, ?, ? )''', ( id, sur, sea, ind, reg, dat, rat) )
            count = count + 1
            if count % 100 == 0:
                print('First: ', count)
            conn.commit()

for series_id, year, period, value, footnote_codes in d:
            cur.execute('''INSERT OR IGNORE INTO Dataset (series_id, year, period, value, footnote_codes) 
            VALUES ( ?, ?, ?, ?, ? )''', (series_id, year, period, value, footnote_codes))
            count2 = count2 + 1
            if count2 % 1000 == 0:
                print('Second: ',count2)
            conn.commit()

print(count)
print(count2)

data_element = 'https://download.bls.gov/pub/time.series/jt/jt.dataelement'
footnote = 'https://download.bls.gov/pub/time.series/jt/jt.footnote'
industry = 'https://download.bls.gov/pub/time.series/jt/jt.industry'
period = 'https://download.bls.gov/pub/time.series/jt/jt.period'
ratelevel = 'https://download.bls.gov/pub/time.series/jt/jt.ratelevel'
region = 'https://download.bls.gov/pub/time.series/jt/jt.region'
seasonal = 'https://download.bls.gov/pub/time.series/jt/jt.seasonal'

cur.execute('''DROP TABLE IF EXISTS Data_Element''')
cur.execute('''DROP TABLE IF EXISTS Footnote''')
cur.execute('''DROP TABLE IF EXISTS Industry''')
cur.execute('''DROP TABLE IF EXISTS Period''')
cur.execute('''DROP TABLE IF EXISTS Ratelevel''')
cur.execute('''DROP TABLE IF EXISTS Region''')
cur.execute('''DROP TABLE IF EXISTS Seasonal''')

cur.execute('''CREATE TABLE IF NOT EXISTS Data_Element
    (code TEXT, text INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Footnote
    (code TEXT, text INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Industry
    (code TEXT, text INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Period
    (period TEXT, abbr TEXT, text INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Ratelevel
    (code TEXT, text INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Region
    (code TEXT, text INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Seasonal
    (code TEXT, text INTEGER)''')

data_l = list()
foot_l = list()
indu_l = list()
peri_l = list()
rate_l = list()
regi_l = list()
seas_l = list()

# Open with a timeout of 30 seconds
document = urllib.request.urlopen(data_element, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    data_l.append(t)

document = urllib.request.urlopen(footnote, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    foot_l.append(t)

document = urllib.request.urlopen(industry, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    indu_l.append(t)

document = urllib.request.urlopen(period, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    peri_l.append(t)

document = urllib.request.urlopen(ratelevel, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    rate_l.append(t)

document = urllib.request.urlopen(region, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    regi_l.append(t)

document = urllib.request.urlopen(seasonal, None, 30, context=ctx)
for line in document:
    txt = line.decode().strip()
    words = txt.split("\t")
    t = list()
    for word in words:
        t.append(word)
    seas_l.append(t)

for code, text, level, selectable, sort_sequence in data_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Data_Element (code, text) 
            VALUES ( ?, ?)''', ( code, text) )
            conn.commit()

for code, text in foot_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Footnote (code, text) 
            VALUES ( ?, ?)''', ( code, text) )
            conn.commit()

for code, text, level, selectable, sort_sequence in indu_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Industry (code, text) 
            VALUES ( ?, ?)''', ( code, text) )
            conn.commit()

for period, abbr, text in peri_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Period (period, abbr, text) 
            VALUES ( ?, ?, ?)''', ( period, abbr, text) )
            conn.commit()

for code, text, level, selectable, sort_sequence in rate_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Ratelevel (code, text) 
            VALUES ( ?, ?)''', ( code, text) )
            conn.commit()

for code, text, level, selectable, sort_sequence in regi_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Region (code, text) 
            VALUES ( ?, ?)''', ( code, text) )
            conn.commit()

for code, text in seas_l[1:]:
            cur.execute('''INSERT OR IGNORE INTO Seasonal (code, text) 
            VALUES ( ?, ?)''', ( code, text) )
            conn.commit()