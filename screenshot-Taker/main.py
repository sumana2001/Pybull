import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width=200, height=200)
canvas1.pack()


def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)


myButton = tk.Button(text='Capture Screenshot',
                     command=takeScreenshot, bg='blue', fg='white', font=10)
canvas1.create_window(100, 100, window=myButton)

root.mainloop()
