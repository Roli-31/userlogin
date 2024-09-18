from flask import Flask, request

app = Flask(__name__)

details=None


@app.route('/reg',methods=['Post'])
def reg():
    global details
    payload=request.get_json()
    details=payload
    return details


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()

    # read file
    #details['name','pass']
    if details['name']== payload['name'] and details['pass']== payload['pass']:
          return 'login success'
    #compare paylaod with file data
          
    else:
        return 'login failed'



app.run(debug=True)
