from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("YouTube Downloader")

Label(root, text="YouTube Downloader", font="arial 20 bold").pack()

link = StringVar()
Label(root, text="Paste Your link here", font="arial 15 bold").place(x=130, y=60)
link_entry = Entry(root, width=70, textvariable= link).place(x=32, y=90)

def high():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text="Downloaded Successfully", font="arial 15 bold").place(x=180, y=210)

Button(root, text="Audio Only", font="arial 15 bold", bg="#e76f51", padx=2, command=high).place(x=180, y=150)

def low():
    url = YouTube(str(link.get()))
    video = url.streams.get_lowest_resolution()
    video.download()
    Label(root, text="Downloaded Successfully", font="arial 15 bold").place(x=180, y=210)

Button(root, text="Low Resolution", font="arial 15 bold", bg="#e76f51", padx=2, command=low).place(x=110, y=200)

def audio_only():
    url = YouTube(str(link.get()))
    video = url.streams.get_audio_only()
    video.download()
    Label(root, text="Downloaded Successfully", font="arial 15 bold").place(x=180, y=210)

Button(root, text="High Resolution", font="arial 15 bold", bg="#e76f51", padx=2, command=audio_only).place(x=260, y=200)



root.mainloop()