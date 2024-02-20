# a simple python script to post text to Mastodon and Bluesky at the same time.
# use pip install Mastodon.py for the mastodon package 
# use pip install atprototools for the bluesky package

from atprototools import Session
from mastodon import Mastodon

vartext = input('Post Your Post: ')
post = vartext
char = (len(post))
print('Character limit 300 , Current Count: ', char)
if char > 300:
    print('Character Limit Exceeded! Try Again...')
    exit()
input("Press Enter to continue...")

# Bluesky login (uses app password)
USERNAME = "bluesky_handle"
PASSWORD = "app_password"
# make a text post in bluesky
session = Session(USERNAME, PASSWORD)
resp = session.postBloot(post)

# post to mastodon (need to create app key first)

mastodon = Mastodon(api_base_url = 'mastodon_instance', access_token = 'access_token')
mastodon.toot(post)
