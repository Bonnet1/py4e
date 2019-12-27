## Geocoding ##

Multi-step data analysis:
- data source to gather
- store data in a database (raw data)
- clean/process the data
- store clean data in a new database
- move to visualize or analyze step

"Personal Data Mining" - simple, rudimentary data problems
more sophisticated: hadoop, spark, redshift etc.

Using Google geodata API:
- geoload.py reads JSON (where.data) and parses, writes into geodata.sqlite (cached)
- geodump.py prints all data on the screen
- where.js / where.html creates dots on the map