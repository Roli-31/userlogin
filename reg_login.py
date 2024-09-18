from flask import Flask,request,jsonify
import json
import sqlite3
from login import login


app=Flask(__name__)

def db_connection():
    conn=None
    try:
        conn = sqlite3.connect('user.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn
    

user_details=[]
@app.route('/reg',methods=['GET','Post','DELETE','PUT'])
def reg():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method == 'GET':
        cursor=conn.execute('Select * from users_details')
        user_details=[dict(id=row[0],first_name=row[1],last_name=row[2],user_name=row[3],password=row[4],email=row[5]) 
                      for row in cursor.fetchall()
                      ]
        if user_details is not None:
            return jsonify(user_details)
        
    if request.method== 'POST':
        new_email=request.form['email']
        email_query=conn.execute(f'''select email from users_details where email="{new_email}"''')
        x=email_query.fetchall()
        print(f"This is {x}")
        #cursor=cursor.execute(email_query)
        if len(x)==0:
            
            new_first_name=request.form['first_name']
            new_last_name=request.form['last_name']
            new_user_name=request.form['user_name']
            new_password=request.form['password']
            new_email=request.form['email']
            sql='''insert into users_details(first_name,last_name,user_name,password,email)
                values(?,?,?,?,?)'''
            cursor=cursor.execute(sql,(new_first_name,new_last_name,new_user_name,new_password,new_email))
            conn.commit()
            return f"user with id:{cursor.lastrowid} created successfully"
        else:
             
             return f"user with email:{new_email} already exist"
        
    
    
    if request.method == 'DELETE':
        sql=conn.execute("Delete from users_details")
        # cursor.execute(sql)
        conn.commit()
        return "table is empty"


    
    if request.method == 'PUT':
        user_id=request.form['user_name']
        new_password=request.form['password']
        info= conn.execute(f'''select user_name from users_details where user_name ="{user_id}"''')
        x=info.fetchall()
        print(f"this is {x}")

        if len(x)==1:
            update_query=f''' update users_details SET
                password="{new_password}" where user_name="{user_id}"'''
            cursor=conn.execute(update_query)
            conn.commit()
            return f"password updated for user with userid:  {user_id} "
        return f"not updated"
    
@app.route('/login',methods=['POST'])
def login():
    conn=db_connection()
    cursor=conn.cursor()

    user_id=request.form['user_name']                                                                              
    cred=request.form['password']
    login(user_id, cred)       
            


if __name__=='__main__':
    app.run(debug=True)
    
