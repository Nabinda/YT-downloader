from tkinter import *
from tkinter.filedialog import askdirectory
from pytube import YouTube

win = Tk()
path = "Downloads"
label = None


def audio_downloader():
    url = user_input.get()
    youtube = YouTube(url)
    audio = youtube.streams.filter(only_audio=True)
    audio[0].download(output_path=path)
    user_input.delete(0, END)


def video_downloader():
    a = (str(user_input.get()))
    vid = YouTube(a)
    down = vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    down.download(output_path=path)
    user_input.delete(0, END)


def download_path():
    global path
    path = askdirectory(title='Select Folder')
    p.configure(text="Download Path: \t"+path)


win.title("Youtube Downloader")
win.geometry('800x500')
Label(win, text="URL:").pack()
user_input = Entry(win, width=60)
user_input.pack()
Button(win, text="Download Audio", command=audio_downloader).pack()
Button(win, text="Download Video", command=video_downloader).pack()
p = Label(win, text="Download Path: \t"+path)
p.pack()
c = Button(win, text="Select Download Folder", command=download_path)
c.pack()


win.mainloop()
