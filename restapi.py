from flask import Flask,request,jsonify

app= Flask(__name__)



book_list=[
    {
         'id':0,
         "author":"chinua achebe",
         "language":"english",
         "title":"things fall apart",
     },
     {
         'id': 1,
         "author": "hans christian andersen",
         "language": "danish",
         "title": "fairy tales",
     },
     {
         'id': 2,
         "author": "samuel beckett",
         "language": "french,english",
         "title": "molloy,malone dies,the unnamable,the triology",
     },
     {
         'id': 6,
         "author": "jorge luis borges",
         "language": "spanish",
         "title": "ficciones",
     },
     {
         'id': 3,
         "author": "giovanni boccaccio",
         "language": "italian",
         "title": "the decameron",
     },
     {
         'id': 5,
         "author": "emily bront",
         "language": "english",
         "title": "wuthering heights",
     },
]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method== 'GET':
       if len(book_list) >0:
           return jsonify(book_list)
       else:
           return 'nothing found',404
    if request.method=='POST':
        new_author=request.json['author']
        new_language=request.json['language']
        new_title=request.json['title']
        iD=book_list[-1]['id']+1

        new_obj={'id':iD,'author':new_author,'language':new_language,'title':new_title}

        book_list.append(new_obj)

        return jsonify(book_list)
if __name__ == '__main__':
    app.run(debug=True)



    
    