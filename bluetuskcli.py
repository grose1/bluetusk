# a simple python script to post text to Mastodon and Bluesky at the same time.
# a simple python script to post text to Mastodon and Bluesky at the same time.
from configparser import ConfigParser
from atproto import Client
from mastodon import Mastodon

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get info from Config File

# Bluesky
bluesky = config_object["BLUESKY"]
bsky_usr = bluesky["username"]
bsky_pass = bluesky["app_password"]
bsky_limit = int(bluesky["char_limit_bsky"])

# Mastodon
masto = config_object["MASTODON"]
masto_inst = masto["instance"]
masto_token = masto["access_token"]
masto_limit = int(masto["char_limit_masto"])


# Post to Mastodon
def masto():
    masto_text = input('Toot Your Toot: ')
    post = masto_text
    char = (len(post))
    print('Character limit Mastodon:', masto_limit)
    print('Current Count:', char)
    if char > masto_limit:
        print('Character Limit Exceeded! Try Again...')
        masto()
    mastodon = Mastodon(api_base_url=masto_inst, access_token=masto_token)
    mastodon.toot(post)
    main()


# Post to Bluesky
def bsky():
    bsky_text = input('Skeet Your Skeet: ')
    post = bsky_text
    char = (len(post))
    print('Character limit Bluesky:', bsky_limit)
    print('Current Count:', char)
    if char > bsky_limit:
        print('Character Limit Exceeded! Try Again...')
        bsky()
    # make a text post in bluesky
    client = Client()
    client.login(bsky_usr, bsky_pass)

    client.send_post(text=post)
    main()


# Crosspost to Both
def crosspost():
    vartext = input('Post Your Post: ')
    post = vartext
    char = (len(post))
    print('Character limit Bluesky:', bsky_limit)
    print('Character limit Mastodon:', masto_limit)
    print('Current Count:', char)
    if char > masto_limit:
        print('Character Limit Exceeded! Try Again...')
        crosspost()
    if char > bsky_limit:
        print('Character Limit Exceeded! Try Again...')
        crosspost()
    main()

    # make a text post in bluesky
    client = Client()
    client.login(bsky_usr, bsky_pass)
    client.send_post(text=post)

    # post to mastodon
    mastodon = Mastodon(api_base_url=masto_inst, access_token=masto_token)
    mastodon.toot(post)


# Main Menu
def main():
    print('Select 1 to post to Mastodon')
    print('Select 2 to post to Bluesky')
    print('Select 3 to post to Both')

    select = input('Choose an Option: ')
    if select == '1':
        masto()
    if select == '2':
        bsky()
    if select == '3':
        crosspost()


if __name__ == "__main__":
    main()
