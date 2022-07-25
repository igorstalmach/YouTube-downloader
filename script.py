import eel
from pytube import YouTube

eel.init("web")

@eel.expose
def get_video(link):
    try:
        yt = YouTube(link)
    except:
        return "Passed link is not a valid YouTube link."
    stream = yt.streams.get_highest_resolution()
    stream.download('~/Downloads')
    return "Video downloaded."

eel.start("index.html", size=(500, 200))