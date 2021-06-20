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


@app.route('/api/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print('username: ', username)
    print('password: ', password)
    conn = sqlite3.connect('chat.db')
    cur = conn.cursor()
    sql = "SELECT * FROM user WHERE username ='"+str(username)+"'"
    cur.execute(sql)
    for row in cur:
        if(password == row[2]):
            return "thanh cong", 201
        return 'error', 401


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
    return "thanh cong", 201


@ app.route('/api/showcomment')
def showcommet():
    Comment = CommentAcction(connection_data)
    result = Comment.show_all()
    return jsonify(result)


@app.route('/api/addpost')
def addpost():

    return "success", 201


@app.route('/api/showpost')
def showpost():
    Post = PostAcction(connection_data)
    rs = Post.show_all()
    return jsonify(rs)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
