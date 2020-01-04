import sqlite3

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Dataset ''')
cur.execute('''DROP TABLE IF EXISTS Decode ''')
cur.execute('''DROP TABLE IF EXISTS Data_Element ''')
cur.execute('''DROP TABLE IF EXISTS Footnote ''')
cur.execute('''DROP TABLE IF EXISTS Industry''')
cur.execute('''DROP TABLE IF EXISTS Period''')
cur.execute('''DROP TABLE IF EXISTS Ratelevel''')
cur.execute('''DROP TABLE IF EXISTS Region''')
cur.execute('''DROP TABLE IF EXISTS Seasonal''')

cur.execute('''CREATE TABLE IF NOT EXISTS Dataset
    (id INTEGER PRIMARY KEY, series_id TEXT, year INTEGER,
     period TEXT, value NUMBER, footnote_codes TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Decode
    (series_id TEXT, survey_abbr TEXT, season_code TEXT,
     industry_code INTEGER, region_code TEXT, dataelement_code TEXT,
     ratelevel_code TEXT)''')
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

conn_1 = sqlite3.connect('content.sqlite')
cur_1 = conn_1.cursor()

cur_1.execute(''' SELECT * FROM Dataset''')

for row in cur_1:
    cur.execute('''INSERT OR IGNORE INTO Dataset''')
    conn.commit()