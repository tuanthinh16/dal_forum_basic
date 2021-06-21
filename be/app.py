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
    if(password == repassword):
        con = sqlite3.connect('chat.db')
        cur = con.cursor()
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
    conn = sqlite3.connect('chat.db')
    cur = conn.cursor()
    sql = "SELECT * FROM user WHERE username ='"+str(username)+"'"
    cur.execute(sql)
    for row in cur:
        if str(row[2]) == password:
            return "thanh cong", 200
        else:
            return "error", 401
    return redirect('/api/')


@app.route('/api/sigout')
def sigout():
    session.pop("username", None)
    flash("You have been log out !!")
    return redirect('/api/login')


@app.route('/api/addcomment', methods=['POST'])
def addcomment():
    detail = request.form["comment"]
    username = request.form["username"]
    time = datetime.datetime.now()
    post_ID = request.form["post_id"]
    conn = sqlite3.connect('chat.db')
    cur = conn.cursor()
    sql = "INSERT INTO comment ('detail','username','time','post_ID') VALUES('" + \
        str(detail)+"','"+str(username)+"','"+str(time)+"')"
    cur.execute(sql)
    conn.commit()
    conn.close()
    return "thanh cong", 200


@ app.route('/api/showcomment')
def showcommet():
    Comment = CommentAcction(connection_data)
    result = Comment.show_all()
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
    cur.execute(sql)
    con.commit()
    con.close()
    return "thanh cong", 200


@app.route('/api/showpost')
def showpost():
    Posts = PostAcction(connection_data)
    rs = Posts.show_all()
    return jsonify(rs)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = True
    app.run()
