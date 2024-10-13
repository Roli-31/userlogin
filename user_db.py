''' user_db module will create table users_details and create a connection with datatbse userinfo'''
import sqlite3

class database:

    def user_table(self):
        '''user_table function will create a user_deatils table'''
        cursor=self.db_connection()
        sql_query= ''' create table users_details(
            id integer PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL,
            email_id text NOT NULL,
            user_name text NOT NULL,
            password text NOT NULL)
            '''
        cursor.execute(sql_query)
        cursor.commit()
        return "Table created"
    
    def db_connection(self):
        ''' db_connection function will makes a connection with database userinfo else return none'''
        conn=None
        try:
            conn=sqlite3.connect("userinfo")
        except sqlite3.error as error:
            print(error)
        return conn
