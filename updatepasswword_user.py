'''This module will update the password of the existing user in database'''
# from flask import Flask
# import userreg_user
from user_db import database
# importing db_connection function from module user_db to establish a connection with database
db=database()

class PassUpdate():
    def update_password(self,user_id,new_password):
        '''update_password func will update the password of existing user in database.
        If entered user exist, it will return password updated if not it will say not updated'''
        conn=db.db_connection()
        # user_id=request.form['user_name']
        # new_password=request.form['password']
        info= conn.execute(f'''select user_name from users_details where user_name ="{user_id}"''')
        res=info.fetchall()
        print(f"this is {res}")
        if len(res)==1:
            update_query=f''' update users_details SET
                        password="{new_password}" where user_name="{user_id}"'''
            conn.execute(update_query)
            conn.commit()
            return f"password updated for user with userid:{user_id}"
        return "not updated"
