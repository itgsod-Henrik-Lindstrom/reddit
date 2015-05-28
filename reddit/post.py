class Post(object):
    def __init__(self, post_data):
        self.post_data = post_data

    def data(self):
        return self.post_data['data']

    def author(self):
        return self.data()['author']

    def text(self):
        return self.data()['selftext']

    def title(self):
        return self.data()['title']