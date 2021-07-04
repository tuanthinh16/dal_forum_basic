import sqlite3
from post import post_model


class PostAcction:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def show_all(self):
        conn = sqlite3.connect(self.db_connection)
        cur = conn.cursor()
        sql = "SELECT * FROM post"
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            posts = post_model.Posts(
                post_ID=row[0],
                title=row[1],
                type=row[2],
                detail=row[3],
                username=row[4]
            )
            result.append(posts.visibale())
        return result

    def showById(self, id):
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        sql = """
            SELECT * FROM post WHERE post_ID = ?
        """
        cursor.execute(sql, (id, ))
        row = cursor.fetchone()
        result = []
        if row == None:
            return 'Customer not found', 404
        posts = post_model.Posts(
            post_ID=row[0],
            title=row[1],
            type=row[2],
            detail=row[3],
            username=row[4],
        )
        result.append(posts.visibale())
        return result

    def showbytype(self, type):
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        sql = "SELECT * FROM post WHERE type ='"+type+"'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            posts = post_model.Posts(
                post_ID=row[0],
                title=row[1],
                type=row[2],
                detail=row[3],
                username=row[4],
            )
            result.append(posts.visibale())
        return result

    def search(self, value):
        conn = sqlite3.connect(self.db_connection)
        cur = conn.cursor()
        sql = "SELECT * FROM post WHERE title Like '%" + \
            value+"%' OR type like '%"+value+"%'"
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            posts = post_model.Posts(
                post_ID=row[0],
                title=row[1],
                type=row[2],
                detail=row[3],
                username=row[4]
            )
            result.append(posts.visibale())
        return result
