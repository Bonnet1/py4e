import sqlite3
import urllib.request
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_element = 'https://download.bls.gov/pub/time.series/jt/jt.dataelement'
footnote = 'https://download.bls.gov/pub/time.series/jt/jt.footnote'
industry = 'https://download.bls.gov/pub/time.series/jt/jt.industry'
period = 'https://download.bls.gov/pub/time.series/jt/jt.period'
ratelevel = 'https://download.bls.gov/pub/time.series/jt/jt.ratelevel'
region = 'https://download.bls.gov/pub/time.series/jt/jt.region'
seasonal = 'https://download.bls.gov/pub/time.series/jt/jt.seasonal'

conn = sqlite3.connect('mapping.sqlite')
cur = conn.cursor()

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
