#from flask import Flask,jsonify, request
'''userlogin_user module will help users to login if their userid and password are valid'''
from user_db import database
db=database()

class LoginUser():

    def login(self,user_id, cred):
        '''login function will pass an argument user_id and cred as user_name and password respectively.
        If user_id and cred are valid it will allow user to login and return login successful'''
        conn=db.db_connection()
        #print( f"select user_name, password from users_details where 
        # user_name={user_id} and passowrd= {cred}")
        cursor=conn.execute(f"""select count(user_name) from users_details
                            where user_name='{user_id}' and password='{cred}'""")
        userinfo=cursor.fetchall()
        print(userinfo)
        if userinfo[0][0]== 1:
            login_user_info_sql= conn.execute(f'''select users_details.id,users_details.first_name,users_details.last_name,
                                                users_details.user_name,users_details.password,users_details.email_id,users_details.status,users_details.role_id,
                                                module_id,api_id,method from users_details
                                                Inner JOIN module_access
                                                ON users_details.role_id = module_access.role_id
                                                where user_name="{user_id}" and password="{cred}"''')
            
            login_user_info=[dict(user_id=row[0],fname=row[1],lname=row[2],user_name=row[3],password=row[4],email=row[5],status=row[6],role_id=row[7],
                                  module_id=row[8],api_id=row[9],method=row[10])
                             for row in login_user_info_sql.fetchall()]
            

            return {"message": "login successful",
                    "data": login_user_info}
        return "login failed"
