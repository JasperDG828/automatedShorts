import redditApi
import screenshots
import tts
import video

commentCount = 3

post = redditApi.getPosts("askreddit", 1)[0]
screenshots.screenPost(post.url, post.id)
tts.say(post.title, f"post_{post.id}")
commentIds = []
for comment in redditApi.getComments(post, commentCount):
    tts.say(comment.body, f"comment_{comment.id}")
    commentIds.append(comment.id)
screenshots.screenComments(post.url, commentIds)
video.generateVideo(post.id, commentIds)
