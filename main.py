'''This is main function. All Api call will happen here'''
import sqlite3
import json
#importing modules
from flask import Flask,request
#importing module flask from class Flask
from user_db import db_connection,user_table
from userreg_user import reg
from userlogin_user import login
from updatepasswword_user import update_password

app=Flask(__name__)
#initalizing class Flask

@app.route('/user_db',methods=['POST'])
def userinfoapi():
    return user_table()

@app.route('/reg',methods=['GET','POST','DELETE'])
def regapi():
    print(f"This is {request.method}")
    if request.method == 'GET' or request.method== 'DELETE':
        get_result=reg(request.method)
        return get_result
    else:
        new_first_name=request.form['first_name']
        new_last_name=request.form['last_name']
        new_user_name=request.form['user_name']
        new_password=request.form['password']
        new_email=request.form['email']
        get_result=reg(request.method,new_first_name,new_last_name,
                       new_user_name,new_password,new_email)
        return get_result

@app.route('/login',methods=['Post'])
def loginapi():
    x=request.form['user_name']
    y=request.form['password']
    result_login= login(x,y)
    return result_login

@app.route('/update_password',methods=['put'])
def update_passwordapi():
    u= request.form['user_name']
    p=request.form['password']
    result_password_update=update_password(u,p)
    return result_password_update

if __name__== '__main__':
    app.run(debug= True)
