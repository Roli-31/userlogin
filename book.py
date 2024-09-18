from flask import Flask,request,jsonify
import json
import sqlite3

app=Flask(__name__)

def db_connection():
    conn=None
    try:
        conn=sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/books',methods=["GET","POST"])
def books():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method == 'GET':
        cursor= conn.execute('select * from book2')
        books=[
            dict(id=row[0],author=row[1],language=row[2],title=row[3]) 
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    if request.method == 'POST':
        new_author=request.form['author']
        new_language=request.form['language']
        new_title=request.form['title']
        sql='''INSERT into book2(author,language,title) 
                values (?,?,?)'''
        cursor=cursor.execute(sql,(new_author,new_language,new_title))
        conn.commit()

        return f"Book with id: {cursor.lastrowid} created successfully",201
    
@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    conn=db_connection()
    cursor=conn.cursor()
    book=None
    if request.method== 'GET':
        cursor=cursor.execute('SELECT * from book2 where id=?',(id,))
        rows=cursor.fetchall()
        #print("asfgasdfgh")
        print("rows:", rows )

        for r in rows:
            book =r
            if book is not None:
                return jsonify(book),200
            else:
                return "Something wrong",404
        return "nothing found",404
    


if __name__ == '__main__':
    app.run(debug=True)


