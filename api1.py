from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/<name>')
def print_name(name):
    return 'Hi {}'.format(name)

@app.route('/person/<int:age>')
def show_age(age):
    return 'Age is %d' %age

@app.route('/height/<float:h>')
def height(h):
    return 'Height is %f' %h

@app.route('/python/')
def hello_python():
   return 'Hello Python'


if  __name__== '__main__':
    app.run(debug=True)

