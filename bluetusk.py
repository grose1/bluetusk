# a simple python script to post text to mastoson and bluesky at the same time. 

from atprototools import Session
from mastodon import Mastodon
import sys


# Bluesky login (uses app password)
USERNAME = "bluesky_username"
PASSWORD = "app_password"

# sys.argv for ios shortcuts app
vartext = sys.argv[-1]
post = vartext
session = Session(USERNAME, PASSWORD)


# make a text post in bluesky
resp = session.postBloot(post)



# post to mastodon (need to create app key first)

mastodon = Mastodon(api_base_url = 'mastodon_url', access_token = 'app_access_token')
mastodon.toot(post)
