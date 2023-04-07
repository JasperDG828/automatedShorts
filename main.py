import redditApi
import screenshots
import tts

postData = {"id": None, "title": None, "comments": []}

post = redditApi.getPosts("askreddit", 1)[0]
postData["id"]=post.id
postData["title"]=post.title
screenshots.screenPost(post.url, post.id)
tts.say(post.title, f"post_{post.id}")
commentIds = []
for comment in redditApi.getComments(post, 3):
    postData["comments"].append({"id": comment.id, "text": comment.body})
    tts.say(comment.body, f"comment_{comment.id}")
    commentIds.append(comment.id)
screenshots.screenComments(post.url, commentIds)
print(postData)