from flask import Flask, json
from flask import jsonify
from flask_cors import CORS
from flask import Flask, redirect, request, render_template, session, flash
import datetime
import sqlite3

from comment.comment_acction import CommentAcction
from post.post_acction import PostAcction

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origin": "*"}})
connection_data = ('chat.db')


@app.route('/api/')
def index():
    return ("hello")


@app.route('/api/resigter', methods=['POST'])
def resigter():
    username = request.form['username']
    password = request.form['password']
    repassword = request.form['repassword']
    email = request.form['email']
    con = sqlite3.connect(connection_data)
    cur = con.cursor()
    isRecordExit = 0
    rows = cur.execute(
        "SELECT * FROM user WHERE username ='"+str(username)+"'")
    for row in rows:
        isRecordExit = 1
    if isRecordExit == 1:
        return "Account has been exited", 401
    else:
        if(password == repassword):
            sql = "INSERT INTO user('username','password','email') VALUES ('"+str(username) + \
                "','"+str(password)+"','"+str(email)+"')"
            cur.execute(sql)
            con.commit()
            con.close()
        else:
            return "Invalid", 401
    return "thanh cong", 200


@app.route('/api/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(username, password)
    conn = sqlite3.connect(connection_data)
    cur = conn.cursor()
    isRecordExit = 0
    sql = "SELECT * FROM user WHERE username ='"+str(username)+"'"
    cur.execute(sql)
    for row in cur:
        isRecordExit = 1
    if isRecordExit == 1:
        if str(row[1]) == username and str(row[2]) == password:
            return "thanh cong", 200
        else:
            return "error", 401
    else:
        print(" tai khoan khong ton tai")
        return "khong ton tai", 401
    return redirect('/api/')


@app.route('/api/sigout')
def sigout():
    session.pop("username", None)
    flash("You have been log out !!")
    return redirect('/api/login')


@app.route('/api/addcmt', methods=['POST'])
def addcomment():
    detail = request.form["comment"]
    username = request.form["username"]
    time = datetime.datetime.now()
    post_ID = request.form["post_ID"]
    conn = sqlite3.connect(connection_data)
    cur = conn.cursor()
    sql = "INSERT INTO comment('detail','username','time','post_ID') VALUES('" + \
        str(detail)+"','"+str(username)+"','" + \
        str(time)+"'," + post_ID+")"
    cur.execute(sql)
    conn.commit()
    conn.close()
    return "thanh cong", 200


@ app.route('/api/showcomment')
def showcommet():
    Comment = CommentAcction(connection_data)
    result = Comment.show_all()
    return jsonify(result)


@app.route('/api/showcmtbyID/<int:id>')
def showcmtbyID(id):
    Comment = CommentAcction(connection_data)
    result = Comment.showbyID(id)
    return jsonify(result)


@app.route('/api/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    type = request.form['type']
    detail = request.form['detail']
    username = request.form['username']
    con = sqlite3.connect(connection_data)
    cur = con.cursor()
    sql = "INSERT INTO post ('title', 'type', 'detail', 'username') VALUES ('"+str(
        title)+"','"+str(type)+"','"+str(detail)+"','"+str(username)+"')"
    cur.execute(sql)
    con.commit()
    con.close()
    return "thanh cong", 200


@app.route('/api/showpost')
def showpost():
    Posts = PostAcction(connection_data)
    rs = Posts.show_all()
    return jsonify(rs)


@app.route('/api/deletepost/<int:id>')
def deletepost(id):
    conn = sqlite3.connect(connection_data)
    cur = conn.cursor()
    sql = "DELETE FROM post WHERE post_ID='"+str(id)+"'"
    cur.execute(sql)
    conn.commit()
    conn.close()
    return "thanh cong", 200


@app.route('/api/selectpost/<int:id>')
def selectpostById(id):
    Posts = PostAcction(connection_data)
    result = Posts.showById(id)
    return jsonify(result)


@app.route('/api/editpost', methods=['POST'])
def editpostById():
    post_ID = request.form['post_ID']
    title = request.form['title']
    type = request.form['type']
    detail = request.form['detail']
    conn = sqlite3.connect(connection_data)
    cur = conn.cursor()
    sql = "UPDATE post SET title='" + \
        str(title)+"', type='"+str(type)+"', detail='" + \
        str(detail)+"' WHERE post_ID = "+post_ID
    cur.execute(sql)
    conn.commit()
    conn.close()
    return "thanh cong", 200


@app.route("/api/showbytype/<int:id>")
def showbyType(id):
    if id == 1:
        type = 'IT'
    elif id == 2:
        type = 'Learning'
    elif id == 3:
        type = 'Working'
    elif id == 4:
        type = 'Photography'
    elif id == 5:
        type = 'Freelance'
    elif id == 6:
        type = 'Other'
    Posts = PostAcction(connection_data)
    result = Posts.showbytype(type)
    return jsonify(result)


@app.route('/api/search/<string:value>')
def search(value):
    Posts = PostAcction(connection_data)
    rs = Posts.search(value)
    return jsonify(rs)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5000)
