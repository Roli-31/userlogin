#importing class Flask and url_for() function
from flask import Flask,redirect,url_for

#initating class Flask
app= Flask(__name__)

#decorator which says which url should call the below defined function
@app.route('/admin')
def admin():
    return 'Hello Admin'

@app.route('/<guest>')
def guest(guest):
    return 'Hello %s as guest' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name== 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest=name))


if __name__ == '__main__':
    #run method to run the app on local dev server
    app.run(debug=True)
