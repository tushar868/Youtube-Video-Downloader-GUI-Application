# importing tkinter
from tkinter import *
# importing YouTube module
import tkinter
from pytube import YouTube
import cv2
import PIL.Image, PIL.ImageTk
from ttkthemes import themed_tk as tk
from tkinter import ttk
# initializing tkinter
root = Tk()

# setting the geometry of the GUI
root.geometry("900x400")
root.configure(background='black')


# setting the title of the GUI
root.title("Youtube Video Downloader Application")
statusbar = ttk.Label(root, text="Developed By [InstaId :- devil.88._] Tushar", anchor=W, font='Ariel 10 ')
statusbar.pack(side=BOTTOM, fill=X)
# defining download function
def download():
    # using try and except to execute program without errors
    try:
        Label.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        Label.set("Mistake")
        root.update()
        link.set("Enter correct link")

# created the Label widget to welcome user
Label(root, text="~ Youtube  Video ~\nDownloader  Application", font="Aclonica 45 ",fg='#D35400', bg='black').pack()
# declaring StringVar type variable
Label = StringVar()
# setting the default text to myVar
Label.set("Enter the link below")
# created the Entry widget to ask user to enter the url

Entry(root, textvariable=Label, width=75,font="Ariel 13 bold",bg='black',fg='white').pack(pady=25)
# declaring StringVar type variable
link = StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, font="Ariel 13 bold",width=75,bg='black',fg='white').pack(pady=10)
# created and called the download function to download video
Button(root, text="D o w n l o a d    V i d e o ",font="Lobster 23 bold", bg='Green',command=download,width= 25,fg='black').pack(pady=25)
# running the mainloop
root.mainloop()