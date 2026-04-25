import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("dataset.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

table_info="""
drop table AEC;

"""

cursor.execute(table_info)

connection.commit()
connection.close()