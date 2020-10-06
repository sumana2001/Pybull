from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import PyPDF2


class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('PDF and Music Player'); window.resizable(0,0)

        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause/Resume',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Speech = Button(window ,text = 'Select PDF',  width = 10, font = ('Times',10), command = self.speech)

        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=50,y=60);Speech.place(x=150, y=60)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()

    def speech(self):

        pdf_File = filedialog.askopenfilename()

        pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
        count = pdf_Reader.numPages
        textList = []

        for i in range(count):
           try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
           except:
               pass

        textString = " ".join(textList)
        # print(textString)

        language = 'en'
        myAudio = gTTS(text=textString, lang=language, slow=False)
        myAudio.save(pdf_File+".mp3")


root = Tk()
app= MusicPlayer(root)
root.mainloop()
