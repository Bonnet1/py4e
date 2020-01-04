import sqlite3
import time
import zlib

howmany = int(input("How many to dump? "))

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''
SELECT Dataset.series_id
, Dataset.year
, Dataset.period
, Dataset.value
, Series.industry_code 
, Industry.text
FROM Dataset 
LEFT JOIN Series on Dataset.series_id = Series.series_id
LEFT JOIN Industry on industry_code = Industry.code
WHERE industry_code > 100000 AND YEAR = '2019'
''')
dataset = dict()
for message_row in cur :
    dataset[message_row[0],message_row[1],message_row[2],message_row[4],message_row[5]] = (message_row[3])

print("Loaded datapoints=",len(dataset))

counts = dict()
for (series_id, value) in list(dataset.items()):
    industry = series_id[4]
    value = value
    if industry not in counts:
        counts[industry] = value
    else:
        counts[industry] += value

print(counts)

print('')
print('Top',howmany,'Industries')

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:howmany]:
    print(val, '\t\t', int(key))