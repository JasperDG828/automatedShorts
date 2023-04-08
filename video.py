from moviepy.editor import *

def generateVideo(postId, commentIds):
    paths = [(f"./screenshots/post_{postId}.png", f"./audio/post_{postId}.mp3")]
    for commentId in commentIds:
        paths.append((f"./screenshots/comment_{commentId}.png", f"./audio/comment_{commentId}.mp3"))

    clips = []
    t=0
    for item in paths:
        backgroundClip = VideoFileClip("./clips/clip2.mp4")
        audio = AudioFileClip(item[1])
        clip = backgroundClip.subclip(t, t+audio.duration+1)
        img = ImageClip(item[0]).resize(height=200)
        imgClip = img.set_position((50, 860))
        imgClip = imgClip.set_duration(audio.duration+1)
        compositeClip = CompositeVideoClip([clip, imgClip])
        compositeClip = compositeClip.set_audio(audio)
        clips.append(compositeClip)
        t+=audio.duration+1
    finalClip = concatenate_videoclips(clips)
    finalClip.write_videofile(f"./output/{postId}.mp4")