from readline import insert_text
import sqlite3

connection = sqlite3.connect('data.db') #URI for our database

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)" #query to create table
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

user = (1, 'jose', 'asdf')
cursor.execute(insert_query, user)

users = [
    (2,  'rolf', 'asdf'),
    (3,  'anne', 'xyz')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
