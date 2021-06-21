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
