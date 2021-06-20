class Post:
    def __init__(self, post_ID=0, title='', type='', username=''):
        self.post_ID = post_ID
        self.title = title
        self.type = type
        self.username = username

    def visibale(self):
        return{
            'post_ID': self.post_ID,
            'title': self.title,
            'type': self.type,
            'username': self.username,
        }
