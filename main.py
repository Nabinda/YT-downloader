from tkinter import *
from pytube import YouTube


def audio_downloader():
    url = user_input.get()
    youtube = YouTube(url)
    audio = youtube.streams.filter(only_audio=True)
    audio[0].download(r'D:/Downloads/Downloaded using Python')
    user_input.delete(0, END)


def video_downloader():
    a = (str(user_input.get()))
    vid = YouTube(a)
    down = vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    down.download(r'D:/Downloads/Downloaded using Python')
    user_input.delete(0, END)


win = Tk()
win.title("Youtube Downloader")
win.geometry('500x500')

Label(win, text="URL:").pack()
user_input = Entry(win, width=60)
user_input.pack()
Button(win, text="Download Audio", command=audio_downloader).pack()
Button(win, text="Download Video", command=video_downloader).pack()

win.mainloop()
