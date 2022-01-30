from tkinter import *
from PIL import ImageTk
win = Tk()
win.title("Daum Log-in")
win.geometry("400x600")
win.option_add("*Font", "궁서 20")

# 다음 로고
lab_d = Label(win)
img = ImageTk.PhotoImage(file='logo.gif', master=win)
lab_d.config(image=img)
lab_d.pack()
# id 라벨
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

# id 입력창
ent1 = Entry(win)

ent1.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text="Password")
lab2.pack()

# pw 입력창
ent2 = Entry(win)

ent2.pack()

# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")
btn.pack()

win.mainloop()
