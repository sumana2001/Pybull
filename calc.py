from tkinter import *

window = Tk()
window.title("Standard Calculator")
window.resizable(0, 0)


def clear():
    s = e1_val.get()
    e1.delete(first=0, last=len(s))


def zero():
    s = e1_val.get()
    e1.insert(END, "0")


def one():
    s = e1_val.get()
    e1.insert(END, "1")


def two():
    s = e1_val.get()
    e1.insert(END, "2")


def three():
    s = e1_val.get()
    e1.insert(END, "3")


def four():
    s = e1_val.get()
    e1.insert(END, "4")


def five():
    s = e1_val.get()
    e1.insert(END, "5")


def six():
    s = e1_val.get()
    e1.insert(END, "6")


def seven():
    s = e1_val.get()
    e1.insert(END, "7")


def eight():
    s = e1_val.get()
    e1.insert(END, "8")


def nine():
    s = e1_val.get()
    e1.insert(END, "9")


def div():
    x = 0.0
    flag = 1
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == "/" or s[i] == "X" or s[i] == "+" or s == "-":
            a = s[0:i]
            b = s[i + 1 : len(s)]
            flag = 0
            if s[i] == "/":
                x = float(a) / float(b)
            elif s[i] == "X":
                x = float(a) * float(b)
            elif s[i] == "+":
                x = float(a) + float(b)
            elif s[i] == "-":
                x = float(a) - float(b)
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, "")
        e1.insert(END, str(x))
    e1.insert(END, "/")


def mult():
    x = 0.0
    flag = 1
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == "/" or s[i] == "X" or s[i] == "+" or s == "-":
            a = s[0:i]
            b = s[i + 1 : len(s)]
            flag = 0
            if s[i] == "/":
                x = float(a) / float(b)
            elif s[i] == "X":
                x = float(a) * float(b)
            elif s[i] == "+":
                x = float(a) + float(b)
            elif s[i] == "-":
                x = float(a) - float(b)
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, "")
        e1.insert(END, str(x))
    e1.insert(END, "X")


def sub():
    x = 0.0
    flag = 1
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == "/" or s[i] == "X" or s[i] == "+" or s == "-":
            a = s[0:i]
            b = s[i + 1 : len(s)]
            flag = 0
            if s[i] == "/":
                x = float(a) / float(b)
            elif s[i] == "X":
                x = float(a) * float(b)
            elif s[i] == "+":
                x = float(a) + float(b)
            elif s[i] == "-":
                x = float(a) - float(b)
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, "")
        e1.insert(END, str(x))
    e1.insert(END, "-")


def dec():
    s = e1_val.get()
    e1.insert(END, ".")


def equal():
    x = 0.0
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == "/" or s[i] == "X" or s[i] == "+" or s == "-":
            a = s[0:i]
            b = s[i + 1 : len(s)]
            if s[i] == "/":
                x = float(a) / float(b)
            elif s[i] == "X":
                x = float(a) * float(b)
            elif s[i] == "+":
                x = float(a) + float(b)
            elif s[i] == "-":
                x = float(a) - float(b)
    e1.delete(first=0, last=len(s))
    e1.insert(END, "")
    e1.insert(END, str(x))


def add():
    x = 0.0
    flag = 1
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == "/" or s[i] == "X" or s[i] == "+" or s == "-":
            a = s[0:i]
            b = s[i + 1 : len(s)]
            flag = 0
            if s[i] == "/":
                x = float(a) / float(b)
            elif s[i] == "X":
                x = float(a) * float(b)
            elif s[i] == "+":
                x = float(a) + float(b)
            elif s[i] == "-":
                x = float(a) - float(b)
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, "")
        e1.insert(END, str(x))
    e1.insert(END, "+")


e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val, width=40)
e1.grid(row=0, column=0, columnspan=3)

clear = Button(window, text="Clear", width=8, height=2, command=clear)
clear.grid(row=0, column=3)

b2 = Button(window, text="7", width=8, height=4, command=seven)
b2.grid(row=1, column=0)

b2 = Button(window, text="8", width=8, height=4, command=eight)
b2.grid(row=1, column=1)

b2 = Button(window, text="9", width=8, height=4, command=nine)
b2.grid(row=1, column=2)

b2 = Button(window, text="/", width=8, height=4, command=div)
b2.grid(row=1, column=3)

b2 = Button(window, text="4", width=8, height=4, command=four)
b2.grid(row=2, column=0)

b2 = Button(window, text="5", width=8, height=4, command=five)
b2.grid(row=2, column=1)

b2 = Button(window, text="6", width=8, height=4, command=six)
b2.grid(row=2, column=2)

b2 = Button(window, text="X", width=8, height=4, command=mult)
b2.grid(row=2, column=3)

b2 = Button(window, text="1", width=8, height=4, command=one)
b2.grid(row=3, column=0)

b2 = Button(window, text="2", width=8, height=4, command=two)
b2.grid(row=3, column=1)

b2 = Button(window, text="3", width=8, height=4, command=three)
b2.grid(row=3, column=2)

b2 = Button(window, text="-", width=8, height=4, command=sub)
b2.grid(row=3, column=3)

b2 = Button(window, text="0", width=8, height=4, command=zero)
b2.grid(row=4, column=0)

b2 = Button(window, text=".", width=8, height=4, command=dec)
b2.grid(row=4, column=1)

b2 = Button(window, text="=", width=8, height=4, command=equal)
b2.grid(row=4, column=2)

b2 = Button(window, text="+", width=8, height=4, command=add)
b2.grid(row=4, column=3)

window.mainloop()
