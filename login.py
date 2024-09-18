def login(user_id, cred):
    print( f"select user_name, password from users_details where user_name={user_id} and passowrd= {cred}")
       
    cursor=conn.execute(f"select count(user_name) from users_details where user_name='{user_id}' and password= '{cred}'")
    userinfo=cursor.fetchall()
    print(userinfo)

    if userinfo[0][0]== 1:
        return "login successful"
    else:
        return"login failed" 