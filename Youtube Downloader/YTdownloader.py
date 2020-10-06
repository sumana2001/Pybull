from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

app = Tk()

app.title("YouTube Downloader")

app.geometry("800x600")

app.config(background="white")

app.resizable(False, False)

img = ImageTk.PhotoImage(Image.open("Yt.png"))
imglabel = Label(app, image=img).grid(row=5, column=1)        

def setURL():
    url = getURL.get()
    print(url)

    global yt
    yt = YouTube(url)
    print(yt.title)

    global videos
    videos = yt.streams.filter(mime_type='video/mp4').all()

    count = 1
    for v in videos:
        listbox.insert(END, str(count)+". "+str(v)+"\n\n")
        count += 1

def Download_Function():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR", "ENTER url ")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR", "ENTER LOCATION ")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Downloading Finish", yt.title+" has been downloaded Sucessfully!!!")


def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def clickReset():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0,END)

headLabel       = Label(app,   text="YOUTUBE VIDEO DOWNLOADER",  font=("Comic Sans MS",25)).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(app,   text="URL",                 font=("Comic Sans MS",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(app,   text="SELECT QUALITY",      font=("Comic Sans MS",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(app,   text="LOCATION",            font=("Comic Sans MS",15)).grid(row=3, column=0, padx=10, pady=10)

getURL = StringVar()
getLoc = StringVar()

urlEntry    = Entry(app,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(app,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

listbox     = Listbox(app, font=("Century Gothic",11), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2,column=1, padx=10, pady=10)

urlButton       = Button(app, text = "SET URL",    font=("Comic Sans MS",10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(app, text = "BROWSE",     font=("Comic Sans MS",10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(app, text = "DOWNLOAD",   font=("Comic Sans MS",10), width=15, relief=SOLID, borderwidth=1, command=Download_Function).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(app, text = "CLEAR ALL",  font=("Comic Sans MS",10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=4, column=2, padx=10, pady=10)


app.mainloop()