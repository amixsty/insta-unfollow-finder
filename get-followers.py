
import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot, utils 

bot = Bot()
bot.login(username="amirhft", password="XXXXXXX")

f = utils.file("followers.txt")
for username in "user":
    followers = bot.get_user_followers(username)
    f.save_list(followers)

