class Posts:
    def __init__(self, post_ID=0, title='', type='', detail='', username=''):
        self.post_ID = post_ID
        self.title = title
        self.type = type
        self.detail = detail
        self.username = username

    def visibale(self):
        return{
            'post_ID': self.post_ID,
            'title': self.title,
            'type': self.type,
            'detail': self.detail,
            'username': self.username,
        }
