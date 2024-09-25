#from flask import Flask,jsonify, request
'''userlogin_user module will help users to login if their userid and password are valid'''
from user_db import db_connection

def login(user_id, cred):
    '''login function will pass an argument user_id and cred as user_name and password respectively.
    If user_id and cred are valid it will allow user to login and return login successful'''
    conn=db_connection()
    #print( f"select user_name, password from users_details where 
    # user_name={user_id} and passowrd= {cred}")
    cursor=conn.execute(f"""select count(user_name) from users_details
                        where user_name='{user_id}' and password='{cred}'""")
    userinfo=cursor.fetchall()
    print(userinfo)
    if userinfo[0][0]== 1:
        return "login successful"
    return "login failed"
