## Relational Databases ##

Store data in rows and columns, applying cleverness to utilize Random Access Media (disk drives)

Database -- contains many tables
Relation (or table) -- contails tuples and attributes
Tuple (or row)
Attribute (or column)

**Structured Query Language** (SQL) is the language we use to issues commands to the database
- Create a table
- Retrieve some data
- Update data
- Delete data

Two roles in Large Projects:
- Application Developer
- Database Administrator, responsible for the design and administration of the database

A **Database Model** or **Database Schema** is the structure or format of a database (contract)

Common database systems:
- Oracle
- MySql
- SqlServer
- Other small projects (free and open source), e.g. Postgres, SQLite

Schema / Contract used for database design to build out multiple tables

Basic rule: don't put the same string data in twice -- use a relationship instead
- start with the thing that is most essential to the application (e.g. Track table, including name, length, rating, and number of plays)
- next, assume tracks belong to albums, and albums below to artists
- then look at genre, track belongs to genre

Once have model, need to augment with:
- **Primary Key**, end point thate we can point to
- **Logical Key**, may be used to search from the outside (e.g. string of primary key)
- **Foreign Key**, add a starting point in one table to point to the primary key in another (e.g. album_id, genre_id)

Create end of arrows before the beginning 