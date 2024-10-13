'''userreg_user module has get, post and delete request and return the data based on the code'''
from flask import jsonify
from user_db import database

db=database()
#user_details=[]
class Userreg():
    def reg(self,*args):
        '''reg function has args with get, post and delete request
        if request is get it will return ;ist uers-deatils with all the columns from table
        post request will allow user to enter new user data if the entered email doesn't exist
        if request id delete it will delete all the enteries from table  '''
        conn=db.db_connection()
        print("args[0]: ", args[0])
        if args[0] == 'GET':
            cursor=conn.execute('Select * from users_details')
            user_details=[dict(id=row[0],first_name=row[1],last_name=row[2],
                            user_name=row[4],password=row[5],email=row[3])
                        for row in cursor.fetchall()
                        ]
            if user_details is not None:
                print("inside: ", user_details)
                return jsonify(user_details)
        if args[0]== 'POST':
            #new_email=request.form['email']
            email_query=conn.execute(f"""select email_id from users_details
                                    where email_id='{args[5]}'""")
            mailresult=email_query.fetchall()
            print(f"This is {mailresult}")
            #cursor=cursor.execute(email_query)
            if len(mailresult)==0:
                sql='''insert into users_details(first_name,last_name,user_name,password,email_id)
                    values(?,?,?,?,?)'''
                cursor=conn.execute(sql,(args[1],args[2],args[3],args[4],args[5]))
                conn.commit()
                return f"user with id:{cursor.lastrowid} created successfully"
            return f"user with email_id:{args[5]} already exist"
        if args[0] == 'DELETE':
            sql=conn.execute("Delete from users_details")
            # cursor.execute(sql)
            conn.commit()
            return "table is empty"
