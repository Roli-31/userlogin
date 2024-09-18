import sqlite3

conn= sqlite3.connect('user.sqlite')
cursor=conn.cursor()

sql_query= ''' create table users_details(
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    user_name text NOT NULL,
    password text NOT NULL)
    '''

sql1='''ALTER table users_details
        ADD email text '''

cursor.execute(sql1)
conn.commit()