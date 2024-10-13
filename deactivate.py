'''This module will deactivate the user account and make the status as number 2'''
from user_db import database
from userlogin_user import LoginUser
# importing db_connection function from module user_db to establish a connection with database

db= database()
log=LoginUser()
class deactivate():
    def deactivate_user(self,login_info):
        '''This function will change the status code to 2 if entered userid and password matches'''
        conn=db.db_connection()
        print(login_info)
        for key,value in login_info.items():
            print(key,value)
            for i in login_info["data"]:
                print("This is",i)
                
                '''code if role is user'''
                if i["role_id"]==1 and i["user_name"]==login_info["user_id"]:
                    # print("role id of loggedin user:",i["role_id"])
                    # print(f'user_name of loggedin user: {i["user_name"]}')
                    # print("user_id that user is trying to de=activate is:",x["user_id"])
                    sql_deactivate=f"update users_details SET status = 2 where user_name='{login_info['user_id']}'"
                    # print(f'''update users_details
                    #             SET status = 2 where user_name={login_info["user_id"]}''')                   
                    conn.execute(sql_deactivate)
                    conn.commit()
                    return f'''user account '{login_info["user_id"]}' deactivated'''
                
                elif  i["role_id"]==0:
                    user_exist_sql=conn.execute(f"select user_name from users_details where user_name='{login_info['user_id']}'" )
                    res=user_exist_sql.fetchall() 
                    #print("This is result",res)                    
                    if len(res) == 1:
                        sql_deactivate_admin= f"update users_details SET status = 2 where user_name='{login_info['user_id']}'"
                        
                        conn.execute(sql_deactivate_admin)
                        conn.commit()
                        #print(f"user account '{login_info["user_id"]}' deactivated")
                        return f"user account '{login_info["user_id"]}' deactivated"
                    else:
                        return "user_id not found"
                else:
                    return "Can't deactivate"
                    



        # status_info= conn.execute(f'''select status from users_details where user_name="{user_id}" and password="{password}"''')
        # x=status_info.fetchall()
        # print(f"this is {x}")
        # if len(x)==1:
        #     deactivate_sql=f'''update users_details
        #                         SET status= 2
        #                         where user_name ="{user_id}" and password ="{password}"'''
        #     conn.execute(deactivate_sql)
        #     conn.commit()
        #     print("this is: ",deactivate_sql)
        #     return f"user:'{user_id}' deactivated"
        # return "can't deactivate account"
            
