from credentials import username, password
from instabot import Bot
import os
import glob
from pathlib import Path


cookie_del = glob.glob("config/*cookie.json")
if cookie_del : os.remove(cookie_del[0])

bot = Bot()
bot.login(username=username, password=password)
file = Path("Files/followers.txt")

followers = bot.get_user_followers("foodys")
count = 0
# print(followers)
for follower in followers:
    print(bot.get_user_info(follower))
    file.write_text(str(follower['username']))
    print("Next.")
    count += 1

print("Followers: ", count)