import praw
import json

settings = json.loads(open("settings.json", "r", encoding="utf8").read())

reddit = praw.Reddit(client_id=settings["clientId"], client_secret=settings["clientSecret"], user_agent=settings["userAgent"])

for post in reddit.subreddit("AskReddit").hot(limit=10):
    print(post.title)