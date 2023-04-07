import praw
import json

settings = json.loads(open("settings.json", "r", encoding="utf8").read())
usedIds = open("usedIds.txt", "r", encoding="utf8").read().split("/")

reddit =praw.Reddit(client_id=settings["clientId"], client_secret=settings["clientSecret"], user_agent=settings["userAgent"])

def writeUsedIds():
    f=open("usedIds.txt", "w+", encoding="utf8")
    outStr = ""
    for id in usedIds:
        outStr=str(outStr+id+"/")
    f.write(outStr)
    f.close()

def getPosts(subreddit, n):
    unfilteredPosts=post = reddit.subreddit(subreddit).hot()
    posts=[]
    i=0
    for post in unfilteredPosts:
        if post.over_18 or post.spoiler or post in usedIds or len(post.title)>150: continue
        i+=1
        posts.append(post)
        usedIds.append(post.id)
        if i==n: break
    writeUsedIds()
    return posts
def getComments(post, n):
    cmnts= []
    i=0
    while i<n:
        try:
            if len(post.comments[i].body)>500: continue
            else:
                cmnts.append(post.comments[i])
                i+=1
                
        except:
            i+=1
            continue
    return cmnts