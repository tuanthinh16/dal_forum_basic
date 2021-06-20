class Comment:
    def __init__(self, comment_ID=0, detail='', username='', time='', post_ID=''):
        self.comment_ID = comment_ID
        self.detail = detail
        self.username = username
        self.time = time
        self.post_ID = post_ID

    def visibale(self):
        return{
            'comment_ID': self.comment_ID,
            'detail': self.detail,
            'username': self.username,
            'time': self.time,
            'post_ID': self.post_ID
        }
