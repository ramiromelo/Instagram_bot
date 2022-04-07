import random as r
from instapy import InstaPy
from instapy import smart_run
import schedule
import time

import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv('INSTA_USER')
password = os.getenv('INSTA_PASS')

print(username, password)

session = InstaPy(username=username, password=password, headless_browser=False)
session.login()


session.like_by_tags(["larissamanoela"], amount=50) # Specifying tags to search posts for, to ultimately like them.
session.set_do_follow(True, percentage=r.randint(40, 60)) # Setting percent chance that the bot will follow the user.
session.set_do_comment(True, percentage=r.randint(10, 30)) # Setting percent chance that the bot will leave a comment on the post.
session.set_comments(["Great!", "Love this", "Nice", "I like this", "Liked!"])

