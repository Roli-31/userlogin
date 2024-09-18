#importing sqlite3 database module
import sqlite3

#establish a connection with database
conn=sqlite3.connect('books.sqlite')

#cursor object is used to execute SQL STATEMENT
cursor=conn.cursor()

#SQL_QUERY IS DEFINED TO CREATE A TABLE
sql_query= '''CREATE TABLE book2(
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)'''


cursor.execute(sql_query)