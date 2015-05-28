from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.post import Post

bojohan = client.login('mrcookierookie')

#bojohan.me()


# python = Subreddit("python")
#
# python.hot()

lol = Subreddit("globaloffensive")

k = lol.hot_children()[0]

p = Post(k)

#print p.post_data['data']['author']

print p.text()










